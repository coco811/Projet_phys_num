import numpy as np
from Simulation_leapfrog import methode_saute_mouton as sp
systeme_solaire_symplifier={'corps':['Soleil','Jupiter','Saturne','Uranus'],
                            'position':np.array([np.array([0,0,0]),np.array([5.20,0,0]),np.array([9.54,0,0]),np.array([19.18,0,0])]),
                            'vitesse':np.array([np.array([0,0,0]),np.array([5.20,0,0]),np.array([9.54,0,0]),np.array([19.18,0,0])]),
                            'masse':np.array([0,0,0,0])}
if __name__ == '__main__':
    sp.saute_mouton(systeme_solaire_symplifier, 0, 10,'Méthode saute mouton pour le sysème solaire').__call__()