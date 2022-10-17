import wordlist

mins=int(input("Minimal reqem: "))
maks=int(input("Maksimal reqem: "))

Soz=input("Wordlist ucun gireceyiniz soz ve ya herfler: ")

fayladi = input("Fayl adi: ")


yarat = wordlist.Generator(Soz)

try: 
    with open(fayladi,"a") as fayl:
        for i in yarat.generate(mins,maks):
             fayl.write(i)
             fayl.write("\n")

except ValueError:
    print("Zehmet olmasa duzgun reqemler girin :)")