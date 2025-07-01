from kafka import KafkaProducer
import json
import random
import time
import uuid

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

categories = ['books', 'electronics', 'fashion']

for _ in range(100):
    order = {
        "order_id": str(uuid.uuid4()),
        "amount": round(random.uniform(5, 500), 2),
        "category": random.choice(categories)
    }
    producer.send('orders', order)
    print(f"Produced: {order}")
    time.sleep(0.5)

producer.flush()
