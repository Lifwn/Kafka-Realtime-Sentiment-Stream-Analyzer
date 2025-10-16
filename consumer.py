from kafka import KafkaConsumer, KafkaProducer
from transformers import pipeline
import json

consumer = KafkaConsumer(
    'comments',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

analyzer = pipeline("sentiment-analysis")

for msg in consumer:
    text = msg.value["comment"]
    result = analyzer(text)[0]
    sentiment = {
        "comment": text,
        "label": result["label"],
        "score": round(result["score"], 2)
    }
    print(f"[RESULT] {text} → {sentiment['label']} ({sentiment['score']})")
    producer.send('sentiment-results', sentiment)
