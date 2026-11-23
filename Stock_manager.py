#STOCK_MANAGER
#Systeme de gestion d'inventaire
#Structure de donnees
produits ={}
historique =[]

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

# FONCTION : SUPPRIMER UN PRODUIT
def supprimer_produit():
    print("\n--- SUPPRIMER UN PRODUIT ---")

    identifiant = int(input("Entrez l'identifiant du produit : "))

    if identifiant in produits:
        nom = produits[identifiant]["nom"]

        del produits[identifiant]

        print("Le produit", nom, "a ete supprime avec succes !")

    else:
        print("Aucun produit trouve avec cet identifiant.")

# FONCTION : RECHERCHER UN PRODUIT
def rechercher_produit():
    print("\n--- RECHERCHER UN PRODUIT ---")

    identifiant = int(input("Entrez l'identifiant du produit : "))

    if identifiant in produits:
        informations = produits[identifiant]

        print("\nProduit trouve !")
        print("Identifiant :", identifiant)
        print("Nom :", informations["nom"])
        print("Prix :", informations["prix"], "$")
        print("Quantite :", informations["quantite"])
        print("Categorie :", informations["categorie"])

    else:
        print("Aucun produit trouve avec cet identifiant.")

# FONCTION : MODIFIER UN PRODUIT
def modifier_produit():
    print("\n--- MODIFIER UN PRODUIT ---")

    identifiant = int(input("Entrez l'identifiant du produit : "))

    if identifiant in produits:
        print("1. Modifier le prix")
        print("2. Modifier la quantite")

        choix = input("Votre choix : ")

        if choix == "1":
            nouveau_prix = float(input("Nouveau prix : "))
            produits[identifiant]["prix"] = nouveau_prix
            print("Prix modifie avec succes !")

        elif choix == "2":
            nouvelle_quantite = int(input("Nouvelle quantite : "))
            produits[identifiant]["quantite"] = nouvelle_quantite
            print("Quantite modifiee avec succes !")

        else:
            print("Choix invalide.")

    else:
        print("Aucun produit trouve avec cet identifiant.")

# FONCTION : VERIFIER LE STOCK
def verifier_stock():
    print("\n--- VERIFICATION DU STOCK ---")

    if len(produits) == 0:
        print("L'inventaire est vide.")
        return

    stock_faible = False

    for identifiant, informations in produits.items():

        if informations["quantite"] <= 5:
            print("\nStock faible !")
            print("Identifiant :", identifiant)
            print("Nom :", informations["nom"])
            print("Quantite restante :", informations["quantite"])

            stock_faible = True

    if stock_faible == False:
        print("Aucun produit en stock faible.")

# FONCTION : CALCULER LA VALEUR TOTALE
def calculer_valeur_totale():
    print("\n--- VALEUR TOTALE DE L'INVENTAIRE ---")

    valeur_totale = 0

    if len(produits) == 0:
        print("L'inventaire est vide.")
        return

    for identifiant, informations in produits.items():
        valeur = informations["prix"] * informations["quantite"]
        valeur_totale = valeur_totale + valeur

    print("Valeur totale de l'inventaire :", round(valeur_totale, 2), "$")

# FONCTION : AFFICHER L'HISTORIQUE
def afficher_historique():
    print("\n--- HISTORIQUE DES MOUVEMENTS ---")

    if len(historique) == 0:
        print("Aucun mouvement enregistre.")
        return

    for mouvement in historique:
        print("-------------------------")
        print("Identifiant :", mouvement[0])
        print("Type de mouvement :", mouvement[1])
        print("Quantite :", mouvement[2])

    print("\nHistorique affiche avec succes !")

#Menu principal
if __name__=="__main__":
    while True :

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
        ajouter_produit()

     elif choix == "2":
        supprimer_produit()

     elif choix == "3":
        rechercher_produit()

     elif choix == "4":
        modifier_produit()

     elif choix == "5":
        afficher_inventaire()

     elif choix == "6":
        verifier_stock()

     elif choix == "7":
        calculer_valeur_totale()

     elif choix == "8":
        afficher_historique()

     elif choix == "9":
        print("Fermeture de StockManager.")
        break

     else:
        print("Choix invalide.")


