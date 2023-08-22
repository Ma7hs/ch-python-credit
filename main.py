import csv


tipos_garantias = {
    1: 'Imovel',
    2: 'Terreno',
    3: 'Veiculo',
    4: 'Celular',
    5: 'Salario',
    6: 'FGTS',
    7: 'Joias',
    8: 'Objetos de valores'
}
solicitantes = {}

def verificar_dados(i):

    print(f'SOLICITANTE {i}')

    tipo_documento = input('Qual tipo de documento você deseja verificar (CPF ou CNPJ)? ').upper()
    while tipo_documento not in ['CPF', 'CNPJ']:
        print('Esse tipo de documento não corresponde ao que estamos solicitando')
        tipo_documento = input('Apenas CPF ou CNPJ: ').upper()

    numero_documento = input(f'Digite o número do {tipo_documento}: ')
  
    print("Opções de garantia disponíveis:")
    for num, garantia in tipos_garantias.items():
        print(f"{num}: {garantia}")

    forma_garantia_num = int(input('Escolha o número correspondente à forma de garantia: '))
    while forma_garantia_num not in tipos_garantias:
        print('Não temos essa opção disponível de forma para garantir seu empréstimo!')
        forma_garantia_num = int(input(f'Escolha uma opção válida: '))

    valor_garantia = int(input(f'Digite o valor da garantia de seu {tipos_garantias[forma_garantia_num]}:'))
    while valor_garantia == '':
        print('O valor não pode estar vazio')
        valor_garantia = input(f'Digite o valor da garantia: ')


    forma_garantia = tipos_garantias[forma_garantia_num]

    return {
        'TIPO_DOCUMENTO': tipo_documento,
        'NUMERO_DOCUMENTO': numero_documento,
        'FORMA_GARANTIA': forma_garantia,
        'VALOR_GARANTIA': valor_garantia
    }

for i in range(1, 6):
    solicitantes[i] = verificar_dados(i)
    print(solicitantes)
    

csv_file = input('Digite o nome do arquivo que deseja criar: ')
csv_filename = csv_file+'.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['TIPO_DOCUMENTO', 'NUMERO_DOCUMENTO', 'FORMA_GARANTIA', 'VALOR_GARANTIA']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for solicitante_id, dados in solicitantes.items():
        print(solicitante_id)
        writer.writerow(dados)

print(f'Dados salvos no arquivo {csv_filename}')
