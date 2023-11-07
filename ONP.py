def ONP(wyrazenie):
    stos=[]
    wyjscie=""
    zapas=[]
    for x in range(len(wyrazenie)):
        if wyrazenie[x]=="(" or wyrazenie[x]==")" or wyrazenie[x]=="+" or wyrazenie[x]=="-" or wyrazenie[x]=="*" or wyrazenie[x]=="/":
            stos.append(wyrazenie[x])
        else:
            wyjscie+=wyrazenie[x]
        if ")" in stos:
            wyjscie+=stos[1]
            stos.clear()
        if len(stos) == 2:
            if stos[1] == "(":
                zapas.append(stos[0])
                stos.clear()
                stos.append("(")
            if not "(" in stos:
                wyjscie+=stos[0]
                stos.remove(stos[0])
        ciog= wyrazenie[x-1]+wyrazenie[x]
        if ")+" == ciog or ")-" == ciog or ")*" == ciog or ")/" == ciog:
            zapas.append(stos[0])
            stos.clear()

    for x in stos:
        wyjscie+=x
    for x in zapas:
        wyjscie+=x
    return wyjscie


