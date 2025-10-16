🎯 Overview

Real-Time Sentiment Stream Analyzer adalah aplikasi sederhana yang memanfaatkan Apache Kafka dan HuggingFace Transformers untuk menganalisis sentimen komentar secara real-time.
Aplikasi ini meniru aliran data (streaming pipeline) dari input komentar ke sistem analisis AI, kemudian menampilkan hasil sentimen (positif, negatif, atau netral) secara langsung melalui terminal atau dashboard Streamlit.

⚙️ Tech Stack

🐳 Docker + Kafka + Zookeeper + Kafka UI — platform streaming utama
🐍 Python (venv) — producer, consumer, dan dashboard
🤖 HuggingFace Transformers — model AI untuk analisis sentimen
📊 Streamlit — tampilan dashboard real-time
💬 Kafka-Python — library untuk komunikasi antar topic Kafka
