def mijn_functie_1(a):
    return a * a
def mijn_functie2(*args):
    return list(args)

tabel = {
    2: mijn_functie_1(2),
    4: mijn_functie_1(4),
    10: mijn_functie_1(10),
    12: mijn_functie_1(12),
    12.3: mijn_functie2(15, 9, 36, 4),
    12.2: mijn_functie2(14, 10, 24, 6),
    10.5: mijn_functie2(15, 5, 50, 2),
    100.20: mijn_functie2(120, 80, 2000, 5)
}

for key, value in tabel.items():
    print(f"Sleutel: {key}, Waarde: {value}")