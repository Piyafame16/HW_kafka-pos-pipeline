 Real-Time POS Data Pipeline with Apache Kafka

โปรเจกต์จำลองการทำ Data Pipeline สำหรับข้อมูลธุรกรรมร้านค้า (Point of Sale) โดยใช้ Apache Kafka ในการรับ-ส่งข้อมูลแบบ Real-time และประมวลผลข้อมูลกลางทาง

System Architecture
โปรเจกต์นี้ทำงานตามแผนผัง Pipeline ดังนี้:
1. Producer: อ่านข้อมูลจากไฟล์ `pos_transaction.csv` แล้วส่ง (Publish) ข้อมูลไปยัง Kafka Topic: `swu-lab`
2. Stream Processor: ดึงข้อมูลจาก `swu-lab` มาประมวลผล (Data Transformation) โดยการแปลงข้อความเป็นตัวพิมพ์ใหญ่ (Upper Case) และส่งต่อไปยัง Topic: `swu-processed`
3. Consumer: รับข้อมูลที่ประมวลผลแล้วจาก `swu-processed` มาบันทึกลงไฟล์ `output_data.csv` ซึ่งเปรียบเสมือนการบันทึกลง Database หรือ Data Lake

Tech Stack
- Apache Kafka & Zookeeper (Confluent Platform)
- Docker สำหรับการจำลอง Infrastructure
- Python (Library: `kafka-python`)
