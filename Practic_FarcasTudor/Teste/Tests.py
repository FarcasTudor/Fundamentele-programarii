import unittest
from repository.Repo_file import FileRepoEmisiuni
from domain.entities import Emisiune

class TestCase:

    def __test_stergere(self):
        """
        Functie care testeaza daca se executa cu succes functia de stergere emisiune
        :return:
        """
        repo = FileRepoEmisiuni("fisier.txt")
        e1 = Emisiune("90_show", "comedie", 2, "copii")
        ok = repo.sterge_emis("90_show", "comedie")
        assert ok == False
        ok = repo.sterge_emis("nu_exista","nu_exista")
        assert ok == False


    def __test_update(self):
        """
        Functie care testeaza daca se executa cu succes functia de update emisiune
        """
        repo = FileRepoEmisiuni("fisier_teste.txt")
        e1 = Emisiune("90_show","actiune",2,"copii")
        e2 = Emisiune("90_show","actiune",3,"gingasi")
        ok = repo.modifica_emis(e2)
        assert(ok == True)
        e3 = Emisiune("nu_exista","nu_este",100,"orice")
        ok = repo.modifica_emis(e3)
        assert ok == False

    def __test_generare(self):
        """
        Functie care testeaza daca se executa cu succes unctia de generare
        """
        repo = FileRepoEmisiuni("fisier_teste.txt")
        inceput = 1
        sfarsit = 24
        lista = repo.generare_tabel(inceput, sfarsit)
        assert len(lista) > 0



    def run(self):
        self.__test_update()
        self.__test_stergere()
        self.__test_generare()



