import random

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


def run_simulation(integrateur, nombre_de_pas=10000, frequence=100):
    position_des_corps = []
    vitesse_des_corps = []
    for corps_etudier in integrateur.corps:
        position_des_corps.append({"x": [], "y": [], "z": [], "nom": corps_etudier.nom})
        vitesse_des_corps.append({"vx": [], "vy": [], "vz": [], "nom": corps_etudier.nom})
    for i in range(1, int(nombre_de_pas)):
        integrateur.calcul_pas_graviter()

        if i % frequence == 0:
            print('ok', i)
            for index, position_corps in enumerate(position_des_corps):
                position_corps["x"].append(integrateur.corps[index].position.x)
                position_corps["y"].append(integrateur.corps[index].position.y)
                position_corps["z"].append(integrateur.corps[index].position.z)

            for index_vit, vitesse_corps in enumerate(vitesse_des_corps):
                vitesse_corps["vx"].append(integrateur.corps[index_vit].vitesse.x)
                vitesse_corps["vy"].append(integrateur.corps[index_vit].vitesse.y)
                vitesse_corps["vz"].append(integrateur.corps[index_vit].vitesse.z)

    return position_des_corps, vitesse_des_corps


def plot_energie(corps, mouvemnt_corps, indice_planete):
    vitesse = mouvemnt_corps[1]
    energie = []
    nb_pas = len(mouvemnt_corps[1][1]['vx'])
    masse = []
    for indice_1, corps_etudier in enumerate(corps):
        masse.append(corps_etudier.masse)
        energie.append({"T": [], "nom": corps_etudier.nom})

    for i in range(1, int(nb_pas)):
        for index, vitesse_du_corps in enumerate(vitesse):
            T = 0.5 * masse[index] * (
                        vitesse_du_corps['vx'][i] ** 2 + vitesse_du_corps['vz'][i] ** 2 + vitesse_du_corps['vy'][
                    i] ** 2)
            energie[index]["T"].append(T)

    fig = plot.figure()
    ax = fig.add_subplot(1, 1, 1)
    temps = np.linspace(0, int(nb_pas), int(nb_pas) - 1)
    ax.plot(temps, energie[indice_planete]['T'])
    plot.title(f'Énergie cinétique de {vitesse[indice_planete]["nom"]} selon le temps ')
    ax.set_xlabel('Temps[s]')
    ax.set_ylabel('Énergie cinétique [J]')
    # print(nb_pas/(365/3))
    # plot.xticks(np.arange(0, int(nb_pas/(365/3)+2), step=1) )
    plot.show()


def Graphique(corps, titre, outfile=None):
    fig = plot.figure()
    fig.tight_layout()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    fig.subplots_adjust(right=0.8)
    max_range = 0
    for corps_obs in corps:
        r = random.random()
        b = random.random()
        g = random.random()
        couleur = (r, g, b)
        max_dim = max(max(corps_obs["x"]), max(corps_obs["y"]), max(corps_obs["z"]))
        if max_dim > max_range:
            max_range = max_dim

        if corps_obs['nom'] != 'Réference':
            corps_obs["x"] = np.array(corps_obs["x"]) - np.array(corps[0]["x"])
            corps_obs["y"] = np.array(corps_obs["y"]) - np.array(corps[0]["y"])
            corps_obs["z"] = np.array(corps_obs["z"]) - np.array(corps[0]["z"])

        if corps_obs['nom'] == 'Simulation\n avec Neptune ':
            ax.scatter(corps_obs["x"], corps_obs["y"], c=couleur, label=corps_obs["nom"], marker='1')
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


def Graphique_plusieurs_corps(corps, titre, depart=0, fin=20, outfile=None):
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


def Graphique_plusieurs_corps_sans_mvt_sol(corps, titre, depart=0, fin=20, outfile=None):
    fig = plot.figure()
    fig.tight_layout()
    fig.subplots_adjust(right=0.8)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    max_range = 0

    for i in range(depart, fin):
        if i != 0:
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


def Graphique_plusieurs_corps_galac(corps, titre, depart=0, fin=20, outfile=None):
    fig = plot.figure()
    fig.tight_layout()
    fig.subplots_adjust(right=0.8)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    max_range = 0

    for i in range(depart, fin):
        if i != 0:
            corps[i]["x"] = np.array(corps[i]["x"]) - np.array(corps[0]["x"])
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

        corps_obs["x"] = np.array(corps_obs["x"]) - np.array(corps[0]["x"])
        corps_obs["y"] = np.array(corps_obs["y"]) - np.array(corps[0]["y"])

        if corps_obs['nom'] == 'Simulation\n avec Neptune ':
            ax.scatter(corps_obs["x"], corps_obs["y"], c=couleur, label=corps_obs["nom"], marker='1')

        else:
            ax.plot(corps_obs["x"], corps_obs["y"], c=couleur, label=corps_obs["nom"])

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
