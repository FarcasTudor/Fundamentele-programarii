
class NoteDTO:

    def __init__(self, id_nota, id_stud, id_disc, val_nota):
        self.__id_nota = id_nota
        self.__id_stud = id_stud
        self.__stud = None
        self.__id_disc = id_disc
        self.__disc = None
        self.__val_nota = val_nota

    def get_id_nota(self):
        return self.__id_nota

    def get_id_stud(self):
        return self.__id_stud

    def get_stud(self):
        return self.__stud

    def get_id_disc(self):
        return self.__id_disc

    def get_disc(self):
        return self.__disc

    def get_val_nota(self):
        return self.__val_nota

    def set_stud(self, value):
        self.__stud = value

    def set_disc(self, value):
        self.__disc = value

    def set_id_disc(self, value):
        self.__id_disc = value

    def __str__(self):
        return "Studentul:" + str(self.__stud) + ", a obtinut nota: " + str(self.__val_nota)

    def __eq__(self, other):
        return self.__id_nota == other.__id_nota

class DiscStudDTO:

    def __init__(self, nume_disc, lista_stud):
        self.__nume_disc = nume_disc
        self.__lista_stud = lista_stud

    def __str__(self):
        st = ""
        st += self.__nume_disc + ":\n"
        for student in self.__lista_stud:
            st += "\t" + str(student) + "\n"
        return st

class NotaGeneralaDTO:
    def __init__(self, nume_stud, nota_generala):
        self.__nume_stud = nume_stud
        self.__nota_generala = nota_generala

    def get_nume(self):
        return self.__nume_stud

    def get_nota_generala(self):
        return self.__nota_generala

    def __str__(self):
        print = ""
        print += "Studentul: " + self.__nume_stud + " cu nota generala: " + str(self.__nota_generala)
        return print


class DiscNrNoteDTO:

    def __init__(self, nume, nr_note):
        self.__nume = nume
        self.__nr_note = nr_note

    def __str__(self):
        st = ""
        st += self.__nume + " cu numarul de note:  " + str(self.__nr_note)
        return st

    def __eq__(self, other):
        return self.__nume == other.__nume and self.__nr_note == other.__nr_note


class NoteStudentDTO:

    def __init__(self, nume, lista_note):
        self.__nume = nume
        self._lista_note = lista_note

    def __str__(self):
        st = ""
        st += self.__nume + ":\n"
        for nota in self._lista_note:
            st += "\t" + str(nota) + "\n"
        return st

    def get_nume(self):
        return self.__nume

    def __eq__(self, other):
        return self.__nume == other.__nume and self._lista_note == other._lista_note



class NotaFisierDTO:

    def __init__(self, id_nota, id_stud, id_disc, val_nota):
        self.__id_nota = id_nota
        self.__id_stud = id_stud
        self.__stud = None
        self.__id_disc = id_disc
        self.__disc = None
        self.__val_nota = val_nota

    def get_id_nota(self):
        return self.__id_nota

    def get_id_stud(self):
        return self.__id_stud

    def get_id_disc(self):
        return self.__id_disc

    def get_val_nota(self):
        return self.__val_nota

    def get_stud(self):
        return self.__stud

    def set_stud(self, stud):
        self.__stud = stud

    def get_disc(self):
        return self.__disc

    def set_disc(self, disc):
        self.__disc = disc

    def set_val_nota(self, value):
        self.__val_nota = value

    def __eq__(self, other):
        """
        o functie care verifica daca 2 note sunt egale
        """
        return self.__id_nota == other.__id_nota

    def __str__(self):
        return "Studentul:" + str(self.__stud) + ", a obtinut nota: " + str(self.__val_nota)