#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ContactsState
import sys
import numpy as np


initiated = False
write_or_append = 'w'
fileName = None
suffix = ""
suffix_2 = ""
direction = None
spd = None

def callback(data):
    global write_or_append
    global initiated
    global fileName
    global suffix, direction, spd

    if fileName == None:
        if suffix == "":
            fileName = rospy.get_param("impact_listener/impact_fileName", "impact_test")
            fileName += "_"
            fileName += suffix_2
            fileName += "_"
            fileName += direction
            fileName += "_"
            fileName += "%0.1f" % spd
            fileName += ".txt"
            
        else:
            fileName = rospy.get_param("impact_listener_%s/impact_fileName" % suffix, "impact_test")
            fileName += "_"+suffix
            fileName += "_"
            fileName += suffix_2
            fileName += "_"
            fileName += direction
            fileName += "_"
            fileName += "%0.1f" % (spd)
            fileName += ".txt"
            rospy.loginfo("filename else:")
            rospy.loginfo(fileName)
    
    rospy.loginfo("In callback")
    rospy.loginfo(fileName)
    timeIndex = -14 #Hardcode starting time index for info variable
    #print("------Running------")
    #print(data)
    states = data.states
    lengthStates = len(states)
    #print("SHAPE OF STATES: ---------------")
    #print(np.shape(states))
    #print(states[0].total_wrench)
    print("filename: ", fileName)

    
    if initiated:
        write_or_append = 'a'
    else:
        initiated = True
    write(fileName, states, lengthStates, timeIndex, write_or_append, direction, spd)

def write(fileName, states, lengthStates, timeIndex, write_or_append, direction,spd):
    with open(fileName, write_or_append) as f:
        for i in range(lengthStates):
            collision_time = states[i].info[timeIndex:]
            name_collision_link = states[i].collision1_name
            name_collision_with = states[i].collision2_name
            #wrenches = states[i].wrenches
            total_wrench = states[i].total_wrench
            f_x = total_wrench.force.x
            f_y = total_wrench.force.y
            f_z = total_wrench.force.z
            #text = "%s %3.4f" % (collision_time.strip(), f_z)
            text = "%s %s %s %s %0.1f %3.4f %3.4f %3.4f" % (collision_time.strip(), name_collision_link,
                                                    name_collision_with, direction, spd, f_x, f_y, f_z)
            f.write(text)
            f.write('\n')

def stop_callback(event):
    rospy.signal_shutdown("Killing impact listener node")

def listener():
    global suffix, suffix_2
    global spd

    # Get required parameters
    listeningDuration = rospy.get_param("time2Kill", 0) # Default set such that node is not killed
    spd = 0.1 * rospy.get_param("speed_mult",1)
    suffix_2 = rospy.get_param("suffix_2", "")

    rospy.init_node('force_listener', anonymous=True)
    
    if suffix == "":
        subTopicName = "/foot_link_contact_state"
    else:
        subTopicName = "/%s_foot_link_contact_state" % suffix
    rospy.Subscriber(subTopicName,ContactsState, callback, queue_size=500)
    if listeningDuration > 0.0:
        rospy.Timer(rospy.Duration(listeningDuration), stop_callback)

    rospy.spin()

def main(argv):
    global suffix, direction
    try:
        suffix = argv[1]
        direction = argv[2]
    except:
        print("No suffix specified. Default to: %s" % suffix)
    listener()

if __name__ == '__main__':
    main(sys.argv)