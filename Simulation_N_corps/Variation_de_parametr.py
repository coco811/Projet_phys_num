from Simulation_N_corps import Donnée
from Simulation_N_corps import simulation_1 as sm1
from Simulation_N_corps import stockage_des_liste

vrai_sun = {"position": sm1.point(0, 0, 0), "masse": 2e30, "vitesse": sm1.point(0, 0, 1700)}
sun = {"position": sm1.point(0, 0, 0), "masse": 2e30, "vitesse": sm1.point(0, 0, 0)}
mercury = {"position": sm1.point(0, 5.7e10, 0), "masse": 3.285e23, "vitesse": sm1.point(47000, 0, 0)}
venus = {"position": sm1.point(0, 1.1e11, 0), "masse": 4.8e24, "vitesse": sm1.point(35000, 0, 0)}
earth = {"position": sm1.point(0, 1.5e11, 0), "masse": 6e24, "vitesse": sm1.point(30000, 0, 0)}
mars = {"position": sm1.point(0, 2.2e11, 0), "masse": 2.4e24, "vitesse": sm1.point(24000, 0, 0)}
jupiter = {"position": sm1.point(0, 7.7e11, 0), "masse": 1e28, "vitesse": sm1.point(13000, 0, 0)}
saturn = {"position": sm1.point(0, 1.4e12, 0), "masse": 5.7e26, "vitesse": sm1.point(9000, 0, 0)}
uranus = {"position": sm1.point(0, 2.8e12, 0), "masse": 8.7e25, "vitesse": sm1.point(6835, 0, 0)}
neptune = {"position": sm1.point(0, 4.5e12, 0), "masse": 1e26, "vitesse": sm1.point(5477, 0, 0)}
pluto = {"position": sm1.point(0, 5.9e12, 0), "masse": 1.3e22, "vitesse": sm1.point(4748, 1700, 1000)}

# test planète rogue
rogue_1 = {"position": sm1.point(3.7e12, 3.7e12, 0), "masse": 2e28, "vitesse": sm1.point(1300, -1300, 300)}

if __name__ == '__main__':
    # simulation du systeme solaire avec le mouvement vers le haut autour de la galaxie.
    corps_simulation_complete_systeme = [
        sm1.corps(position=vrai_sun["position"], masse=vrai_sun["masse"], vitesse=vrai_sun["vitesse"], nom="Sun"),
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
    # mouvement_complet_avec_mouve_galatic = sm1.run_simulation(corps_simulation_complete_systeme, pas_temps=50000,nombre_de_pas=200000,frequence=1000)
    # print(mouvement_complet_avec_mouve_galatic)
    # mouvement_complet_avec_mouve_galatic= stockage_des_liste.mouve_galatic()
    # sm1.Graphique_plusieurs_corps(mouvement_complet_avec_mouve_galatic,"Simulation de l'orbite des planètes géantes \n avec le mouvement du soleil autour du centre de la galaxie",5, 10, outfile=None)

    # graph 2d
    # mouvement_complet_avec_mouve_galatic_juste_z= stockage_des_liste.mouve_galatic_juste_z()
    # sm1.graph2d(mouvement_complet_avec_mouve_galatic_juste_z,"Graphique de comparaison avec la référence \n de l'orbite d'Uranus avec l'influence de Neptune ",outfile=None)





    # Simulation Rogue 1 Masse:2xjupitere
    corps_simulation_rogue_1 = [
        sm1.corps(position=sun["position"], masse=sun["masse"], vitesse=sun["vitesse"], nom="Sun"),
        sm1.corps(position=mercury["position"], masse=mercury["masse"], vitesse=mercury["vitesse"], nom="Mercure"),
        sm1.corps(position=venus["position"], masse=venus["masse"], vitesse=venus["vitesse"], nom="Venus"),
        sm1.corps(position=earth["position"], masse=earth["masse"], vitesse=earth["vitesse"], nom="Earth"),
        sm1.corps(position=mars["position"], masse=mars["masse"], vitesse=mars["vitesse"], nom="Mars"),
        sm1.corps(position=jupiter["position"], masse=jupiter["masse"], vitesse=jupiter["vitesse"], nom="Jupiter"),
        sm1.corps(position=saturn["position"], masse=saturn["masse"], vitesse=saturn["vitesse"], nom="Saturn"),
        sm1.corps(position=uranus["position"], masse=uranus["masse"], vitesse=uranus["vitesse"], nom="Uranus "),
        sm1.corps(position=neptune["position"], masse=neptune["masse"], vitesse=neptune["vitesse"], nom="Neptune "),
        sm1.corps(position=pluto["position"], masse=pluto["masse"], vitesse=pluto["vitesse"], nom="Pluton"),
        sm1.corps(position=rogue_1["position"], masse=rogue_1["masse"], vitesse=rogue_1["vitesse"],
                  nom=" Première Rogue ")]
    # mouvement_complet_avec_rogue_1 = sm1.run_simulation(corps_simulation_rogue_1, pas_temps=50000, nombre_de_pas=250000,
    #                                                     frequence=1000)
    # mouvement_complet_avec_rogue_1= stockage_des_liste.rogue_1()
    # sm1.Graphique_plusieurs_corps(mouvement_complet_avec_rogue_1,
    #                               "Simulation de l'orbite des planètes géantes \n avec une planète vagabonde",
    #                               5, 11, outfile=None)
