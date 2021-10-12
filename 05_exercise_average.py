# input

nota_1 = float(input('digite a nota 1: '))
nota_2 = float(input('digite a nota 2: '))
nota_3 = float(input('digite a nota 3: '))

# Summary calculation

media = (nota_1 + nota_2 + nota_3) / 3

# Print Grade

print(media)

if media > 8:
    print('Parabens!!!')