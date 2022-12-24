#!/usr/bin/env python3.6
import ssl
import paho.mqtt.client as paho


awshost = "avsnsxi1w2nv8-ats.iot.me-central-1.amazonaws.com"  # Endpoint
awsport = 8883  # Port no.
clientId = "iot_thing"  # Thing_Name
thingName = "iot_thing"  # Thing_Name
caPath = "AmazonRootCA1.pem"  # Root_CA_Certificate_Name
certPath = "d42194e6a78b821823451cc7b1d29896291e00dffd00576f6197250175f33b2b-certificate.pem.crt"  # <Thing_Name>.cert.pem
keyPath = "d42194e6a78b821823451cc7b1d29896291e00dffd00576f6197250175f33b2b-private.pem.key"  # <Thing_Name>.private.key
TOPIC = "test/testing"


def on_connect(client, userdata, flags, rc):  # func for making connection
    print("Connection returned result: " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC, 1)  # Subscribe to all topics


# def on_log(client, userdata, level, msg):
#    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()  # mqttc object
mqttc.on_connect = on_connect  # assign on_connect func
# mqttc.on_log = on_log

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
mqttc.connect(awshost, awsport, keepalive=60)  # connect to aws server
#mqttc.loop_start()
