import random
def loe_failist(f):
    fail = open(f, 'r', encoding="utf-8")
    mas = [] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def salvesta_failisse(f, mas):
    fail = open(f, 'w', encoding="utf-8")
    for element in mas:
        fail.write(element + '\n')
    fail.close()

def lisamine_sonastikku(s, mas):
    if s not in mas:
        print(f"Sõna '{s}' puudub sõnastikus. Kas soovite selle lisada?")
        vastus = input("Jah (j) / Ei (e): ").lower()
        if vastus == 'j':
            mas.append(s)
            print(f"Sõna '{s}' on lisatud sõnastikku.")
        else:
            print("Sõna ei lisatud.")
    else:
        print(f"Sõna '{s}' on juba sõnastikus.")

def parandamine_sonastikus(vana_sona, uus_sona, mas):
    if vana_sona in mas:
        index = mas.index(vana_sona)
        mas[index] = uus_sona
        print(f"Sõna '{vana_sona}' on edukalt asendatud sõnaga '{uus_sona}'.")
    else:
        print(f"Sõna '{vana_sona}' ei leitud sõnastikust.")

def kontrolli(sisend_mas, kontroll_mas):
    oiged_vastused = 0
    for sona in sisend_mas:
        if sona in kontroll_mas:
            oiged_vastused += 1
    protsent = (oiged_vastused / len(sisend_mas)) * 100
    return protsent

rus_mas = loe_failist("rus.txt")
est_mas = loe_failist("est.txt")


while True:
    print("\nVali tegevus:")
    print("1. Tõlgi eesti keelest vene keelde")
    print("2. Tõlgi vene keelest eesti keelde")
    print("3. Lisa sõna sõnastikku")
    print("4. Paranda sõnastikus olevat sõna")
    print("5. Kontrolli oma teadmisi")
    print("6. Lõpeta programmi kasutamine")

    valik = input("Sisesta valik (1-6): ")

    if valik == '1':
        sona = input("Sisesta sõna eesti keeles: ")
        lisamine_sonastikku(sona, est_mas)
    elif valik == '2':
        sona = input("Sisesta sõna vene keeles: ")
        lisamine_sonastikku(sona, rus_mas)
    elif valik == '3':
        sona = input("Sisesta sõna, mida soovid lisada sõnastikku: ")
        lisamine_sonastikku(sona, est_mas)
    elif valik == '4':
        vana_sona = input("Sisesta sõna, mida soovid parandada: ")
        uus_sona = input("Sisesta uus sõna: ")
        parandamine_sonastikus(vana_sona, uus_sona, est_mas)
    elif valik == '5':
        print("\nKontrolli oma teadmisi:")
        kontroll_mas = est_mas.copy()  
        print("Tõlgi järgnevad sõnad vene keelde:")
        for i in range(5):  
            random_sona = random.choice(kontroll_mas)
            print(f"{i+1}. {random_sona}")
            kontroll_mas.remove(random_sona)
        sisend_mas = [input(f"Sisesta vene keelde tõlgitud sõna {i+1}: ") for i in range(5)]
        protsent = kontrolli(sisend_mas, est_mas)
        print(f"Sinu tulemus: {protsent}%")
    elif valik == '6':
        print("Programmi kasutamine lõpetatud.")
        break
    else:
        print("Vigane valik. Palun sisesta number vahemikus 1-6.")

