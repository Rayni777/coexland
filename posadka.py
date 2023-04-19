import rospy
from clover import srv
from std_srvs.srv import Trigger
import dynamic_reconfigure.client
from clover.srv import SetLEDEffect
import os

#подгрузить карту аруко

set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
arming = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)

rospy.init_node('flight')

set_effect(effect='flash', r=255, g=0, b=0) 

navigate(x=0, y=0, z=2, frame_id='body', speed=0.5, auto_arm=True)  # взлет на 2 метра

time.sleep(5)

navigate(frame_id='aruco_5', x=0, y=0, z=1)

time.sleep(5)

navigate(frame_id='aruco_5', x=0, y=0, z=1)

time.sleep(5)

set_effect(effect='flash', r=255, g=0, b=0)  # синий

navigate(frame_id='aruco_101', x=0, y=0, z=0.1)

def land_wait():
    land()
    while get_telemetry().armed:
        rospy.sleep(0.2)

set_effect(effect='flash', r=255, g=0, b=0)  #зелёный

land_wait()
arming(False)  # дизарм


