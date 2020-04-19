from Simulation_N_corps import simulation_1 as sm1
import math
import random
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

sun = {"location": sm1.point(0, 0, 0), "mass": 2e30, "velocity": sm1.point(0, 0, 0)}
mercury = {"location": sm1.point(0, 5.7e10, 0), "mass": 3.285e23, "velocity": sm1.point(47000, 0, 0)}
venus = {"location": sm1.point(0, 1.1e11, 0), "mass": 4.8e24, "velocity": sm1.point(35000, 0, 0)}
earth = {"location": sm1.point(0, 1.5e11, 0), "mass": 6e24, "velocity": sm1.point(30000, 0, 0)}
mars = {"location": sm1.point(0, 2.2e11, 0), "mass": 2.4e24, "velocity": sm1.point(24000, 0, 0)}
jupiter = {"location": sm1.point(0, 7.7e11, 0), "mass": 1e28, "velocity": sm1.point(13000, 0, 0)}
saturn = {"location": sm1.point(0, 1.4e12, 0), "mass": 5.7e26, "velocity": sm1.point(9000, 0, 0)}
uranus = {"location": sm1.point(0, 2.8e12, 0), "mass": 8.7e25, "velocity": sm1.point(6835, 0, 0)}
neptune = {"location": sm1.point(0, 4.5e12, 0), "mass": 1e26, "velocity": sm1.point(5477, 0, 0)}
pluto = {"location": sm1.point(0, 3.7e12, 0), "mass": 1.3e22, "velocity": sm1.point(4748, 0, 0)}

if __name__ == "__main__":
    # build list of planets in the simulation, or create your own
    bodies = [
        sm1.body(location=sun["location"], mass=sun["mass"], velocity=sun["velocity"], name="sun"),
        sm1.body(location=earth["location"], mass=earth["mass"], velocity=earth["velocity"], name="earth"),
        sm1.body(location=mars["location"], mass=mars["mass"], velocity=mars["velocity"], name="mars"),
        sm1.body(location=venus["location"], mass=venus["mass"], velocity=venus["velocity"], name="venus"),
    ]
    # sm1.body(location=jupiter["location"], mass=jupiter["mass"], velocity=jupiter["velocity"], name="jupiter"),
    # sm1.body(location=saturn["location"], mass=saturn["mass"], velocity=saturn["velocity"], name="saturn"),
    # sm1.body(location=uranus["location"], mass=uranus["mass"], velocity=uranus["velocity"], name="uranus "),
    # sm1.body(location=neptune["location"], mass=neptune["mass"], velocity=neptune["velocity"], name="neptune ")
    motions = sm1.run_simulation(bodies, time_step=100, number_of_steps=80000, report_freq=1000)
    print(motions)
    sm1.plot_output(motions, outfile=None)
    # sm1.animation3d(motions, 'allo')