import unittest
from ClassProjet import *


class TestEnqueteMethods(unittest.TestCase):

    def test_set_age(self):
        person = personne()
        person.set_age("26-02-2002")
        self.assertEqual(person.get_jour, 26, "Test age pour voir si l'année est valide")
        self.assertEqual(person.get_mois, 2, "Test age pour voir si le mois est valide")
        self.assertEqual(person.get_annee, 2002, "Test age pour voir si le jour est valide")
        self.assertRaises(MauvaisDateException, person.set_age, "26-02-200") #Test avec un format qui ne correspond pas
        self.assertRaises(MauvaisDateException, person.set_age, "bonjour")  #Test avec un paramètre qui ne convient pas
        self.assertRaises(MauvaisDateException, person.set_age, 3)  # Test avec un paramètre qui ne convient pas
        self.assertRaises(MauvaisDateException, person.set_age, "26-02-2027")  #Test avec année qui n'est pas encore arrivé
        self.assertRaises(MauvaisDateException, person.set_age, "32-02-2021")  # Test avec un jour qui n'existe pas
        self.assertRaises(MauvaisDateException, person.set_age, "26-13-2021")  # Test avec un mois qui n'existe pas

    def test_get_age(self):
        person = personne()
        person.set_age("26-02-2002")
        self.assertEqual(person.get_age, 21, "Test age entre 2002 et aujourd'hui")
