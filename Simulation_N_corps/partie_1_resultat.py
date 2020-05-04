from Simulation_N_corps import extraction_donnees
from Simulation_N_corps import code_simulation as sm1
import numpy as np
from Simulation_N_corps import Graph_2
from Simulation_N_corps import integrateur as inte
try:
    import cPickle as pickle
except ImportError:  # python 3.x
    import pickle
import time

sun = {"position": sm1.point(0, 0, 0), "masse": 2e30, "vitesse": sm1.point(0, 0, 0)}
mercury = {"position": sm1.point(0, 5.7e10, 0), "masse": 3.285e23, "vitesse": sm1.point(47000, 0, 0)}
venus = {"position": sm1.point(0, 1.1e11, 0), "masse": 4.8e24, "vitesse": sm1.point(35000, 0, 0)}
earth = {"position": sm1.point(0, 1.5e11, 0), "masse": 6e24, "vitesse": sm1.point(30000, 0, 0)}
mars = {"position": sm1.point(0, 2.2e11, 0), "masse": 2.4e24, "vitesse": sm1.point(24000, 0, 0)}
jupiter = {"position": sm1.point(0, 7.7e11, 0), "masse": 1e28, "vitesse": sm1.point(13000, 0, 0)}
saturn = {"position": sm1.point(0, 1.4e12, 0), "masse": 5.7e26, "vitesse": sm1.point(9000, 0, 0)}
uranus = {"position": sm1.point(0, 2.8e12, 0), "masse": 8.7e25, "vitesse": sm1.point(7135, 0, 0)}
neptune = {"position": sm1.point(0, 4.5e12, 0), "masse": 1e26, "vitesse": sm1.point(5477, 0, 0)}
pluto = {"position": sm1.point(0, 3.7e12, 0), "masse": 1.3e22, "vitesse": sm1.point(4748, 0, 0)}


if __name__ == "__main__":
    "  Simulation  "

    "  systeme solaire classique  "

    corps_simulation_complete_systeme = [
        sm1.corps(position=sun["position"], masse=sun["masse"], vitesse=sun["vitesse"], nom="Soleil"),
        sm1.corps(position=mercury["position"], masse=mercury["masse"], vitesse=mercury["vitesse"], nom="Mercure"),
        sm1.corps(position=venus["position"], masse=venus["masse"], vitesse=venus["vitesse"], nom="Venus"),
        sm1.corps(position=earth["position"], masse=earth["masse"], vitesse=earth["vitesse"], nom="Earth"),
        sm1.corps(position=mars["position"], masse=mars["masse"], vitesse=mars["vitesse"], nom="Mars"),
        sm1.corps(position=jupiter["position"], masse=jupiter["masse"], vitesse=jupiter["vitesse"], nom="Jupiter"),
        sm1.corps(position=saturn["position"], masse=saturn["masse"], vitesse=saturn["vitesse"], nom="Saturn"),
        sm1.corps(position=uranus["position"], masse=uranus["masse"], vitesse=uranus["vitesse"], nom="Uranus "),
        sm1.corps(position=neptune["position"], masse=neptune["masse"], vitesse=neptune["vitesse"], nom="Neptune "),
    ]
    """ 
    pas_temps=86400 [nb seconde]
    nombre_de_pas=([nb ans] *[nb jours])
    """

    # integration=inte.euler(corps_simulation_complete_systeme,pas_temps=3*86400)
    # mouvement_complet_energie = sm1.run_simulation(integration, nombre_de_pas=(50*365/3), frequence=1)
    # sm1.plot_energie(corps_simulation_complete_systeme,mouvement_complet_energie,4)


    # temps_ini = time.time()
    # integration = inte.euler(corps_simulation_complete_systeme, pas_temps=2 * 86400)
    # mouvement_complet_avec_Neptune = sm1.run_simulation(integration, nombre_de_pas=(165 * 365 / 2), frequence=1)
    # temps_final = time.time()
    # print(temps_final - temps_ini)
    # with open('mouvement_avec_neptune.p', 'wb') as fp:
    #     pickle.dump( mouvement_complet_avec_Neptune , fp, protocol=pickle.HIGHEST_PROTOCOL)

    # with open('mouvement_avec_neptune.p', 'rb') as fp:
    #     mouvement_complet_avec_Neptune_data = pickle.load(fp)

    # sm1.Graphique_plusieurs_corps(mouvement_complet_avec_Neptune_data[0],"Simulation de l'orbite des planètes géantes",5,9,outfile=None)

    "   systeme solaire sans neptune  "

    corps_simulation_sans_Neptune = [
        sm1.corps(position=sun["position"], masse=sun["masse"], vitesse=sun["vitesse"], nom="Soleil"),
        sm1.corps(position=mercury["position"], masse=mercury["masse"], vitesse=mercury["vitesse"], nom="Mercure"),
        sm1.corps(position=venus["position"], masse=venus["masse"], vitesse=venus["vitesse"], nom="Venus"),
        sm1.corps(position=earth["position"], masse=earth["masse"], vitesse=earth["vitesse"], nom="Earth"),
        sm1.corps(position=mars["position"], masse=mars["masse"], vitesse=mars["vitesse"], nom="Mars"),
        sm1.corps(position=jupiter["position"], masse=jupiter["masse"], vitesse=jupiter["vitesse"], nom="Jupiter"),
        sm1.corps(position=saturn["position"], masse=saturn["masse"], vitesse=saturn["vitesse"], nom="Saturn"),
        sm1.corps(position=uranus["position"], masse=uranus["masse"], vitesse=uranus["vitesse"], nom="Uranus "),
    ]
    # integration = inte.euler(corps_simulation_sans_Neptune, pas_temps=2 * 86400)
    # mouvement_complet_sans_Neptune = sm1.run_simulation(integration, nombre_de_pas=(165 * 365/2), frequence=1)
    #
    # with open('mouvement_sans_neptune.p', 'wb') as fp:
    #     pickle.dump( mouvement_complet_sans_Neptune , fp, protocol=pickle.HIGHEST_PROTOCOL)

    # with open('mouvement_sans_neptune.p', 'rb') as fp:
    #     mouvement_complet_sans_Neptune_data = pickle.load(fp)

    # sm1.Graphique_plusieurs_corps(mouvement_complet_sans_Neptune_data[0], "Simulation de l'orbite des planètes géantes sans Neptune", 5, 8, outfile='systeme_sans_neptune')

    "  Comparaison des simulation  "

    " comparaison avec et sans Neptune de l'orbite d'Uranus"

    with open('mouvement_sans_neptune.p', 'rb') as fp:
        mouvement_complet_sans_Neptune_data = pickle.load(fp)
    #
    with open('mouvement_avec_neptune.p', 'rb') as fp:
        mouvement_complet_avec_Neptune_data = pickle.load(fp)

    " Différence de position dans l'orbite Avec\sans"
    rayon_avec = np.sqrt((np.array(mouvement_complet_avec_Neptune_data[0][7]['y']) - np.array(
        mouvement_complet_avec_Neptune_data[0][0]['y'])) ** 2 + (
                                 np.array(mouvement_complet_avec_Neptune_data[0][7]['x']) - np.array(
                             mouvement_complet_avec_Neptune_data[0][0]['x'])) ** 2)
    rayon_sans = np.sqrt((np.array(mouvement_complet_sans_Neptune_data[0][7]['y']) - np.array(
        mouvement_complet_sans_Neptune_data[0][0]['y'])) ** 2 + (
                                 np.array(mouvement_complet_sans_Neptune_data[0][7]['x']) - np.array(
                             mouvement_complet_sans_Neptune_data[0][0]['x'])) ** 2)
    print(f'sans {rayon_sans.mean():.5e}')
    print(f'avec {rayon_avec.mean():.5e}')
    print(f'La différence entre les deux rayons est de: {(abs(rayon_sans.mean() - rayon_avec.mean())):.3e}')
    print(f'Le pourcentage de différence entre les deux rayons est de: {(1 - abs((rayon_avec.mean()) / rayon_sans.mean())) * 100:.3} % ')

    # mouvement_pour_graph=[]
    # mvt=[]
    # mouvement_complet_avec = mouvement_complet_avec_Neptune_data[0]
    # mouvement_complet_sans = mouvement_complet_sans_Neptune_data[0]
    # mouvement_complet_avec[7]['nom'] = 'Simulation\n avec Neptune '
    # mouvement_complet_sans[7]['nom'] = 'Simulation\n sans Neptune '
    # mouvement_pour_graph.append([mouvement_complet_avec[0],mouvement_complet_avec[7]])
    # mouvement_pour_graph.append([mouvement_complet_sans[0], mouvement_complet_sans[7]])

    # Graph_2.Graphique_comparaison_avec_sans( mouvement_pour_graph,
    #               "Graphique de comparaison avec et sans l'influence de Neptune\n sur l'orbite d'Uranus",
    #               outfile='avec_sans_3d')
    # Graph_2.graph2d_compa(mouvement_pour_graph, "Graphique de comparaison avec et sans l'influence de Neptune\n sur l'orbite d'Uranus",outfile=None)

    " Comparaison reference et simulation Uranus avec neptune"

    mouvement_complet = mouvement_complet_avec_Neptune_data[0]
    nom_fichier = 'horizons_results-3.txt'
    nom_planete = 'Réference'
    mouvement_ref = extraction_donnees.extraire_donne(nom_fichier, nom_planete)
    mouvement_complet[7]['nom'] = 'Simulation\n avec Neptune '
    mouvement_ref.append(mouvement_complet)

    # Graph_2.graph3d_ref(mouvement_ref, "Graphique de comparaison avec la référence \n de l'orbite d'Uranus avec l'influence de Neptune ", outfile=None)
    # Graph_2.graph2d_ref(mouvement_ref,"Graphique de comparaison entre la référence \n de l'orbite d'Uranus avec l'influence de Neptune ",outfile=None)

    "Différence de position dansl'orbite Avec \ ref"


    rayon_ref = np.sqrt(np.array(mouvement_ref[0]['y']) ** 2 + np.array(mouvement_ref[0]['x']) ** 2)


    print(f'ref {rayon_ref.mean():.5e}')
    print(f'avec {rayon_avec.mean():.5e}')
    print(
        f'La différence entre les deux rayons est de: {abs(abs(rayon_ref.mean() - rayon_avec.mean())):.5e}  ')

    print(f'Le pourcentage de différence entre les deux rayons est de: {abs(1-abs((rayon_avec.mean()))/rayon_ref.mean())*100:.5} % ')

    "comparaison reference et simulation Uranus sans neptune"

    mouvement_complet =mouvement_complet_sans_Neptune_data[0]
    nom_fichier = 'horizons_results-3.txt'
    nom_planete = 'Réference'
    mouvement_ref = extraction_donnees.extraire_donne(nom_fichier, nom_planete)
    mouvement_complet[7]['nom'] = 'Simulation \n sans Neptune '
    mouvement_ref.append(mouvement_complet)
    # Graph_2.graph3d_ref(mouvement_ref, "Graphique de comparaison entre la référence \n de l'orbite d'Uranus sans l'influence de Neptune ", outfile=None)

    # Graph_2.graph2d_ref(mouvement_ref,
    #             "Graphique de comparaison entre la référence \n de l'orbite d'Uranus sans l'influence de Neptune ",
    #             outfile=None)

    "Différence de position dansl'orbite sans \ ref"

    rayon_ref = np.sqrt(np.array(mouvement_ref[0]['y']) ** 2 + np.array(mouvement_ref[0]['x']) ** 2)

    print(f'ref {rayon_ref.mean():.5e}')
    print(f'sans {rayon_sans.mean():.5e}')
    print(
        f'La différence entre les deux rayons est de: {abs(abs(rayon_ref.mean() - rayon_sans.mean())):.5e}  ')

    print(
        f'Le pourcentage de différence entre les deux rayons est de: { abs(1 - abs(rayon_sans.mean()) / rayon_ref.mean()) * 100} % ')
