import math
from Simulation_N_corps import code_simulation as code


class euler:
    def __init__(self,corps,pas_temps=1):
        self.pas_temps = pas_temps
        self.corps = corps

    def calcul_position(self):
        for corps_obs in self.corps:
            corps_obs.position.x += corps_obs.vitesse.x * self.pas_temps
            corps_obs.position.y += corps_obs.vitesse.y * self.pas_temps
            corps_obs.position.z += corps_obs.vitesse.z * self.pas_temps

    def calcul_vitesse(self):
        for indice_corps, corps_obs in enumerate(self.corps):
            acceleration = self.calcul_acc_un_corps(indice_corps)
            corps_obs.vitesse.x += acceleration.x * self.pas_temps
            corps_obs.vitesse.y += acceleration.y * self.pas_temps
            corps_obs.vitesse.z += acceleration.z * self.pas_temps

    def calcul_acc_un_corps(self, indice_corps):
        G_const = 6.67408e-11  # m3 kg-1 s-2
        acceleration = code.point(0, 0, 0)
        corps_obs = self.corps[indice_corps]
        for index, corps_exterieur in enumerate(self.corps):
            if index != indice_corps:
                r = (corps_obs.position.x - corps_exterieur.position.x) ** 2 + (
                            corps_obs.position.y - corps_exterieur.position.y) ** 2 + (
                                corps_obs.position.z - corps_exterieur.position.z) ** 2
                r = math.sqrt(r)
                tmp = G_const * corps_exterieur.masse / r ** 3
                acceleration.x += tmp * (corps_exterieur.position.x - corps_obs.position.x)
                acceleration.y += tmp * (corps_exterieur.position.y - corps_obs.position.y)
                acceleration.z += tmp * (corps_exterieur.position.z - corps_obs.position.z)

        return acceleration

    def calcul_pas_graviter(self):
        self.calcul_vitesse()
        self.calcul_position()

