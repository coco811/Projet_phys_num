from Simulation_N_corps import extraction_donnees
from Simulation_N_corps import code_simulation as sm1
try:
    import cPickle as pickle
except ImportError:  # python 3.x
    import pickle
from Simulation_N_corps import integrateur as inte
import numpy as np
from Simulation_N_corps import Graph_2

vrai_sun = {"position": sm1.point(0, 0, 0), "masse": 2e30, "vitesse": sm1.point(0, 0, 1700)}
sun = {"position": sm1.point(0, 0, 0), "masse": 2e30, "vitesse": sm1.point(0, 0, 0)}
mercury = {"position": sm1.point(0, 5.7e10, 0), "masse": 3.285e23, "vitesse": sm1.point(47000, 0, 0)}
venus = {"position": sm1.point(0, 1.1e11, 0), "masse": 4.8e24, "vitesse": sm1.point(35000, 0, 0)}
earth = {"position": sm1.point(0, 1.5e11, 0), "masse": 6e24, "vitesse": sm1.point(30000, 0, 0)}
mars = {"position": sm1.point(0, 2.2e11, 0), "masse": 2.4e24, "vitesse": sm1.point(24000, 0, 0)}
jupiter = {"position": sm1.point(0, 7.7e11, 0), "masse": 1e28, "vitesse": sm1.point(13000, 0, 0)}
saturn = {"position": sm1.point(0, 1.4e12, 0), "masse": 5.7e26, "vitesse": sm1.point(9000, 0, 0)}
uranus = {"position": sm1.point(0, 2.8e12, 0), "masse": 8.7e25, "vitesse": sm1.point(7135, 0, 0)}
neptune = {"position": sm1.point(0, 4.5e12, 0), "masse": 1e26, "vitesse": sm1.point(5477, 0, 0)}
pluto = {"position": sm1.point(0, 5.9e12, 0), "masse": 1.3e22, "vitesse": sm1.point(4748, 1700, 1000)}

# Planéte 9
#  situé a environ (350-800 ua) et masse environ (10mt)
planete_9_min = {"position": sm1.point(0, 3e13, 0), "masse": 10*6e24, "vitesse": sm1.point(3267.80,0, 0)}


if __name__ == '__main__':

    "simulation du systeme solaire avec le mouvement vers le haut autour de la galaxie."

    corps_simulation_complete_systeme = [
        sm1.corps(position=vrai_sun["position"], masse=vrai_sun["masse"], vitesse=vrai_sun["vitesse"], nom="Soleil"),
        sm1.corps(position=mercury["position"], masse=mercury["masse"], vitesse=mercury["vitesse"], nom="Mercure"),
        sm1.corps(position=venus["position"], masse=venus["masse"], vitesse=venus["vitesse"], nom="Venus"),
        sm1.corps(position=earth["position"], masse=earth["masse"], vitesse=earth["vitesse"], nom="Earth"),
        sm1.corps(position=mars["position"], masse=mars["masse"], vitesse=mars["vitesse"], nom="Mars"),
        sm1.corps(position=jupiter["position"], masse=jupiter["masse"], vitesse=jupiter["vitesse"], nom="Jupiter"),
        sm1.corps(position=saturn["position"], masse=saturn["masse"], vitesse=saturn["vitesse"], nom="Saturn"),
        sm1.corps(position=uranus["position"], masse=uranus["masse"], vitesse=uranus["vitesse"], nom="Uranus "),
        sm1.corps(position=neptune["position"], masse=neptune["masse"], vitesse=neptune["vitesse"], nom="Neptune "),
        sm1.corps(position=pluto["position"], masse=pluto["masse"], vitesse=pluto["vitesse"], nom="Pluton")
    ]

    # graph 3d  du mouvement
    # integration = inte.euler(corps_simulation_complete_systeme, pas_temps=2 * 86400)
    # mouvement_complet_avec_mouve_galatic = sm1.run_simulation(integration,nombre_de_pas=182*365/2,frequence=1)

    # with open('mouvement_complet_avec_mouve_galatic.p', 'wb') as fp:
    #     pickle.dump( mouvement_complet_avec_mouve_galatic , fp, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('mouvement_complet_avec_mouve_galatic.p', 'rb') as fp:
    #     mouvement_complet_avec_mouve_galatic_data = pickle.load(fp)
    # sm1.Graphique_plusieurs_corps_galac(mouvement_complet_avec_mouve_galatic_data[0],"Simulation de l'orbite des planètes géantes \n avec le mouvement du soleil autour du centre de la galaxie",5, 10, outfile=None)

    # graph 2d
    # mouvement_complet_avec_mouve_galatic_juste_z= stockage_des_liste.mouve_galatic_juste_z()
    # sm1.graph2d(mouvement_complet_avec_mouve_galatic_juste_z,"Graphique de comparaison avec la référence \n de l'orbite d'Uranus avec l'influence de Neptune ",outfile=None)

    "Simulation planete X(9) "

    corps_simulation_planete_9_min = [
        sm1.corps(position=sun["position"], masse=sun["masse"], vitesse=sun["vitesse"], nom="Soleil"),
        sm1.corps(position=mercury["position"], masse=mercury["masse"], vitesse=mercury["vitesse"], nom="Mercure"),
        sm1.corps(position=venus["position"], masse=venus["masse"], vitesse=venus["vitesse"], nom="Venus"),
        sm1.corps(position=earth["position"], masse=earth["masse"], vitesse=earth["vitesse"], nom="Earth"),
        sm1.corps(position=mars["position"], masse=mars["masse"], vitesse=mars["vitesse"], nom="Mars"),
        sm1.corps(position=jupiter["position"], masse=jupiter["masse"], vitesse=jupiter["vitesse"], nom="Jupiter"),
        sm1.corps(position=saturn["position"], masse=saturn["masse"], vitesse=saturn["vitesse"], nom="Saturn"),
        sm1.corps(position=uranus["position"], masse=uranus["masse"], vitesse=uranus["vitesse"], nom="Uranus "),
        sm1.corps(position=neptune["position"], masse=neptune["masse"], vitesse=neptune["vitesse"], nom="Neptune "),
        sm1.corps(position=pluto["position"], masse=pluto["masse"], vitesse=pluto["vitesse"], nom="Pluton"),
        sm1.corps(position=planete_9_min["position"], masse=planete_9_min["masse"], vitesse=planete_9_min["vitesse"],
                  nom=" Première 9 ")]

    # integration = inte.euler(corps_simulation_planete_9_min, pas_temps=7 * 86400)
    # mouvement_complet_avec_planete_9_min = sm1.run_simulation(integration,nombre_de_pas=1000*365/7,frequence=1)
    # with open('mouvement_complet_avec_planete_9_min.p', 'wb') as fp:
    #     pickle.dump(mouvement_complet_avec_planete_9_min, fp, protocol=pickle.HIGHEST_PROTOCOL)

    # sm1.Graphique_plusieurs_corps(mouvement_complet_avec_planete_9_min[0],"Simulation du système solaire (Planètes Géantes) \n avec une planète 9",8, 11, outfile=None)

    nom_fichier = 'horizons_results-3.txt'
    nom_planete = 'Réference'
    mouvement_ref = extraction_donnees.extraire_donne(nom_fichier, nom_planete)

    with open('mouvement_avec_neptune.p', 'rb') as fp:
        mouvement_avec_neptune = pickle.load(fp)
    with open('mouvement_complet_avec_planete_9_min.p', 'rb') as fp:
        mouvement_complet_avec_planete_9_min = pickle.load(fp)

    """ comparaison orbite 9 et reference"""
    mouvement_complet = mouvement_complet_avec_planete_9_min[0]
    mouvement_complet[7]['nom'] = 'Simulation\n avec planète 9 '
    mouvement_ref.append(mouvement_complet)
    # Graph_2.graph2d_ref(mouvement_ref,
    #                     "Graphique de comparaison entre la référence \n de l'orbite d'Uranus avec l'influence de la planète 9 ",
    #                     outfile=None)
    rayon_avec_9 = np.sqrt((np.array(mouvement_complet_avec_planete_9_min[0][7]['y']) - np.array(mouvement_complet_avec_planete_9_min[0][0]['y'])) ** 2 + (
                                 np.array(mouvement_complet_avec_planete_9_min[0][7]['x']) - np.array(
                             mouvement_complet_avec_planete_9_min[0][0]['x'])) ** 2)
    rayon_ref = np.sqrt(np.array(mouvement_ref[0]['y']) ** 2 + np.array(mouvement_ref[0]['x']) ** 2)
    print(f'rayon de la réference :{rayon_ref.mean():.5e}')
    print(f'rayon avec planète 9 :{rayon_avec_9.mean():.5e}')
    print(f'La différence entre les deux rayons est de: {abs(abs(rayon_ref.mean() - rayon_avec_9.mean())):.5e}  ')

    print(f'Le pourcentage de différence entre les deux rayons est de: {abs(1 - abs((rayon_avec_9.mean())) / rayon_ref.mean()) * 100:.5} % ')

    # sm1.Graphique_plusieurs_corps(mouvement_complet_avec_planete_9_max[0],"Simulation du système solaire (Planètes Géantes) \n avec une planète 9", 8, 11,outfile=None)

    # """ comparaison orbite 9 et simulation avec Neptune"""

    with open('mouvement_complet_avec_planete_9_min.p', 'rb') as fp:
        mouvement_complet_avec_planete_9_min = pickle.load(fp)
    with open('mouvement_avec_neptune.p', 'rb') as fp:
        mouvement_avec_neptune_2 = pickle.load(fp)


    mouvement_complet_avec_9 = mouvement_complet_avec_planete_9_min[0]
    rayon_avec = np.sqrt((np.array(mouvement_complet_avec_9[7]['y']) - np.array(mouvement_complet_avec_9[0]['y'])) ** 2 + (
            np.array(mouvement_complet_avec_9[7]['x']) - np.array(
        mouvement_complet_avec_9[0]['x'])) ** 2)
    rayon_ref_2 = np.sqrt((np.array(mouvement_avec_neptune_2[0][7]['y']) - np.array(mouvement_avec_neptune_2[0][0]['y'])) ** 2 + (
            np.array(mouvement_avec_neptune_2[0][7]['x']) - np.array(mouvement_avec_neptune_2[0][0]['x'])) ** 2)
    print(f'rayon sans planète 9 :{rayon_ref_2.mean():.5e}')
    print(f'rayon avec planète 9 :{rayon_avec.mean():.5e}')
    print(f'La différence entre les deux rayons est de: {abs(abs(rayon_ref_2.mean() - rayon_avec.mean())):.5e}  ')

    print(f'Le pourcentage de différence entre les deux rayons est de: {abs(1 - abs((rayon_avec.mean())) / rayon_ref_2.mean()) * 100:.5} % ')

    mouvement_pour_graph = []
    mvt=[]
    mouvement_complet_sans_9 = mouvement_avec_neptune_2[0]
    mouvement_complet_avec_9[7]['nom'] = 'Simulation\n avec planète 9 '
    mouvement_complet_sans_9[7]['nom'] = 'Simulation\n sans planète 9'
    mouvement_pour_graph.append([mouvement_complet_sans_9[0], mouvement_complet_sans_9[7]])
    mouvement_pour_graph.append([mouvement_complet_avec_9[0],mouvement_complet_avec_9[7]])

    # Graph_2.graph2d_compa(mouvement_pour_graph, "Graphique de comparaison avec et sans l'influence de la planète 9 \n sur l'orbite d'Uranus",outfile=None)
#
