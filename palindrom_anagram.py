def palindrom(slowo):
    l=0
    p=len(slowo)-1
    while l<p:
        if slowo[l] != slowo[p]:
            return False
        l+=1
        p-=1
    return True

def anagram(slowo1,slowo2):
    l = 0
    while l != len(slowo1):
        if slowo1[l] in slowo2:
            pass
        else:
            return False
        l+=1
    return True



