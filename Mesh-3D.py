import json

with open("CenariosMesh.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


class Data(object):
    sourceX = sourceY = targetX = targetY = auxX = auxY = int()


def router(Data):
    print(f"Source = [{Data.sourceX}][{Data.sourceY}]")
    print(f"Target = [{Data.targetX}][{Data.targetY}]")
    print(f"\nProc[{Data.sourceX}][{Data.sourceY}] criou a mensagem")

    # Rota da Coluna
    incremento = -1 if Data.targetY - Data.sourceY > 0 and (Data.targetY - Data.sourceY) > (
        jTam-1)/2 or Data.targetY - Data.sourceY < 0 and abs(Data.targetY - Data.sourceY) <= (jTam-1)/2 else 1
    while Data.auxY != Data.targetY:
        # 3D
        if Data.auxY == jTam-1 and incremento == 1 or Data.auxY == 0 and incremento == -1:
            Data.auxY = 0 if Data.auxY == jTam-1 else jTam-1
            print(f"Proc[{Data.sourceX}][{jTam-1-Data.auxY}] enviou a mensagem para o Proc[{Data.sourceX}][{Data.auxY}]")
            print(f"Proc[{Data.sourceX}][{Data.auxY}] recebeu a mensagem do Proc[{Data.sourceX}][{jTam-1-Data.auxY}]")
            if Data.sourceX != Data.targetX or Data.auxY != Data.targetY: print(f"Proc[{Data.sourceX}][{Data.auxY}] NAO e o destino")
        # 2D
        else:
            print(f"Proc[{Data.sourceX}][{Data.auxY}] enviou a mensagem do Proc[{Data.sourceX}][{Data.auxY+incremento}]")
            print(f"Proc[{Data.sourceX}][{Data.auxY+incremento}] recebeu a mensagem do Proc[{Data.sourceX}][{Data.auxY}]")
            if Data.sourceX != Data.targetX or Data.auxY + incremento != Data.targetY: print(f"Proc[{Data.sourceX}][{Data.auxY+incremento}] NAO e o destino")
            Data.auxY += incremento

    # Rota da Linha
    incremento = -1 if Data.targetX - Data.sourceX > 0 and (Data.targetX - Data.sourceX) > (
        iTam-1)/2 or Data.targetX - Data.sourceX < 0 and abs(Data.targetX - Data.sourceX) <= (iTam-1)/2 else 1
    while Data.auxX != Data.targetX:
        # 3D
        if Data.auxX == iTam-1 and incremento == 1 or Data.auxX == 0 and incremento == -1:
            Data.auxX = 0 if Data.auxX == iTam-1 else iTam-1
            print(f"Proc[{iTam-1-Data.auxX}][{Data.targetY}] enviou a mensagem para o Proc[{Data.auxX}][{Data.targetY}]")
            print(f"Proc[{Data.auxX}][{Data.targetY}] recebeu a mensagem do Proc[{iTam-1-Data.auxX}][{Data.targetY}]")
            if Data.auxX != Data.targetX: print(f"Proc[{Data.auxX}][{Data.targetY}] NAO e o destino")
        # 2D
        else:
            print(f"Proc[{Data.auxX}][{Data.targetY}] enviou a mensagem para o Proc[{Data.auxX+incremento}][{Data.targetY}]")
            print(f"Proc[{Data.auxX+incremento}][{Data.targetY}] recebeu a mensagem do Proc[{Data.auxX}][{Data.targetY}]")
            if Data.auxX+incremento != Data.targetX: print(f"Proc[{Data.auxX+incremento}][{Data.targetY}] NAO e o destino")
            Data.auxX += incremento
    print(f"Proc[{Data.targetX}][{Data.targetY}] e o destino")
    print(f"Proc[{Data.targetX}][{Data.targetY}] consumiu a mensagem\n")


iTam = dados['Size']['X']
jTam = dados['Size']['Y']
k = 1

print("\nMesh: ")
print("\nY\n^ ")
print("|\n|")
for i in range(iTam, -1, -1):
    print("|", end="")
    for j in range(0, jTam+1, 1):
        print(f"  {j}{i}", end="")
    print("")
for i in range(0, jTam*2, 1):
    print("--", end="")
print("------>  X")

for i in dados['Packages']:
    print(f"Exemplo {k}: ")
    k += 1
    Data.sourceX = Data.auxX = int(i['Source']['X'])
    Data.sourceY = Data.auxY = int(i['Source']['Y'])
    Data.targetX = int(i['Target']['X'])
    Data.targetY = int(i['Target']['Y'])

    router(Data)

print("Volte Sempre")
