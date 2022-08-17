class Data(object):
    sourceX = sourceY = targetX = targetY = auxI = auxJ = int()


def routerJ(Data, incremento=1):
    while True:
        if Data.auxJ == Data.targetY:
            break
        elif Data.auxJ == jTam-1 and incremento == 1 or Data.auxJ == 0 and incremento == -1:
            Data.auxJ = 0 if Data.auxJ == jTam-1 else jTam-1
            print(
                f"Proc[{Data.sourceX}][{jTam-1-Data.auxJ}] enviou a mensagem para o Proc[{Data.sourceX}][{Data.auxJ}]")
            print(
                f"Proc[{Data.sourceX}][{Data.auxJ}] recebeu a mensagem do Proc[{Data.sourceX}][{jTam-1-Data.auxJ}]")
            if Data.sourceX != Data.targetX or Data.auxJ != Data.targetY:
                print(
                    f"Proc[{Data.sourceX}][{Data.auxJ}] NAO e o destino")
        else:
            print(
                f"Proc[{Data.sourceX}][{Data.auxJ}] enviou a mensagem do Proc[{Data.sourceX}][{Data.auxJ+incremento}]")
            print(
                f"Proc[{Data.sourceX}][{Data.auxJ+incremento}] recebeu a mensagem do Proc[{Data.sourceX}][{Data.auxJ}]")
            if Data.sourceX != Data.targetX or Data.auxJ + incremento != Data.targetY:
                print(
                    f"Proc[{Data.sourceX}][{Data.auxJ+incremento}] NAO e o destino")
            Data.auxJ += incremento


def routerI(Data, incremento=1):
    while True:
        if Data.auxI == Data.targetX:
            break
        elif Data.auxI == iTam-1 and incremento == 1 or Data.auxI == 0 and incremento == -1:
            Data.auxI = 0 if Data.auxI == iTam-1 else iTam-1
            print(
                f"Proc[{iTam-1-Data.auxI}][{Data.targetY}] enviou a mensagem para o Proc[{Data.auxI}][{Data.targetY}]")
            print(
                f"Proc[{Data.auxI}][{Data.targetY}] recebeu a mensagem do Proc[{iTam-1-Data.auxI}][{Data.targetY}]")
            if Data.auxI != Data.targetX:
                print(
                    f"Proc[{Data.auxI}][{Data.targetY}] NAO e o destino")
        else:
            print(
                f"Proc[{Data.auxI}][{Data.targetY}] enviou a mensagem para o Proc[{Data.auxI+incremento}][{Data.targetY}]")
            print(
                f"Proc[{Data.auxI+incremento}][{Data.targetY}] recebeu a mensagem do Proc[{Data.auxI}][{Data.targetY}]")
            if Data.auxI+incremento != Data.targetX:
                print(
                    f"Proc[{Data.auxI+incremento}][{Data.targetY}] NAO e o destino")
            Data.auxI += incremento


iTam = int(input("Quantas linhas tem a matriz? "))
jTam = int(input("Quantas colunas tem a matriz? "))

while True:

    print("")

    for i in range(iTam):
        for j in range(jTam):
            print("  " + str(i) + str(j), end="")
        print("")

    Data.sourceX = int(input("\nQuem e o X do Source? "))
    Data.sourceY = int(input("Quem e o Y do Source? "))
    Data.targetX = int(input("Quem e o X do Target? "))
    Data.targetY = int(input("Quem e o Y do Target? "))

    print(f"\nProc[{Data.sourceX}][{Data.sourceY}] criou a mensagem")

    Data.auxI = Data.sourceX
    Data.auxJ = Data.sourceY

    if Data.targetY - Data.sourceY > 0 and (Data.targetY - Data.sourceY) > (jTam-1)/2 or Data.targetY - Data.sourceY < 0 and abs(Data.targetY - Data.sourceY) <= (jTam-1)/2:
        routerJ(Data, -1)
    else:
        routerJ(Data)
    if Data.targetX - Data.sourceX > 0 and (Data.targetX - Data.sourceX) > (iTam-1)/2 or Data.targetX - Data.sourceX < 0 and abs(Data.targetX - Data.sourceX) <= (iTam-1)/2:
        routerI(Data, -1)
    else:
        routerI(Data)

    print(f"Proc[{Data.targetX}][{Data.targetY}] e o destino")
    print(f"Proc[{Data.targetX}][{Data.targetY}] consumiu a mensagem")

    sair = input("Deseja sair? [S/N] ")
    if (sair in "SIMsim"):
        print("Volte sempre!")
        break
    print("")
