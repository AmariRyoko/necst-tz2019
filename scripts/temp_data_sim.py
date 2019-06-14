#topic(/dev/218/)にデータを投げるだけのsimulator用script(温度計用シミュレータ)
name = "temp_data_sim"

import time
import rospy
import std_msgs.msg
import threading


class sa_data_sim(object):

    def __init__(self):


        self.pub_temp_data = rospy.Publisher(
                name = "/dev/218/",
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
    sa = temp_data_sim()
    sa.thread()
    sa.data()
    rospy.spin()
