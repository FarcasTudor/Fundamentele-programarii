
from Prezentare.UI import Consola
from business.servicii import ServiceStudenti,ServiceDiscipline,ServiceNote
from infrastructura.repozitorii import RepoStudenti,RepoDiscipline,RepoNote
from infrastructura.repozitorii import FileRepoStudenti,FileRepoDiscipline,FileRepoNota
from validare.validatori import ValidatorStudent,ValidatorDisciplina,ValidatorNota
from testare.teste import Teste

if __name__ == '__main__':

    valid_student = ValidatorStudent()
    valid_disciplina = ValidatorDisciplina()
    valid_nota = ValidatorNota()

    #repo_studenti = RepoStudenti()
    #repo_discipline = RepoDiscipline()
    #repo_note = RepoNote()

    repo_studenti = FileRepoStudenti("studenti.txt")
    repo_discipline = FileRepoDiscipline("discipline.txt")
    repo_note = FileRepoNota("note.txt")

    srv_studenti = ServiceStudenti(valid_student, repo_studenti)
    srv_discipline = ServiceDiscipline(valid_disciplina, repo_discipline)
    srv_note = ServiceNote(valid_nota, repo_note, repo_studenti, repo_discipline )

    ui = Consola(srv_studenti, srv_discipline, srv_note)

    #teste = Teste()
    #teste.run_all_tests()

    ui.run()