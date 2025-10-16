from kafka import KafkaProducer
import json

# Inisialisasi producer Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("=== Real-Time Comment Producer ===")
print("Ketik komentar kamu (atau ketik 'exit' untuk keluar):")

while True:
    comment = input("> ")
    if comment.lower() == "exit":
        print("Keluar dari producer...")
        break

    msg = {"comment": comment}
    producer.send('comments', msg)
    print("Terkirim ke Kafka:", msg)
