'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:
    
    Ime, prezime, godinu rođenja, državu rođenja, status radnog odnosa, težinu te spol
    
    Stranice a i b, četverokuta te za površinu tog četverokuta.
    
    Izračun mjesečne potrošnje el. struje te cijene el. struje koju potroši 
    mikrovalna pećnica snage 1,3 kW ako se koristi 2 sata dnevno?
    
    Stranice trokuta, površinu trokuta (P = (𝑎 ∗ 𝑣_𝑎)/2, 𝑣_𝑎 je visina na stranicu a) te opseg trokuta.
'''

first_name = "Ivo"
last_name = "Ivic'"
birth_year = 1991
state_of_birth = "Hrvatska"
if_employed = True
weight = 80.00 # in kg
gender = "male"


print()                                                     # \n
print('Ime:', first_name, end='; ')                         # \n
print('Prezime:', last_name, end='; ')                      # \n
print('Datum rodjenja', birth_year)
print('Drzava rodjenja:', state_of_birth)
print('Radni status:', if_employed)
print('Tezina:', weight)
print('Spol:', gender)
print()




a = 10
b = 5
p = a * b




power = 1.3
usage_time = 2