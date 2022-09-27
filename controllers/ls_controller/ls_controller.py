"""ls_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

TIMESTEP = 64
MAX_SPEED = 10

def run_robot(robot):
    
    wheels = []
    wheelsName = ['wheel1','wheel2','wheel3','wheel4']
    for ind in range(4):
        wheels.append(robot.getMotor(wheelsName[ind]))
        wheels[ind].setPosition(float('inf'))
        wheels[ind].setVelocity(0.0)
    
    light_sensors = []
    ls_names = ['ls_left','ls_right']
    for ind in range(2):
        light_sensors.append(robot.getLightSensor(ls_names[ind]))
        light_sensors[ind].enable(TIMESTEP)
    
    
    while robot.step(TIMESTEP) != -1:
        
        left_ls_value = light_sensors[0].getValue()/100
        right_ls_value = light_sensors[1].getValue()/100
        
        left_speed = right_ls_value
        right_speed = left_ls_value
        
        print("------------------------------------------------")
        print("left_ls_value : {}".format(left_ls_value))
        print("right_ls_value : {}".format(right_ls_value))
        print("left_speed : {}".format(left_speed))
        print("right_speed : {}".format(right_speed))
        
        wheels[0].setVelocity(left_speed)
        wheels[2].setVelocity(left_speed)
        
        wheels[1].setVelocity(right_speed)
        wheels[3].setVelocity(right_speed)


if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()    
    run_robot(robot)


