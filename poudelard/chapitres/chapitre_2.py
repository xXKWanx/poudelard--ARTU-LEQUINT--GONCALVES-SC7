from poudelard.utils.input_utils import demander_choix
from poudelard.univers.maison import repartition_maison


def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train se lance, accélère et part en direction du Nord...")
    print("Un jeune homme roux entre dans votre dans votre cabine")

    print("Salut! Moi c'est Ron Weasley. Tu veux bien qu'on partage le voyage ensemble ?")
    choix_ron = demander_choix("Que répondez-vous ?", ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."])

    if choix_ron == "Bien sûr, assieds-toi !":
        joueur['Attributs']['loyauté'] += 1
        print("Ron sourit : Génial ! Tu verras, Poudlard, c'est incroyable !")
    else:
        joueur['Attributs']['ambition'] += 1
        print("Ron hausse les épaules et part chercher une autre place.")

    print("Une fille magnifique entre ensuite, portant déjà une pile de livres.")
    print("Bonjour, je m'appelle Hermione Granger. Vous avez déjà lu Marie Curie ?")

    choix_hermione = demander_choix("Que répondez-vous ?", ["Oui, j'adore apprendre de nouvelles choses !",
                                                            "Euh... non, je préfère les aventures aux livres."])

    if choix_hermione == "Oui, j'adore apprendre de nouvelles choses !":
        joueur['Attributs']['intelligence'] += 1
        print("Hermione sourit : C'est fascinant, n'est-ce pas ?")
    else:
        joueur['Attributs']['courage'] += 1
        print("Hermione fronce les sourcils : Il faudrait pourtant s'y mettre un jour !")

    print("Puis un garçon blond entre avec un air arrogant.")
    print("Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")

    choix_drago = demander_choix("Comment réagissez-vous ?",
                                 ["Je lui serre la main poliment.", "Je l'ignore complètement.",
                                  "Je lui réponds avec arrogance."])

    if choix_drago == "Je lui serre la main poliment.":
        joueur['Attributs']['ambition'] += 1
        print("Drago hoche la tête avec satisfaction.")
    elif choix_drago == "Je l'ignore complètement.":
        joueur['Attributs']['loyauté'] += 1
        print("Drago fronce les sourcils, vexé : Tu le regretteras !")
    else:
        joueur['Attributs']['courage'] += 1
        print("Drago vous lance un regard noir avant de partir.")

    print("Le train continue sa route. Le château de Poudlard se profile à l'horizon...")
    print("Tes choix semblent déjà en dire long sur ta personnalité !")
    print(f"Tes attributs mis à jour : {joueur['Attributs']}")

def mot_de_bienvenue():
    print("\n--- Grande Salle de Poudlard ---")
    print("Le professeur Dumbledore se lève et demande le SILENCE !")
    print("Dumbledore : Bienvenue ! Bienvenue pour une nouvelle année à Poudlard !")
    print("Avant de commencer notre banquet, je voudrais dire quelques mots. Et les voici : Imbécile ! Gras ! Bizarre !")
    print("Merci !")
    input("\nAppuyez sur Entrée pour commencer la cérémonie de répartition...")


def ceremonie_repartition(joueur):
        print("\n--- Cérémonie de Répartition ---")
        print("La cérémonie de répartition commence dans la Grande Salle...")
        print("Le Choixpeau magique t'observe longuement avant de poser ses questions :")

        questions = [
            (
                "Tu vois un ami en danger. Que fais-tu ?",
                ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l'aide", "Je reste calme et j'observe"],
                ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
            ),
            (
                "Quel trait te décrit le mieux ?",
                ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
                ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
            ),
            (
                "Face à un défi difficile, tu...",
                ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis",
                 "Analyses le problème"],
                ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
            )
        ]

        maison_assignee = repartition_maison(joueur, questions)
        joueur['Maison'] = maison_assignee

        print(f"\nLe Choixpeau s'exclame : {maison_assignee} !!!")
        print(f"Tu rejoins les élèves de {maison_assignee} sous leurs applaudissements !")