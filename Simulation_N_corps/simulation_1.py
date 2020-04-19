import math
import random
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
class point:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class corps:
    def __init__(self, position, masse, vitesse, nom = ""):
        self.position = position
        self.masse = masse
        self.vitesse = vitesse
        self.nom = nom

def calcul_acceleration(corps, index_corps):
    G = 6.67408e-11 #m3 kg-1 s-2
    acceleration = point(0,0,0)
    corps_obs = corps[index_corps]
    for index, corps_ext in enumerate(corps):
        if index != index_corps:
            r = (corps_obs.position.x - corps_ext.position.x)**2 + (corps_obs.position.y - corps_ext.position.y)**2 + (corps_obs.position.z - corps_ext.position.z)**2
            r = math.sqrt(r)
            tmp = G * corps_ext.mass / r**3
            acceleration.x += tmp * (corps_ext.position.x - corps_obs.position.x)
            acceleration.y += tmp * (corps_ext.position.y - corps_obs.position.y)
            acceleration.z += tmp * (corps_ext.position.z - corps_obs.position.z)

    return acceleration

def calcul_vitesse(corps, pas_temps = 1):
    for body_index, corps_obs in enumerate(corps):
        acceleration = calcul_acceleration(corps, body_index)
        corps_obs.velocity.x += acceleration.x * pas_temps
        corps_obs.velocity.y += acceleration.y * pas_temps
        corps_obs.velocity.z += acceleration.z * pas_temps

def calcul_position(corps, pas_temps = 1):
    for corps_obs in corps:
        corps_obs.position.x += corps_obs.velocity.x * pas_temps
        corps_obs.position.y += corps_obs.velocity.y * pas_temps
        corps_obs.position.z += corps_obs.velocity.z * pas_temps

def calcul_pas_grav(corps, pas_temps = 1):
    calcul_vitesse(corps, pas_temps = pas_temps)
    calcul_position(corps, pas_temps = pas_temps)


def run_simulation(corps, noms=None, pas_temps=1,nombre_de_pas=10000, frequence=100):
    position_des_corps = []
    for corps_etudier in corps:
        position_des_corps.append({"x": [], "y": [], "z": [], "nom": corps_etudier.nom})

    for i in range(1,nombre_de_pas):
        calcul_pas_grav(corps, pas_temps=1000)

        if i % frequence == 0:
            for index, position_corps in enumerate(position_des_corps):
                position_corps["x"].append(corps[index].position.x)
                position_corps["y"].append(corps[index].position.y)
                position_corps["z"].append(corps[index].position.z)
    print(position_des_corps)
    return position_des_corps


def plot_output(corps, outfile=None):
    fig = plot.figure()
    colours = ['r', 'b', 'g', 'y', 'm', 'c']
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    max_range = 0
    for current_body in corps:
        max_dim = max(max(current_body["x"]), max(current_body["y"]), max(current_body["z"]))
        if max_dim > max_range:
            max_range = max_dim
        ax.plot(current_body["x"], current_body["y"], current_body["z"], c=random.choice(colours),
                label=current_body["nom"])

    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.legend()

    if outfile:
        plot.savefig(outfile)
    else:
        plot.show()

