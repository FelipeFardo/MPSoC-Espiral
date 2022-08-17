import json

with open("CenariosMesh.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


class Data(object):
    sourceX = sourceY = targetX = targetY = auxX = auxY = int()


def routerJ(Data, incremento=1):
    while True:
        if Data.auxY == Data.targetY:
            break
        elif Data.auxY == jTam-1 and incremento == 1 or Data.auxY == 0 and incremento == -1:
            Data.auxY = 0 if Data.auxY == jTam-1 else jTam-1
            print(
                f"Proc[{Data.sourceX}][{jTam-1-Data.auxY}] enviou a mensagem para o Proc[{Data.sourceX}][{Data.auxY}]")
            print(
                f"Proc[{Data.sourceX}][{Data.auxY}] recebeu a mensagem do Proc[{Data.sourceX}][{jTam-1-Data.auxY}]")
            if Data.sourceX != Data.targetX or Data.auxY != Data.targetY:
                print(f"Proc[{Data.sourceX}][{Data.auxY}] NAO e o destino")
        else:
            print(
                f"Proc[{Data.sourceX}][{Data.auxY}] enviou a mensagem do Proc[{Data.sourceX}][{Data.auxY+incremento}]")
            print(
                f"Proc[{Data.sourceX}][{Data.auxY+incremento}] recebeu a mensagem do Proc[{Data.sourceX}][{Data.auxY}]")
            if Data.sourceX != Data.targetX or Data.auxY + incremento != Data.targetY:
                print(
                    f"Proc[{Data.sourceX}][{Data.auxY+incremento}] NAO e o destino")
            Data.auxY += incremento


def routerI(Data, incremento=1):
    while True:
        if Data.auxX == Data.targetX:
            break
        elif Data.auxX == iTam-1 and incremento == 1 or Data.auxX == 0 and incremento == -1:
            Data.auxX = 0 if Data.auxX == iTam-1 else iTam-1
            print(
                f"Proc[{iTam-1-Data.auxX}][{Data.targetY}] enviou a mensagem para o Proc[{Data.auxX}][{Data.targetY}]")
            print(
                f"Proc[{Data.auxX}][{Data.targetY}] recebeu a mensagem do Proc[{iTam-1-Data.auxX}][{Data.targetY}]")
            if Data.auxX != Data.targetX:
                print(f"Proc[{Data.auxX}][{Data.targetY}] NAO e o destino")
        else:
            print(
                f"Proc[{Data.auxX}][{Data.targetY}] enviou a mensagem para o Proc[{Data.auxX+incremento}][{Data.targetY}]")
            print(
                f"Proc[{Data.auxX+incremento}][{Data.targetY}] recebeu a mensagem do Proc[{Data.auxX}][{Data.targetY}]")
            if Data.auxX+incremento != Data.targetX:
                print(
                    f"Proc[{Data.auxX+incremento}][{Data.targetY}] NAO e o destino")
            Data.auxX += incremento


iTam = dados['Size']['X']
jTam = dados['Size']['Y']

for i in range(iTam):
    for j in range(jTam):
        print("  " + str(i) + str(j), end="")
    print("")
print("")

j = 1
for i in dados['Packages']:
    print(f"Exemplo {j}: ")
    j += 1
    Data.sourceX = Data.auxX = int(i['Source']['X'])
    Data.sourceY = Data.auxY = int(i['Source']['Y'])
    Data.targetX = int(i['Target']['X'])
    Data.targetY = int(i['Target']['Y'])

    print(f"Source = [{Data.sourceX}][{Data.sourceY}]")
    print(f"Target = [{Data.targetX}][{Data.targetY}]")
    print(f"\nProc[{Data.sourceX}][{Data.sourceY}] criou a mensagem")

    if Data.targetY - Data.sourceY > 0 and (Data.targetY - Data.sourceY) > (jTam-1)/2 or Data.targetY - Data.sourceY < 0 and abs(Data.targetY - Data.sourceY) <= (jTam-1)/2:
        routerJ(Data, -1)
    else:
        routerJ(Data)
    if Data.targetX - Data.sourceX > 0 and (Data.targetX - Data.sourceX) > (iTam-1)/2 or Data.targetX - Data.sourceX < 0 and abs(Data.targetX - Data.sourceX) <= (iTam-1)/2:
        routerI(Data, -1)
    else:
        routerI(Data)

    print(f"Proc[{Data.targetX}][{Data.targetY}] e o destino")
    print(f"Proc[{Data.targetX}][{Data.targetY}] consumiu a mensagem\n")

print("Volte Sempre")
