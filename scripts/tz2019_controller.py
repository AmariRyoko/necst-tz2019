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

    def set_pulisher(self, topic_name, data_class, queue_size, latch = True):
        if topic_name not in self.pub:
            self.pub[topic_name] = rospy.Publishr(topic_name = topic_name, data_class = data_class, queue_size = queue_size, latch = latch)
            time.sleep(0.01)

        else:
            pass
        return


class SWITCH(object):
