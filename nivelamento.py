altura = []
genero = []
altparamedia = 0
n_masc = 0

for i in range(15):

#Repetição para a altura
    while True:
        try: #Para lidar com exceções (erros) na execução - e.g.: para caso o usuário digite letras ao invés de colocar números.
            alt = float(input(f'Digite a altura {i+1} (m.cm): '))
            if alt > 0:
                altura.append(alt)
                break
            else:
                print('A altura deve ser um número válido')
        
        except ValueError: #Para evitar que o programa finalize dando erro por causa de letras no float. 
            print('Altura inválida. Digite um número válido.')

#Repetição para o genero:  
    while True:
        gen = input(f'Digite o gênero da pessoa {i+1} (Masculino/Feminino): ').strip().lower()

        if gen in ['masculino','feminino']:
            genero.append(gen)

            if gen == 'masculino':
                altparamedia += alt
                n_masc += 1

            break
        else:
            print('Gênero inválido. Digite uma das duas opções')
        
#Maior e menor altura
maior_altura = max(altura)
menor_altura = min(altura)

#Média de alturas masculino
media = altparamedia / n_masc

#Número de pessoas do gênero Feminino
num_fem = genero.count('feminino')

#Printando
print(f"Maior altura do grupo: {maior_altura:.2f}m")
print(f"Menor altura do grupo: {menor_altura:.2f}m")
print(f'A média de altura dos homens desse grupo é igual a {media}')
print(f'O número de mulheres no grupo é igual a: {num_fem}')
