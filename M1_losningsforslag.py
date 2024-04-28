#%%

# MODUL 1

# Oppgave 1
navn = "Ole"
alder = 25

print(f"Hei, mitt navn er {navn}, og jeg er {alder} år gammel.")

#%%

# Oppgave 2

tall = 10

if tall > 0:
    print("Tallet er positivt.")
elif tall == 0:
    print("Tallet er null.")
else:
    print("Tallet er negativt.")


#%%

# Oppgave 3
# Definer poengsummen som skal vurderes
# Du kan endre denne verdien for å teste forskjellige utdata
poeng = 75  

# Sjekk poengsummen og skriv ut tilsvarende tilbakemelding
if poeng > 80:
    print("Utmerket")
elif 50 <= poeng <= 80:
    print("Godt")
elif 30 <= poeng < 50:
    print("Bestått")
else:
    print("Prøv igjen")

#%%