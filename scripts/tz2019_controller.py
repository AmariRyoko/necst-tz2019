#!/usr/bin/env python3

name = 'tz2019_controller'

import rospy

import time
import std_msgs.msg


class controller(object):

    def __init__(self):
        self.ps = PS()
        self.switch = SWITCH()
        self.losg = LOSG()


class PS(object):

    def __init__(self):
        self.pub = {}
        pass

    def publish(self, topic_name, msg):
        self.pub[topic_name].publish(msg)
        return

    def set_publisher(self, topic_name, data_class, queue_size, latch = True):
        if topic_name not in self.pub:
            self.pub[topic_name] = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = queue_size, latch = latch)
            time.sleep(0.01)

        else:
            pass
        return


class SWITCH(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = PS()

    def if_switch(self, command):
        topic_name = '/tz2019/switch/cmd'

        self.ps.set_publisher(topic_name = topic_name, data_class = std_msgs.msg.Float64, queue_size = 1, latch = True)

        self.ps.publish(topic_name = topic_name, msg = command)
        return


class LOSG(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = PS()

    def losg_f(self, command):
        topic_name = '/tz2019/losg/f_cmd'

        self.ps.set_publisher(topic_name = topic_name, data_class = std_msgs.msg.Float64, queue_size = 1, latch = True)

        self.ps.publish(topic_name = topic_name, msg = command)
        return

    def losg_p(self, command):
        topic_name = '/tz2019/losg/p_cmd'

        self.ps.set_publisher(topic_name = topic_name, data_class = std_msgs.msg.Float64, queue_size = 1, latch = True)

        self.ps.publish(topic_name = topic_name, msg = command)
        return
