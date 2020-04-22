
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import numpy as np




def Graphique_comparaison_avec_sans(corps, titre, outfile=None):
    fig = plot.figure()
    fig.tight_layout()
    ax = fig.add_subplot(1, 1, 1,projection='3d')
    fig.subplots_adjust(right=0.8)
    max_range = 0
    for i in range(len(corps)):
        for corps_obs in corps[i]:
            if corps_obs['nom'] !='Soleil':
                r = random.random()
                b = random.random()
                g = random.random()
                couleur = (r, g, b)
                max_dim = max(max(corps_obs["x"]), max(corps_obs["y"]), max(corps_obs["z"]))
                if max_dim > max_range:
                    max_range = max_dim
                corps_obs["x"] = np.array(corps_obs["x"]) - np.array(corps[i][0]["x"])
                corps_obs["y"] = np.array(corps_obs["y"]) - np.array(corps[i][0]["y"])
                corps_obs["z"] = np.array(corps_obs["z"]) - np.array(corps[i][0]["z"])

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

def graph2d_compa(corps, titre, outfile=None):

    fig = plot.figure()
    fig.tight_layout()
    fig.subplots_adjust(right=0.8)
    ax = fig.add_subplot(1, 1, 1)
    max_range = 0

    for i in range(len(corps)):
        for corps_obs in corps[i]:
            if corps_obs['nom'] != 'Soleil':
                r = random.random()
                b = random.random()
                g = random.random()
                couleur = (r, g, b)
                max_dim = max(max(corps_obs["x"]), max(corps_obs["y"]), max(corps_obs["z"]))
                if max_dim > max_range:
                    max_range = max_dim
                corps_obs["x"] = np.array(corps_obs["x"]) - np.array(corps[i][0]["x"])
                corps_obs["y"] = np.array(corps_obs["y"]) - np.array(corps[i][0]["y"])

                if corps_obs['nom'] == 'Simulation\n avec Neptune ':
                    ax.scatter(corps_obs["x"], corps_obs["y"], c=couleur, label=corps_obs["nom"], marker='1')
                else:
                    ax.plot(corps_obs["x"], corps_obs["y"], c=couleur,
                            label=corps_obs["nom"])
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

def graph2d_ref(corps, titre, outfile=None):

    fig = plot.figure()
    fig.tight_layout()
    fig.subplots_adjust(right=0.8)
    ax = fig.add_subplot(1, 1, 1)
    max_range = 0

    soleil_2d = corps[1][0]
    corps[1] = corps[1][7]

    for corps_obs in corps:

        r = random.random()
        b = random.random()
        g = random.random()
        couleur = (r, g, b)
        max_dim = max(max(corps_obs["x"]), max(corps_obs["y"]))

        if max_dim > max_range:
            max_range = max_dim

        if corps_obs['nom'] != 'Réference':
            corps_obs["x"] = np.array(corps_obs["x"]) - np.array(soleil_2d["x"])
            corps_obs["y"] = np.array(corps_obs["y"]) - np.array(soleil_2d["y"])

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

def graph3d_ref(corps, titre, outfile=None):

    fig = plot.figure()
    fig.tight_layout()
    fig.subplots_adjust(right=0.8)
    ax = fig.add_subplot(1, 1, 1,projection='3d')
    max_range = 0

    soleil_2d = corps[1][0]
    corps[1] = corps[1][7]

    for corps_obs in corps:

        r = random.random()
        b = random.random()
        g = random.random()
        couleur = (r, g, b)
        max_dim = max(max(corps_obs["x"]), max(corps_obs["y"]))

        if max_dim > max_range:
            max_range = max_dim

        if corps_obs['nom'] != 'Réference':
            corps_obs["x"] = np.array(corps_obs["x"]) - np.array(soleil_2d["x"])
            corps_obs["y"] = np.array(corps_obs["y"]) - np.array(soleil_2d["y"])
            corps_obs["z"] = np.array(corps_obs["z"]) - np.array(soleil_2d["z"])

        if corps_obs['nom']=='Simulation\n avec Neptune ':
            ax.scatter(corps_obs["x"], corps_obs["y"], c=couleur, label=corps_obs["nom"],marker='1')

        else:
            ax.plot(corps_obs["x"], corps_obs["y"],corps_obs['z'], c=couleur,label=corps_obs["nom"])

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
