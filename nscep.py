import requests
import os

def main():
    os.system("clear")
    print("""\033[1;31m
 _   _ ____         ____ _____ ____  
| \ | / ___|       / ___| ____|  _ \ 
|  \| \___ \ _____| |   |  _| | |_) |
| |\  |___) |_____| |___| |___|  __/ 
|_| \_|____/       \____|_____|_|    
    """)

    cep_input = input("\033[1;31m-\033[1;34mCEP\033[1;31m->")

    if len(cep_input) != 8:
        print("Seu idiota, você digitou uma quantidade de numeros menor ou maior que 8, digita essa porra direito")
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print()
        print('\033[1;32m>>> \033[1;31mCEP ENCONTRADO \033[1;32m<<<')
        print()
        print('\033[1;36mCEP: {}'.format(address_data['cep']))
        print('LOGRADOURO: {}'.format(address_data['logradouro']))
        print('COMPLEMENTO: {}'.format(address_data['complemento']))
        print('BAIRRO: {}'.format(address_data['bairro']))
        print('CIDADE: {}'.format(address_data['localidade']))
        print('ESTADO: {}'.format(address_data['uf']))
        print('IBGE: {}'.format(address_data['ibge']))
        print('GIA: {}'.format(address_data['gia']))
        print('DDD: {}'.format(address_data['ddd']))
        print('SIAFI: {}'.format(address_data['siafi']))
        print()
        
    else:
        print('\033[1;35m{} é um CEP inválido seu retardado'.format(cep_input))
    
    opt = input('\033[1;33mDeseja realizar uma nova consulta? \033[1;32ms\033[1;33m/\033[1;31mn\033[1;33m: ')
    if opt == 's':
        main()

    if opt == 'n':
        print("\033[1;35mVocê escolheu sair, volte sempre meu caro infectado ^-^")

if __name__== '__main__':
    main()
