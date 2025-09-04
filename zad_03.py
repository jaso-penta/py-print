''' Izračun mjesečne potrošnje el. struje te cijene el. struje koju potroši 
    mikrovalna pećnica snage 1,3 kW ako se koristi 2 sata dnevno?'''



el_price = 5.99
power = 1.3 # kW
hours_per_day = 2
days_per_month = 30


monthly_consumption = power * hours_per_day * days_per_month
price_by_month = monthly_consumption * el_price


print(f'Mjesecna potrosnja el. energije je: {monthly_consumption}, cijena potrosnje je: {price_by_month}')

print()
print('Mjesecna potrosnja el. energije i', 'cijena potrosnje je:', end=' ')
print(monthly_consumption, price_by_month, sep=', ')


    
  