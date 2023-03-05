from domain.entities import Emisiune
class Service_emisiuni:
    def __init__(self, repo):
        self.__repo = repo

    def sterge_emisiune(self, nume, tip):
        """
        Functie care se va ajuta de lista din fisier pentru a sterge emisiunea in functie de tip si nume
        :param nume: numele emisiunii
        :param tip: tipul emisiunii
        :return: True daca s-a sters, False daca nu s-a gasit in lista emisiunea
        """
        ok = self.__repo.sterge_emis(nume, tip)
        return ok

    def modifica_emisiune(self, nume, tip, durata, descriere):
        """
        Functie care se va ajuta de lista din fisier pentru a modifica durata si descrierea emisiunii
        :param nume: numele emisiunii
        :param tip: tipul emisiunii
        :param durata: noua durata a emisiunii
        :param descriere: noua dscriere a emisiunii
        :return: True daca s-a modificat, False daca nu s-a gasit in lista emisiunea
        """
        emisiune = Emisiune(nume, tip, durata, descriere)
        return self.__repo.modifica_emis(emisiune)

    def generare(self, inceput, sfarsit):
        """
        Functie care se va ajuta de lista din fisier pentru a construi un tabel
        :param inceput: ora de inceput
        :param sfarsit: ora de final
        :return: o lista cu emisiunile ordonate random
        """
        return self.__repo.generare_tabel(inceput,sfarsit)