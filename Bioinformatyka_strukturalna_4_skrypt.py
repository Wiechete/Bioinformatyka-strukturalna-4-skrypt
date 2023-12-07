# -*- coding: utf-8 -*-
from modeller import *
from modeller.automodel import *

env = Environ()
env.io.atom_files_directory = [".", "./atom_files"]
#Tworzy obiekt �rodowiska (Environment) Modeller i ustawia katalogi, w kt�rych b�d� przechowywane pliki atomowe.
# "6f14", "1ctp"
a = AutoModel(env,alnfile="aligment.txt",knowns=("6F14", "3J4Q", "1CTP"),sequence="sus_quence",)
#Tworzy obiekt AutoModel, kt�ry jest automatycznym modelem bia�ka. Podaje �rodowisko, plik do wyr�wnania (alignment), znane struktury bia�ek ("3j4q", "6f14", "1ctp") oraz sekwencj� bia�ka ("sus_quence").

a.make()
#Uruchamia proces modelowania bia�ka.

a.write("sus_quence.pdb")
#Zapisuje uzyskan� struktur� bia�ka do pliku PDB o nazwie "sus_quence.pdb".