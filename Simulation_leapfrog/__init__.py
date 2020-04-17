import numpy as np
from Simulation_leapfrog import methode_saute_mouton as sp

# np.array([1000e24,1e12,1e12,1e12])
systeme_solaire_symplifier={'corps':['Soleil','Jupiter','Saturne','Uranus'],
                            'position':np.array([np.array([0.1,0.1,0.1]),np.array([5.20*(150000000),0,0]),np.array([9.54*(150000000),0,0]),np.array([19.18*(150000000),0,0])]),
                            'vitesse':np.array([np.array([0,0,0]),np.array([0,13e7,0]),np.array([0,9.7e7,0]),np.array([0,6.8e7,0])]),
                            'masse':np.array([1988900e24,1899.0e24 ,568.60e24 ,86.840e24 ])}
if __name__ == '__main__':
    pass
    # sp.saute_mouton(systeme_solaire_symplifier, 0, 10,'Méthode saute mouton pour le sysème solaire').__call__()