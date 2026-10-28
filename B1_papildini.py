skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        limenis = rinda.split()[2]
          Skaits[limenis] = skaits.get(limenis. 0) + 1

for limenis, daudzums in sorted(skaits.items(), Key=lambda x: x[1], reverse=True) :
  print(f"{limenis}: {daudzums}")
