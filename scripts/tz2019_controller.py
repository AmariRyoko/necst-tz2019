#!/usr/bin/env python3

name = 'tz2019_controller'

import rospy

import time
import std_msgs.msg


class controller(object):

    def __init__(self):
        self.switch = switch()
        self.losg = losg()
        self.loatt_h = loatt_h()
        self.loatt_v = loatt_v()


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


class switch(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_ch(self, command):
        topic_name = '/tz2019/switch/cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class losg(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_freq(self, command):
        topic_name = '/tz2019/losg/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_power(self, command):
        topic_name = '/tz2019/losg/p_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class loatt_h(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_vol(self, command):
        topic_name = '/dev/vcva/ip192.168.100.183'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class loatt_v(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_vol(self, command):
        topic_name = '/dev/vcva/ip192.168.100.184'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return
