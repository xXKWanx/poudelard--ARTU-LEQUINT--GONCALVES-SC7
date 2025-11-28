
def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] += points
    else:
        print(f"Erreur : La maison '{nom_maison}' est introuvable.\n")


def afficher_maison_gagnante(maisons):
    if not maisons:
        print("Classement des maisons indisponible : aucune maison enregistrée.\n")
        return

    score_maximal = -1
    maisons_gagnantes = []

    for score in maisons.values():
        if score > score_maximal:
            score_maximal = score

    for nom, points in maisons.items():
        if points == score_maximal:
            maisons_gagnantes.append(nom)

    print("CLASSEMENT ACTUEL DES MAISONS\n")

    if len(maisons_gagnantes) == 1:
        nom_gagnant = maisons_gagnantes[0]
        print(f"La maison gagnante est : {nom_gagnant} avec {score_maximal} points !\n")

    elif len(maisons_gagnantes) > 1:
        noms_egaux = ", ".join(maisons_gagnantes)
        print(f"Égalité ! Les maisons en tête sont : {noms_egaux} avec {score_maximal} points ex æquo.\n")

    else:
        print("Aucune maison n'a de score positif.")


def repartition_maison(joueur, scores_quiz):
    scores_repartition = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}
    attributs = joueur["Attributs"]

    scores_repartition["Gryffondor"] += attributs["courage"] * 2
    scores_repartition["Serpentard"] += attributs["ambition"] * 2
    scores_repartition["Poufsouffle"] += attributs["loyauté"] * 2
    scores_repartition["Serdaigle"] += attributs["intelligence"] * 2

    for maison, score_quiz in scores_quiz.items():
        scores_repartition[maison] += score_quiz

    print("Résumé des scores :\n")
    for maison, score in scores_repartition.items():
        print(f"{maison}: {score} points")

    maison_finale = ""
    score_maximal = -1

    for maison, score in scores_repartition.items():
        if score > score_maximal:
            score_maximal = score
            maison_finale = maison
    return maison_finale
