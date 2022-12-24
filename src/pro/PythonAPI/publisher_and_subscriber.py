#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


class Echo(object):
    def __init__(self):
        self.value = 0

        rospy.init_node('echoer')

        self.pub = rospy.Publisher('/out_value', Int32, latch=True, queue_size=5)
        rospy.Subscriber('/in_value', Int32, self.update_value)

    def update_value(self, msg):
        self.value = msg.data

    def run(self):
        r = rospy.Rate(1)
        while not rospy.is_shutdown():
            self.pub.publish(self.value)
            r.sleep()
            self.value += 1


if __name__ == '__main__':
    echo_obj = Echo()
    echo_obj.run()
