import ursina
from ursina import *
import numpy as np

app = Ursina()


# Assumption for this solar system project:
#  1. We will make the trajectory of the planets a circle
#  2. We will assume it take the same amount of time for
#     the planets to revolve around the sun
#  3. All planets will be 45 degrees of distance from the
#     planets it's next to as we have 8 planets - sorry Pluto

# rotation/ angle of planets
def update():
    global s
    s = s + 0.02
    angle = np.pi * 45 / 180

    sun.rotation_y += 30 * time.dt

    r1 = 4
    mercury.x = np.cos(s) * r1
    mercury.z = np.sin(s) * r1
    mercury.rotation_y += 30 * time.dt

    r2 = 4.4
    venus.x = np.cos(s + angle) * r2
    venus.z = np.sin(s + angle) * r2
    venus.rotation_y += 30 * time.dt

    r3 = 4.8
    earth.x = np.cos(s + angle * 2) * r3
    earth.z = np.sin(s + angle * 2) * r3
    earth.rotation_y += 30 * time.dt

    r4 = 5.2
    mars.x = np.cos(s + angle * 3) * r4
    mars.z = np.sin(s + angle * 3) * r4
    mars.rotation_y += 30 * time.dt

    r5 = 5.6
    jupiter.x = np.cos(s + angle * 4) * r5
    jupiter.z = np.sin(s + angle * 4) * r5
    jupiter.rotation_y += 30 * time.dt

    r6 = 6.0
    saturn.x = np.cos(s + angle * 5) * r6
    saturn.z = np.sin(s + angle * 5) * r6
    saturn.rotation_y += 30 * time.dt

    r7 = 6.4
    uranus.x = np.cos(s + angle * 6) * r7
    uranus.z = np.sin(s + angle * 6) * r7
    uranus.rotation_y += 30 * time.dt

    r8 = 6.8
    neptune.x = np.cos(s + angle * 7) * r8
    neptune.z = np.sin(s + angle * 7) * r8
    neptune.rotation_y += 30 * time.dt

    # camera_control()

# implement camera controls
# def camera_control():
#     camera.z +=

# background
background = Entity(model='cube', texture='2k_stars_milky_way', scale=50, double_sided=True)

# sun
sun = Entity(model="sphere", texture='2k_sun', scale=4)

# planets- shape, texture (images found from https://www.solarsystemscope.com/textures/) & size of planets
mercury = Entity(model="sphere", texture='2k_mercury', scale=0.4)
venus = Entity(model="sphere", texture='2k_venus_atmosphere', scale=1.2)
earth = Entity(model="sphere", texture='2k_earth', scale=1.2)
mars = Entity(model="sphere", texture='2k_mars', scale=0.8)
jupiter = Entity(model="sphere", texture='2k_jupiter', scale=1.4)
saturn = Entity(model="sphere", texture='2k_saturn', scale=1.2)
uranus = Entity(model="sphere", texture='2k_uranus', scale=0.6)
neptune = Entity(model="sphere", texture='2k_neptune', scale=0.6)

# moon
moon = Entity(model="sphere", texture='2k_moon', position=(0.8, 0, 0.8), scale=0.2)
moon.rotation_y += 50 * time.dt
moon.reparent_to(earth)

# saturn ring
ring = Entity(model="torus", position=saturn.position, scale=1.1)
ring.scale_y = 0.8
ring.texture = 'saturn_ring'
ring.rotation_x = 20
ring.reparent_to(saturn)

s = -np.pi

app.run()
