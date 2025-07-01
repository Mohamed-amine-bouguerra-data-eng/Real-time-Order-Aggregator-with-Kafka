from kafka import KafkaConsumer
import json
import time
import os

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='order-processor-v2',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    consumer_timeout_ms=1000
)

order_count = 0
revenue = 0
high_value_threshold = 200
window_duration = 10
start_time = time.time()

# Make sure history file exists
if not os.path.exists("order_stats_history.json"):
    with open("order_stats_history.json", "w") as f:
        json.dump([], f)

print("Stream processor started...")

while True:
    now = time.time()
    messages = consumer.poll(timeout_ms=1000)

    for _, records in messages.items():
        for msg in records:
            order = msg.value
            amount = order['amount']
            order_count += 1
            revenue += amount

            if amount > high_value_threshold:
                with open('high_value_orders.log', 'a') as f:
                    f.write(json.dumps(order) + '\n')

    # Write stats every 10 seconds
    if now - start_time >= window_duration:
        stats = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "orders": order_count,
            "revenue": round(revenue, 2)
        }
        print(f"🧾 Window closed: {stats}")

        # Overwrite latest snapshot
        with open('order_stats.json', 'w') as f:
            json.dump(stats, f, indent=2)

        # Append to history
        with open('order_stats_history.json', 'r+') as f:
            history = json.load(f)
            history.append(stats)
            f.seek(0)
            json.dump(history[-20:], f, indent=2)  # Keep only last 20 windows
            f.truncate()

        order_count = 0
        revenue = 0
        start_time = now
