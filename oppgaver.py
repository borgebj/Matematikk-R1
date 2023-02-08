
# Oppgave 1
# Algoritme som summerer 2 tall hvor bruker legger inn 2 tall

def sum(a, b):
    return a + b

a = int(input("Tall A: "))
b = int(input("Tall B: "))
print(f'Sum av {a} og {b} er {sum(a, b)}')

print("\n", "-"*15, "\n")
# Oppgave 2
# Algoritme som regner  fra millimeter til meter hvor bruker legger inn tall

def mm_to_m(mm):
    return mm / 1000

mm = int(input("Skriv inn millimeter: "))
print(f'{mm} mm til meter = {mm_to_m(mm)} m')

print("\n", "-"*15, "\n")
# Oppgave 3
# Algoritme som regner fra celsius til fahrenheit

def celsius_to_fahrenheit(celsius):
    return (9/5)*celsius+32

celsius = int(input("Skriv inn celsius: "))
print(f'{celsius} grader celsius = {celsius_to_fahrenheit(celsius)} grader fahrenheit')

print("\n", "-"*15, "\n")
# Oppgave 4
# Algoritme som regner minutter til timer og minutter med brukerinput
def min_to_hour(min):
    res_tim = min // 60
    res_min = min % 60
    return res_tim, res_min

minutter = int(input("Skriv inn antall minutter: "))
tim, min = min_to_hour(minutter)

print(f'\nDu srkev {minutter} minutter')
print(f'{minutter} = {tim} timer og {min}')