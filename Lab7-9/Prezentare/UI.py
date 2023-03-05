from termcolor import colored
from erori.exceptii import ValidationError,RepositoryError

import random, string

from random import seed




class Consola:

    def __init__(self, srv_studenti, srv_discipline, srv_note):
        self.__srv_studenti = srv_studenti
        self.__srv_discipline = srv_discipline
        self.__srv_note = srv_note

    def __print_tipuri_de_statistici(self):
        print("\n1.Lista de studenti si notele lor la o disciplina data, ordonat alfabetic dupa nume")
        print("2.Lista de studenti si notele lor la o disciplina data, ordonat dupa nota")
        print("3.Primi 20% din studenti ordonat dupa media notelor la toate disciplinele (nume si nota)")


    def __ui_print_note(self):
        note = self.__srv_note.get_all_note()
        for x in note:
            print(x)

    def __primele_3_disc_cu_cele_mai_multe_note(self):
        try:
            lista_disc = self.__srv_note.discipline_cele_mai_multe_note()
            for disciplina in lista_disc:
                print(str(disciplina))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

    def __ui_create_nota(self):
        id_nota = 0
        id_stud = 0
        id_disc = 0
        nota = 0

        try:
            id_nota = int(input("Introduceti id-ul notei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:

            try:
                id_stud = int(input("Introduceti id-ul studentului caruia doriti sa ii atribuiti o nota: "))
            except ValueError:
                print("\nId-ul trebuie sa fie un numar intreg\n")
                return
            if self.__srv_studenti.exist_with_id(id_stud) == False:
                raise ValueError("Nu exista student cu id-ul dat!")
            try:
                id_disc = int(input("Introduceti id-ul disciplinei la care vom avea o nota: "))
            except ValueError:
                print("\nId-ul trebuie sa fie un numar intreg\n")
                return
            if self.__srv_discipline.exist_with_id(id_disc) == False:
                raise ValueError("Nu exista disciplina cu id-ul dat!")

        except ValueError as ve:
            print()
            print("Validation error: " + str(ve))
            return
        try:
            nota = float(input("Introduceti o nota: "))
        except ValueError:
            print("\nvaloarea notei trebuie sa fie un numar real\n")
            return
        try:
            self.__srv_note.asignare_nota(id_nota, id_stud, id_disc, nota)
            print(colored("\nNota adaugata cu succes!\n", "green"))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))


    def __ordonare_dupa_nume(self):
        try:
            id_disc = int(input("Introduceti id-ul disciplinei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            note_studenti = self.__srv_note.ordonare_alfabetica(id_disc)
            for student in note_studenti:
                print(str(student))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))


    def __ordonare_dupa_nota(self):
        try:
            id_disc = int(input("Introduceti id-ul disciplinei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            note_studenti = self.__srv_note.ordoneaza_note_dupa_val_note(id_disc)
            for student in note_studenti:
                print(str(student))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

    def __primii_20_la_suta_din_stud(self):
        note_dtos = self.__srv_note.get_all_note()
        if len(note_dtos) == 0:
            print()
            print("Nu exista nicio nota atribuita!")
            return
        else:
            try:
                note_generale = self.__srv_note.ordonare_primii_20()
                for x in note_generale:
                    print(str(x))
            except RepositoryError as re:
                print("\nrepository error: " + str(re))
            except ValidationError as ve:
                print("\nvalidation error: " + str(ve))

    def randomword(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def ui_generate(self):
        try:
            nr_generari = int(input("Introduceti numarul de generari: "))
            de_unde_incepe = int(input("Introduceti o valoare de unde doriti sa se genereze primul id: "))
        except ValueError:
            print(colored("Valoare numerica invalida", "red"))
            return
        try:
            seed(1)
            for i in range(de_unde_incepe , nr_generari + de_unde_incepe):
                id_stud = i
                nume = self.randomword(10)
                self.__srv_studenti.adauga_student(id_stud, nume)
            print(colored("Studenti adaugati cu succes!", "green"))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

    def __ui_adauga_student(self):
        """
        Functie in care introducem id-ul si numele necesare pentru a adauga un student in lista de studenti
        """
        try:
            id_stud = int(input("Id student: "))
        except ValueError:
            print("Id numeric invalid!")
            return
        nume = input("Nume: ")
        self.__srv_studenti.adauga_student(id_stud, nume)
        print("Student adaugat cu succes!")

    def __ui_adauga_disciplina(self):
        """
        Functie in care introducem de la tastatura id-ul, numele si profesorul unei discipline, urmand sa introducem aceasta disciplina in lista
        """
        try:
            id_disc = int(input("Id disciplina: "))
        except ValueError:
            print("Id numeric invalid!")
            return
        nume = input("Nume: ")
        profesor = input("Nume profesor: ")
        self.__srv_discipline.adauga_disc(id_disc, nume, profesor)
        print("Disciplina adaugata cu succes!")

    def __stergere_student(self):
        """
        Functie in care alegem de la tastatura id-ul unui student pe care dorim sa il stergem din lista de studenti, daca exista, urmand sa stergem acel student determinat de id-ul id_stud
        """

        try:
            id_stud = int(input("Id student dorit: "))
        except ValueError:
            print(colored("Id numeric invalid!", "red"))
            return
        try:
            self.__srv_studenti.sterg_student(id_stud)
            print("Student sters cu succes!")
        except RepositoryError as re:
            print("repository error: " + colored(str(re), "red"))

    def __stergere_disciplina(self):
        """
        Functie in care alegem de la tastatura id-ul unei discipline pentru a o sterge din lista de discipline, daca aceasta exista
        """
        try:
            id_disc = int(input("Id disciplina dorit: "))
        except ValueError:
            print("Id numeric invalid!")
            return
        try:
            self.__srv_discipline.sterg_disciplina(id_disc)
            print("Disciplina stearsa cu succes!")
        except RepositoryError as re:
            print("repository error: " + colored(str(re), "red"))


    def __modifica_student(self):
        """
        Functie in care introducem id-ul si numele unui student caruia dorim sa ii modificam numele
        """
        try:
            id_stud = int(input("Id student dorit: "))
        except ValueError:
            print("Id numeric invalid!")
            return
        try:
            try:
                nume = input("Introduceti noul nume: ")
                self.__srv_studenti.modifica_student(id_stud, nume)
                print("Student modificat cu succes!")
            except:
                print(colored("Valoarea introdusa incorect!", "red"))

        except RepositoryError as re:
            print("repository error: " + str(re))
        except ValidationError as ve:
            print("validation error: " + str(ve))


    def __modifica_disciplina(self):
        """
        Functie in care introducem id-ul, numele si profesorul unei discipline careia dorim sa ii modificam numele si profesorul
        """
        try:
            id_disc = int(input("Id disciplina dorit: "))
        except ValueError:
            print("Id numeric invalid!")
            return
        try:
            print()
            try:
                nume = input("Introduceti noul nume: ")
                profesor = input("Introduceti noul profesor: ")
                self.__srv_discipline.modifica_disciplina(id_disc, nume, profesor)
                print("Disciplina modificata cu succes!")
            except:
                print(colored("Valoarea introdusa incorect!", "red"))
        except RepositoryError as re:
            print("repository error: " + str(re))
        except ValidationError as ve:
            print("validation error: " + str(ve))

    def __cauta_student_dupa_id(self):
        """
        Functie in care introducem de la tastatura id-ul unui student pe care dorim sa il gasim in functie de id, iar daca acesta exista, sa il si afisam
        """
        try:
            id_stud = int(input("Id student dorit: "))
        except ValueError:
            print("Id numeric invalid!")
            return
        try:

            stud = self.__srv_studenti.gaseste_stud_dupa_id(id_stud)
            print("Student cautat este: ")
            print(stud)

        except RepositoryError as re:
            print("repository error: " + str(re))
        except ValidationError as ve:
            print("validation error: " + str(ve))

    def __cauta_student_dupa_nume(self):
        """
        Functie in care introducem de la tastatura numele unui student pe care dorim sa il gasim in functie de nume, iar daca acesta exista, il afisam
        """
        try:
            nume = input("Nume student dorit: ")
        except NameError:
            print("Nume invalid!")
            return
        try:

            stud = self.__srv_studenti.gaseste_stud_dupa_nume(nume)
            print("Student cautat este: ")
            print(stud)

        except RepositoryError as re:
            print("repository error: " + str(re))
        except ValidationError as ve:
            print("validation error: " + str(ve))

    def __cauta_disciplina_dupa_id(self):
        """
        Functie in care introducem de la tastatura id-ul unei discipline pe care dorim sa o gasim in functie de id, iar daca aceasta exista, sa o afisam
        """
        try:
            id_disc = int(input("Id disciplina dorita: "))
        except ValueError:
            print("Id numeric invalid!")
            return
        try:

            disc = self.__srv_discipline.gaseste_disc_dupa_id(id_disc)
            print("Disciplina cautata este: ")
            print(disc)

        except RepositoryError as re:
            print("repository error: " + str(re))
        except ValidationError as ve:
            print("validation error: " + str(ve))


    def __cauta_disciplina_dupa_nume(self):
        """
        Functie in care introducem de la tastatura numele unei discipline pe care dorim sa o gasim in functie de nume, iar daca aceasta exista, sa o afisam
        """
        try:
            nume = input("Nume disciplina dorita: ")
        except NameError:
            print("Nume invalid!")
            return
        try:

            disc = self.__srv_discipline.gaseste_disc_dupa_nume(nume)
            print("Disciplina cautata este: ")
            print(disc)

        except RepositoryError as re:
            print("repository error: " + str(re))
        except ValidationError as ve:
            print("validation error: " + str(ve))

    def __cauta_disciplina_dupa_profesor(self):
        """
        Functie in care introducem de la tastatura profesorul unei discipline pe care dorim sa o gasim in functie de profesor, iar daca aceasta exista, sa o afisam
        """
        try:
            profesor = input("Profesorul dorit este: ")
        except NameError:
            print("Profesor invalid!")
            return
        try:

            disc = self.__srv_discipline.gaseste_disc_dupa_profesor(profesor)
            print("Disciplina cautata este: ")
            print(disc)

        except RepositoryError as re:
            print("repository error: " + str(re))
        except ValidationError as ve:
            print("validation error: " + str(ve))

    def __ui_print_studs(self):
        """
        Functie care preia toti studentii existenti in lista si ii afiseaza pe rand
        """
        print("Lista curenta este:")
        studenti = self.__srv_studenti.get_all_studenti()
        for student in studenti:
            print(student)

    def __ui_print_disc(self):
        """
        Functie care preia toate disciplinele existente in lista de discipline si le afiseza pe rand
        """
        print("Lista curenta este:")
        discipline = self.__srv_discipline.get_all_disc()
        for disciplina in discipline:
            print(disciplina)

    def __print_meniu_principal(self):
        """
        Functie care afiseaza meniul principal al consolei
        """
        print()
        print("1.Meniu studenti")
        print("2.Meniu discipline")
        print("3.Generare student random")
        print("4.Asignare de note student-disciplina")
        print("5.Statistici")
        print("6.Primele 3 discipline cu cele mai multe note.")
        print("7.Exit")
        print()

    def __print_meniu_studenti(self):
        """
        Functie care afiseaza meniul oferit in gestiunea studentilor
        """
        print()
        print("1.Adauga student")
        print("2.Sterge student")
        print("3.Modifica student")
        print("4.Cauta student")
        print("5.Print lista studenti")
        print()

    def __print_meniu_discipline(self):
        """
        Functie care afiseaza meniul oferit in gestiunea disciplinelor
        """
        print()
        print("1.Adauga disciplina")
        print("2.Sterge disciplina")
        print("3.Modifica disciplina")
        print("4.Cauta disciplina")
        print("5.Print lista disciplina")
        print()


    def run(self):
        while True:
            self.__print_meniu_principal()

            cmd = input("Optiunea dumneavoastra este: ")
            if cmd == "7":
                return
            elif cmd == "1":
                self.__print_meniu_studenti()
                cmd1 = input("Optiunea dumneavoastra este: ")
                if cmd1 == "1":
                    try:
                        self.__ui_adauga_student()
                    except ValidationError as ve:
                        print("validation error:\n" + str(ve))
                    except RepositoryError as re:
                        print("repository error:\n" + str(re))

                elif cmd1 == "2":
                    try:
                        self.__stergere_student()
                    except ValidationError as ve:
                        print("validation error:\n" + str(ve))
                    except RepositoryError as re:
                        print("repository error:\n" + str(re))

                elif cmd1 == "3":
                    try:
                        self.__modifica_student()
                    except ValidationError as ve:
                        print("validation error:\n" + str(ve))
                    except RepositoryError as re:
                        print("repository error:\n" + str(re))

                elif cmd1 == "4":
                    print("1. Cauta student dupa id")
                    print("2. Cauta student dupa nume")
                    print()
                    try:
                        option = int(input("Optiunea dumneavoastra este: "))
                        if option == 1:
                            try:
                                self.__cauta_student_dupa_id()
                            except ValidationError as ve:
                                print("validation error:\n" + str(ve))
                            except RepositoryError as re:
                                print("repository error:\n" + str(re))
                        elif option == 2:
                            try:
                                self.__cauta_student_dupa_nume()
                            except ValidationError as ve:
                                print("validation error:\n" + str(ve))
                            except RepositoryError as re:
                                print("repository error:\n" + str(re))
                        else:
                            print(colored("comanda invalida!", "red"))
                    except:
                        print(colored("comanda invalida!", "red"))

                if cmd1 == "5":
                    self.__ui_print_studs()

            elif cmd == "2":
                self.__print_meniu_discipline()
                cmd1 = input("Optiunea dumneavoastra este: ")
                if cmd1 == "1":
                    try:
                        self.__ui_adauga_disciplina()
                    except ValidationError as ve:
                        print("validation error:\n" + str(ve))
                    except RepositoryError as re:
                        print("repository error:\n" + str(re))

                elif cmd1 == "2":
                    try:
                        self.__stergere_disciplina()
                    except ValidationError as ve:
                        print("validation error:\n" + str(ve))
                    except RepositoryError as re:
                        print("repository error:\n" + str(re))

                elif cmd1 == "3":
                    try:
                        self.__modifica_disciplina()
                    except ValidationError as ve:
                        print("validation error:\n" + str(ve))
                    except RepositoryError as re:
                        print("repository error:\n" + str(re))

                elif cmd1 == "4":
                    print("1. Cauta disciplina  dupa id")
                    print("2. Cauta disciplina dupa nume")
                    print("3. Cauta disciplina dupa profesor")
                    print()
                    try:
                        option = input("Optiunea dumneavoastra este: ")
                        if option == "1":
                            try:
                                self.__cauta_disciplina_dupa_id()
                            except ValidationError as ve:
                                print("validation error:\n" + str(ve))
                            except RepositoryError as re:
                                print("repository error:\n" + str(re))

                        elif option == "2":
                            try:
                                self.__cauta_disciplina_dupa_nume()
                            except ValidationError as ve:
                                print("validation error:\n" + str(ve))
                            except RepositoryError as re:
                                print("repository error:\n" + str(re))

                        elif option == "3":
                            try:
                                self.__cauta_disciplina_dupa_profesor()
                            except ValidationError as ve:
                                print("validation error:\n" + str(ve))
                            except RepositoryError as re:
                                print("repository error:\n" + str(re))
                        else:
                            print(colored("comanda invalida!", "red"))
                    except:
                        print(colored("comanda invalida!", "red"))

                elif cmd1 == "5":
                    self.__ui_print_disc()
            elif cmd == "3":
                self.ui_generate()

            elif cmd == "4":
                cmd1 = input("Doriti sa vedeti toate notele?\n")
                if cmd1 == "da":
                    self.__ui_print_note()
                else:
                    self.__ui_create_nota()

            elif cmd == "5":
                self.__print_tipuri_de_statistici()
                cmd1 = input("Optiunea dumneavostra este: ")
                if cmd1 == "1":
                    self.__ordonare_dupa_nume()
                elif cmd1 == "2":
                    self.__ordonare_dupa_nota()
                elif cmd1 == "3":
                    self.__primii_20_la_suta_din_stud()
                else:
                    continue
            elif cmd == "6":
                self.__primele_3_disc_cu_cele_mai_multe_note()
            else:
                print(colored("comanda invalida!", "red"))