import random

NUMEROS = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7]

print('BEM VINDO A MÁQUINA DE CAÇA-NÍQUEIS')
print('o valor total da maquina é | $50.000,00 |')

while True:
    wallet = int(input('Quantos dolares vai ser depositado na máquina? $'))   

    if wallet < 50:
        print('Valores abaixo de $50 não são aceito')
    elif wallet > 1000:
        print('Valores acima de $1000 não são aceito')
    else:
        break

cretites = wallet * 20
print(f'Seus creditos são | ${cretites} |')

while cretites > 0 or cretites < 1000000:
    print('O que bocê deseja?')
    print (' 1 = Ver creditos \n 2 = Apostar')
    opc = int(input())

    if opc == 1:
        print(f'Seus creditos são | ${cretites} |')
    elif opc == 2:
        while True:
            while True:
                print('Quantos você deseja apostar')

                if cretites >= 525:
                    print (' 1 = 75 | 2 = 150 | 3 = 225 | 4 = 300 | 5 = 375 | 6 = 450 | 7 = 525 ')
                    while True:
                        apo = int(input())
                        if apo == 1:
                            x = 75
                            break
                        elif apo == 2:
                            x = 150
                            break
                        elif apo == 3:
                            x = 225
                            break
                        elif apo == 4:
                            x = 300
                            break
                        elif apo == 5:
                            x = 375
                            break
                        elif apo == 6:
                            x = 450
                            break
                        elif apo == 7:
                            x = 525
                            break
                        else:
                            print('Valor de aposta invalido')
                            break
                elif cretites >= 450:
                    print (' 1 = 75 | 2 = 150 | 3 = 225 | 4 = 300 | 5 = 375 | 6 = 450 ')
                    while True:
                        apo = int(input())
                        if apo == 1:
                            x = 75
                            break
                        elif apo == 2:
                            x = 150
                            break
                        elif apo == 3:
                            x = 225
                            break
                        elif apo == 4:
                            x = 300
                            break
                        elif apo == 5:
                            x = 375
                            break
                        elif apo == 6:
                            x = 450
                            break
                        else:
                            print('Valor de aposta invalido')
                            break
                elif cretites >= 375:
                    print (' 1 = 75 | 2 = 150 | 3 = 225 | 4 = 300 | 5 = 375 ')
                    while True:
                        apo = int(input())
                        if apo == 1:
                            x = 75
                            break
                        elif apo == 2:
                            x = 150
                            break
                        elif apo == 3:
                            x = 225
                            break
                        elif apo == 4:
                            x = 300
                            break
                        elif apo == 5:
                            x = 375
                            break
                        else:
                            print('Valor de aposta invalido')
                            break
                elif cretites >= 300:
                    print (' 1 = 75 | 2 = 150 | 3 = 225 | 4 = 300 ')
                    while True:
                        apo = int(input())
                        if apo == 1:
                            x = 75
                            break
                        elif apo == 2:
                            x = 150
                            break
                        elif apo == 3:
                            x = 225
                            break
                        elif apo == 4:
                            x = 300
                            break
                        else:
                            print('Valor de aposta invalido')
                            break
                elif cretites >= 225:
                    print (' 1 = 75 | 2 = 150 | 3 = 225 ')
                    while True:
                        apo = int(input())
                        if apo == 1:
                            x = 75
                            break
                        elif apo == 2:
                            x = 150
                            break
                        elif apo == 3:
                            x = 225
                            break
                        else:
                            print('Valor de aposta invalido')
                            break
                elif cretites >= 150:
                    print (' 1 = 75 | 2 = 150')
                    while True:
                        apo = int(input())
                        if apo == 1:
                            x = 75
                            break
                        elif apo == 2:
                            x = 150
                            break
                        else:
                            print('Valor de aposta invalido')
                            break
                else:
                    print (' 1 = 75 ')
                    while True:
                        apo = int(input())
                        if apo == 1:
                            x = 75
                            break
                        else:
                            print('Valor de aposta invalido')
                            break
                
                if apo >= 1 and apo <= 7:
                    break
                else:
                    print('escolha umas das opções desejada')
            
            num1 = random.choice(NUMEROS)
            num2 = random.choice(NUMEROS)
            num3 = random.choice(NUMEROS)
            num4 = random.choice(NUMEROS)
            num5 = random.choice(NUMEROS)
            num6 = random.choice(NUMEROS)
            num7 = random.choice(NUMEROS)
            num8 = random.choice(NUMEROS)
            num9 = random.choice(NUMEROS)
            print(f' | {num1} | {num2} | {num3} | ')
            print(f'-|-{num4}-|-{num5}-|-{num6}-|-')
            print(f' | {num7} | {num8} | {num9} | ')

            if num4 == 1 or num5 == 1 or num6 == 1:
                if num4 == 1 and num5 == 1 and num6 == 1:
                    pre = x * 4
                    print('Perdeu total')
                    cretites = cretites - pre
                elif num4 == 1 and num5 == 1 or num4 == 1 and num6 == 1 or num5 == 1 and num6 == 1:
                    pre = x * 2
                    print('Perdeu em dobro')
                    cretites = cretites - pre
                else:
                    print('Perdeu a rodada')
                    cretites = cretites - x
            elif num4 == num5 == num6:
                if num5 in [2, 3, 4]:
                    pre = x * 4
                    print(f'prêmio modesto {pre}')
                    cretites = cretites + pre
                elif num5 in [5, 6]:
                    pre = x * 6
                    print(f'prêmio medio {pre}')
                    cretites = cretites + pre
                elif num5 == 7:
                    pre = x * 8
                    print(f'prêmio grandioso {pre}')
                    cretites = cretites + pre
            elif num4 == num5 or num4 == num6:
                if num4 in [2, 3, 4]:
                    pre = x * 2
                    print(f'prêmio modesto {pre}')
                    cretites = cretites + pre
                elif num4 in [5, 6]:
                    pre = x * 3
                    print(f'prêmio medio {pre}')
                    cretites = cretites + pre
                elif num4 == 7:
                    pre = x * 4
                    print(f'prêmio grandioso {pre}')
                    cretites = cretites + pre
            elif num5 == num6:
                if num5 in [2, 3, 4]:
                    pre = x * 2
                    print(f'prêmio modesto {pre}')
                    cretites = cretites + pre
                elif num5 in [5, 6]:
                    pre = x * 3
                    print(f'prêmio medio {pre}')
                    cretites = cretites + pre
                elif num5 == 7:
                    pre = x * 4
                    print(f'prêmio grandioso {pre}')
                    cretites = cretites + pre
            else:
                print('Perdeu a rodada')
                cretites = cretites - x

            if cretites > 0:
                wallet
            elif cretites >= 1000000:
                print('PARABENS VOCÊ GANHOU $50.000,00')
            else:
                print('Game Over')
                break
            
            sair = float(input('Deseja continuar ( 1 = SIM | 2 = NÃO )?'))
            if sair == 1:
                continue
            else:
                break
    else:
        continue
