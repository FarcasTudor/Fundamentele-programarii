
class Emisiune:
    def __init__(self, nume, tip, durata, descriere):
        self.__nume =nume
        self.__tip = tip
        self.__durata = durata
        self.__descriere = descriere

    def get_nume(self):
        """
        Functie care returneaza numele unei emisiuni
        :return: numele emisiunii
        """
        return self.__nume

    def get_tip(self):
        """
         Functie care returneaza tipul unei emisiuni
        :return: tipul emisiunii
        """

        return self.__tip

    def get_durata(self):
        """
        Functie care returneaza durata unei emisiuni

        :return: durata emisiunii
        """
        return self.__durata

    def get_descriere(self):
        """
        Functie care returneaza descrierea unei emisiuni

        :return: descrierea emisiunii
        """
        return self.__descriere

    def set_durata(self, value):
        self.__durata = value

    def set_descriere(self, value):
        self.__descriere = value

class Emisiune_Aleatorie:
    def __init__(self, ora, nume, tip,  descriere):
        self.__ora = ora
        self.__nume = nume
        self.__tip = tip
        self.__descriere = descriere

    def set_ora(self, value):
        """
        Functie care seteaza o valoare pentru ora
        :param value: tip ora
        """

        self.__ora = value

    def set_nume(self, value):
        """
        Functie care seteaza o valoare pentru nume
        :param value: tip nume
        :return:
        """
        self.__nume = value

    def set_tip(self, value):
        """
        Functie care seteaza o valoare pentru tip
        :param value: tipul emisiunii
        """
        self.__tip = value

    def set_descriere(self, value):
        """
        Functie care seteaza o valoare pentru descriere
        :param value: tipul descriere

        """
        self.__descriere = value

    def __str__(self):
        return str(self.__ora) + "\t" + self.__nume + "\t" + self.__tip + "\t" + self.__descriere + "\n"