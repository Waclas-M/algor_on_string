#23+23+/


def ONP_revers(wyrazenie):
    liczba=0
    liczby = []
    operatory=[]
    for x in range(len(wyrazenie)):
        if wyrazenie[x]=="(" or wyrazenie[x]==")":
            pass

        if wyrazenie[x]=="+" or wyrazenie[x]=="-" or wyrazenie[x]=="*" or wyrazenie[x]=="/":
            operatory.append(wyrazenie[x])
        else:
            liczby.append(wyrazenie[x])
    j=0
    wynik=0
    while j != len(operatory):
        if len(liczby)==1:
            if operatory[j]=="+":
                wynik += int(liczby[y])
                #operatory.pop(y)

            elif operatory[j]=="-":
                wynik -= int(liczby[y])
                #operatory.pop(y)

            elif operatory[j]=="/":
                wynik /= int(liczby[y])
                #operatory.pop(y)

            elif operatory[j]=="*":
                wynik *= int(liczby[y])
                #operatory.pop(y)
            j+=1
            break

        y=0
        if operatory[j]=="+":
            wynik += int(liczby[y]) + int(liczby[y+1])
            #operatory.pop(y)

        elif operatory[j]=="-":
            wynik += int(liczby[y])- int(liczby[y+1])
            #operatory.pop(y)

        elif operatory[j]=="/":
            wynik += int(liczby[y])/ int(liczby[y+1])
            #operatory.pop(y)

        elif operatory[j]=="*":
            wynik += int(liczby[y])* int(liczby[y+1])
            #operatory.pop(y)
        liczby.pop(y)
        liczby.pop(y)
        j+=1
    return  wynik







print(ONP_revers("23+233+/"))
