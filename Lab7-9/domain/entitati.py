
class Student:

    def __init__(self, id_stud, nume):
        self.__id_stud = id_stud
        self.__nume = nume

    def get_id_stud(self):
        """
        Functie care returneaza id-ul unui student
        :return: id-ul studentuli
        """
        return self.__id_stud

    def get_nume(self):
        """
        Functie care returneaza numele unui student
        :return: numele studentului
        """
        return self.__nume

    def set_nume(self, value):
        """
        Functie care seteaza numele unui student cu valoare value
        :param value: string
        :return: numele studentului devine value
        """
        self.__nume = value

    def __str__(self):
        return "[" + str(self.__id_stud) + "]" + self.__nume

    def __eq__(self, other):
        return self.__id_stud == other.__id_stud

class Disciplina:

    def __init__(self, id_disciplina, nume, profesor):
        self.__id_disciplina = id_disciplina
        self.__nume = nume
        self.__profesor = profesor

    def get_id_disc(self):
        """
        Functie care returneaza id-ul unei discipline
        :return: id-ul disciplinei
        """
        return self.__id_disciplina

    def get_nume(self):
        """
        Functie care returneaza numele unei discipline
        :return: numele disciplinei
        """
        return self.__nume

    def get_profesor(self):
        """
        Functie care returneaza profesorul unei discipline
        :return: profesorul discplinei
        """
        return self.__profesor

    def set_nume(self, value):
        """
        Functie care seteaza numele unei discipline pe value
        :param value: string
        :return: numele disciplinei devine value
        """
        self.__nume = value

    def set_profesor(self, value):
        """
        Functie care seteaza profesorul unei discipline pe value
        :param value: string
        :return: profesorul disciplinei devine value
        """
        self.__profesor = value

    def __str__(self):
        return "[" + str(self.__id_disciplina) + "]" + self.__nume + " -> " + self.__profesor

    def __eq__(self, other):
        return self.__id_disciplina == other.__id_disciplina
