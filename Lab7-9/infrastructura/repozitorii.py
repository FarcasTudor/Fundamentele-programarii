from erori.exceptii import RepositoryError
import math
from domain.entitati import Student, Disciplina
from domain.DTOs import NotaFisierDTO
class RepoStudenti:

    def __init__(self):
        self._studenti = []

    def __len__(self):
        """
        Functie care returneaza lungimea listei de studenti
        """
        return len(self._studenti)

    def adauga_student_recursiv(self, stud, poz):
        """
        O functie care incearca sa adauge un student in lista de studenti
        :param stud: studentul pe care dorim sa il introducem in lista
        :return: un obiect de tipul student
        """
        if poz == len(self._studenti):
            return False
        elif self._studenti[poz] == stud:
            return True
        else:
            return self.adauga_student_recursiv(stud, poz+1)

    def adauga_student(self, stud):
        """
        Functie care adauga in lista de studenti studentul stud
        :param stud: studentul care e format de un id si un nume
        """
        """
        Aici era codul original
        for _stud in self._studenti:
            if _stud == stud:
                raise RepositoryError("id existent!")
        self._studenti.append(stud)
        """
        exist_in_list = self.adauga_student_recursiv(stud, 0)
        if exist_in_list == False:
            self._studenti.append(stud)
        else:
            raise RepositoryError("id existent!")

    def exist_with_id(self,id):
        for stud in self._studenti:
            if stud.get_id_stud() == id:
                return True
        return False

    def cauta_recursiv(self, id_stud, poz):
        """
        O funtie care incearca sa caute recursiv un student dupa un id dat
        :param id_stud: id-u; studentului
        :param poz: un contor
        :return: obiect de tipul student
        """
        if poz == len(self._studenti):
            return [False, 0]
        elif self._studenti[poz].get_id_stud() == id_stud:
            return [True, self._studenti[poz]]
        else:
            return self.cauta_recursiv(id_stud, poz + 1)

    def cauta_dupa_id(self, id_stud):
        """
        Functie care returneaza un student cautat in functie de id-ul id_stud
        :param id_stud: id-ul dupa care gasim studentul dorit
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Studiu complexitate:
        caz favorabil: primul element este cel dorit, cautat => T(n) = 1 apartine teta(1)
        caz defavorabil: ultimul element este cel dorit, cautat => T(n) = n apartine teta(n)
        caz mediu: se pot parcurge 1,2,3,...,n-1,n pasi, avand aceeasi probabilitate de 1/n
                   deci T(n) = (1+2+3+...+(n-1)+n)/n = (n+1)/2 apartine teta(n)
        => complexitate: O(n)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """

        """
        Aici era codul original
        ok = True
        for _stud in self._studenti:
            if _stud.get_id_stud() == id_stud:
                return _stu
        if ok:
            raise RepositoryError("id inexistent!")
        """
        lst = self.cauta_recursiv(id_stud, 0)
        if lst[0] == True:
            return lst[1]
        else:
            raise RepositoryError("id inexistent!")

    def cauta_dupa_nume(self, nume):
        """
        Functie care cauta un student dupa numele nume
        :param nume: nume dupa care cautam un student
        """
        ok = True
        for _stud in self._studenti:
            if _stud.get_nume() == nume:
                return _stud
        if ok:
            raise RepositoryError("nume inexistent!")



    def sterge_student(self, id_stud):
        """
        Functie care sterge un student din lista de studenti, daca exista
        :param id_stud: id-ul dupa care ne ghidam ce student sa stegrem
        """
        student = self.cauta_dupa_id(id_stud)
        self._studenti.remove(student)

    def modifica_stud(self, id_stud ,nume):
        """
        Functie care modifica ekementele unui student
        :param id_stud: id-ul studentului
        :param nume: numele nou al studentului
        """
        student = self.cauta_dupa_id(id_stud)
        student.set_nume(nume)


    def get_all_studs(self):
        """
        Functie care returneaza lista cu toti studentii
        """
        return self._studenti[:]

class FileRepoStudenti(RepoStudenti):

    def __init__(self, file_path):
        RepoStudenti.__init__(self)
        self.__file_path = file_path

    def __read_all_from_file(self):
        """
        o functie care citeste elementele din fisier;
        """
        with open(self.__file_path, "r") as f:
            self._studenti = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    parts = line.split(",")
                    id_stud = int(parts[0])
                    nume = parts[1]
                    student = Student(id_stud, nume)
                    self._studenti.append(student)
            return self._studenti

    def __append_to_file(self, student):
        """
        o functie care adauga o disciplina in fisier
        :param student - un obiect de tipul Student
        """
        with open(self.__file_path, "a") as f:
            f.write(str(student.get_id_stud()) + "," + student.get_nume() + "\n")

    def __write_to_file(self):
        """
        o functie care rescrie fisierul
        """
        with open(self.__file_path, "w") as f:
            for student in self._studenti:
                f.write(str(student.get_id_stud()) + "," + student.get_nume() + "\n")

    def exist_with_id(self,id):
        self.__read_all_from_file()
        return RepoStudenti.exist_with_id(self, id)

    def adauga_student(self, student):
        """
        o functie care incearca sa adauge un participant in lista de participanti
        :param student - un obiect de tipul Student
        """
        self.__read_all_from_file()
        RepoStudenti.adauga_student(self, student)
        self.__append_to_file(student)


    def cauta_dupa_id(self, id_stud):
        """
        o functie care incearca sa caute un student dupa id
        :param id_stud - id-ul studentului
        :return un obiect de tipul student
        """
        self.__read_all_from_file()
        return RepoStudenti.cauta_dupa_id(self, id_stud)

    def __len__(self):
        """
        o functie care returneaza lungimea listei de studenti
        :return un nr intreg
        """
        self.__read_all_from_file()
        return RepoStudenti.__len__(self)

    def cauta_dupa_nume(self, nume):
        """
        Functie care cauta un student dupa numele nume
        :param nume: nume dupa care cautam un student
        """
        self.__read_all_from_file()
        return RepoStudenti.cauta_dupa_nume(self, nume)

    def sterge_student(self, id_stud):
        """
        Functie care sterge un student din lista de studenti, daca exista
        :param id_stud: id-ul dupa care ne ghidam ce student sa stegrem
        """
        self.__read_all_from_file()
        RepoStudenti.sterge_student(self, id_stud)
        self.__write_to_file()

    def modifica_stud(self, id_stud ,nume):
        """
        Functie care modifica ekementele unui student
        :param id_stud: id-ul studentului
        :param nume: numele nou al studentului
        """
        self.__read_all_from_file()
        RepoStudenti.modifica_stud(self, id_stud, nume)
        self.__write_to_file()




    def get_all_studs(self):
        """
        Functie care returneaza lista cu toti studentii
        """
        return self.__read_all_from_file()



class RepoDiscipline:

    def __init__(self):
        self._discipline = []

    def __len__(self):
        """
        Functie care returneaza lungimea listei de discipline
        """
        return len(self._discipline)

    def exist_with_id(self, id_disc):
        for disc in self._discipline:
            if disc.get_id_disc() == id_disc:
                return True
        return False

    def adauga_disciplina(self, disc):
        """
        Functie care adauga in lista de discipline o disciplina
        :param disc: disciplina pe care o adaugam
        """
        for _disc in self._discipline:
            if _disc == disc:
                raise RepositoryError("id existent!")
        self._discipline.append(disc)

    def sterge_disciplina(self, id_disc):
        """
        Functie care sterge din lista de discipline disciplina determinata de id_disc
        :param id_disc: id-ul disciplinei pe care dorim sa o stergem din lista
        """
        disciplina = self.cauta_dupa_id(id_disc)
        self._discipline.remove(disciplina)

    def modifica_disciplina(self, id_disc, nume, profesor):
        """
        Fuctie care modifica elementele unei discipline
        :param id_disc: id-ul disciplinei dorite
        :param nume: noul nume al disciplinei
        :param profesor: noul profesor al disciplinei
        """
        disciplina = self.cauta_dupa_id(id_disc)
        disciplina.set_nume(nume)
        disciplina.set_profesor(profesor)

    def cauta_dupa_id(self, id_disciplina):
        """
        Functie care cauta dupa id-ul id_disciplina o disciplina
        :param id_disciplina: id-ul dupa care cautam disciplina
        """
        ok = True
        for _disc in self._discipline:
            if _disc.get_id_disc() == id_disciplina:
                return _disc
        if ok:
            raise RepositoryError("id inexistent!")

    def cauta_dupa_nume(self, nume):
        """
        Functie care cauta dupa numele nume o disciplina
        :param nume: numele dupa care cautam disciplina
        """
        ok = True
        for _disc in self._discipline:
            if _disc.get_nume() == nume:
                return _disc
        if ok:
            raise RepositoryError("nume inexistent!")

    def cauta_dupa_profesor(self, profesor):
        """
        Functie care cauta dupa profesorul profesor o disciplina
        :param profesor: profesorul dupa care cautam disciplina
        """
        ok = True
        for _disc in self._discipline:
            if _disc.get_profesor() == profesor:
                return _disc
        if ok:
            raise RepositoryError("profesor inexistent!")


    def get_all_discipline(self):
        """
        Functie care returneaza lista cu toate disciplinele
        """
        return self._discipline[:]

class FileRepoDiscipline(RepoDiscipline):

    def __init__(self, file_path):
        RepoDiscipline.__init__(self)
        self.__file_path = file_path

    def __read_all_from_file(self):
        """
        o functie care citeste elementele din fisier;

        """
        with open(self.__file_path, "r") as f:
            self._discipline = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    parts = line.split(",")
                    idDisciplina = int(parts[0])
                    numeDisciplina = parts[1]
                    profesor = parts[2]
                    disciplina = Disciplina(idDisciplina, numeDisciplina, profesor)
                    self._discipline.append(disciplina)
            return self._discipline

    def __append_to_file(self, disciplina):
        """
        o functie care adauga o disciplina in fisier
        :param disciplina - un obiect de tipul Disciplina
        """
        with open(self.__file_path, "a") as f:
            f.write( str(disciplina.get_id_disc()) + "," + disciplina.get_nume() + "," + disciplina.get_profesor() + "\n" )

    def __write_to_file(self):
        """
        o functie care rescrie fisierul disciplinelor
        """
        with open(self.__file_path, "w") as f:
            for disciplina in self._discipline:
                f.write( str(disciplina.get_id_disc()) + "," + disciplina.get_nume() + "," + disciplina.get_profesor() + "\n")

    def __len__(self):
        """
        Functie care returneaza lungimea listei de discipline
        """
        self.__read_all_from_file()
        return RepoDiscipline.__len__(self)

    def exist_with_id(self, id_disc):
        self.__read_all_from_file()
        return RepoDiscipline.exist_with_id(self, id_disc)

    def adauga_disciplina(self, disc):
        """
        Functie care adauga in lista de discipline o disciplina
        :param disc: disciplina pe care o adaugam
        """
        self.__read_all_from_file()
        RepoDiscipline.adauga_disciplina(self, disc)
        self.__append_to_file(disc)

    def sterge_disciplina(self, id_disc):
        """
        Functie care sterge din lista de discipline disciplina determinata de id_disc
        :param id_disc: id-ul disciplinei pe care dorim sa o stergem din lista
        """
        self.__read_all_from_file()
        RepoDiscipline.sterge_disciplina(self, id_disc)
        self.__write_to_file()

    def modifica_disciplina(self, id_disc, nume, profesor):
        """
        Fuctie care modifica elementele unei discipline
        :param id_disc: id-ul disciplinei dorite
        :param nume: noul nume al disciplinei
        :param profesor: noul profesor al disciplinei
        """
        self.__read_all_from_file()
        RepoDiscipline.modifica_disciplina(self,id_disc, nume, profesor)
        self.__write_to_file()

    def cauta_dupa_id(self, id_disciplina):
        """
        Functie care cauta dupa id-ul id_disciplina o disciplina
        :param id_disciplina: id-ul dupa care cautam disciplina
        """
        self.__read_all_from_file()
        return RepoDiscipline.cauta_dupa_id(self, id_disciplina)


    def cauta_dupa_nume(self, nume):
        """
        Functie care cauta dupa numele nume o disciplina
        :param nume: numele dupa care cautam disciplina
        """
        self.__read_all_from_file()
        return RepoDiscipline.cauta_dupa_nume(self, nume)

    def cauta_dupa_profesor(self, profesor):
        """
        Functie care cauta dupa profesorul profesor o disciplina
        :param profesor: profesorul dupa care cautam disciplina
        """
        self.__read_all_from_file()
        return RepoDiscipline.cauta_dupa_nume(self, profesor)


    def get_all_discipline(self):
        """
        Functie care returneaza lista cu toate disciplinele
        """
        return self.__read_all_from_file()



class RepoNote:
    def __init__(self):
        self._note = []

    def __len__(self):
        """
        Functie care returneaza lungimea listei de discipline
        """
        return len(self._note)

    def exist_with_id(self, id_nota):
        for nota in self._note:
            if nota.get_id_nota() == id_nota:
                return True
        return False

    def cauta_nota_dupa_id(self, id_nota):
        ok = True
        for _nota in self._note:
            if _nota.get_id_nota() == id_nota:
                return _nota
        if ok:
            raise RepositoryError("id inexistent!")

    def get_all(self):
        return self._note

    def adauga_nota_repo(self, nota):
        """
        Functie care adauga in lista de note o nota
        :param nota: nota pe care o adaugam
        """
        for _nota in self._note:
            if _nota.get_id_nota() == nota.get_id_nota():
                raise RepositoryError("id existent!")
        self._note.append(nota)



    def sort_by_val_notes(self):
        """
        Functie care sorteaza crescator lista de note in functie de notele studentilor
        :return: lista de note sortata crescator dupa valoarea notelor
        """
        for i in range(0, len(self._note) - 1):
            val_nota1 = float(self._note[i].get_val_nota())
            for j in range(i + 1, len(self._note)):
                val_nota2 = float(self._note[j].get_val_nota())
                if val_nota1 > val_nota2:
                    self._note[i], self._note[j] = self._note[j], self._note[i]

    def sort_by_medii_20(self):
        copy_list = self._note[:]

        for i in range(0, len(copy_list) - 1):
            val_nota1 = float( copy_list[i].get_val_nota())
            for j in range(i + 1, len(copy_list)):
                val_nota2 = float( copy_list[j].get_val_nota())
                if val_nota1 < val_nota2:
                    copy_list[i], copy_list[j] = copy_list[j], copy_list[i]

        n = len(copy_list)
        if n <= 5:
            x = 1
        else:
            x = math.trunc(n*0.2)

        return copy_list[:x]





class FileRepoNota(RepoNote):

    def __init__(self, file_path):
        RepoNote.__init__(self)
        self.__file_path = file_path

    def __read_all_from_file(self):
        """
         o functie care citeste elementele din fisier;
        """
        with open(self.__file_path, "r") as f:
            self._note = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    parts = line.split(",")
                    id_nota = int(parts[0])
                    id_stud= int(parts[1])
                    id_disc = int(parts[2])
                    val_nota = float(parts[3])
                    notaFisierDTO = NotaFisierDTO(id_nota, id_stud, id_disc, val_nota)
                    self._note.append(notaFisierDTO)


    def __append_to_file(self, notaFisierDto):
        """
        o functie care adauga o nota in fisier
        """
        with open(self.__file_path, "a") as f:
            f.write(str(notaFisierDto.get_id_nota()) + "," + str(notaFisierDto.get_id_stud()) + "," + str(
                notaFisierDto.get_id_disc()) + "," + str(notaFisierDto.get_val_nota()) + "\n")

    def __write_to_file(self):
        """
        o functie care rescrie fisierul disciplinelor
        """
        with open(self.__file_path, "w") as f:
            for notaFisierDTO in self._note:
                f.write(str(notaFisierDTO.get_id_nota()) + "," + str(notaFisierDTO.get_id_stud()) + "," + str(
                    notaFisierDTO.get_id_disc()) + "," + str(notaFisierDTO.get_val_nota()) + "\n")

    def __len__(self):
        """
        Functie care returneaza lungimea listei de discipline
        """
        self.__read_all_from_file()
        return RepoNote.__len__(self)

    def exist_with_id(self, id_nota):
        self.__read_all_from_file()
        return RepoNote.exist_with_id(self, id_nota)

    def cauta_nota_dupa_id(self, id_nota):
        self.__read_all_from_file()
        RepoNote.cauta_nota_dupa_id(self, id_nota)


    def get_all(self):
        self.__read_all_from_file()
        return RepoNote.get_all(self)

    def adauga_nota_repo(self, nota):
        """
        Functie care adauga in lista de note o nota
        :param nota: nota pe care o adaugam
        """
        self.__read_all_from_file()
        RepoNote.adauga_nota_repo(self, nota)
        self.__append_to_file(nota)






