    
'''Stranice a i b, četverokuta te za površinu tog četverokuta. '''




a = 5
b = 8

p = a * b


# Povrsina cetverkota stranica: a = [vrijednost varijable]; b = [vrijednost varijable] je: [vrijednost varijable]


print(f'povrsina cetverokuta stranice: a = {a}; b = {b} je: {p}') # provjera rjesenja

# Kreirate privremene varijable koje sluze za pripremu poruke korisniku
first_part = 'Povrsina stranice a: = ' 
second_part = ' ; b = ' 
third_part = ' je: ' 
fourth_part = ' . '

print(first_part, a, second_part, b, third_part, p, fourth_part, sep='')


# Unutar print() funkcije mozemo raditi racunanje
print('Povrsina cetverokuta stranica: a = ', a, '; b = ', b, ' je: ', a * b, '.', sep='')



print('Povrsina cetverokuta stranica: a = ', a, '; b = ', b, ' je: ', p, '.', sep='')