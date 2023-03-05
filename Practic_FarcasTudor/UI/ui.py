
class Consola:
    def __init__(self, srv):
        self.__srv = srv

    def __print_menu(self):
        """
        Functie care printeaza meniul principal
        """
        print("1.Sterge emisiune")
        print("2.Modifica o emisiune")
        print("3.Tiparire program aleator")
        print("4.Exit")

    def __sterge(self):
        """
        Functie care printeaza pe ecran daca am reusit sau nu sa stergem o emisiune din lista
        """
        nume = input("Nume: ")
        tip = input("Tip: ")
        ok = self.__srv.sterge_emisiune(nume, tip)
        if ok == False:
            print("Emisiunea cu datele introduse nu exista in lista!")
            return
        else:
            print("Emisiunea cu numele si tipul introdus s-a sters cu succes!")

    def __modify(self):
        """
        Functie care printeaza pe ecran daca am reusit sau nu sa modificam o emisiune din lista
        :return:
        """
        nume = input("Nume: ")
        tip = input("Tip: ")
        try:
            durata = int(input("Durata: "))
        except:
            print("Durata trebuie sa fie un intreg pozitiv!")
        descriere = input("Descriere: ")
        ok = self.__srv.modifica_emisiune(nume, tip, durata, descriere)
        if ok == False:
            print("Emisiunea cu numele si tipul introdus nu exista in lista!")
            return
        else:
            print("Emisiunea s-a modificat cu succes!")

    def __program_generat(self):
        """
        Functie care va genera un program aleator
        """
        ora_inceput = int(input("Ora inceput: "))
        ora_sfarsit = int(input("Ora sfarsit: "))
        lista_programe = self.__srv.generare(ora_inceput, ora_sfarsit)
        print("Ora\tNume\tTip\tDescriere\n")
        for el in lista_programe:
            print(str(el))


    def run(self):
        while True:
            self.__print_menu()
            cmd  = input("Optiunea dumneavoastra este: ")
            if cmd == "1":
                self.__sterge()
            elif cmd == "2":
                self.__modify()
            elif cmd == "3":
                self.__program_generat()
            elif cmd == "4":
                return
