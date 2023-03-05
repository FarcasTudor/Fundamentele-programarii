from domain.entitati import Student, Disciplina
from domain.DTOs import DiscStudDTO, NoteDTO, NotaGeneralaDTO, DiscNrNoteDTO, NoteStudentDTO
import math
from business.sorter import BubbleSort

class ServiceStudenti:

    def __init__(self, valid_student, repo_studenti):
        self.__valid_student = valid_student
        self.__repo_studenti = repo_studenti

    def get_all_studenti(self):
        """
        Functie care va returna toti studentii
        """
        return self.__repo_studenti.get_all_studs()

    def exist_with_id(self, id_stud):
        return self.__repo_studenti.exist_with_id(id_stud)

    def get_nr_studenti(self):
        """
        Functie care returneaza lungimea listei de studenti
        """
        return len(self.__repo_studenti)

    def sterg_student(self, id_stud):
        """
        Functie care ajuta la stergerea unui student cu id-ul id_stud din lista de studenti
        :param id_stud: id-ul dupa care stergem studentul
        """
        self.__repo_studenti.sterge_student(id_stud)

    def adauga_student(self, id_stud, nume):
        """
        Functie care va apela o functie din repozitorii pentru a adauga un student in lista de studenti
        :param id_stud: id-ul studentului
        :param nume: numele studentului
        """
        student = Student(id_stud, nume)
        self.__valid_student.valideaza(student)
        self.__repo_studenti.adauga_student(student)

    def modifica_student(self, id_stud, nume):
        """
        Functie care modifica numele unui student determinat de id_stud
        :param id_stud: id-ul studentului
        :param nume: numele nou al studentului
        """
        self.__repo_studenti.modifica_stud(id_stud, nume)

    def gaseste_stud_dupa_id(self, id_stud):
        """
        Functie care gaseste un student dupa  id-ul id_stud
        :param id_stud: id-ul dupa care gasim un student
        """
        student = self.__repo_studenti.cauta_dupa_id(id_stud)
        return student

    def gaseste_stud_dupa_nume(self, nume):
        """
        Functie care gaseste un student dupa numele nume
        :param nume: numele dupa care gasim un student
        :return:
        """
        student = self.__repo_studenti.cauta_dupa_nume(nume)
        return student


class ServiceDiscipline:

    def __init__(self, valid_disciplina, repo_discipline):
        self.__valid_disciplina = valid_disciplina
        self.__repo_discipline = repo_discipline

    def get_all_disc(self):
        """
        Functie care returneaza toate disciplinele
        """
        return self.__repo_discipline.get_all_discipline()

    def exist_with_id(self, id_disc):
        return self.__repo_discipline.exist_with_id(id_disc)

    def get_nr_disc(self):
        """
        Functie care returneaza numarul de discipline din lista de discipline
        """
        return len(self.__repo_discipline)

    def adauga_disc(self, id_disc, nume, profesor):
        """
        Functie care creaza o disciplina prin intermediul id-ului id_disc, numelui nume si profesorul profesor
        :param id_disc: id-ul disciplinei
        :param nume: numele disciplinei
        :param profesor: profesorul disciplinei
        """
        disc = Disciplina(id_disc, nume, profesor)
        self.__valid_disciplina.valideaza(disc)
        self.__repo_discipline.adauga_disciplina(disc)

    def sterg_disciplina(self, id_disc):
        """
        Functie care apeleaza o functie din repozitorii pentru a sterge o disciplina din lista de discipline
        :param id_disc: id-ul dupa care stergem disciplina respectiva
        """

        self.__repo_discipline.sterge_disciplina(id_disc)

    def modifica_disciplina(self, id_disc, nume, profesor):
        """
        Functie care apeleaza o functie din repozitorii pentru a modifica elementele unei discipline
        :param id_disc: id-ul disciplinei e care o sa o modificam
        :param nume: noul nume al disciplinei
        :param profesor: noul profesor al disciplinei
        """
        self.__repo_discipline.modifica_disciplina(id_disc, nume, profesor)

    def gaseste_disc_dupa_id(self, id_disc):
        """
        Functie care gaseste o disciplina dupa id-ul id_disc
        :param id_disc: id-ul dupa care cautam o disciplina
        """
        disciplina = self.__repo_discipline.cauta_dupa_id(id_disc)
        return disciplina

    def gaseste_disc_dupa_nume(self, nume):
        """
        Functie care gaseste o disciplina dupa numele nume
        :param nume: numele dupa care cautam o disciplina
        """
        disciplina = self.__repo_discipline.cauta_dupa_nume(nume)
        return disciplina

    def gaseste_disc_dupa_profesor(self, profesor):
        """
        Functie care gaseste o disciplina dupa profesorul profesor
        :param profesor: profesorul dupa cautam o disciplina
        """
        disciplina = self.__repo_discipline.cauta_dupa_profesor(profesor)
        return disciplina


class ServiceNote:

    def __init__(self, valid_nota, repo_note, repo_studenti, repo_discipline):
        self.__valid_nota = valid_nota
        self.__repo_note = repo_note
        self.__repo_studenti = repo_studenti
        self.__repo_discipline = repo_discipline

    def exist_with_id(self, id_nota):
        """
        Functie care verifica daca exista o nota cu id-ul id_nota
        :param id_nota: id-ul notei pe care dorim sa o verificam
        :return:
        """
        return self.__repo_note.exist_with_id(id_nota)

    def cauta_nota_dupa_id(self, id_nota):
        nota = self.__repo_note.cauta_nota_dupa_id(id_nota)
        return nota

    def asignare_nota(self, id_nota, id_stud, id_disc, val_nota):
        """
        Functie care atribuie o nota cu id-ul id_nota, unui student cu id-ul id_stud, la o disciplina cu id-ul id_disc, si o nota val_nota
        :param id_nota: int
        :param id_stud: int
        :param id_disc: int
        :param val_nota: int
        """
        nota = NoteDTO(id_nota, id_stud, id_disc, val_nota)
        self.__valid_nota.valideaza(nota)
        self.__repo_note.adauga_nota_repo(nota)

    def bubble_sort(self, lista):

        for i in range(len(lista)):
            for j in range(len(lista) - 1):
                if lista[j].get_stud().get_nume() > lista[j + 1].get_stud().get_nume():
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def shellSort(self, array, n):

        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval

                array[j] = temp
            interval //= 2
        return array

    def comparare(self, nota1, nota2):
        if nota1.get_stud.get_nume() > nota2.get_stud.get_nume():
            return False
        else:
            if nota1.get_stud.get_nume() == nota2.get_stud.get_nume():
                if nota1.get_val_nota() < nota2.get_val_nota():
                    return True
                else:
                    return False


    def ordonare_alfabetica(self, id_disc):
        """
        o functie care returneaza toti studentii ordonati alfabetic si notele lor la o disciplina
        :return o lista de obiecte de tipul NoteStudentDTO
        """
        noteFisierDto = self.__repo_note.get_all()
        for nota in noteFisierDto:
            idStud2 = nota.get_id_stud()
            idDisciplina2 = nota.get_id_disc()
            student2 = self.__repo_studenti.cauta_dupa_id(idStud2)
            disciplina2 = self.__repo_discipline.cauta_dupa_id(idDisciplina2)
            nota.set_stud(student2)
            nota.set_disc(disciplina2)
        disciplina = self.__repo_discipline.cauta_dupa_id(id_disc)
        note_la_disciplina = []
        for nota in noteFisierDto:
            if disciplina == nota.get_disc():
                note_la_disciplina.append(nota)

        #note_la_disciplina = sorted(note_la_disciplina, key=lambda x: x.get_stud().get_nume())

        sorter = BubbleSort()
        sorter.sort(note_la_disciplina, cmp=lambda x, y: x.get_stud().get_nume() > y.get_stud().get_nume() or (x.get_stud().get_nume() == y.get_stud().get_nume() and x.get_val_nota() < y.get_val_nota()))

        #for i in range(len(note_la_disciplina) - 1):
        #    for j in range(i + 1, len(note_la_disciplina)):
        #        if note_la_disciplina[i].get_stud().get_nume() > note_la_disciplina[j].get_stud().get_nume():
        #            aux = note_la_disciplina[i]
        #            note_la_disciplina[i] = note_la_disciplina[j]
        #            note_la_disciplina[j] = aux

        n = len(note_la_disciplina)
        #note_la_disciplina = self.shellSort(note_la_disciplina, n)

        #note_la_disciplina = self.bubble_sort(note_la_disciplina)
        note_studenti = {}
        for nota in note_la_disciplina:
            student = nota.get_stud()
            if student.get_id_stud() not in note_studenti:
                note_studenti[student.get_id_stud()] = []
            note_studenti[student.get_id_stud()].append(nota.get_val_nota())

        rezultat = []
        for note_student in note_studenti:
            id_stud = note_student
            student = self.__repo_studenti.cauta_dupa_id(id_stud)
            lista_note = note_studenti[note_student]
            nota_student_dto = NoteStudentDTO(student.get_nume(), lista_note)
            rezultat.append(nota_student_dto)
        return rezultat

    def ordoneaza_note_dupa_val_note(self, id_disc):
        """
        o functie care returneaza toti studentii ordonati dupa nota si notele lor la o disciplina
        :param idDisciplina - id-ul disciplinei
        :return o lista de obiecte de tipul NoteStudentDTO
        """
        noteFisierDto = self.__repo_note.get_all()
        for nota in noteFisierDto:
            idStud2 = nota.get_id_stud()
            idDisciplina2 = nota.get_id_disc()
            student2 = self.__repo_studenti.cauta_dupa_id(idStud2)
            disciplina2 = self.__repo_discipline.cauta_dupa_id(idDisciplina2)
            nota.set_stud(student2)
            nota.set_disc(disciplina2)
        self.get_all_note()
        disciplina = self.__repo_discipline.cauta_dupa_id(id_disc)
        note_la_disciplina = []
        for nota in noteFisierDto:
            if nota.get_disc() == disciplina:
                note_la_disciplina.append(nota)
        note_studs = {}
        for nota in note_la_disciplina:
            student = nota.get_stud()
            if student.get_id_stud() not in note_studs:
                note_studs[student.get_id_stud()] = []
            note_studs[student.get_id_stud()].append(nota.get_val_nota())
        rez_neord = []
        for note_stud in note_studs:
            id_stud = note_stud
            student = self.__repo_studenti.cauta_dupa_id(id_stud)
            lista_note = note_studs[note_stud]
            nota_student_dto = NoteStudentDTO(student.get_nume(), lista_note)
            medie = 0
            for nota in lista_note:
                medie += nota
            medie = medie / len(lista_note)
            nota_tuplu = (nota_student_dto, medie)
            rez_neord.append(nota_tuplu)
        for i in range(len(rez_neord) - 1):
            for j in range(i + 1, len(rez_neord)):
                if rez_neord[i][1] < rez_neord[j][1]:
                    aux = rez_neord[i]
                    rez_neord[i] = rez_neord[j]
                    rez_neord[j] = aux
        rezultat = []
        for nota in rez_neord:
            rezultat.append(nota[0])
        return rezultat

    def ordonare_primii_20(self):
        """
        Functie care returneaza primi 20% din studenti ordonat dupa media notelor la toate disciplinele
        """
        note_dtos = self.__repo_note.get_all()
        for nota in note_dtos:
            id_stud = nota.get_id_stud()
            id_disc = nota.get_id_disc()
            stud = self.__repo_studenti.cauta_dupa_id(id_stud)
            disc = self.__repo_discipline.cauta_dupa_id(id_disc)
            nota.set_stud(stud)
            nota.set_disc(disc)
        note_generale = self.calcul_medie_generala()
        for i in range(len(note_generale) - 1):
            for j in range(i + 1, len(note_generale)):
                if note_generale[i][1] < note_generale[j][1]:
                    aux = note_generale[i]
                    note_generale[i] = note_generale[j]
                    note_generale[j] = aux
        rezultat = []
        L = len(self.__repo_studenti)
        if L <= 5:
            x = 1
        else:
            x = math.trunc(L * 0.2)
        k = 0
        while k < x:
            nota = note_generale[k]
            notaDTO = NotaGeneralaDTO(nota[0].get_nume(), nota[1])
            rezultat.append(notaDTO)
            k += 1
        return rezultat

    def calcul_medie_generala(self):
        """
        o functie care calculeaza media notelor la toate disciplinele pentru fiecare student
        :return o lista de liste cu 2 elemente (student si medie generala)
        """
        note_dtos = self.__repo_note.get_all()
        for nota in note_dtos:
            id_stud = nota.get_id_stud()
            id_disc = nota.get_id_disc()
            stud = self.__repo_studenti.cauta_dupa_id(id_stud)
            disc = self.__repo_discipline.cauta_dupa_id(id_disc)
            nota.set_stud(stud)
            nota.set_disc(disc)
        self.get_all_note()
        discipline = self.__repo_discipline.get_all_discipline()
        studenti = self.__repo_studenti.get_all_studs()
        note_generale = []
        for student in studenti:
            stud_nota = [0, 0]
            stud_nota[0] = student
            medie_generala = 0
            for disciplina in discipline:
                medie_disciplina = 0
                nr_note = 0
                for nota in note_dtos:
                    if nota.get_stud() == student and nota.get_disc() == disciplina:
                        nr_note += 1
                        medie_disciplina += nota.get_val_nota()
                if nr_note != 0:
                    medie_disciplina = medie_disciplina / nr_note
                medie_generala += medie_disciplina
            if len(discipline) != 0:
                medie_generala = medie_generala / len(discipline)
            stud_nota[1] = medie_generala
            note_generale.append(stud_nota)
        return note_generale

    def get_all_note(self):
        """
        Functie care returneaza toata notele create
        :return:
        """
        note_dtos = self.__repo_note.get_all()
        note = {}
        for note_dto in note_dtos:
            stud = self.__repo_studenti.cauta_dupa_id(note_dto.get_id_stud())
            disc = self.__repo_discipline.cauta_dupa_id(note_dto.get_id_disc())
            note_dto.set_stud(stud)
            note_dto.set_disc(disc)
            if disc.get_id_disc() not in note:
                note[disc.get_id_disc()] = []
            note[disc.get_id_disc()].append(note_dto)

        rezultat = []
        for nota in note:
            id_disc = nota
            disc = self.__repo_discipline.cauta_dupa_id(id_disc)
            studenti = note[nota]
            disc_stud_dto = DiscStudDTO(disc.get_nume(), studenti)
            rezultat.append(disc_stud_dto)
        return rezultat

    def discipline_cele_mai_multe_note(self):
        """
        Functie care returneaza o lista cu disciplinele care contin cele mai multe note
        :return:
        """
        note_dtos = self.__repo_note.get_all()
        for nota in note_dtos:
            id_stud = nota.get_id_stud()
            id_disc = nota.get_id_disc()
            stud = self.__repo_studenti.cauta_dupa_id(id_stud)
            disc = self.__repo_discipline.cauta_dupa_id(id_disc)
            nota.set_stud(stud)
            nota.set_disc(disc)
        discipline = self.__repo_discipline.get_all_discipline()
        disc_note = {}
        for disc in discipline:
            if disc.get_id_disc() not in disc_note:
                disc_note[disc.get_id_disc()] = 0
            for nota in note_dtos:
                if nota.get_disc() == disc:
                    disc_note[disc.get_id_disc()] += 1

        rezultat = []
        x = 1
        for i in range(len(disc_note) - 1):
            id_disc = 0
            if x <= 3:
                maxi = 0
                for disc in disc_note:
                    if disc_note[disc] > maxi:
                        maxi = disc_note[disc]
                        id_disc = disc
                disc = self.__repo_discipline.cauta_dupa_id(id_disc)
                discNrNoteDTO = DiscNrNoteDTO(disc.get_nume(), maxi)
                rezultat.append(discNrNoteDTO)
                x += 1
                disc_note.pop(id_disc)
                i -= 1
        return rezultat
