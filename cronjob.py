import os
import time
from confluent_kafka import Producer
import socket
import json


conf = {
    'bootstrap.servers': "pkc-2396y.us-east-1.aws.confluent.cloud:9092",
    'client.id': socket.gethostname(),
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'B3DQTWKCGZTVSBDL',
    'sasl.password': 'fqRSlQWvnV4bzpCyDVvaqFqJwZyD0xyuSB5YddEicgOjMokLd44zTJtdd/VFEL8/',
}
topic = "fleet-telemetry"
producer = Producer(conf)


def delivery_callback(err, msg):
    if err:
        print('ERROR: Message failed delivery: {}'.format(err))
    else:
        print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
            topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))


# cmd = 'mgeneratejs tracking.json -n 5 | mongoimport --uri mongodb+srv://mycluster-ABCDE.azure.mongodb.net/ \
#    --username=MYUSERNAME \
#    --password=SECRETPASSWORD --collection=mycollectionname'

# cmd = 'mgeneratejs tracking.json -n 1 > data.json'


file = open("data.json", "r")
data = file.read()

while True:
    # os.system(cmd)
    producer.produce(topic, data, callback=delivery_callback)
    print("Telemetry data sent")
    # producer.poll(1) # Aknowledge message sent
    time.sleep(30)
