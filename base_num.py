def nome():
    name = str(input('Qual o seu nome? '))
    return name

def intro():
    name = nome()
    print('Olá {}, seja bem vindo! \n'.format(name))
    return calculo()

def calculo():
    print("--Este é o cálculo de bases númericas")
    print("Qual cálculo deseja realizar?")    
    while True:
        op = input("[1] binário -> decimal\n[2] decimal -> binário\nR.:")
        if op == "1":
            bin = input("Digite um número binário para transformar em decimal: ")
            if all(cod in '01' for cod in  bin):
                lista = list(bin[::-1])
                decimal = 0
                for i, num in enumerate(lista):
                    decimal += int(num) * (2 ** i)
                print("R.:",decimal)
                break
            else: 
                print("informe apenas 0s e 1s")
        elif op == "2":
            dec = input("Digite um número decimal para transformar em binário: ")
            lista = [dec]
            lista_resto = []
            for i, num in enumerate(lista):
                if int(num) >= 2:
                    lista.append(int(num) // 2)
                    lista_resto.append(int(num) % 2)
                else:
                    lista_resto.append(1)
                    lista_resto.reverse()
            print("R.:",*lista_resto)
            break
        else:
            print("Informe a opção correta")
            continue
    
intro()
