from kafka import KafkaConsumer
import json
import time
from collections import defaultdict

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='order-processor',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Aggregation buckets
order_count = 0
revenue = 0
high_value_threshold = 200
stats_interval = 10  # seconds
start_time = time.time()

while True:
    msg = next(consumer)
    order = msg.value
    amount = order['amount']
    order_count += 1
    revenue += amount

    # High-value order alert
    if amount > high_value_threshold:
        with open('high_value_orders.log', 'a') as f:
            f.write(json.dumps(order) + '\n')

    # Every N seconds, save current stats
    if time.time() - start_time >= stats_interval:
        stats = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "orders": order_count,
            "revenue": round(revenue, 2)
        }
        print("Saving stats:", stats)
        with open('order_stats.json', 'w') as f:
            json.dump(stats, f, indent=2)

        # Reset for next interval
        order_count = 0
        revenue = 0
        start_time = time.time()
