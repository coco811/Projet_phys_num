from Simulation_N_corps import extraction_donnees
from Simulation_N_corps import code_simulation as sm1
from Simulation_N_corps import stockage_des_liste
from Simulation_N_corps import Graph_2

sun = {"position": sm1.point(0, 0, 0), "masse": 2e30, "vitesse": sm1.point(0, 0,0)}
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
    # mouvement_complet = sm1.run_simulation(corps_simulation_complete_systeme, pas_temps=12500, nombre_de_pas=400000,frequence=1000)
    # mouvement_complet=stockage_des_liste.avec_neptune()
    # sm1.Graphique_plusieurs_corps(mouvement_complet,"Simulation de l'orbite des planètes géantes",5,9,outfile=None)


    "   systeme solaire sans neptune  "

    corps_simulation_sans_Neptune = [
        sm1.corps(position=sun["position"], masse=sun["masse"], vitesse=sun["vitesse"], nom="Sun"),
        sm1.corps(position=mercury["position"], masse=mercury["masse"], vitesse=mercury["vitesse"], nom="Mercure"),
        sm1.corps(position=venus["position"], masse=venus["masse"], vitesse=venus["vitesse"], nom="Venus"),
        sm1.corps(position=earth["position"], masse=earth["masse"], vitesse=earth["vitesse"], nom="Earth"),
        sm1.corps(position=mars["position"], masse=mars["masse"], vitesse=mars["vitesse"], nom="Mars"),
        sm1.corps(position=jupiter["position"], masse=jupiter["masse"], vitesse=jupiter["vitesse"], nom="Jupiter"),
        sm1.corps(position=saturn["position"], masse=saturn["masse"], vitesse=saturn["vitesse"], nom="Saturn"),
        sm1.corps(position=uranus["position"], masse=uranus["masse"], vitesse=uranus["vitesse"], nom="Uranus "),
    ]

    # mouvement_complet_sans_Neptune = sm1.run_simulation(corps_simulation_sans_Neptune, pas_temps=10000, nombre_de_pas=250000,
    #                                                     frequence=1000)
    # mouvement_complet_sans_Neptune = stockage_des_liste.sans_neptune()
    # sm1.Graphique_plusieurs_corps(mouvement_complet_sans_Neptune, "Simulation de l'orbite des planètes géantes sans Neptune", 5, 8, outfile=None)



    "  Comparaison des simulation  "


    " comparaison avec et sans Neptune de l'orbite d'Uranus"

    # mouvement_pour_graph=[]
    # mvt=[]
    # mouvement_complet_avec = stockage_des_liste.avec_neptune()
    # mouvement_complet_sans = stockage_des_liste.sans_neptune()
    # mouvement_complet_avec[7]['nom'] = 'Simulation\n avec Neptune '
    # mouvement_complet_sans[7]['nom'] = 'Simulation\n sans Neptune '
    # mouvement_pour_graph.append([mouvement_complet_avec[0],mouvement_complet_avec[7]])
    # mouvement_pour_graph.append([mouvement_complet_sans[0], mouvement_complet_sans[7]])

    # Graph_2.Graphique_comparaison_avec_sans( mouvement_pour_graph,
    #               "Graphique de comparaison avec et sans l'influence de Neptune\n sur l'orbite d'Uranus",
    #               outfile=None)
    # Graph_2.graph2d_compa(mouvement_pour_graph,"Graphique de comparaison avec la référence \n de l'orbite d'Uranus avec l'influence de Neptune ",outfile=None)

    "  Comparaison reference et simulation Uranus Avec neptune  "

    # mouvement_complet = stockage_des_liste.avec_neptune()
    # nom_fichier = 'horizons_results-3.txt'
    # nom_planete = 'Réference'
    # mouvement_ref = Donnée.extraire_donne(nom_fichier, nom_planete)
    # mouvement_complet[7]['nom'] = 'Simulation\n avec Neptune '
    # mouvement_ref.append(mouvement_complet)
    # Graph_2.graph3d_ref(mouvement_ref, "Graphique de comparaison avec la référence \n de l'orbite d'Uranus avec l'influence de Neptune ", outfile=None)
    # Graph_2.graph2d_ref(mouvement_ref,"Graphique de comparaison avec la référence \n de l'orbite d'Uranus avec l'influence de Neptune ",outfile=None)



    "comparaison reference et simulation Uranus sans neptune"

    # mouvement_complet = stockage_des_liste.sans_neptune()
    # nom_fichier = 'horizons_results-3.txt'
    # nom_planete = 'Réference'
    # mouvement_ref = Donnée.extraire_donne(nom_fichier, nom_planete)
    # mouvement_complet[7]['nom'] = 'Simulation \n sans Neptune '
    # mouvement_ref.append(mouvement_complet)
    # print(mouvement_ref)
    # Graph_2.graph3d_ref(mouvement_ref, "Graphique de comparaison avec la référence \n de l'orbite d'Uranus sans l'influence de Neptune ", outfile=None)

    # Graph_2.graph2d_ref(mouvement_ref,
    #             "Graphique de comparaison avec la référence \n de l'orbite d'Uranus avec l'influence de Neptune ",
    #             outfile=None)