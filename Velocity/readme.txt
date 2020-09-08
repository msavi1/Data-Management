1. Avviare zookeeper da promt 1: C:\kafka_2.12-2.0.0>zookeeper-server-start.bat config\zookeeper.properties 
2. Avviare kafka da promt 2: C:\kafka_2.12-2.0.0>kafka-server-start.bat config\server.properties
3. Avviare consumer da promt 3: C:\kafka_2.12-2.0.0>kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic LCDP
4. Avviare MongoDB da promt4: C:\Program Files\MongoDB\Server\4.4\bin\mongo.exe
5. Eseguire Producer.py
6. Eseguire Consumer.py