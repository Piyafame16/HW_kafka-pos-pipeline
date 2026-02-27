import csv
import os
from kafka import KafkaConsumer

try:
    print("Connecting to Kafka...")
    consumer = KafkaConsumer(
        'swu-processed',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        group_id='csv-group',
        consumer_timeout_ms=10000  # ถ้าไม่มีข้อมูลใน 10 วินาทีให้แจ้ง
    )
    print("Connected! Waiting for messages from 'swu-processed'...")

    filename = 'output_data.csv'
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # เขียนหัวตารางถ้าไฟล์ยังว่าง
        if os.path.getsize(filename) == 0 if os.path.exists(filename) else True:
            writer.writerow(['Topic', 'Partition', 'Offset', 'Message_Value'])

        for message in consumer:
            data_value = message.value.decode('utf-8')
            writer.writerow([message.topic, message.partition, message.offset, data_value])
            file.flush()
            print(f"-> Recorded: {data_value}")

except Exception as e:
    print(f"Error: {e}")