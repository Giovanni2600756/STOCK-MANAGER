#STOCK_MANAGER
#Systeme de gestion d'inventaire
#Structure de donnees
produits ={}
historique ={}
#Menu principal
while True:
    print("\n===== STOCKMANAGER =====")
    print("1. Ajouter un produit")
    print("2. Supprimer un produit")
    print("3. Rechercher un produit")
    print("4. Modifier un produit")
    print("5. Afficher l'inventaire")
    print("6. Verifier le stock")
    print("7. Calculer la valeur totale")
    print("8. Consulter l'historique")
    print("9. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        print("Ajouter un produit")

    elif choix == "2":
        print("Supprimer un produit")

    elif choix == "3":
        print("Rechercher un produit")

    elif choix == "4":
        print("Modifier un produit")

    elif choix == "5":
        print("Afficher l'inventaire")

    elif choix == "6":
        print("Verifier le stock")

    elif choix == "7":
        print("Calculer la valeur totale")

    elif choix == "8":
        print("Consulter l'historique")

    elif choix == "9":
        print("Fermeture de StockManager.")
        break

    else:
        print("Choix invalide.")


# FONCTION : AFFICHER L'INVENTAIRE
def afficher_inventaire():
    print("\n--- AFFICHER L'INVENTAIRE ---")

    if len(produits) == 0:
        print("L'inventaire est vide.")
        return

    for identifiant in produits:
        print("\n-------------------------")
        print("Identifiant :", identifiant)
        print("Nom :", produits[identifiant]["nom"])
        print("Prix :", produits[identifiant]["prix"], "$")
        print("Quantite :", produits[identifiant]["quantite"])
        print("Categorie :", produits[identifiant]["categorie"])

    print("\nInventaire affiche avec succes !")

    # FONCTION : AJOUTER UN PRODUIT
    def ajouter_produit():
        print("\n--- AJOUTER UN PRODUIT ---")

        identifiant = int(input("Identifiant : "))

        if identifiant in produits:
            print("Cet identifiant existe deja.")
            return

        nom = input("Nom du produit : ")
        prix = float(input("Prix du produit : "))
        quantite = int(input("Quantite en stock : "))
        categorie = input("Categorie : ")

        produits[identifiant] = {
            "nom": nom,
            "prix": prix,
            "quantite": quantite,
            "categorie": categorie
        }

        historique.append([identifiant, "Entree", quantite])

        print("Produit ajoute avec succes !")