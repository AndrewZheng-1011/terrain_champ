#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist

def talker(command, spd_mult):
    msgTwist = Twist()

    pub = rospy.Publisher('cmd_vel/',Twist, queue_size=1)
    rospy.init_node('quadr_cmd', anonymous=True)
    rate = rospy.Rate(20)
    
    msgTwist.linear.x = 0.0
    msgTwist.linear.y = 0.0
    msgTwist.linear.z = 0.0
    msgTwist.angular.x = 0.0
    msgTwist.angular.y = 0.0
    msgTwist.angular.z = 0.0

    if command == "forward":
        msgTwist.linear.x = 0.1*float(spd_mult)
    elif command == "backward":
        msgTwist.linear.x = -0.1*float(spd_mult)
    elif command =="left":
        msgTwist.linear.y = -0.1*float(spd_mult)
    elif command == "right":
        msgTwist.linear.y = 0.1*float(spd_mult)

    while not rospy.is_shutdown():
        pub.publish(msgTwist)
        rate.sleep()

if __name__ == '__main__':
    '''
    Runs system to command quadruped to do a gait operation
    '''
    print(sys.argv)
    command = sys.argv[1]
    spd_mult = sys.argv[2]
    try:

        from time import sleep
        print('Sleeping 3 seconds to publish')
        sleep(3)
        print('Sleep finished.')
        talker(command, spd_mult)
    except rospy.ROSInterruptException:
        pass