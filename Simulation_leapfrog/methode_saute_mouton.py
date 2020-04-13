import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt


class saute_mouton:
    def __init__(self, systeme: dict, tmin: int, tmax: int, **kwargs):
        self.nom_corps=systeme['corps']
        self.position = systeme['position']
        self.vitesse = systeme['vitesse']
        self.masse = systeme['masse']
        self.tmin = tmin
        self.tmax = tmax
        self.nb_point = kwargs['nb_point', 1000]
        self.trajectoire3d = np.array([])
        self.trajectoire2d = np.array([])
        self.nombre_de_corps = len(self.position)

    def leapfrog2d(self):
        '''

        :param position: array des positions initiales
        :param vitesse:  array des vitesse initiales
        :param tmin: temps zéros
        :param tmax: temps max
        :param nb_point: le nombre de point voulue
        :param masse: array des masses
        :return: un array des trajectoire où chaque élement exemple x1 est une liste de la
         trajectoires des points en x pour la masse 1 [[x1,y1],[x2,y2],[x3,y3]]
        '''
        G = 4 * np.pi ** 2
        t = 0
        dt = (self.tmax - self.tmin) / self.nb_point
        nombre_de_corps = self.nombre_de_corps
        # défini les vecteurs de vistesse dans chaque direction. [corps1,corps2,corps3]
        position_x = np.zeros(nombre_de_corps)
        position_y = np.zeros(nombre_de_corps)
        vitesse_x = np.zeros(nombre_de_corps)
        vitesse_y = np.zeros(nombre_de_corps)
        trajectoire = []
        for j in range(nombre_de_corps):
            trajectoire.append([[],[]])

        for i in range(nombre_de_corps):
            position_x[i] += (self.position[i][0])
            position_y[i] += (self.position[i][1])
            vitesse_x[i] += (self.vitesse[i][0])
            vitesse_y[i] += (self.vitesse[i][1])
            trajectoire[i][0].append(position_x[i])
            trajectoire[i][1].append(position_y[i])
        while t < self.tmax:
            for i in range(self.nombre_de_corps):
                # commence en Rk2
                position_x[i] += vitesse_x[i] * dt / 2
                position_y[i] += vitesse_y[i] * dt / 2
            for i in range(nombre_de_corps):
                acce_x = 0
                acce_y = 0
                for j in range(nombre_de_corps):
                    if i != j:
                        dx = position_x[i] - position_x[j]
                        dy = position_y[i] - position_y[j]
                        rayon = np.sqrt(dx ** 2 + dy ** 2)
                        acc_total = - G * self.masse[j] / (rayon ** 2)
                        acce_x += acc_total / rayon * dx
                        acce_y += acc_total / rayon * dy
                vitesse_x[i] += acce_x * dt
                vitesse_y[i] += acce_y * dt
            for i in range(nombre_de_corps):
                position_x[i] += vitesse_x[i] * dt / 2
                position_y[i] += vitesse_y[i] * dt / 2
                trajectoire[i][0].append(position_x[i])
                trajectoire[i][1].append(position_y[i])

            t += dt
            self.trajectoire2d = np.array(trajectoire)
        return np.array(trajectoire)

    def leapfrog3d(self):
        '''

        :param position: array des positions initiales
        :param vitesse:  array des vitesse initiales
        :param tmin: temps zéros
        :param tmax: temps max
        :param nb_point: le nombre de point voulue
        :param masse: array des masses
        :return: un array des trajectoire où chaque élement exemple x1 est une liste de la
         trajectoires des points en x pour la masse 1 [[x1,y1],[x2,y2],[x3,y3]]
        '''
        G = 4 * np.pi ** 2
        t = 0
        dt = (self.tmax - self.tmin) / self.nb_point
        nombre_de_corps = self.nombre_de_corps
        # défini les vecteurs de vistesse dans chaque direction. [corps1,corps2,corps3]
        position_x = np.zeros(nombre_de_corps)
        position_y = np.zeros(nombre_de_corps)
        position_z = np.zeros(nombre_de_corps)
        vitesse_x = np.zeros(nombre_de_corps)
        vitesse_y = np.zeros(nombre_de_corps)
        vitesse_z = np.zeros(nombre_de_corps)
        trajectoire = []

        for j in range(nombre_de_corps):
            trajectoire.append([[],[],[]])

        for i in range(nombre_de_corps):
            position_x[i] += (self.position[i][0])
            position_y[i] += (self.position[i][1])
            position_z[i] += (self.position[i][2])
            vitesse_x[i] += (self.vitesse[i][0])
            vitesse_y[i] += (self.vitesse[i][1])
            vitesse_z[i] += (self.vitesse[i][3])
            trajectoire[i][0].append(position_x[i])
            trajectoire[i][1].append(position_y[i])
            trajectoire[i][2].append(position_z[i])
        while t < self.tmax:
            for i in range(nombre_de_corps):
                # commence en Rk2
                position_x[i] += vitesse_x[i] * dt / 2
                position_y[i] += vitesse_y[i] * dt / 2
                position_z[i] += vitesse_z[i] * dt / 2
            for i in range(nombre_de_corps):
                acce_x = 0
                acce_y = 0
                acce_z = 0
                for j in range(nombre_de_corps):
                    if i != j:
                        dx = position_x[i] - position_x[j]
                        dy = position_y[i] - position_y[j]
                        dz = position_z[i] - position_z[j]
                        rayon = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
                        acc_total = - G * self.masse[j] / (rayon ** 2)
                        acce_x += acc_total / rayon * dx
                        acce_y += acc_total / rayon * dy
                        acce_z += acc_total / rayon * dz
                vitesse_x[i] += acce_x * dt
                vitesse_y[i] += acce_y * dt
                vitesse_z[i] += acce_z * dt
            for i in range(nombre_de_corps):
                position_x[i] += vitesse_x[i] * dt / 2
                position_y[i] += vitesse_y[i] * dt / 2
                position_z[i] += vitesse_z[i] * dt / 2
                trajectoire[i][0].append(position_x[i])
                trajectoire[i][1].append(position_y[i])
                trajectoire[i][2].append(position_z[i])

            t += dt
            self.trajectoire3d = np.array(trajectoire)
        return np.array(trajectoire)

    def limite2d(self,):

        liste_xextr = []
        liste_yextr = []

        for i in range(self.nombre_de_corps):
            x_max = self.trajectoire2d[i][0][np.argmax(self.trajectoire2d[i][0])]
            x_min = self.trajectoire2d[i][0][np.argmin(self.trajectoire2d[i][0])]
            liste_xextr.append(x_max)
            liste_xextr.append(x_min)
            y_max = self.trajectoire2d[i][1][np.argmax(self.trajectoire2d[i][1])]
            y_min = self.trajectoire2d[i][1][np.argmin(self.trajectoire2d[i][1])]
            liste_yextr.append(y_max)
            liste_yextr.append(y_min)
        array_x = np.array(liste_xextr)
        array_y = np.array(liste_yextr)
        X_max_to = array_x[np.argmax(array_x)]
        Y_max_to = array_y[np.argmax(array_y)]
        X_min_to = array_x[np.argmin(array_x)]
        Y_min_to = array_y[np.argmin(array_y)]
        return [(X_min_to - 2, X_max_to + 2), (Y_min_to - 2, Y_max_to + 2)]

    def Animation2d(self, titre):

        nb_points = len(self.trajectoire2d[0][0])

        data = {'xA': self.trajectoire2d[0][0], 'yA': self.trajectoire2d[0][1], 'xB': self.trajectoire2d[1][0],
                'yB': self.trajectoire2d[1][1], 'xC': self.trajectoire2d[2][0], 'yC': self.trajectoire2d[2][1]}
        borne = self.limite2d()
        fig = plt.figure()
        ax = plt.axes(xlim=borne[0],
                      ylim=borne[1])

        lines = [ax.plot([], [])[0] for _ in range(self.nombre_de_corps)]
        for j in range(self.nombre_de_corps):
            lines[j].set_label(self.nom_corps[j])


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

        anim = animation.FuncAnimation(fig, animate, frames=nb_points, interval=2, repeat=False)
        plt.title(titre)
        plt.xlabel('position en x')
        plt.ylabel('position en y')
        plt.legend()
        plt.show()
        # writer = animation.writers['imagemagick'](fps=30)
        # anim.save(f'/{titre}.gif',writer=writer)
