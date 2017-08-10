# Copyright:Danhua Yan, Jiajie Cen
# 2017.8.7 Verson 2.0.0
import re

def split_input(input_name, grams):
    atom_mass_dict = import_atom()
    atom = re.findall(r"[A-Z][a-z]*", input_name)
    numbers = list(map(float, re.findall(r"[0-9.]+", input_name)))
    grams = float(grams)

    mass = 0
    for i in atom:
        mass += atom_mass_dict[i] * numbers[atom.index(i)]

    mol = grams / mass

    atom_mol = dict(zip(atom, [i * mol for i in numbers]))
    return atom_mol

def import_atom():
    file = open("atomicmass.txt")
    atom_mass_dict = dict()
    for line in file:
        atom = line.split()
        atom_mass_dict[atom[0]] = float(atom[1])
    return atom_mass_dict




#def molarmass(molecule):
#    #creat atomic mass dictionary eledict
#    file = open("atomicmass.txt")
#    elelist = list()
#    eledict = dict()
#    for line in file:
#        str = line.rstrip()
#        elelist = str.split('\t')
#        eledict[elelist[0]] = elelist[1]
#    #Deconstruct input chemical name into atomic mass.
#    summary = list()
#    #split chemical expression, from codego.net/9145913
#    elementlist = re.findall(r'[A-Z][a-z]*|\d+', re.sub('[A-Z][a-z]*(?![\da-z])', r'\g<0>1', molecule))
#    for name in elementlist:
#        x = eledict.get(name,name)
#        summary.append(x)
#    #Cacl. total molecule molar mass.
#    n = 0
#    tot = 0
#    while n < len(summary):
#        val = float(summary[n]) * float(summary[n+1])
#        n = n + 2
#        tot = tot + val
#    return tot

if __name__ == '__main__':
    t_name = input("Please key in the target name:")
    t_gram = input("Please key in the target gram:")
    if len(t_name) < 1:
        t_name = "Ti0.8O1La1Ta7"

    x = split_input(t_name, t_gram)
    print(x)
