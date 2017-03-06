## The spaceship class has two fields:
# self.angle is the ship orientation (the angle, in radians, of the ship's forward velocity from the x-axis)
# self.angle_vel is the speed in which the ship moves in the current direction

## Acceleration
# Acceleration can be modeled by increasing the velocity with time, just as in Pong...
# ...increasing the velocity increased the speed with time (positive 2nd derivative!)
# Acceleration adds itself to the velocity vector for every time step. This velocity...
# ...vector is in turn added to the position vector.
# The acceleration vector is given as: forward = [math.cos(self.angle), math.sin(self.angle)]

## Friction
# Friction can be modeled by scaling the velocity vector by a slightly negative number...
# In the limit, the velocity vector will go to zero.
