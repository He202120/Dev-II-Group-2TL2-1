import unittest
from ClassProjet import *
import os

def fichier_existe(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)

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
        person.set_age("26-02-2023")
        self.assertEqual(person.get_age, 0, "Test age entre 2002 et aujourd'hui")

    def test_lat_long(self):
        lieux = lieu("1380", "Maransart", "Route de l'Etat", "285")
        lieux.lat_long()
        self.assertEqual(lieux.get_lat, 50.662037299999994, "Test lieu voir si la latitude est bien initialisé")
        self.assertEqual(lieux.get_long, 4.462281610711313, "Test lieu voir si la longitude est bien initialisé")
        lieux = lieu("1", "dsqdjsqds", "mvpvw", "55343")
        self.assertRaises(MauvaiseValeurException, lieux.lat_long)  # Test avec un lieu qui n'existe pas

    def test_fichier_person_map_existe(self):

        lieux = lieu("1380", "Maransart", "Route de l'Etat", "285")
        lieux.lat_long()
        lieux.getmapPers("1")

        dossier = "lieux-personnes/"
        fichier = "2.html"

        self.assertFalse(fichier_existe(dossier, fichier), "Le fichier n'existe pas dans le dossier renseigné")

    def test_fichier_person_map_existe_pas(self):

        dossier = "lieux-personnes/"
        fichier = "1.html"

        self.assertTrue(fichier_existe(dossier, fichier), "Le fichier existe dans le dossier renseigné")

    def test_map_person_creer(self):
        lieux = lieu("1", "dsqdjsqds", "mvpvw", "55343")
        self.assertRaises(MauvaiseValeurException, lieux.getmapPers, 1)

    def test_fichier_enquete_map_existe(self):
        lieux = lieu("1380", "Maransart", "Route de l'Etat", "285")
        lieux.lat_long()
        lieux.getmapEnq("1")

        dossier = "lieux-enquetes/"
        fichier = "2.html"

        self.assertFalse(fichier_existe(dossier, fichier), "Le fichier n'existe pas dans le dossier renseigné")

    def test_fichier_enquete_map_existe_pas(self):
        dossier = "lieux-enquetes/"
        fichier = "1.html"

        self.assertTrue(fichier_existe(dossier, fichier), "Le fichier existe dans le dossier renseigné")

    def test_map_enquete_creer(self):
        lieux = lieu("1", "dsqdjsqds", "mvpvw", "55343")
        self.assertRaises(MauvaiseValeurException, lieux.getmapEnq, 1)

    def test_person_meme_ville(self):
        martin_lieux = lieu("1380", "Maransart", "Route de l'Etat", "285")
        martin = personne("martin", "charlier", martin_lieux)

        zawil_lieux = lieu("1380", "Maransart", "Route de l'Etat", "285")
        zawil = personne("martin", "charlier", zawil_lieux)

        self.assertTrue(zawil == martin, "les personnes habite dans la même ville")

    def test_person_diff_ville(self):
        martin_lieux = lieu("1380", "Maransart", "Route de l'Etat", "285")
        martin = personne("martin", "charlier", martin_lieux)

        zawil_lieux = lieu("1380", "Liège", "Route de l'Etat", "285")
        zawil = personne("zawill", "va", zawil_lieux)

        self.assertFalse(zawil == martin, "les personnes habite dans la même ville")
