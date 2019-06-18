#! /usr/bin/env python3
name = "vacuum_data_sim"

import time
import rospy
import std_msgs.msg
import threading


class vacuum_data_sim(object):

    def __init__(self):


        self.pub_vacuum_data = rospy.Publisher(
                name = "/dev/tpg/usb/f_cmd",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

    def data(self):
        while not rospy.is_shutdown():
            self.pub_vacuum_data.publish(1)
            time.sleep(1)
            continue

    def thread(self):
        th = threading.Thread(target=self.data)
        th.setDaemon(True)
        th.start()



if __name__ == "__main__":

    rospy.init_node(name)
    v = vacuum_data_sim()
    v.thread()
    rospy.spin()
