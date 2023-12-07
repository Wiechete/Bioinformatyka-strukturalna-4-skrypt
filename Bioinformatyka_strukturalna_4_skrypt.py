# -*- coding: utf-8 -*-
from modeller import *
from modeller.automodel import *

env = Environ()
env.io.atom_files_directory = [".", "./atom_files"]
#Tworzy obiekt œrodowiska (Environment) Modeller i ustawia katalogi, w których bêd¹ przechowywane pliki atomowe.
# "6f14", "1ctp"
a = AutoModel(env,alnfile="aligment.txt",knowns=("6F14", "3J4Q", "1CTP"),sequence="sus_quence",)
#Tworzy obiekt AutoModel, który jest automatycznym modelem bia³ka. Podaje œrodowisko, plik do wyrównania (alignment), znane struktury bia³ek ("3j4q", "6f14", "1ctp") oraz sekwencjê bia³ka ("sus_quence").

a.make()
#Uruchamia proces modelowania bia³ka.

a.write("sus_quence.pdb")
#Zapisuje uzyskan¹ strukturê bia³ka do pliku PDB o nazwie "sus_quence.pdb".