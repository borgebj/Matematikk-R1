
# konverterer minutter til timer og minutter
def min_to_hour(min):
    res_tim = min // 60
    res_min = min % 60
    return res_tim, res_min

minutter = int(input("Skriv inn antall minutter: "))
tim, min = min_to_hour(minutter)

print(f'\nDu srkev {minutter} minutter')
print(f"{minutter} = {tim} timer og {min} minutter")

print("\n", "-"*15, "\n")

# Legger sammen alle tall fra a til b
a = int(input("Fra: "))
b = int(input("Til: "))
sum = a
for i in range(a, b+1):
    sum += i
print(f'Summen av tall fra {a} til {b} er {sum}')