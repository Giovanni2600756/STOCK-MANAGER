import unittest
import Stock_manager


class TestStockManager(unittest.TestCase):

       def setUp(self):
        Stock_manager.produits.clear()
        Stock_manager.historique.clear()

       def test_ajouter_produit(self):
        Stock_manager.produits[101] = {
            "nom": "Clavier",
            "prix": 49.99,
            "quantite": 10,
            "categorie": "Informatique"
        }

        self.assertIn(101, Stock_manager.produits)

       def test_rechercher_produit(self):
        Stock_manager.produits[101] = {
            "nom": "Clavier",
            "prix": 49.99,
            "quantite": 10,
            "categorie": "Informatique"
        }

        self.assertEqual(
            Stock_manager.produits[101]["nom"],
            "Clavier"
        )

       def test_calcul_valeur(self):
        Stock_manager.produits[101] = {
            "nom": "Clavier",
            "prix": 50.0,
            "quantite": 2,
            "categorie": "Informatique"
        }

        valeur = 0

        for produit in Stock_manager.produits.values():
            valeur += produit["prix"] * produit["quantite"]

        self.assertEqual(valeur, 100.0)


       def test_supprimer_produit(self):
        Stock_manager.produits[102] = {
            "nom": "Souris",
            "prix": 24.99,
            "quantite": 5,
            "categorie": "Informatique"
        }

        del Stock_manager.produits[102]

        self.assertNotIn(102, Stock_manager.produits)

       def test_verifier_stock(self):
        Stock_manager.produits[103] = {
            "nom": "Clavier",
            "prix": 49.99,
            "quantite": 3,
            "categorie": "Informatique"
        }

        self.assertLessEqual(
            Stock_manager.produits[103]["quantite"], 5
        )


if __name__ == "__main__":
    unittest.main()
