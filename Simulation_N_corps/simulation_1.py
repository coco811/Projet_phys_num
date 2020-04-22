import math
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import numpy as np

class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class corps:
    def __init__(self, position, masse, vitesse, nom=""):
        self.position = position
        self.masse = masse
        self.vitesse = vitesse
        self.nom = nom


def calcul_acceleration(corps, index_corps):
    G = 6.67408e-11  # m3 kg-1 s-2
    acceleration = point(0, 0, 0)
    corps_obs = corps[index_corps]
    for index, corps_ext in enumerate(corps):
        if index != index_corps:
            r = (corps_obs.position.x - corps_ext.position.x) ** 2 + (
                        corps_obs.position.y - corps_ext.position.y) ** 2 + (
                            corps_obs.position.z - corps_ext.position.z) ** 2
            r = math.sqrt(r)
            tmp = G * corps_ext.masse / r ** 3
            acceleration.x += tmp * (corps_ext.position.x - corps_obs.position.x)
            acceleration.y += tmp * (corps_ext.position.y - corps_obs.position.y)
            acceleration.z += tmp * (corps_ext.position.z - corps_obs.position.z)

    return acceleration


def calcul_vitesse(corps, pas_temps=1):
    for body_index, corps_obs in enumerate(corps):
        acceleration = calcul_acceleration(corps, body_index)
        corps_obs.vitesse.x += acceleration.x * pas_temps
        corps_obs.vitesse.y += acceleration.y * pas_temps
        corps_obs.vitesse.z += acceleration.z * pas_temps


def calcul_position(corps, pas_temps=1):
    for corps_obs in corps:
        corps_obs.position.x += corps_obs.vitesse.x * pas_temps
        corps_obs.position.y += corps_obs.vitesse.y * pas_temps
        corps_obs.position.z += corps_obs.vitesse.z * pas_temps


def calcul_pas_grav(corps, pas_temps=1):
    calcul_vitesse(corps, pas_temps=pas_temps)
    calcul_position(corps, pas_temps=pas_temps)


def run_simulation(corps, noms=None, pas_temps=1, nombre_de_pas=10000, frequence=100):
    position_des_corps = []
    for corps_etudier in corps:
        position_des_corps.append({"x": [], "y": [], "z": [], "nom": corps_etudier.nom})

    for i in range(1, nombre_de_pas):
        calcul_pas_grav(corps, pas_temps=pas_temps)
        if i % frequence == 0:
            print('ok', i)
            for index, position_corps in enumerate(position_des_corps):
                position_corps["x"].append(corps[index].position.x)
                position_corps["y"].append(corps[index].position.y)
                position_corps["z"].append(corps[index].position.z)
    return position_des_corps


def Graphique(corps, titre, outfile=None):
    fig = plot.figure()
    fig.tight_layout()
    ax = fig.add_subplot(1, 1, 1,projection='3d')
    fig.subplots_adjust(right=0.8)
    r = random.random()
    b = random.random()
    g = random.random()
    couleur = (r, g, b)

    max_range = 0
    for corps_obs in corps:
        r = random.random()
        b = random.random()
        g = random.random()
        couleur = (r, g, b)
        max_dim = max(max(corps_obs["x"]), max(corps_obs["y"]), max(corps_obs["z"]))
        if max_dim > max_range:
            max_range = max_dim
        corps_obs["x"] = np.array(corps_obs["x"]) - np.array(corps[0]["x"])
        corps_obs["y"] = np.array(corps_obs["y"]) - np.array(corps[0]["y"])
        corps_obs["z"] = np.array(corps_obs["z"]) - np.array(corps[0]["z"])
        if corps_obs['nom']=='Simulation\n avec Neptune ':
            ax.scatter(corps_obs["x"], corps_obs["y"], c=couleur, label=corps_obs["nom"],marker='1')
        else:
            ax.plot(corps_obs["x"], corps_obs["y"], corps_obs["z"], c=couleur,
                label=corps_obs["nom"])
    plot.title(titre)
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.legend(loc='center left', bbox_to_anchor=(1.07, 0.5), fontsize=7)
    ax.set_xlabel('Position en x [ $10^{12}$m]')
    ax.set_ylabel('Position en y [ $10^{12}$m]')
    ax.set_zlabel('Position en z [ $10^{12}$m]')
    ax.xaxis.get_offset_text().set_visible(False)
    ax.yaxis.get_offset_text().set_visible(False)
    ax.zaxis.get_offset_text().set_visible(False)
    if outfile:
        plot.savefig(outfile)
    else:
        plot.show()


def Graphique_plusieurs_corps(corps, titre, depart=0, fin=20, outfile=None ):
    fig = plot.figure()
    fig.tight_layout()
    fig.subplots_adjust(right=0.8)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    max_range = 0


    for i in range(depart, fin):
        corps[i]["x"] = np.array(corps[i]["x"]) - np.array(corps[0]["x"])
        corps[i]["y"] = np.array(corps[i]["y"]) - np.array(corps[0]["y"])
        corps[i]["z"] = np.array(corps[i]["z"]) - np.array(corps[0]["z"])
        r = random.random()
        b = random.random()
        g = random.random()
        couleur = (r, g, b)
        max_dim = max(max(corps[i]["x"]), max(corps[i]["y"]), max(corps[i]["z"]))
        if max_dim > max_range:
            max_range = max_dim
        ax.plot(corps[i]["x"], corps[i]["y"], corps[i]["z"], c=couleur,
                label=corps[i]["nom"])
    ax.plot(corps[0]["x"], corps[0]["y"], corps[0]["z"], c='k', label=corps[0]["nom"])
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.legend(loc='center left', bbox_to_anchor=(1.07, 0.5), fontsize=7)
    ax.set_xlabel('Position en x [$10^{12}$m]', labelpad=10)
    ax.set_ylabel('Position en y [$10^{12}$m]', labelpad=10)
    ax.set_zlabel('Position en z [$10^{12}$m]', labelpad=10)
    ax.xaxis.get_offset_text().set_visible(False)
    ax.yaxis.get_offset_text().set_visible(False)
    ax.zaxis.get_offset_text().set_visible(False)
    plot.title(titre)

    if outfile:
        plot.savefig(outfile)
    else:
        plot.show()

def graph2d(corps, titre, depart=0, fin=20, outfile=None):
    fig = plot.figure()
    fig.tight_layout()
    fig.subplots_adjust(right=0.8)
    ax = fig.add_subplot(1, 1, 1)
    max_range = 0
    for corps_obs in corps:
        r = random.random()
        b = random.random()
        g = random.random()
        couleur = (r, g, b)
        max_dim = max(max(corps_obs["x"]), max(corps_obs["y"]))
        if max_dim > max_range:
            max_range = max_dim
        corps_obs["x"]=np.array(corps_obs["x"]) - np.array(corps[0]["x"])
        corps_obs["y"] = np.array(corps_obs["y"]) - np.array(corps[0]["y"])
        corps_obs["z"] = np.array(corps_obs["z"]) - np.array(corps[0]["z"])
        if corps_obs['nom']=='Simulation\n avec Neptune ':
            ax.scatter(corps_obs["x"], corps_obs["y"], c=couleur, label=corps_obs["nom"],marker='1')
        else:
            ax.plot(corps_obs["x"], corps_obs["y"], c=couleur,label=corps_obs["nom"])
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.legend(loc='center left', bbox_to_anchor=(1.07, 0.5), fontsize=7)
    ax.set_xlabel('Position en x [$10^{12}$m]', labelpad=10)
    ax.set_ylabel('Position en y [$10^{12}$m]', labelpad=10)
    ax.xaxis.get_offset_text().set_visible(False)
    ax.yaxis.get_offset_text().set_visible(False)
    plot.title(titre)
    ax.set_aspect('equal')

    if outfile:
        plot.savefig(outfile)
    else:
        plot.show()
