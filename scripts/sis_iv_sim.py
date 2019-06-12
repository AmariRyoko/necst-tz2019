#!/usr/bin/env python3

name = "sis_iv_sim"

import time
import rospy
import std_msgs.msg


class sis_iv_sim(object):

    def __init__(self):
#hu_vp
        self.sub_hu_vp = rospy.Subscriber(
                name = "/dev/cpz340816rsw0/ch1",
                data_class = std_msgs.msg.Float64,
                callback = self.sis_hu_iv
            )

        self.pub_hu_v = rospy.Publisher(
                name = "/dev/cpz3177/rsw0/ch1",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

        self.pub_hu_i = rospy.Publisher(
                name = "/dev/cpz3177/rsw0/ch5",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

#hl_vp
        self.sub_hl_vp = rospy.Subscriber(
                name = "/dev/cpz340816rsw0/ch2",
                data_class = std_msgs.msg.Float64,
                callback = self.sis_hu_iv
            )

        self.pub_hl_v = rospy.Publisher(
                name = "/dev/cpz3177/rsw0/ch2",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

        self.pub_hl_i = rospy.Publisher(
                name = "/dev/cpz3177/rsw0/ch6",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

#vu_vp
        self.sub_vu_vp = rospy.Subscriber(
                name = "/dev/cpz340816rsw0/ch3",
                data_class = std_msgs.msg.Float64,
                callback = self.sis_hu_iv
            )

        self.pub_hl_v = rospy.Publisher(
                name = "/dev/cpz3177/rsw0/ch3",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

        self.pub_hl_i = rospy.Publisher(
                name = "/dev/cpz3177/rsw0/ch7",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

#vl_vp
        self.sub_vu_vp = rospy.Subscriber(
                name = "/dev/cpz340816rsw0/ch4",
                data_class = std_msgs.msg.Float64,
                callback = self.sis_hu_iv
            )

        self.pub_hl_v = rospy.Publisher(
                name = "/dev/cpz3177/rsw0/ch4",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

        self.pub_hl_i = rospy.Publisher(
                name = "/dev/cpz3177/rsw0/ch8",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

#hu_pub
    def sis_hu_iv(self,q):
        self.pub_hu_v.publish(q.data)
        self.pub_hu_i.publish(q.data)

#hl_pub
    def sis_hl_iv(self,q):
        self.pub_hl_v.publish(q.data)
        self.pub_hl_i.publish(q.data)

#vu_pub
    def sis_hl_iv(self,q):
        self.pub_vu_v.publish(q.data)
        self.pub_vu_i.publish(q.data)

#vl_pub
    def sis_hl_iv(self,q):
        self.pub_vl_v.publish(q.data)
        self.pub_vl_i.publish(q.data)

if __name__ == "__main__":
    rospy.init_node(name)
    rospy.spin()
