import json

with open("AppsDesafio.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


class Data(object):
    sourceX = sourceY = targetX = targetY = auxX = auxY = qtdPacotes = int()
    sSource = sTarget = str()


iTam = jTam = int()

rota = dados['rota']


def crie_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas+1):
        linha = []
        for j in range(n_colunas+1):
            linha.append(0)
        matriz.append(linha)
    return matriz


matrizCalor = matrizMapeamento = list()


def mapeamento():
    print("Mapeamento:\n\nY\n^\n|\n| ")

    for i in range(iTam, -1, -1):
        print("|", end="")
        for j in range(0, jTam+1, 1):
            print(f"  {matrizMapeamento[j][i]}", end="")
        print()
    print("  ", end="")
    for i in range(0, jTam * 2, 1):
        print("--", end="")
    print("--->  X")


def contadorDePacotes():

    print("\nContador de pacotes por PE:")
    print("\nY\n^ ")
    print("|\n|")

    for i in range(iTam, -1, -1):
        print("|", end="")
        for j in range(0, jTam+1, 1):
            print(f"{matrizCalor[j][i]:>3}", end="")
        print("")
    print(end="  ")
    for i in range(0, jTam * 2, 1):
        print("--", end="")
    print("--->  X\n\n")


def router(Data):
    if rota:
        print(f"Source = [{Data.sourceX}][{Data.sourceY}]")
        print(f"Target = [{Data.targetX}][{Data.targetY}]")
        print(f"\nProc[{Data.sourceX}][{Data.sourceY}] criou a mensagem")

    matrizCalor[Data.sourceX][Data.sourceY] += Data.qtdPacotes
    incremento = 1
    if Data.targetY - Data.sourceY > 0 and ((Data.targetY - Data.sourceY) > (jTam) / 2) or Data.targetY - Data.sourceY < 0 and abs(Data.targetY - Data.sourceY) <= (jTam) / 2:
        incremento = -1
    while Data.auxY != Data.targetY:
        if Data.auxY == jTam and incremento == 1 or Data.auxY == 0 and incremento == -1:
            Data.auxY = 0 if Data.auxY == jTam  else jTam 
            if rota:
                print(f"Proc[{Data.sourceX}][{jTam-Data.auxY}] enviou a mensagem para o Proc[{Data.sourceX}][{Data.auxY}]")
                print(f"Proc[{Data.sourceX}][{Data.auxY}] recebeu a mensagem do Proc[{Data.sourceX}][{jTam-Data.auxY}]")
                if Data.sourceX != Data.targetX or Data.auxY != Data.targetY:
                    print(f"Proc[{Data.sourceX}][{Data.auxY}] NAO e o destino")
        else:
            if rota:
                print(f"Proc[{Data.sourceX}][{Data.auxY}] enviou a mensagem do Proc[{Data.sourceX}][{Data.auxY+incremento}]")
                print(f"Proc[{Data.sourceX}][{Data.auxY+incremento}] recebeu a mensagem do Proc[{Data.sourceX}][{Data.auxY}]")
                if Data.sourceX != Data.targetX or Data.auxY + incremento != Data.targetY:
                    print(f"Proc[{Data.sourceX}][{Data.auxY+incremento}] NAO e o destino")
            Data.auxY += incremento
        matrizCalor[Data.sourceX][Data.auxY] += Data.qtdPacotes

    incremento = 1
    if Data.targetX - Data.sourceX > 0 and (Data.targetX - Data.sourceX) > (iTam) / 2 or (Data.targetX - Data.sourceX) < 0 and abs(Data.targetX - Data.sourceX) <= (iTam) / 2:
        incremento = -1
    while Data.auxX != Data.targetX:
        if Data.auxX == iTam and incremento == 1 or Data.auxX == 0 and incremento == -1:
            Data.auxX = 0 if Data.auxX == iTam else iTam
            if rota:
                print(f"Proc[{iTam-Data.auxX}][{Data.targetY}] enviou a mensagem para o Proc[{Data.auxX}][{Data.targetY}]")
                print(f"Proc[{Data.auxX}][{Data.targetY}] recebeu a mensagem do Proc[{iTam-Data.auxX}][{Data.targetY}]")
                if Data.auxX != Data.targetX:
                    print(f"Proc[{Data.auxX}][{Data.targetY}] NAO e o destino")
        else:
            if rota:
                print(f"Proc[{Data.auxX}][{Data.targetY}] enviou a mensagem para o Proc[{Data.auxX+incremento}][{Data.targetY}]")
                print(f"Proc[{Data.auxX+incremento}][{Data.targetY}] recebeu a mensagem do Proc[{Data.auxX}][{Data.targetY}]")
                if Data.auxX+incremento != Data.targetX:
                    print(f"Proc[{Data.auxX+incremento}][{Data.targetY}] NAO e o destino")
            Data.auxX += incremento
        matrizCalor[Data.auxX][Data.targetY] += Data.qtdPacotes
    if rota:
        print(f"Proc[{Data.targetX}][{Data.targetY}] e o destino")
        print(f"Proc[{Data.targetX}][{Data.targetY}] consumiu a mensagem\n")
        contadorDePacotes()


print(""" -----------------------------------------------------------------------------------------------------------------
| Bem vindo ao Contador de Pacotes por PE de processamento MPSoC!                                                 |
| O Algoritmo identifica qual o melhor caminho para realizar o trafego, sendo um Mesh-3D                          |
| Caso deseja ver o trafego da informacao detalhadamente, mude para TRUE o valor de ROTA no AppsDesafio.json      |
| Caso tambem queira modificar ou adicionar um caso de teste e so alterar diretamente no arquivo AppsDesafio.json |""")
if rota:
    print(
        "| GUIA: Proc[Coluna][Linha]                                                                                       |")
print(" -----------------------------------------------------------------------------------------------------------------")

k = 1
for posAplic in dados['aplicacoes']:
    print(f"\nAplicacao {k}: \n")
    k += 1
    iTam = posAplic['size']['Y']
    jTam = posAplic['size']['X']

    matrizCalor = crie_matriz(iTam, jTam)
    matrizMapeamento = crie_matriz(iTam, jTam)

    for posPonto in posAplic['pontos']:
        ponto = posPonto['ponto']
        x = posPonto['X']
        y = posPonto['Y']
        matrizMapeamento[x][y] = ponto

    mapeamento()

    for posGT in posAplic['grafo_tarefas']:
        Data.sSource = posGT['tarefa_origem']
        Data.sTarget = posGT['tarefa_destino']
        Data.qtdPacotes = posGT['quantidade_pacotes']

        for i in range(iTam, -1, -1):
            for j in range(0, jTam+1, 1):
                if matrizMapeamento[j][i] == Data.sSource:
                    Data.sourceX = Data.auxX = j
                    Data.sourceY = Data.auxY = i
                if matrizMapeamento[j][i] == Data.sTarget:
                    Data.targetX = j
                    Data.targetY = i
        router(Data)

    contadorDePacotes()

print("\n\nVolte sempre!\n")
