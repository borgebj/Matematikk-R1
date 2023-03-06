''' Oppgave 2 '''

a = 1
b = 2
c = 1

d = b ** 2-4*a*c

if d < 0:
    print("Ingen løsning")

elif d == 0:
    e = (-b/(2*a))
    print("èn løsning : x=", e)

else:
    x1 = (-b+d**(1/2))/(2*a)
    x2 = (-b-d**(1/2))/(2*a)
    print(f'Det er 2 løsninger, x1={x1} og x2={x2}')
print("\n")

''' Oppgave 5 '''


def eddie_fluer(fluer=1000, dag=0):
    '''
    Kjører til ant fluer er 0
    '''

    while fluer > 0:
        # En dag hver loop
        dag += 1

        # edderkopp spiser 100 hver dag
        fluer -= 100

        # fluer økes med 5% hver dag
        fluer *= 1.05

        print(f'Antall fluer dag {dag} er {fluer}')

        # # Eddie venter slik at fluene kan bli over 1000 igjen
        # while fluer < 1000:
        #     dag += 1
        #     fluer *= 1.05

    return dag


print(f'\nEtter {eddie_fluer()} dager spiste Eddie alle edderkopper')
