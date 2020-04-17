
import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt

from Simulation_leapfrog import methode_saute_mouton as sp


# Conditions initiales

rA = np.array([1, 2])
rB = np.array([-2, 1])
rC = np.array([1, -1])
positions = np.array([rA, rB, rC])

vitA = np.array([0.1, 0.1])
vitB = np.array([0.1, 0.1])
vitC = np.array([0.1, 0.1])

vitesses = np.array([vitA, vitB, vitC])

masse = np.array([3, 4, 5])

systeme_solaire_symplifier={'corps':['A','B','C'],
                            'position':positions,
                            'vitesse':vitesses,
                            'masse':masse}


''' exploration '''
rA_explo = np.array([1, 7])
rB_explo = np.array([-2, -1])
rC_explo = np.array([0, -2])
positions_explo = np.array([rA_explo, rB_explo, rC_explo])

vitA_explo = np.array([32, 4])
vitB_explo = np.array([-6, 12])
vitC_explo = np.array([0, 5])

vitesses_explo = np.array([vitA_explo, vitB_explo, vitC_explo])

masse_explo = np.array([20, 2, 7])

''' constante du c'''

rA_c = np.array([3.3030197, -0.82771837])
rB_c = np.array([-3.3030197, 0.82771837])
rC_c = np.array([0, 0])
positions_c = np.array([rA_c, rB_c, rC_c])

vitA_c = np.array([1.587433767 , 1.47221479])
vitB_c = np.array([1.587433767 ,1.47221479])
vitC_c = np.array([-3.174867535 ,-2.94442961])

vitesses_c = np.array([vitA_c, vitB_c, vitC_c])

masse_c = np.array([1, 1, 1])


''' exploration_c) '''
rA_explo_c = np.array([3.3030197, -4])
rB_explo_c = np.array([8, 0.82771837])
rC_explo_c = np.array([2, 1])
positions_explo_c = np.array([rA_explo_c, rB_explo_c, rC_explo_c])

vitA_explo_c = np.array([13 , 0])
vitB_explo_c = np.array([22.3 ,-5.6])
vitC_explo_c = np.array([-7.174867535 ,-2.94442961])

vitesses_explo_c = np.array([vitA_explo_c, vitB_explo_c, vitC_explo_c])

masse_explo_c = np.array([17, 3, 2])

def limitie(donne,nb_objet):

    liste_xextr=[]
    liste_yextr=[]

    for i in range(nb_objet):
        x_max=donne[i][0][np.argmax(donne[i][0])]
        x_min = donne[i][0][np.argmin(donne[i][0])]
        liste_xextr.append(x_max)
        liste_xextr.append(x_min)
        y_max = donne[i][1][np.argmax(donne[i][1])]
        y_min = donne[i][1][np.argmin(donne[i][1])]
        liste_yextr.append(y_max)
        liste_yextr.append(y_min)
    array_x=np.array(liste_xextr)
    array_y = np.array(liste_yextr)
    X_max_to=array_x[np.argmax(array_x)]
    Y_max_to = array_y[np.argmax(array_y)]
    X_min_to = array_x[np.argmin(array_x)]
    Y_min_to = array_y[np.argmin(array_y)]
    return [(X_min_to-2,X_max_to+2),(Y_min_to-2,Y_max_to+2)]

def Animation(donnes_a_anime,titre):

    nb_points = len(donnes_a_anime[0][0])

    data = {'xA': donnes_a_anime[0][0], 'yA': donnes_a_anime[0][1], 'xB': donnes_a_anime[1][0],
            'yB': donnes_a_anime[1][1], 'xC': donnes_a_anime[2][0], 'yC': donnes_a_anime[2][1]}
    borne=limitie(donnes_a_anime,3)
    fig = plt.figure()
    ax = plt.axes(xlim=borne[0],
                  ylim=borne[1])

    lines = [ax.plot([], [])[0] for _ in range(3)]
    lines[0].set_color('r')
    lines[1].set_color('b')
    lines[2].set_color('g')
    lines[0].set_label('Corps A')
    lines[1].set_label('Corps B')
    lines[2].set_label('Corps C')

    xdataA, ydataA = [], []
    xdataB, ydataB = [], []
    xdataC, ydataC = [], []


    def animate(i):
        xdataA.append(data["xA"][i])
        ydataA.append(data["yA"][i])
        xdataB.append(data["xB"][i])
        ydataB.append(data["yB"][i])
        xdataC.append(data["xC"][i])
        ydataC.append(data["yC"][i])
        lines[0].set_data(xdataA, ydataA)
        lines[1].set_data(xdataB, ydataB)
        lines[2].set_data(xdataC, ydataC)

        return lines

    anim = animation.FuncAnimation(fig, animate, frames=nb_points, interval=2, repeat=False,blit=True)
    plt.title(titre)
    plt.xlabel('position en x')
    plt.ylabel('position en y')
    plt.legend()
    plt.show()
    # writer = animation.writers['imagemagick'](fps=30)
    # anim.save(f'/{titre}.gif',writer=writer)








if __name__ == '__main__':

    sp.saute_mouton(systeme_solaire_symplifier,0,10).__call__()















    # """ liste des points du a) [[[x1...],[y1...]],[[x2...],[y2...]],[[x3...],[y3...]]] """
    # # collision de deux corps et après libération
    # trajectoire_num_a = methode_saute_mouton.leapfrog(positions, vitesses, 0, 1, 1000, masse)
    # Animation(trajectoire_num_a,"Animation de la solution au problème à 3 corps")
    # #
    # '''exploration'''
    #
    # ''' variation dans les vitesse initial'''
    # # corps bleu et verre reste lier gravitaionnelment
    # # corps rouge atteint vitesse de liberation et criss sont camps
    # trajectoire_num_explo_1 = methode_saute_mouton.leapfrog(positions, vitesses_explo, 0, 1, 1000, masse)
    # Animation(trajectoire_num_explo_1,"Animation de la solution au problème à 3 corps avec différente vitesse")
    #
    # ''' variation dans les positions de dépars'''
    # # collision bleu et vert et senfuit apres
    # # coprs rouge A possede une masse plus petite et est trop loins l'influence des deux autre devient negligable et donc reste presque stable.
    # trajectoire_num_explo_2 = methode_saute_mouton.leapfrog(positions_explo, vitesses, 0, 1, 1000, masse)
    # Animation(trajectoire_num_explo_2,"Animation de la solution au problème à 3 corps avec différente position de départ")
    #
    # ''' variation dans les masses'''
    # #  corps A le plus massif et donc lui qui apres la collision vas le moins loins
    # #  les deux autres se retrouvent projeter plus loins a cause de l'echange d'energie
    # trajectoire_num_explo_2 = methode_saute_mouton.leapfrog(positions, vitesses, 0, 1, 1000, masse_explo)
    # Animation(trajectoire_num_explo_2,"Animation de la solution au problème à 3 corps avec différente masse")
    #
    #
    #
    #
    # ''' liste des points du b) '''
    # # Commen en A mais plus long donc les objetvont plus loins. Ne sont plus lier gravitationnelemnt
    # trajectoire_b = methode_saute_mouton.leapfrog(positions, vitesses, 0, 10, 10000, masse)
    #
    # Animation(trajectoire_b,"Longue animation de la solution au problème à 3 corps ")
    #
    #
    #
    # ''' liste des points du c) '''
    # #  la trjaectoire donne une orbite stable en forme d'infini malade.
    # # stabiliter atteint. On a ici une belle demonstration d'un systeme stable d'etoiles triple
    # # orbitant les une autours des autre
    # trajectoire_c = methode_saute_mouton.leapfrog(positions_c, vitesses_c, 0, 10, 10000, masse_c)
    #
    # Animation(trajectoire_c,"Animation de la solution au problème à 3 corps dans les années 2000")
    #
    # '''exploration c)'''
    #
    # ''' variation dans les vitesse initial en c)'''
    # # Vitesse vient grandement influence la chose. On perd totalement la stabiliter qu'on avait.
    #
    # trajectoire_num_explo_1_c = methode_saute_mouton.leapfrog(positions_c, vitesses_explo_c, 0, 10, 1000, masse_c)
    # Animation(trajectoire_num_explo_1_c,"Animation de la solution au problème à 3 corps des années 2000 \n avec différente vitesse")
    #
    # ''' variation dans les positions de départ en c)'''
    # # On voit que Rouge(A) et bleue (B) reste liée gravitationellement par la suite.(orbite une et autre autours du centre de masse)
    # # Dans ce cas les masse sont toute egale a 1 donc. mais si m(A/rouge )>m(B/bleue) on aurait un corps
    # # qui orbiterait plus autour de l'autre comme la lune autour de la terre.
    # # C'est la masse la plus petiet qui orbite autour de l'autre normalement. car le centre de masse change de position. donc peut se retrouver dans la planete la plus massive
    # # comme la terre-lune ou le centre de masse du systeme est presque au centre de la terre. Donc lune tourne presque autour de du centre de la terre.
    #
    # # L'influence sur la trajectoire de vert(C) est visible aussi courbe autour des deux autre corps.
    #
    # #  je trouve cette animation vraiment interresante aussi
    # #  jai mis 30 dans le temps pour voir l'interarion de bleur et rouge ensemnbe
    # trajectoire_num_explo_2_c = methode_saute_mouton.leapfrog(positions_explo_c, vitesses_c, 0, 30, 1000, masse_c)
    # Animation(trajectoire_num_explo_2_c,"Animation de la solution au problème à 3 corps des années 2000 \n avec différente position de départ")
    #
    # ''' variation dans les massesen c)'''
    # # tout le monde crisse leur camps.
    # # Les masse on vraiment une grande influence sur la stabiliter car la force en depend directement.
    # # modifie tout l'equilibre d'un systemen
    # trajectoire_num_explo_3_c = methode_saute_mouton.leapfrog(positions_c, vitesses_c, 0, 10, 1000, masse_explo_c)
    # Animation(trajectoire_num_explo_3_c,"Animation de la solution au problème à 3 corps des années 2000 \n avec différente masse")
