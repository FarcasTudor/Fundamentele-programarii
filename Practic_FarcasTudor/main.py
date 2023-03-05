from repository.Repo_file import FileRepoEmisiuni
from ServiceEmisiuni.service import Service_emisiuni
from UI.ui import Consola
from Teste.Tests import TestCase

if __name__ == '__main__':

    repo = FileRepoEmisiuni("fisier.txt")
    srv = Service_emisiuni(repo)

    teste = TestCase()
    #teste.run()

    ui = Consola(srv)
    ui.run()

