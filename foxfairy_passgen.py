import random
import os

types_start = [
    "rakott",
    "rantott",
    "grill",
    "piritott",
    "porkolt",
    "dinsztelt",
    "sult",
    "fott",
    "toltott",
    "ecetes",
    "salata",
    "savanyu",
    "turos",
    "kakaos",
    "kokuszos",
    "vanilias",
    "panirozott",
    "sajtos",
    "szaftos",
    "csipos",
    "tejszines",
    "mustaros",
    "mezes",
    "gombas",
    "paprikas",
    "ropogos",
    "daralt",
    "zseles",
    "edes",
    "sos",
    "keseru",
    "tojasos"
]

vegetables = [
    "bab",
    "borso",
    "brokkoli",
    "cekla",
    "cukkini",
    "fokhagyma",
    "kaposzta",
    "karalabe",
    "karfiol",
    "kelbimbo",
    "kelkaposzta",
    "krumpli",
    "kukorica",
    "lilahagyma",
    "padlizsan",
    "paradicsom",
    "retek",
    "dinnye",
    "sparga",
    "spenot",
    "sutotok",
    "szoja",
    "uborka",
    "voroshagyma",
    "zeller",
    "zoldbab"
]

meats = [
    "csulok",
    "maj",
    "csirkemell",
    "zuza",
    "karaj",
    "tarja",
    "file",
    "sziv",
    "pacal",
    "fasirt",
    "szalonna",
    "kolbasz",
    "sonka",
    "parizsi",
    "sertescomb"
]

fruits = [
    "berkenye",
    "gesztenye",
    "ananasz",
    "avokado",
    "banan",
    "ribizli",
    "szolo",
    "csipkebogyo",
    "dio",
    "durian",
    "eper",
    "szamoca",
    "datolya",
    "cseresznye",
    "granatalma",
    "korte",
    "barack",
    "fuge",
    "szamoca",
    "mango",
    "licsi",
    "malna",
    "mandula",
    "mazsola",
    "szilva",
    "papaja",
    "paradicsom",
    "dinnye"
]

types_end = [
    "leves",
    "pecsenye",
    "muszaka",
    "gyros",
    "pizza",
    "burger",
    "szelet",
    "pure",
    "rizs",
    "nokedli",
    "fozelek",
    "martas",
    "teszta",
    "fank",
    "fagylalt",
    "guba",
    "pite",
    "kifli",
    "burek",
    "pogacsa",
    "rud",
    "taller",
    "lekvar",
    "gabonapehely",
    "muzli",
    "felvagott",
    "virsli",
    "pastetom",
    "martas",
    "paprikas",
    "szendvics",
    "hus",
    "becsinalt"
]

deserts = [
    "keksz",
    "sutemeny",
    "torta",
    "krem",
    "puding",
    "pite",
    "lepeny"
]

while True:
    print('(L)ong or (S)hort? or (Q)uit...')
    x = input().lower()

    if (x == "l"):
        os.system('clear')
        start = random.choice(types_start)

        rand_one = random.randint(0, 2)

        if (rand_one == 0):
            mid = random.choice(vegetables)
        elif (rand_one == 1):
            mid = random.choice(fruits)
        else:
            mid = random.choice(meats)

        rand_one = random.randint(0, 1)

        if (rand_one == 0):
            end = random.choice(types_end)
        else:
            end = random.choice(deserts)
        
        merged = start + mid + end
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        nrs = ['4', '3', '1', '0', '_']

        count = len(vowels)
        crypt = merged
        for c in range(int(count)):
            crypt = crypt.replace(vowels[c], nrs[c])
                                       
        print(merged)
        print(crypt)
        print()
        print()
        print()


    elif (x == "s"):
        os.system('clear')
        rand_one = random.randint(0, 1)

        if (rand_one == 0):
            start = random.choice(types_start)  

            rand_one = random.randint(0, 2)

            if (rand_one == 0):
                mid = random.choice(vegetables)
            elif (rand_one == 1):
                mid = random.choice(fruits)
            else:
                mid = random.choice(meats)

            
            merged = start + mid

            vowels = ['a', 'e', 'i', 'o', 'u']
            nrs = ['4', '3', '1', '0', '_']

            count = len(vowels)
            crypt = merged
            for c in range(int(count)):
                crypt = crypt.replace(vowels[c], nrs[c])
                                        
            print(merged)
            print(crypt)
            print()
            print()
            print()
            print()
        else:
            os.system('clear')
            rand_one = random.randint(0, 2)

            if (rand_one == 0):
                start = random.choice(vegetables)
            elif (rand_one == 1):
                start = random.choice(fruits)
            else:
                start = random.choice(meats)
            
            if (rand_one == 0):
                end = random.choice(types_end)
            else:
                end = random.choice(deserts)

            vowels = ['a', 'e', 'i', 'o', 'u']
            nrs = ['4', '3', '1', '0', '_']
            merged = start + end
            count = len(vowels)
            crypt = merged
            for c in range(int(count)):
                print(c)
                crypt = crypt.replace(vowels[c], nrs[c])
                                        
            print(merged)
            print(crypt)            
            print()
            print()
            print()
            print()
    elif (x == "q"):
        break

        

