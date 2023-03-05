from erori.exceptii import ValidationError

class ValidatorStudent:

    def valideaza(self, stud):
        """
        Functie care valideaza un student stud
        :param stud: studentul pe care il verificam daca e valid
        """
        errors = ""
        if stud.get_id_stud() <= 0:
            errors += "id invalid!\n"
        if stud.get_nume() == "":
            errors += "nume invalid!\n"
        if len(errors) > 0:
            raise ValidationError(errors)


class ValidatorDisciplina:

    def valideaza(self, disc):
        """
        Functie care valideaza o disciplina disc
        :param disc: disciplina pe care o verificam daca e valida
        """
        errors = ""
        if disc.get_id_disc() <= 0:
            errors += "id invalid!\n"
        if disc.get_nume() == "":
            errors += "nume invalid!\n"
        if disc.get_profesor() == "":
            errors += "profesor invalid!\n"
        if len(errors) > 0:
            raise ValidationError(errors)

class ValidatorNota:

    def valideaza(self, nota):
        """
         Functie care valideaza o nota
        :param nota: nota pe care o verificam daca e valida
        """
        errors = ""
        if nota.get_id_nota() <= 0:
            errors += "id invalid!\n"
        if nota.get_val_nota() < 1 or nota.get_val_nota() > 10:
            errors += "nota invalida!\n"
        if len(errors) > 0:
            raise ValidationError(errors)






