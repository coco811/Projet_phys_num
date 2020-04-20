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
saturn = {"position": sm1.point(0, 1.4e12, 0), "masse": 5.7e26, "vitesse": sm1.point(9000, 0, 0)}
uranus = {"position": sm1.point(0, 2.8e12, 0), "masse": 8.7e25, "vitesse": sm1.point(6835, 0, 0)}
neptune = {"position": sm1.point(0, 4.5e12, 0), "masse": 1e26, "vitesse": sm1.point(5477, 0, 0)}
pluto = {"position": sm1.point(0, 3.7e12, 0), "masse": 1.3e22, "vitesse": sm1.point(4748, 0, 0)}

if __name__ == "__main__":
    # systeme solaire classique
    corps_simulation_complete_systeme = [
        sm1.corps(position=sun["position"], masse=sun["masse"], vitesse=sun["vitesse"], nom="Sun"),
        sm1.corps(position=earth["position"], masse=earth["masse"], vitesse=earth["vitesse"], nom="Earth"),
        sm1.corps(position=mars["position"], masse=mars["masse"], vitesse=mars["vitesse"], nom="Mars"),
        sm1.corps(position=venus["position"], masse=venus["masse"], vitesse=venus["vitesse"], nom="Venus"),
        sm1.corps(position=jupiter["position"], masse=jupiter["masse"], vitesse=jupiter["vitesse"], nom="Jupiter"),
        sm1.corps(position=saturn["position"], masse=saturn["masse"], vitesse=saturn["vitesse"], nom="Saturn"),
        sm1.corps(position=uranus["position"], masse=uranus["masse"], vitesse=uranus["vitesse"], nom="Uranus "),
        sm1.corps(position=neptune["position"], masse=neptune["masse"], vitesse=neptune["vitesse"], nom="Neptune ")
    ]

    mouvement= sm1.run_simulation(corps_simulation_complete_systeme, pas_temps=10000, nombre_de_pas=200000, frequence=5000)
    # sm1.Graphique(motions, outfile=None)
    sm1.Graphique_uranus_seul(mouvement,"Graphique de l'orbite d'Uranus avec l'influence de Neptune",outfile=None)
    sm1.Graphique_uranus_neptune(mouvement, "Graphique de l'orbite d'Uranus et de Neptune avec l'influence de Neptune", outfile=None)
