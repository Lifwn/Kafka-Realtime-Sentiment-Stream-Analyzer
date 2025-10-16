import streamlit as st
from kafka import KafkaConsumer
import json

st.title("📊 Real-Time Sentiment Stream Analyzer")
st.subheader("Live comments sentiment result")

consumer = KafkaConsumer(
    'sentiment-results',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for msg in consumer:
    data = msg.value
    st.write(f"🗨️ {data['comment']}")
    st.progress(data['score'])
    st.write(f"**Sentiment:** {data['label']}")