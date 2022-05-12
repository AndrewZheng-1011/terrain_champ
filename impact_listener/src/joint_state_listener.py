#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
import numpy as np

initiated = False
write_or_append = 'w'
fileName = None
direction = None
spd = None
suffix_2 = ""

def callback(data):
    global write_or_append
    global initiated
    global fileName
    global spd, direction, suffix_2

    if fileName == None:
        fileName = rospy.get_param("joint_state_listener/joint_state_fileName", "joint_state_test")
        fileName += "_"
        fileName += suffix_2
        fileName += "_"
        fileName += direction
        fileName += "_"
        fileName += "%0.1f" % spd
        fileName +=".txt"
    time_sec = data.header.stamp.secs
    time_nsec = float(data.header.stamp.nsecs) * 1e-9
    timeIndex = time_sec+time_nsec
    #print(timeIndex)
    names = data.name
    positions = data.position
    velocities = data.velocity
    efforts = data.effort

    #print("------Running------")
    
    
    if initiated:
        write_or_append = 'a'
    else:
        initiated = True
    write(fileName, timeIndex, names, positions, velocities, efforts, write_or_append)
    


def write(fileName, timeIndex, names, positions, velocities, efforts, write_or_append):
    text = ""
    with open(fileName, write_or_append) as f:
        text += "%3.4f" % timeIndex
        #print(len(names))
        for i in range(len(names)):
            text += "%3.4f " % positions[i]
        for i in range(len(names)):
            text += "%3.4f " % velocities[i]
        for i in range(len(names)):
            text += "%3.4f " % efforts[i]
        f.write(text)
        f.write('\n')


def stop_callback(event):
    rospy.signal_shutdown("Killing impact listener node")
            
def listener():
    global direction, spd, suffix_2
    listeningDuration = rospy.get_param("time2Kill", 0)
    direction = rospy.get_param("quad_cmd", "forward")
    spd = 0.1 * rospy.get_param("speed_mult",1)
    suffix_2 = rospy.get_param("suffix_2", "")
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('joint_state_listener', anonymous=True)
    

    rospy.Subscriber("/joint_states",JointState, callback, queue_size=500)
    if listeningDuration > 0:
        rospy.Timer(rospy.Duration(listeningDuration), stop_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()