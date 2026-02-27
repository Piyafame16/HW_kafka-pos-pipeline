from kafka import KafkaConsumer, KafkaProducer

try:
    consumer = KafkaConsumer('swu-lab', bootstrap_servers=['localhost:9092'])
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    print("--- Stream Processor Running ---")
    for msg in consumer:
        data = msg.value.decode('utf-8').upper() # แปลงเป็นตัวพิมพ์ใหญ่
        producer.send('swu-processed', value=data.encode('utf-8'))
        print(f"Processed & Sent: {data}")
        producer.flush()
except Exception as e:
    print(f"Error: {e}")