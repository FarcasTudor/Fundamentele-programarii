from domain.entitati import Student,Disciplina
from domain.DTOs import NoteDTO
from validare.validatori import ValidatorStudent,ValidatorDisciplina,ValidatorNota
from erori.exceptii import ValidationError,RepositoryError
from infrastructura.repozitorii import RepoStudenti,RepoDiscipline,RepoNote, FileRepoStudenti, FileRepoDiscipline, FileRepoNota
from business.servicii import ServiceStudenti,ServiceDiscipline,ServiceNote
import unittest

class TesteCase(unittest.TestCase):

    def setUp(self):
        file_path_stud = "teste_studenti.txt"
        file_path_disc = "teste_discipline.txt"
        file_path_note = "teste_note.txt"
        with open(file_path_stud, "w") as f:
            f.write("")
        self.repo_stud = FileRepoStudenti(file_path_stud)
        self.valid_stud = ValidatorStudent()
        self.srv_stud = ServiceStudenti(self.valid_stud, self.repo_stud)
        with open(file_path_disc, "w") as g:
            g.write("")
        self.repo_disc = FileRepoDiscipline(file_path_disc)
        self.valid_disc = ValidatorDisciplina()
        self.srv_disc = ServiceDiscipline(self.valid_disc, self.repo_disc)
        with open(file_path_note, "w") as h:
            h.write("")
        self.repo_note = FileRepoNota(file_path_note)
        self.valid_note = ValidatorNota()
        self.srv_note = ServiceNote(self.valid_note, self.repo_note, self.repo_stud, self.repo_disc)

    def test_creeaza_student(self):
        """
        Functie de test care verifica daca un student este creat cu succes
        """
        id_stud = 12
        nume = "Andrei"
        stud = Student(id_stud, nume)
        self.assertEqual(stud.get_id_stud(), id_stud)
        self.assertEqual(stud.get_nume() , nume)
        self.assertEqual(str(stud) , "[12]Andrei")
        self.assertEqual(stud.__str__() , "[12]Andrei")
        return stud

    def test_studenti_egali(self):
        idStud = 123
        numeStud = "george"
        student1 = Student(idStud, numeStud)
        numeStud2 = "mihai"
        student2 = Student(idStud, numeStud2)
        idStud2 = 124
        student3 = Student(idStud2, numeStud2)
        self.assertEqual(student1, student2)
        self.assertNotEqual(student2, student3)

    def test_valideaza_student(self):
        """
        Functie de test care verifica daca un student este valid
        Cuprinde atat cazuri in care studentul este valid, cat si daca avem un id invalid sau nume invalid, cauzuri in care vom vea erori
        """
        stud = self.test_creeaza_student()
        self.valid_stud.valideaza(stud)

        inv_id_stud = -23
        inv_nume = ""
        nume = "Andrei"
        stud_inv_id = Student(inv_id_stud, nume)
        stud_inv = Student(inv_id_stud, inv_nume)
        with self.assertRaises(ValidationError) as ve:
            self.valid_stud.valideaza(stud_inv_id)
        self.assertEqual(str(ve.exception) , "id invalid!\n")

        with self.assertRaises(ValidationError) as ve:
            self.valid_stud.valideaza(stud_inv)
        self.assertEqual(str(ve.exception) , "id invalid!\nnume invalid!\n")

    def test_adauga_student_repo(self):
        """
        Functie de test care verifica daca un student se adauga cu succes in lista de studenti
        Cuprinde si cazuri in care daca de exista un student si dorim sa introducem un student nou cu acelasi id, sa verifice ca nu se introduce al doilea student, deoarece fiecare student are un id unic
        """
        self.assertEqual(len(self.repo_stud) , 0)
        self.assertEqual(self.repo_stud.__len__() , 0)

        id_stud = 12
        nume = "Andrei"
        stud = Student(id_stud, nume)
        self.repo_stud.adauga_student(stud)
        self.assertEqual(len(self.repo_stud) , 1)
        stud_gasit = self.repo_stud.cauta_dupa_id(id_stud)
        self.assertEqual(stud_gasit , stud)
        self.assertEqual(stud_gasit.get_nume() , stud.get_nume())

        all = self.repo_stud.get_all_studs()
        self.assertEqual(len(all) , 1)
        self.assertEqual(all[0] , stud)
        self.assertEqual(all[0].get_nume() , stud.get_nume())

        id_stud_inexist = 24
        with self.assertRaises(RepositoryError) as re:
            self.repo_stud.cauta_dupa_id(id_stud_inexist)
        self.assertEqual(str(re.exception), "id inexistent!")

        alt_nume = "George"
        alt_stud_same_id = Student(id_stud, alt_nume)
        #with self.assertRaises(RepositoryError) as re:
       #     self.repo_stud.cauta_dupa_id(id_stud)
        #self.assertEqual(str(re.exception) ,  "id existent!")


    def test_adauga_student_service(self):
        """
        Functie de test care verifica daca se adauga cu succes un student in clasa ServiceStudent
        """
        self.assertEqual(self.srv_stud.get_nr_studenti() , 0 )
        id_stud = 12
        nume = "Andrei"
        self.srv_stud.adauga_student(id_stud, nume)
        self.assertEqual(self.srv_stud.get_nr_studenti() , 1)
        alt_nume = "Gabi"
        with self.assertRaises(RepositoryError) as re:
            self.srv_stud.adauga_student(id_stud, alt_nume)
        self.assertEqual(str(re.exception) , "id existent!")

        inv_id_stud = -23
        inv_nume = ""
        with self.assertRaises(ValidationError) as ve:
            self.srv_stud.adauga_student(inv_id_stud, inv_nume)
        self.assertEqual(str(ve.exception) , "id invalid!\nnume invalid!\n")

    def test_sterge_student(self):
        """
        Functie de test care verifica daca un student se sterge cu succes din lista de studenti
        """
        self.assertEqual(len(self.repo_stud), 0)
        id_stud = 4
        nume = "CasaBlanca"
        stud = Student(id_stud, nume)
        self.repo_stud.adauga_student(stud)
        self.assertEqual(len(self.repo_stud) , 1)
        self.repo_stud.sterge_student(id_stud)
        self.assertEqual(len(self.repo_stud) , 0)

    def test_modifica_student(self):
        """
        Functie de test care verifica daca un student isi modifica cu succes numele
        """
        self.assertEqual(len(self.repo_stud), 0)
        id_stud = 4
        nume = "Ioan"
        stud = Student(id_stud, nume)
        self.repo_stud.adauga_student(stud)
        self.assertEqual(len(self.repo_stud), 1)
        self.repo_stud.modifica_stud(id_stud, "Gabriel")
        self.assertEqual(stud.get_nume() , "Ioan")

    def test_creeaza_disciplina(self):
        """
        Functie de test care verifica daca o disciplina se creeaza cu succes
        """
        id_disciplina = 13
        nume = "Informatica"
        profesor = "Gabitza"
        disc = Disciplina( id_disciplina, nume, profesor )
        self.assertEqual(disc.get_id_disc() , id_disciplina)
        self.assertEqual(disc.get_nume() , nume)
        self.assertEqual(str(disc) , "[13]Informatica -> Gabitza")
        self.assertEqual(disc.__str__() , "[13]Informatica -> Gabitza")

    def test_valideaza_disciplina(self):
        """
        Functie de test care verifica daca o disciplina este valida
        Cuprinde si cazuri in care se introduc date gresite la id, nume sau profesor
        """
        id_disciplina = 13
        nume = "Informatica"
        profesor = "Gabitza"
        disc = Disciplina(id_disciplina, nume, profesor)
        self.valid_disc.valideaza(disc)

        inv_id_disc = -23
        inv_nume = ""
        profesor = "Gabi"
        inv_profesor = ""
        disc_inv_id = Disciplina(inv_id_disc, nume, profesor)
        disc_inv = Disciplina(inv_id_disc, inv_nume, inv_profesor )
        with self.assertRaises(ValidationError) as ve:
            self.valid_disc.valideaza(disc_inv_id)
        self.assertEqual(str(ve.exception) , "id invalid!\n")

        with self.assertRaises(ValidationError) as ve:
            self.valid_disc.valideaza(disc_inv)
        self.assertEqual(str(ve.exception) , "id invalid!\nnume invalid!\nprofesor invalid!\n")


    def test_adauga_disciplina_repo(self):
        """
        Functie de test care verifica daca se adauga cu succes o disciplina in lista de discipline
        """


        self.assertEqual(len(self.repo_disc) , 0)
        self.assertEqual(self.repo_disc.__len__() , 0)
        id_disciplina = 13
        nume = "Informatica"
        profesor = "Gabitza"
        disc = Disciplina(id_disciplina, nume, profesor)
        self.repo_disc.adauga_disciplina(disc)
        self.assertEqual (len(self.repo_disc) , 1)
        self.assertEqual (self.repo_disc.__len__() , 1)
        disc_gasit = self.repo_disc.cauta_dupa_id(id_disciplina)
        self.assertEqual(disc_gasit , disc)
        self.assertEqual(disc_gasit.get_nume() , disc.get_nume())
        self.assertEqual(disc_gasit.get_profesor() , disc.get_profesor())
        all = self.repo_disc.get_all_discipline()
        self.assertEqual(len(all) , 1)
        self.assertEqual(all[0] , disc)
        self.assertEqual(all[0].get_nume() , disc.get_nume())
        self.assertEqual(all[0].get_profesor() , disc.get_profesor())
        id_disc_inexist = 24
        with self.assertRaises(RepositoryError) as re:
            self.repo_disc.cauta_dupa_id(id_disc_inexist)
        self.assertEqual(str(re.exception) ,  "id inexistent!")


    def test_adauga_disciplina_service(self):
        """
        Functie de test care verifica daca se adauga cu succes o disciplina in clasa ServiceDiscipline
        """
        self.assertEqual(self.srv_disc.get_nr_disc() , 0)
        id_disc = 12
        nume = "Info"
        profesor = "Ioan"
        self.srv_disc.adauga_disc(id_disc, nume, profesor)
        self.assertEqual(self.srv_disc.get_nr_disc() , 1)
        alt_nume = "Mate"
        with self.assertRaises(RepositoryError) as re:
            self.srv_disc.adauga_disc(id_disc, alt_nume, profesor)
        self.assertEqual(str(re.exception) , "id existent!")

        inv_id_disc = -23
        inv_nume = ""
        with self.assertRaises(ValidationError) as ve:
            self.srv_disc.adauga_disc(inv_id_disc, inv_nume, profesor)
        self.assertEqual(str(ve.exception) , "id invalid!\nnume invalid!\n")

    def test_sterge_disciplina(self):
        """
        Functie de test care verifica daca se sterge cu succes o disciplina din lista de discipline
        """
        self.assertEqual(len(self.repo_disc) , 0)
        id_disc = 4
        nume = "ASC"
        profesor = "Vancea"
        disc = Disciplina(id_disc, nume, profesor)
        self.repo_disc.adauga_disciplina(disc)
        self.assertEqual(len(self.repo_disc), 1)
        self.repo_disc.sterge_disciplina(id_disc)
        self.assertEqual(len(self.repo_disc) , 0)

    def test_modifica_disciplina(self):
        """
        Functie de test care verifica daca se modifica cu succes numele si profesorul unei discipline
        """
        self.assertEqual( len(self.repo_disc) , 0)
        id_disc= 4
        nume = "Info"
        profesor = "Ildiko"
        disc = Disciplina(id_disc, nume, profesor)
        self.repo_disc.adauga_disciplina(disc)
        self.assertEqual(len(self.repo_disc), 1)
        nume2 = "Matematica"
        profesor2 = "Marcel"
        self.repo_disc.modifica_disciplina(id_disc, nume2 , profesor2)
        self.assertEqual(disc.get_nume() , "Info")
        self.assertEqual(disc.get_profesor() , "Ildiko")

    def test_cauta_disc_dupa_nume(self):
        self.assertEqual(len(self.repo_disc) , 0)
        id_disc = 4
        nume = "Info"
        profesor = "Ildiko"
        disc = Disciplina(id_disc, nume, profesor)
        self.repo_disc.adauga_disciplina(disc)
        disc1 = self.repo_disc.cauta_dupa_nume(nume)
        self.assertEqual(disc1 , disc)

    def test_creeaza_nota(self):
        """
        Functie care testeaza daca se creeaza cu succes o nota
        """
        id_stud = 1
        nume_stud = "Andrei"
        stud = Student(id_stud, nume_stud)
        self.srv_stud.adauga_student(id_stud, nume_stud)
        id_disc = 1
        nume_disc = "Mate"
        profesor = "Pop Carmen"
        disc = Disciplina(id_disc, nume_disc, profesor)
        self.srv_disc.adauga_disc(id_disc, nume_disc, profesor)
        id_nota = 1
        val_nota = 8
        nota = NoteDTO(id_nota, id_stud, id_disc, val_nota)

        self.assertEqual(nota.get_id_nota() , id_nota)
        self.assertEqual (nota.get_id_stud() , id_stud)
        self.assertEqual (nota.get_id_disc() , id_disc)

    def test_valideaza_nota(self):
        """
        Functie care verifica daca o nota este valida
        """
        id_stud = 1
        nume_stud = "Andrei"
        stud = Student(id_stud, nume_stud)
        self.srv_stud.adauga_student(id_stud, nume_stud)
        id_disc = 1
        nume_disc = "Mate"
        profesor = "Pop Carmen"
        disc = Disciplina(id_disc, nume_disc, profesor)
        self.srv_disc.adauga_disc(id_disc, nume_disc, profesor)
        id_nota = 1
        val_nota = 8
        nota = NoteDTO(id_nota, id_stud, id_disc, val_nota)

        self.valid_note.valideaza(nota)

        id_nota_inv = -23
        val_nota_inv = 0
        nota_inv_id = NoteDTO(id_nota_inv, id_stud, id_disc, val_nota)

        with self.assertRaises(ValidationError) as ve:
            self.valid_note.valideaza(nota_inv_id)
        self.assertEqual(str(ve.exception) , "id invalid!\n")

        nota_inv = NoteDTO(id_nota_inv, id_stud, id_disc, val_nota_inv)

        with self.assertRaises(ValidationError) as ve:
            self.valid_note.valideaza(nota_inv)
        self.assertEqual(str(ve.exception) , "id invalid!\nnota invalida!\n")


    def test_adauga_nota_repo(self):
        """
        Functie care verifica daca o nota este adaugata cu succes in repository
        """
        self.assertEqual( len(self.repo_note) , 0)
        id_stud = 1
        nume_stud = "Andrei"
        stud = Student(id_stud, nume_stud)
        self.srv_stud.adauga_student(id_stud ,nume_stud)
        id_disc = 1
        nume_disc = "Mate"
        profesor = "Pop Carmen"
        disc = Disciplina(id_disc, nume_disc, profesor)
        self.srv_disc.adauga_disc(id_disc, nume_disc, profesor)
        id_nota = 1
        val_nota = 8
        nota = NoteDTO(id_nota, id_stud, id_disc, val_nota)
        self.assertEqual(len(self.repo_note) , 0)
        self.assertEqual(self.repo_note.__len__() , 0)
        self.repo_note.adauga_nota_repo(nota)
        self.assertEqual (len(self.repo_note) , 1)
        self.assertEqual (self.repo_note.__len__() , 1)

        all = self.repo_note.get_all()
        self.assertEqual (len(all) , 1)

        self.assertEqual (all[0].get_id_nota() , nota.get_id_nota())
        self.assertEqual (all[0].get_val_nota() , nota.get_val_nota())

    def ordoneaza_note_dupa_nume(self):
        """
        Functie care verifica daca se ordoneaza notele in ordine alfabetica in functie de numele studentilor
        """
        repo_note = RepoNote()
        repodiscipline = RepoDiscipline()
        repostudenti = RepoStudenti()
        id_stud = 1
        nume_stud = "Zebra"
        std1 = Student(id_stud, nume_stud)
        id_disciplina = 1
        nume_disciplina = "Mate"
        profesor = "Andrei"
        disciplina1 = Disciplina(id_disciplina, nume_disciplina, profesor)
        repodiscipline.adauga_disciplina(disciplina1)
        repostudenti.adauga_student(std1)
        valid_nota = ValidatorNota()
        srvnote = ServiceNote(valid_nota, repo_note, repostudenti, repodiscipline)
        id_notare = 1
        val_nota = 5.5
        nota1 = NoteDTO(id_notare, id_stud, id_disciplina, val_nota)
        srvnote.asignare_nota(id_notare, id_stud, id_disciplina, val_nota)

        id_stud_2 = 2
        nume_stud_2 = "Andrei"
        std2 = Student(id_stud_2, nume_stud_2)
        repostudenti.adauga_student(std2)
        id_notare_2 = 2
        val_nota_2 = 6.5
        nota2 = NoteDTO(id_notare_2, id_stud_2, id_disciplina, val_nota_2)
        srvnote.asignare_nota(id_notare_2, id_stud_2, id_disciplina, val_nota_2)
        assert len(repo_note) == 2

        lista_nota = srvnote.ordonare_alfabetica(id_disciplina)
        assert len(lista_nota) == 2
        assert lista_nota[0].get_nume() == "Andrei"
        assert lista_nota[1].get_nume() == "Zebra"

    def test_odonoeaza_dupa_nota(self):
        """
        Functie care verifica daca se ordoneaza notele in ordinea crescatoare in functie de valoare notelor
        """
        repo_note = RepoNote()
        repodiscipline = RepoDiscipline()
        repostudenti = RepoStudenti()
        id_stud = 1
        nume_stud = "Zebra"
        std1 = Student(id_stud, nume_stud)
        id_disciplina = 1
        nume_disciplina = "Mate"
        profesor = "Andrei"
        disciplina1 = Disciplina(id_disciplina, nume_disciplina, profesor)
        repodiscipline.adauga_disciplina(disciplina1)
        repostudenti.adauga_student(std1)
        valid_nota = ValidatorNota()
        srvnote = ServiceNote(valid_nota, repo_note, repostudenti, repodiscipline)
        id_notare = 1
        val_nota = 5.5
        nota1 = NoteDTO(id_notare, id_stud, id_disciplina, val_nota)
        srvnote.asignare_nota(id_notare, id_stud, id_disciplina, val_nota)

        id_stud_2 = 2
        nume_stud_2 = "Andrei"
        std2 = Student(id_stud_2, nume_stud_2)
        repostudenti.adauga_student(std2)
        id_notare_2 = 2
        val_nota_2 = 6.5
        nota2 = NoteDTO(id_notare_2, id_stud_2, id_disciplina, val_nota_2)
        srvnote.asignare_nota(id_notare_2, id_stud_2, id_disciplina, val_nota_2)
        assert len(repo_note) == 2

        lista_nota = srvnote.ordoneaza_note_dupa_val_note(id_disciplina)
        self.assertTrue (len(lista_nota) == 2)
        self.assertTrue (lista_nota[0].get_nume() == "Andrei")
        self.assertTrue (lista_nota[1].get_nume() == "Zebra")

    def test_primii_20(self):
        repo_note = RepoNote()
        repo_disc = RepoDiscipline()
        repo_stud = RepoStudenti()
        id_stud = 1
        nume_stud = "Andrei"
        stud1 = Student(id_stud, nume_stud)
        id_stud_2 = 2
        nume_stud_2 = "Musat"
        stud2 = Student(id_stud_2, nume_stud_2)
        id_disc = 1
        nume_disc = "Mate"
        profesor = "Ion"
        disc1 = Disciplina(id_disc, nume_disc, profesor)
        repo_disc.adauga_disciplina(disc1)
        repo_stud.adauga_student(stud1)
        repo_stud.adauga_student(stud2)
        valid_nota = ValidatorNota()
        srv_note = ServiceNote(valid_nota, repo_note, repo_stud, repo_disc)
        id_nota = 1
        val_nota = 6.9
        nota = NoteDTO(id_nota, id_stud, id_disc, val_nota)
        srv_note.asignare_nota(id_nota, id_stud, id_disc, val_nota)
        id_notare_2 = 2
        val_nota_2 = 7.9
        nota_2 = NoteDTO(id_notare_2, id_stud_2, id_disc, val_nota_2)
        srv_note.asignare_nota(id_notare_2, id_stud_2, id_disc, val_nota_2)


        primii_20_studs = srv_note.ordonare_primii_20()
        self.assertTrue (len(primii_20_studs) == 1)
        self.assertTrue(primii_20_studs[0].get_nume() == "Musat")
        self.assertTrue (primii_20_studs[0].get_nota_generala() == 7.9)

class Teste:


    def __test_creeaza_student(self):
        """
        Functie de test care verifica daca un student este creat cu succes
        """
        id_stud = 12
        nume = "Andrei"
        stud = Student(id_stud, nume)
        assert(stud.get_id_stud() == id_stud)
        assert(stud.get_nume() == nume)
        assert(str(stud) == "[12]Andrei")
        assert(stud.__str__() == "[12]Andrei")



    def __test_valideaza_student(self):
        """
        Functie de test care verifica daca un student este valid
        Cuprinde atat cazuri in care studentul este valid, cat si daca avem un id invalid sau nume invalid, cauzuri in care vom vea erori
        """
        id_stud = 12
        nume = "Andrei"
        stud = Student(id_stud, nume)
        valid = ValidatorStudent()
        valid.valideaza(stud)

        inv_id_stud = -23
        inv_nume = ""
        stud_inv_id = Student(inv_id_stud, nume)
        stud_inv = Student(inv_id_stud, inv_nume)
        try:
            valid.valideaza(stud_inv_id)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!\n")

        try:
            valid.valideaza(stud_inv)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!\nnume invalid!\n")

    def __test_adauga_student_repo(self):
        """
        Functie de test care verifica daca un student se adauga cu succes in lista de studenti
        Cuprinde si cazuri in care daca de exista un student si dorim sa introducem un student nou cu acelasi id, sa verifice ca nu se introduce al doilea student, deoarece fiecare student are un id unic
        """
        repo = RepoStudenti()
        assert(len(repo) == 0)
        assert(repo.__len__() == 0)

        id_stud = 12
        nume = "Andrei"
        stud = Student(id_stud, nume)
        repo.adauga_student(stud)
        assert (len(repo) == 1)
        stud_gasit = repo.cauta_dupa_id(id_stud)
        assert(stud_gasit == stud)
        assert (stud_gasit.get_nume() == stud.get_nume())

        all = repo.get_all_studs()
        assert(len(all) == 1)
        assert (all[0] == stud)
        assert (all[0].get_nume() == stud.get_nume())

        id_stud_inexist = 24
        try:
            repo.cauta_dupa_id(id_stud_inexist)
            assert(False)
        except RepositoryError as re:
            assert(str(re) == "id inexistent!")

        alt_nume = "George"
        alt_stud_same_id = Student(id_stud, alt_nume)
        try:
            repo.adauga_student(alt_stud_same_id)
            assert(False)
        except RepositoryError as re:
            assert(str(re) == "id existent!")

    def __test_adauga_student_service(self):
        """
        Functie de test care verifica daca se adauga cu succes un student in clasa ServiceStudent
        """
        repo = RepoStudenti()
        valid = ValidatorStudent()
        srv = ServiceStudenti(valid, repo)
        id_stud = 12
        nume = "Andrei"
        assert (srv.get_nr_studenti() == 0)
        srv.adauga_student(id_stud, nume)
        assert (srv.get_nr_studenti() == 1)
        alt_nume = "Gabi"
        try:
            srv.adauga_student(id_stud, alt_nume)
            assert (False)
        except RepositoryError as re:
            assert (str(re) == "id existent!")

        inv_id_stud = -23
        inv_nume = ""
        try:
            srv.adauga_student(inv_id_stud, inv_nume)
            assert (False)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\n")

    def __test_sterge_student(self):
        """
        Functie de test care verifica daca un student se sterge cu succes din lista de studenti
        """
        id_stud = 4
        nume = "CasaBlanca"
        stud = Student(id_stud, nume)
        repo = RepoStudenti()
        repo.adauga_student(stud)
        assert(len(repo) == 1)
        repo.sterge_student(id_stud)
        assert(len(repo) == 0)

    def __test_modifica_student(self):
        """
        Functie de test care verifica daca un student isi modifica cu succes numele
        """
        id_stud = 4
        nume = "Ioan"
        stud = Student(id_stud, nume)
        repo = RepoStudenti()
        repo.adauga_student(stud)
        repo.modifica_stud(id_stud, "Gabriel")
        assert(stud.get_nume() == "Gabriel")

    def __test_creeaza_disciplina(self):
        """
        Functie de test care verifica daca o disciplina se creeaza cu succes
        """
        id_disciplina = 13
        nume = "Informatica"
        profesor = "Gabitza"
        disc = Disciplina( id_disciplina, nume, profesor )
        assert (disc.get_id_disc() == id_disciplina)
        assert (disc.get_nume() == nume)
        assert (str(disc) == "[13]Informatica -> Gabitza")
        assert (disc.__str__() == "[13]Informatica -> Gabitza")

    def __test_valideaza_disciplina(self):
        """
        Functie de test care verifica daca o disciplina este valida
        Cuprinde si cazuri in care se introduc date gresite la id, nume sau profesor
        """
        id_disciplina = 13
        nume = "Informatica"
        profesor = "Gabitza"
        disc = Disciplina(id_disciplina, nume, profesor)
        valid = ValidatorDisciplina()
        valid.valideaza(disc)

        inv_id_disc = -23
        inv_nume = ""
        profesor = "Gabi"
        inv_profesor = ""
        disc_inv_id = Disciplina(inv_id_disc, nume, profesor)
        disc_inv = Disciplina(inv_id_disc, inv_nume, inv_profesor )
        try:
            valid.valideaza(disc_inv_id)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!\n")

        try:
            valid.valideaza(disc_inv)
            assert(False)
        except ValidationError as ve:
            assert(str(ve) == "id invalid!\nnume invalid!\nprofesor invalid!\n")

    def __test_adauga_disciplina_repo(self):
        """
        Functie de test care verifica daca se adauga cu succes o disciplina in lista de discipline
        """

        repo = RepoDiscipline()
        assert(len(repo) == 0)
        assert(repo.__len__() == 0)
        id_disciplina = 13
        nume = "Informatica"
        profesor = "Gabitza"
        disc = Disciplina(id_disciplina, nume, profesor)
        repo.adauga_disciplina(disc)
        assert (len(repo) == 1)
        assert (repo.__len__() == 1)
        disc_gasit = repo.cauta_dupa_id(id_disciplina)
        assert(disc_gasit == disc)
        assert(disc_gasit.get_nume() == disc.get_nume())
        assert(disc_gasit.get_profesor() == disc.get_profesor())
        all = repo.get_all_discipline()
        assert(len(all) == 1)
        assert(all[0] == disc)
        assert(all[0].get_nume() == disc.get_nume())
        assert(all[0].get_profesor() == disc.get_profesor())
        id_disc_inexist = 24
        try:
            repo.cauta_dupa_id(id_disc_inexist)
            assert(False)
        except RepositoryError as re:
            assert(str(re) == "id inexistent!")

    def __test_adauga_disciplina_service(self):
        """
        Functie de test care verifica daca se adauga cu succes o disciplina in clasa ServiceDiscipline
        """
        repo = RepoDiscipline()
        valid = ValidatorDisciplina()
        srv = ServiceDiscipline(valid, repo)
        id_disc = 12
        nume = "Info"
        profesor = "Ioan"
        assert (srv.get_nr_disc() == 0)
        srv.adauga_disc(id_disc, nume, profesor)
        assert (srv.get_nr_disc() == 1)
        alt_nume = "Mate"
        try:
            srv.adauga_disc(id_disc, alt_nume, profesor)
            assert (False)
        except RepositoryError as re:
            assert (str(re) == "id existent!")

        inv_id_disc = -23
        inv_nume = ""
        try:
            srv.adauga_disc(inv_id_disc, inv_nume, profesor)
            assert (False)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\n")

    def __test_sterge_disciplina(self):
        """
        Functie de test care verifica daca se sterge cu succes o disciplina din lista de discipline
        """
        id_disc = 4
        nume = "ASC"
        profesor = "Vancea"
        disc = Disciplina(id_disc, nume, profesor)
        repo = RepoDiscipline()
        repo.adauga_disciplina(disc)
        assert (len(repo) == 1)
        repo.sterge_disciplina(id_disc)
        assert (len(repo) == 0)

    def __test_modifica_disciplina(self):
        """
        Functie de test care verifica daca se modifica cu succes numele si profesorul unei discipline
        """
        id_disc= 4
        nume = "Info"
        profesor = "Ildiko"
        disc = Disciplina(id_disc, nume, profesor)
        repo = RepoDiscipline()
        repo.adauga_disciplina(disc)
        repo.modifica_disciplina(id_disc, "Matematica", "Marcel")
        assert(disc.get_nume() == "Matematica")
        assert(disc.get_profesor() == "Marcel")

    def test_cauta_disc_dupa_nume(self):
        id_disc = 4
        nume = "Info"
        profesor = "Ildiko"
        disc = Disciplina(id_disc, nume, profesor)
        repo = RepoDiscipline()
        repo.adauga_disciplina(disc)
        disc1 = repo.cauta_dupa_nume(nume)
        assert disc1 == disc


    def __test_creeaza_nota(self):
        """
        Functie care testeaza daca se creeaza cu succes o nota
        """
        id_stud = 1
        nume_stud = "Andrei"
        stud = Student(id_stud, nume_stud)
        id_disc = 1
        nume_disc = "Mate"
        profesor = "Pop Carmen"
        disc = Disciplina(id_disc, nume_disc, profesor)
        id_nota = 1
        val_nota = 8
        nota = NoteDTO(id_nota, id_stud, id_disc, val_nota)

        assert (nota.get_id_nota() == id_nota)
        assert (nota.get_id_stud() == id_stud)
        assert (nota.get_id_disc() == id_disc)

    def __test_valideaza_nota(self):
        """
        Functie care verifica daca o nota este valida
        """
        id_stud = 1
        nume_stud = "Andrei"
        stud = Student(id_stud, nume_stud)
        id_disc = 1
        nume_disc = "Mate"
        profesor = "Pop Carmen"
        disc = Disciplina(id_disc, nume_disc, profesor)
        id_nota = 1
        val_nota = 8
        nota = NoteDTO(id_nota, id_stud, id_disc, val_nota)

        valid = ValidatorNota()
        valid.valideaza(nota)

        id_nota_inv = -23
        val_nota_inv = 0
        nota_inv_id = NoteDTO(id_nota_inv, id_stud, id_disc, val_nota)

        try:
            valid.valideaza(nota_inv_id)
            assert False
        except ValidationError as ve:
            assert(str(ve) == "id invalid!\n")

        nota_inv = NoteDTO(id_nota_inv, id_stud, id_disc, val_nota_inv)
        try:
            valid.valideaza(nota_inv)
            assert False
        except ValidationError as ve:
            assert(str(ve) == "id invalid!\nnota invalida!\n")

    def __test_adauga_nota_repo(self):
        """
        Functie care verifica daca o nota este adaugata cu succes in repository
        """
        id_stud = 1
        nume_stud = "Andrei"
        stud = Student(id_stud, nume_stud)
        id_disc = 1
        nume_disc = "Mate"
        profesor = "Pop Carmen"
        disc = Disciplina(id_disc, nume_disc, profesor)
        id_nota = 1
        val_nota = 8
        nota = NoteDTO(id_nota, id_stud, id_disc, val_nota)
        repo = RepoNote()

        assert (len(repo) == 0)
        assert (repo.__len__() == 0)
        repo.adauga_nota_repo(nota)
        assert (len(repo) == 1)
        assert (repo.__len__() == 1)
        all = repo.get_all()
        assert (len(all) == 1)
        assert (all[0] == nota)
        assert (all[0].get_id_nota() == nota.get_id_nota())
        assert (all[0].get_val_nota() == nota.get_val_nota())

    def __ordoneaza_note_dupa_nume(self):
        """
        Functie care verifica daca se ordoneaza notele in ordine alfabetica in functie de numele studentilor
        """
        repo_note = RepoNote()
        repodiscipline = RepoDiscipline()
        repostudenti = RepoStudenti()
        id_stud = 1
        nume_stud = "Zebra"
        std1 = Student(id_stud, nume_stud)
        id_disciplina = 1
        nume_disciplina = "Mate"
        profesor = "Andrei"
        disciplina1 = Disciplina(id_disciplina, nume_disciplina, profesor)
        repodiscipline.adauga_disciplina(disciplina1)
        repostudenti.adauga_student(std1)
        valid_nota = ValidatorNota()
        srvnote = ServiceNote(valid_nota, repo_note, repostudenti, repodiscipline)
        id_notare = 1
        val_nota = 5.5
        nota1 = NoteDTO(id_notare, id_stud, id_disciplina, val_nota)
        srvnote.asignare_nota(id_notare, id_stud, id_disciplina, val_nota)

        id_stud_2 = 2
        nume_stud_2 = "Andrei"
        std2 = Student(id_stud_2, nume_stud_2)
        repostudenti.adauga_student(std2)
        id_notare_2 = 2
        val_nota_2 = 6.5
        nota2 = NoteDTO(id_notare_2, id_stud_2, id_disciplina, val_nota_2)
        srvnote.asignare_nota(id_notare_2, id_stud_2, id_disciplina, val_nota_2)
        assert len(repo_note) == 2

        lista_nota = srvnote.ordonare_alfabetica(id_disciplina)
        assert len(lista_nota) == 2
        assert lista_nota[0].get_nume() == "Andrei"
        assert lista_nota[1].get_nume() == "Zebra"

    def __test_odonoeaza_dupa_nota(self):
        """
        Functie care verifica daca se ordoneaza notele in ordinea crescatoare in functie de valoare notelor
        """
        repo_note = RepoNote()
        repodiscipline = RepoDiscipline()
        repostudenti = RepoStudenti()
        id_stud = 1
        nume_stud = "Zebra"
        std1 = Student(id_stud, nume_stud)
        id_disciplina = 1
        nume_disciplina = "Mate"
        profesor = "Andrei"
        disciplina1 = Disciplina(id_disciplina, nume_disciplina, profesor)
        repodiscipline.adauga_disciplina(disciplina1)
        repostudenti.adauga_student(std1)
        valid_nota = ValidatorNota()
        srvnote = ServiceNote(valid_nota, repo_note, repostudenti, repodiscipline)
        id_notare = 1
        val_nota = 5.5
        nota1 = NoteDTO(id_notare, id_stud, id_disciplina, val_nota)
        srvnote.asignare_nota(id_notare, id_stud, id_disciplina, val_nota)

        id_stud_2 = 2
        nume_stud_2 = "Andrei"
        std2 = Student(id_stud_2, nume_stud_2)
        repostudenti.adauga_student(std2)
        id_notare_2 = 2
        val_nota_2 = 6.5
        nota2 = NoteDTO(id_notare_2, id_stud_2, id_disciplina, val_nota_2)
        srvnote.asignare_nota(id_notare_2, id_stud_2, id_disciplina, val_nota_2)
        assert len(repo_note) == 2

        lista_nota = srvnote.ordoneaza_note_dupa_val_note(id_disciplina)
        assert len(lista_nota) == 2
        assert lista_nota[0].get_nume() == "Andrei"
        assert lista_nota[1].get_nume() == "Zebra"

    def __test_primii_20(self):
        repo_note = RepoNote()
        repo_disc = RepoDiscipline()
        repo_stud = RepoStudenti()
        id_stud = 1
        nume_stud = "Andrei"
        stud1 = Student(id_stud, nume_stud)
        id_stud_2 = 2
        nume_stud_2 = "Musat"
        stud2 = Student(id_stud_2, nume_stud_2)
        id_disc = 1
        nume_disc = "Mate"
        profesor = "Ion"
        disc1 = Disciplina(id_disc, nume_disc, profesor)
        repo_disc.adauga_disciplina(disc1)
        repo_stud.adauga_student(stud1)
        repo_stud.adauga_student(stud2)
        valid_nota = ValidatorNota()
        srv_note = ServiceNote(valid_nota, repo_note, repo_stud, repo_disc)
        id_nota = 1
        val_nota = 6.9
        nota = NoteDTO(id_nota, id_stud, id_disc, val_nota)
        srv_note.asignare_nota(id_nota, id_stud, id_disc, val_nota)
        id_notare_2 = 2
        val_nota_2 = 7.9
        nota_2 = NoteDTO(id_notare_2, id_stud_2, id_disc, val_nota_2)
        srv_note.asignare_nota(id_notare_2, id_stud_2, id_disc, val_nota_2)


        primii_20_studs = srv_note.ordonare_primii_20()
        assert len(primii_20_studs) == 1
        assert primii_20_studs[0].get_nume() == "Musat"
        assert primii_20_studs[0].get_nota_generala() == 7.9



    def run_all_tests(self):
        """
        Aceasta functie se ocupa de testarea tuturor functiilor de test a programului
        """
        #Teste pentru studenti
        self.__test_creeaza_student()
        self.__test_valideaza_student()
        self.__test_adauga_student_repo()
        self.__test_adauga_student_service()
        self.__test_sterge_student()
        self.__test_modifica_student()
        #Teste pentru discipline
        self.__test_creeaza_disciplina()
        self.__test_valideaza_disciplina()
        self.__test_adauga_disciplina_repo()
        self.__test_adauga_disciplina_service()
        self.__test_sterge_disciplina()
        self.__test_modifica_disciplina()
        #Teste pentru note
        self.__test_creeaza_nota()
        self.__test_valideaza_nota()
        self.__test_adauga_nota_repo()
        self.__ordoneaza_note_dupa_nume()
        self.__test_odonoeaza_dupa_nota()
        self.__test_primii_20()

