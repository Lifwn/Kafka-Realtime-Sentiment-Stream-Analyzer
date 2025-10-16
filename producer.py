from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

comments = [
    "I love this app, it's so useful!",
    "The service was terrible and slow.",
    "Pretty decent experience overall.",
    "Worst product ever.",
    "I'm extremely satisfied with the support team!"
]

while True:
    msg = {"comment": random.choice(comments)}
    producer.send('comments', msg)
    print("Sent:", msg)
    time.sleep(2)
