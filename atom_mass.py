#Copyright:Danhua Yan
import re
def molarmass(molecule):
    #creat atomic mass dictionary eledict
    file = open("atomicmass.txt")
    elelist = list()
    eledict = dict()
    for line in file:
        str = line.rstrip()
        elelist = str.split('\t')
        eledict[elelist[0]] = elelist[1]
    #Deconstruct input chemical name into atomic mass.
    summary = list()
    #split chemical expression, from codego.net/9145913
    elementlist = re.findall(r'[A-Z][a-z]*|\d+', re.sub('[A-Z][a-z]*(?![\da-z])', r'\g<0>1', molecule))
    for name in elementlist:
        x = eledict.get(name,name)
        summary.append(x)
    #Cacl. total molecule molar mass.
    n = 0
    tot = 0
    while n < len(summary):
        val = float(summary[n]) * float(summary[n+1])
        n = n + 2
        tot = tot + val
    return tot

M1 = 0
M2 = 0
n1 = 0
n2 = 0
x = 0 #targeted grams in total
a = 0 #molar rario

while True:
    try:
        M1n = raw_input("Name of component 1:")
        M1 = molarmass(M1n)
        print "Molar mass of", M1n, "is:",M1
        M2n = raw_input("Molecular weight of component 2:")
        M2 = molarmass(M2n)
        print "Molar mass of", M2n, "is:",M2

        while True:
            x = raw_input("Please enter weight for your target (in grams):")
            x = float(x)
            a = raw_input("Com1:Com2 molar ratio:")
            a = float(a)

            n2 = x / (a * M1 + M2)
            n1 = a * n2

            print "m1 =", n1 * M1
            print "m2 =", n2 * M2

            term = raw_input("Enter any button (except 0) to calculate another ratio. Enter 0 to quit.\n")
            if term == '0':
                break
            else: continue
    except:
        print "Syntax Error. Please check your input."
        continue
    quit()