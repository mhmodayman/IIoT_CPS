#!/usr/bin/env python3
import serial
import json
import time
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT


# Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, MESSAGE, TOPIC, and RANGE
ENDPOINT = "avsnsxi1w2nv8-ats.iot.me-central-1.amazonaws.com"
CLIENT_ID = "iot_thing"
PATH_TO_CERTIFICATE = "d42194e6a78b821823451cc7b1d29896291e00dffd00576f6197250175f33b2b-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "d42194e6a78b821823451cc7b1d29896291e00dffd00576f6197250175f33b2b-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "AmazonRootCA1.pem"
TOPIC = "test/testing"

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)
myAWSIoTMQTTClient.configureMQTTOperationTimeout(1000)
myAWSIoTMQTTClient.connect()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
ser.reset_input_buffer()


def sr():
    reading = ser.readline().decode()
    reading = reading.strip()
    distance = int(reading) if len(reading) > 0 else 0
    return distance


def publish_to_cloud(msg):
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(msg), 1)
    

if __name__ == '__main__':
    counter = 0
    while True:
        distance = sr()
        publish_to_cloud(distance)
        #time.sleep(1)
        print(distance)
