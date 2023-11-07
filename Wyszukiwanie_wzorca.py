def wzor(tekst,wzor):
    liczba_wzorow = 0
    indexy=[]

    for x in range(len(tekst)):
        j=x+1
        if j+1 == len(tekst):
            break
        if j+1 == len(tekst)+1:
            break
        slowo = tekst[x]+tekst[j]+tekst[j+1]
        if slowo==wzor:
            liczba_wzorow +=1
            pocz = x+1
            kon = j+2
            indexy.append(f'{pocz}-{kon}')
        else:
            pass
    return liczba_wzorow, indexy
tekst="dawawkttokotokonkinkot moc kota"
liczba_wzor,indexy=wzor("dawawkttokotokonkinkot moc kota","kot")
print(f"wyszukono {liczba_wzor} wzory, w miejscach {indexy} ")
print(f"{tekst[9:12]} , {tekst[19:22]} , {tekst[27:30]}")







#tekst: Matematyka pyka tyka myka mat | wzorzec: mat
