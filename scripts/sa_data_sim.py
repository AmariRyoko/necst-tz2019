name = "sa_data_sim"

import time
import rospy
import std_msgs.msg
import threading


class sa_data_sim(object):

    def __init__(self):

        self.pub_sa_data = rospy.Publisher(
                name = "/dev/n9343/",
                data_class = std_msgs.msg.Float64,
                latch = True,
                queue_size = 1,
            )

    def data(self):
        while not rospy.is_shutdown():
            self.pub_sa_data.publish(1)
            time.sleep(1)
            continue

    def thread(self):
        th = threading.Thread(target=self.data)
        th.setDaemon(True)
        th.start()



if __name__ == "__main__":

    rospy.init_node(name)
    sa = sa_data_sim()
    sa.thread()
    sa.data()
