#!/usr/bin/env python3.7

import time
import sys
sys.path.append("/home/m/catkin_ws/src/pro/scripts/PythonAPI/iot")
import rospy
import random
from std_msgs.msg import Float32
from subscribe import mqttc


class Echo(object):
    def __init__(self):
        rospy.init_node('echoer')
        self.pub = rospy.Publisher('/out_value', Float32, latch=True, queue_size=10)
        rospy.Subscriber('/out_value', Float32)
        self.distance = 0

    def on_message(self, client, userdata, msg):  # Func for receiving msgs
        # print("topic: " + msg.topic)
        # print("payload: " + str(msg.payload))
        self.distance = int(msg.payload.decode("utf-8"))
        print(msg.payload, self.distance)

    def run(self):
        mqttc.loop_start()
        while not rospy.is_shutdown():
            self.pub.publish(self.distance)


if __name__ == '__main__':
    echo_obj = Echo()
    mqttc.on_message = echo_obj.on_message  # assign on_message func
    time.sleep(0.1)
    echo_obj.run()
