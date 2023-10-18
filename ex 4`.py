def trouver_position_sous_chaine(chaine, sous_chaine):
    return chaine.find(sous_chaine)

chaine = input("Entrez une chaîne de caractères : ")
sous_chaine = input("Entrez la sous-chaîne à chercher : ")
position = trouver_position_sous_chaine(chaine, sous_chaine)
if position != -1:
    print("La sous-chaîne se trouve à la position :", position)
else:
    print("La sous-chaîne n'a pas été trouvée.")
