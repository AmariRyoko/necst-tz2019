#!/usr/bin/env python3

name = 'tz2019_tuning_controler'

import rospy
import time
import std_msgs.msg


class controller(object):

    def __init__(self):
        self.loatt_tuning = loatt_tuning()


class make_pub(object):

    def __init__(self):

        self.pub = {}
        pass

    def publish(self, topic_name, data_class, msg):
        if topic_name not in self.pub:
            self.set_publisher(topic_name = topic_name, data_class = data_class)
            pass

        self.pub[topic_name].publish(msg)
        return

    def set_publisher(self, topic_name, data_class):
        if topic_name not in self.pub:
            self.pub[topic_name] = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = False)
            time.sleep(0.01)
            pass
        return


class loatt_tuning(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_loatth_tuning(self, command):
        topic_name = '/dev/vcva/ip192.168.100.183'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_loattv_tuning(self, command):
        topic_name = '/dev/vcva/ip192.168.100.184'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return
