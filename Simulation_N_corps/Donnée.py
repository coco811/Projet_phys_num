def extraire_donne(nom_fichier, nom_planete):
    fichier = open(nom_fichier, 'r')
    donnee = {'x': [], 'y': [], 'z': [], 'nom': nom_planete}
    for i in fichier.readlines():
        if 'X =' in i:
            v = i.split()
            v.remove('X')
            v.remove('Y')
            v.remove('Z')
            v.remove('=')
            v.remove('=')
            v.remove('=')
            donnee['x'].append(float(v[0]) * 150000000e3)
            donnee['y'].append(float(v[1]) * 150000000e3)
            donnee['z'].append(float(v[2]) * 150000000e3)
    return [donnee]
