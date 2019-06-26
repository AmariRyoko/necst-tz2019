#! /usr/bin/env python3
name = "temp_data_sim"

import time
import rospy
import std_msgs.msg
import threading


class temp_data_sim(object):

    def __init__(self):


        self.pub_temp_data_4k = rospy.Publisher(
                name = "/dev/218/ip_192_168_100_187/ch1",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

        self.pub_temp_data_sis1 = rospy.Publisher(
                name = "/dev/218/ip_192_168_100_187/ch2",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

        self.pub_temp_data_sis2 = rospy.Publisher(
                name = "/dev/218/ip_192_168_100_187/ch3",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

        self.pub_temp_data_70k = rospy.Publisher(
                name = "/dev/218/ip_192_168_100_187/ch4",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

    def data(self):
        while not rospy.is_shutdown():
            self.pub_temp_data_4k.publish(1)
            self.pub_temp_data_70k.publish(1)
            self.pub_temp_data_sis1.publish(1)
            self.pub_temp_data_sis2.publish(1)
            time.sleep(1)
            continue

    def thread(self):
        th = threading.Thread(target=self.data)
        th.setDaemon(True)
        th.start()



if __name__ == "__main__":

    rospy.init_node(name)
    temp = temp_data_sim()
    temp.thread()
    rospy.spin()
