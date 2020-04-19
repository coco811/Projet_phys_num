from Simulation_N_corps import simulation_1 as sm1
import math
import random
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

sun = {"position": sm1.point(0, 0, 0), "masse": 2e30, "vitesse": sm1.point(0, 0, 0)}
mercury = {"position": sm1.point(0, 5.7e10, 0), "masse": 3.285e23, "vitesse": sm1.point(47000, 0, 0)}
venus = {"position": sm1.point(0, 1.1e11, 0), "masse": 4.8e24, "vitesse": sm1.point(35000, 0, 0)}
earth = {"position": sm1.point(0, 1.5e11, 0), "masse": 6e24, "vitesse": sm1.point(30000, 0, 0)}
mars = {"position": sm1.point(0, 2.2e11, 0), "masse": 2.4e24, "vitesse": sm1.point(24000, 0, 0)}
jupiter = {"position": sm1.point(0, 7.7e11, 0), "masse": 1e28, "vitesse": sm1.point(13000, 0, 0)}
saturn = {"position": sm1.point(0, 1.4e12, 0), "massee": 5.7e26, "vitesse": sm1.point(9000, 0, 0)}
uranus = {"position": sm1.point(0, 2.8e12, 0), "masse": 8.7e25, "vitesse": sm1.point(6835, 0, 0)}
neptune = {"position": sm1.point(0, 4.5e12, 0), "masse": 1e26, "vitesse": sm1.point(5477, 0, 0)}
pluto = {"position": sm1.point(0, 3.7e12, 0), "masse": 1.3e22, "vitesse": sm1.point(4748, 0, 0)}

if __name__ == "__main__":
    # build list of planets in the simulation, or create your own
    bodies = [
        sm1.corps(position=sun["position"], masse=sun["masse"], vitesse=sun["vitesse"], nom="sun"),
        sm1.corps(position=earth["position"], masse=earth["masse"], vitesse=earth["vitesse"], nom="earth"),
        sm1.corps(position=mars["position"], masse=mars["masse"], vitesse=mars["vitesse"], nom="mars"),
        sm1.corps(position=venus["position"], masse=venus["masse"], vitesse=venus["vitesse"], nom="venus"),
    ]
    # sm1.corps(position=jupiter["position"], masse=jupiter["masse"], vitesse=jupiter["vitesse"], nom="jupiter"),
    # sm1.corps(position=saturn["position"], masse=saturn["masse"], vitesse=saturn["vitesse"], nom="saturn"),
    # sm1.corps(position=uranus["position"], masse=uranus["masse"], vitesse=uranus["vitesse"], nom="uranus "),
    # sm1.corps(position=neptune["position"], masse=neptune["masse"], vitesse=neptune["vitesse"], nom="neptune ")
    motions = sm1.run_simulation(bodies, pas_temps=100, nombre_de_pas=80000, frequence=1000)
    print(motions)
    sm1.plot_output(motions, outfile=None)
    # sm1.animation3d(motions, 'allo')