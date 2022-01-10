"""
1.15.2: Sphere volume.
"""

# pi = 3.14159
# sphere_volume = 0.0

# sphere_radius = float(input())

# sphere_volume = ((4.0 / 3.0 ) * pi) * sphere_radius**3

# print('Sphere volume: {:.2f}'.format(sphere_volume))

G = 6.673e-11
M = 5.98e24
accel_gravity = 0.0

dist_center = 6.3782e6

''' (G * M) / (d 2)  6.3782e6'''

accel_gravity = (G * M) / (dist_center**2)

print('Acceleration of gravity: {:.2f}'.format(accel_gravity))