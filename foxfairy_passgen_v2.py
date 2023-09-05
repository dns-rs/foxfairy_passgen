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
    print('Length (int) or (Q)uit...')
    x = input().lower()

    if (x.isnumeric() == True):
        os.system('clear')
        start = random.choice(types_start)
        dice = random.randint(0, 2)
        if (dice == 0):
            mid = random.choice(vegetables)
        elif (dice == 1):
            mid = random.choice(fruits)
        else:
            mid = random.choice(meats)
        
        dice = random.randint(0, 1)

        if (dice == 0):
            end = random.choice(types_end)
        else:
            end = random.choice(deserts)
        
        merged = start + mid + end
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        nrs = ['4', '3', '1', '0', '_']

        count = len(vowels)
        crypt = merged
        print("base: " + crypt)
        for c in range(int(count)):
            dice = random.randint(0, 1)
            crypt = crypt.replace(vowels[c], nrs[c])
            
        print("alnu: " + crypt)            

        while (int(x) < len(crypt)):
            random_index = random.randrange(len(crypt))
            crypt = crypt[:random_index] + crypt[random_index+1:]

        while (int(x) > len(crypt)):
            random_char = random.choice("1234567890!@#$^&*()_?abcdefghijklmnopqrstuvwxyz")
            random_index = random.randrange(len(crypt) + 1)
            crypt = crypt[:random_index] + random_char + crypt[random_index:]



        crypt = ''.join(random.choice([str.upper, str.lower])(char) for char in crypt)
        line = len(crypt) + 6
        line = "-" * line
        print(line)
        print("case: " + crypt)

        for i in range(3):
            random_char = random.choice("!@#$^&*()_?")
            random_index = random.randrange(0, len(crypt))
            crypt = list(crypt)
            crypt[random_index] = random_char
            crypt = "".join(crypt)

        print("spec: " + crypt)
        print()
        print()

        # break

    elif (x == "q"):
        break


        

