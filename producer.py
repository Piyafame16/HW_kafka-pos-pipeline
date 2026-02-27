import csv
import time
from kafka import KafkaProducer

try:
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    topic = 'swu-lab'
    
    with open('pos_transaction.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("--- Starting Producer ---")
        for row in reader:
            # ดึงข้อมูล Product_Name และ Total_Price มาส่ง
            message = f"{row['Transaction_ID']},{row['Product_Name']},{row['Total_Price']}"
            producer.send(topic, value=message.encode('utf-8'))
            print(f"Sent: {message}")
            time.sleep(0.5) # ส่งทีละนิดให้เห็น flow
            producer.flush()
except Exception as e:
    print(f"Error: {e}")