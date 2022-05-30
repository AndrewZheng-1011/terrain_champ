#!/bin/bash


# Notes:
#       1) Representing more action (side to side or left and then right repeated)
#               - Or clockwise and counterclockwise
#       2) Modify xacro file of champ s.t. can change kp and kd values through script
description_file="/home/andrewzheng1011/champ_ws/src/terrain_champ/champ/champ_description/urdf/champ.urdf.xacro"
environment='emptyWorld'
worldFilePath="/home/andrewzheng1011/champ_ws/src/terrain_champ/impact_listener/worlds/emptyWorld.world"
#"/home/andrewzheng1011/champ_ws/src/impact_listener/worlds/planeWorld.world"

time2Term="120" # seconds
displayNum=7 # Which multiplier to showcase gazebo gui
actions=('forward' 'backward' 'left' 'right')
gui="false" # false to run in "headless" mode
spawnHeight="0.6" # Spawn height for plane > 1.0m and < 1.5m (#1.2 seems good for blue plane and 0.6 for empty world)


for action in "${actions[@]}"
do
        for speedMult in {1..7} # Base speed: 0.1 with speed_mult --> speed = base * speedMult
        do
                if [ $speedMult -eq $displayNum ]
                then
                        gui="true"
                fi
                #echo $gui
                echo "Running action $action with environment: $environment"
                echo "---------------------------------------------------"
                echo "Speed Multipler: $speedMult"
                roslaunch impact_listener start.launch suffix_2:=$environment quad_cmd:=$action \
                speed_mult:=$speedMult time2Terminate:=$time2Term height_spawn:=$spawnHeight worldFile:=$worldFilePath \
                gui:=$gui description_file:=$description_file
                gui="false"
        done
done