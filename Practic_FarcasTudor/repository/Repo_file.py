from domain.entities import Emisiune, Emisiune_Aleatorie
from random import randint

class FileRepoEmisiuni:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        """
        Functie care citeste din fisier si introduce o lista care contine emisiunile din fisier
        :return: lista de emisiuni
        """
        emisiuni = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                nume, tip, durata, descriere = [token.strip() for token in line.split(",")]
                durata = int(durata)
                emisiune = Emisiune(nume, tip, durata, descriere)
                emisiuni.append(emisiune)
        return emisiuni

    def __save_to_file(self, emisiuni):
        """
        Functie care scrie in fisier toate emisiunile
        :param emisiuni: lista de emisiuni
        """

        with open(self.__filename, "w") as f:
            for emisiune in emisiuni:
                emisiune_str = str(emisiune.get_nume()) + "," + str(emisiune.get_tip()) + "," \
                            + str(emisiune.get_durata()) + "," + str(emisiune.get_descriere()) + "\n"
                f.write(emisiune_str)


    def size(self):
        """
        Functie care returneaza lungimea listei de emisiuni
        :return:
        """
        emisiuni = self.__load_from_file()
        return len(emisiuni)

    def __find_by_index(self, all_emisiuni, nume,tip ):
        """
        functia cu care gasesc indexul elementelor
        :return:index
        :rtype:int
        """
        index = -1
        for i in range(len(all_emisiuni)):
            if all_emisiuni[i].get_nume() == nume and all_emisiuni[i].get_tip() == tip:
                index = i
        return index

    def sterge_emis(self, nume, tip):
        """
        Functie care va sterge din lista de emisiuni o emisiune care are numele nume si tipul tip
        :param nume: numele emisiunii
        :param tip: tipul emisiunii
        :return: True daca s-a sters, False daca nu s-a gasit in lista emisiunea
        """
        emisiuni  = self.__load_from_file()
        index = self.__find_by_index(emisiuni, nume, tip)
        if index == -1:
            return False
        else:
            emisiuni.remove(emisiuni[index])
            self.__save_to_file(emisiuni)
            return True

    def modifica_emis(self, emisiune):
        """
        Functie care incearca sa modifice o emisiune dupa nume si tip
        :param emisiune: noua emisiune
        :return: True daca s-a modificat, False daca nu s-a gasit in lista emisiunea
        """
        emisiuni = self.__load_from_file()
        index = self.__find_by_index(emisiuni, emisiune.get_nume(), emisiune.get_tip())
        if index == -1:
            return False
        else:
            emisiuni[index].set_durata(emisiune.get_durata())
            emisiuni[index].set_descriere(emisiune.get_descriere())
            self.__save_to_file(emisiuni)
            return True

    def generare_tabel(self, inceput, sfarsit):
        """
        Functie care va returna o lista cu emisiunile care inceo in intervalul orar
        :param inceput: ora de inceput
        :param sfarsit: ora de final
        :return: lista cu emisiunile care inceo in intervalul orar
        """
        emisiuni = self.__load_from_file()
        result = []
        vf = [0,0,0,0,0,0,0,0,0,0,0]
        k = 0
        verif = 0
        while inceput + verif< sfarsit and inceput + verif < 25 :
            index = randint(1,10)
            if k == 0:
                ora = inceput
                k = 1
            else:
                ora = inceput + emisiuni[index].get_durata()

            if vf[index] == 0:
                nume = emisiuni[index].get_nume()
                tip = emisiuni[index].get_tip()
                descriere = emisiuni[index].get_descriere()
                program = Emisiune_Aleatorie(ora, nume, tip, descriere)
            else:
                nume = emisiuni[index].get_nume()
                tip = emisiuni[index].get_tip()
                descriere = "****"
                program = Emisiune_Aleatorie(ora, nume, tip, descriere)
            vf[index] = vf[index] + 1
            inceput = inceput + emisiuni[index].get_durata()

            result.append(program)
            verif = emisiuni[index].get_durata()

        return result






