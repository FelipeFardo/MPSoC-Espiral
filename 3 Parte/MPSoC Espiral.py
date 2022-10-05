import json

with open("Test4.json", encoding='utf-8') as meu_json:
    teste1 = json.load(meu_json)

rota=True

class Header(object):
    X = Y = int()


class Data(object):
    tamMatriz = Header()
    aux = Header()
    source = Header()
    target = Header()
    distancia = Header()
    qtdPacotes = posPonto = limiteTasks = qtd = id= ultimoId = numId = int()
    sSource = sTarget = str()
    matrizEspiral = list()
    matrizCalor = list()
    grafoTarefas = list()
    tarefas = list()
    ultimosId = list()
    posAplic = dict()

# funcao para criar as matrizes
def crie_matriz(data):
    data.matrizEspiral = []
    data.matrizCalor = []
    for y in range(data.tamMatriz.Y):
        linhaEspiral = []
        linhaCalor = []
        for x in range(data.tamMatriz.X):
            linhaEspiral.append([])
            linhaCalor.append(0)
        data.matrizEspiral.append(linhaEspiral)
        data.matrizCalor.append(linhaCalor)

def mostraMatriz(data,matriz=1):
    if matriz==1:
        print("\nMapa de Calor:")
    elif matriz==2:
        print(("\nMapeamento dos pontos:"))
    print("\n  Y\n  ^ ")
    print(f"{data.tamMatriz.Y+1:>2}|\n{data.tamMatriz.Y:>2}|")

    for y in range(data.tamMatriz.Y-1,-1,-1):
        print(f"{y:>2}|", end="")
        for x in range(data.tamMatriz.X):
            if matriz==1:
                print(f"{data.matrizCalor[y][x]:>3}", end="")
            elif matriz==2:
                print('[',end='')
                flag=False
                if len(data.matrizEspiral[y][x])==0:
                    print('00',end='')
                else:
                    for cheese in data.matrizEspiral[y][x]:
                        if flag==True:
                            print('/',end='')
                        else:
                            flag=True
                        print(f"{cheese['nome']}{cheese['id']}", end='')
                print(']',end='')
        print("")
    print(end="     ")
    for i in range(0, data.tamMatriz.X * 2, 1):
        print("--", end="")
    print("--->  X\n   ",end="")
    for i in range(data.tamMatriz.X):
        print(f"{i:>3}", end="")
    print(f"{data.tamMatriz.X:>3}{data.tamMatriz.X+1:>3}\n")


def MarcarPonto(data,raio):
    data.aux.Y = data.source.Y
    data.aux.X = data.source.X
    distancia = 0
    # calcula qual é a distancia do centro
    incremento = 1 if data.target.Y - data.source.Y > 0 else -1
    while data.aux.Y != data.target.Y:
        data.aux.Y += incremento
        distancia += 1
    incremento = 1 if data.target.X - data.source.X > 0 else -1
    while data.aux.X != data.target.X:
        data.aux.X += incremento
        distancia += 1
    # se a distancia for igual ao raio o ponto será marcado naquela posicao
    if distancia == raio and len(data.matrizEspiral[data.aux.Y][data.aux.X])<data.limiteTasks and data.ultimoId<data.qtd:
        pontoId = {'nome': data.tarefas[data.posPonto], 'id':  int(data.id)}
        data.matrizEspiral[data.aux.Y][data.aux.X].append(pontoId)
        data.posPonto+=1
        if data.posPonto == len(data.tarefas):
            data.ultimoId+=1
            data.id+=1
            data.posPonto=0

def distancia(data):
    data.source.Y = int(data.tamMatriz.Y/2)-1 if data.tamMatriz.Y % 2 == 0 else int(data.tamMatriz.Y/2)
    data.source.X = int(data.tamMatriz.X/2)-1 if data.tamMatriz.X % 2 == 0 else int(data.tamMatriz.X/2)
    raio = (data.tamMatriz.Y-1 - data.source.Y) + (data.tamMatriz.X-1 - data.source.X)
    # while para diminuir o raio a cada passada na matriz
    while raio >= 0:
        # 1 Quadrante
        for x in range(data.tamMatriz.X-1, data.source.X-1, -1):
            for y in range(data.tamMatriz.Y-1,data.source.Y-1,-1):
                data.target.X = x
                data.target.Y = y
                if (len(data.matrizEspiral[y][x])<data.limiteTasks):
                    MarcarPonto(data,raio)
        # 2 Quadrante
        for y in range(data.tamMatriz.Y-1,data.source.Y-1,-1):
            for x in range(data.source.X-1,-1,-1):
                data.target.X = x 
                data.target.Y = y
                if (len(data.matrizEspiral[y][x])<data.limiteTasks):
                    MarcarPonto(data,raio)
        # 3 Quadrante 
        for x in range (data.source.X):
            for y in range (data.source.Y):
                data.target.X = x 
                data.target.Y = y
                if (len(data.matrizEspiral[y][x])<data.limiteTasks):
                    MarcarPonto(data,raio)
        # 4 quadrante 
        for x in range(data.source.X, data.tamMatriz.X,1):
            for y in range(data.source.Y):
                data.target.X = x
                data.target.Y = y
                if (len(data.matrizEspiral[y][x])<data.limiteTasks):
                    MarcarPonto(data,raio)
        raio-=1
    

def router(data):
    if not rota:
        mostraMatriz(data, 2)
    #Aqui vai os testes de ponto
    for data.grafoTarefas in aplic["grafo_tarefas"]:
        data.sSource = data.grafoTarefas["tarefa_origem"]
        data.sTarget = data.grafoTarefas["tarefa_destino"]
        data.qtdPacotes = data.grafoTarefas['quantidade_pacotes']
        # percorre a matriz
        for y in range(data.tamMatriz.Y):
            for x in range(data.tamMatriz.X):
                for w in range(len(data.matrizEspiral[y][x])):
                    # acha a posicao do source
                    if data.matrizEspiral[y][x][w]['nome']==data.sSource and data.matrizEspiral[y][x][w]['id']==data.numId:
                        data.source.X = data.aux.X = x
                        data.source.Y = data.aux.Y = y
                    # acha a posicao do target
                    if data.matrizEspiral[y][x][w]['nome']==data.sTarget and data.matrizEspiral[y][x][w]['id']==data.numId:
                        data.target.X=x
                        data.target.Y=y
        if rota:
            mostraMatriz(data, 2)
            print(f"\nSource = {data.sSource} de ID = {data.numId} na Posição = [{data.source.X}][{data.source.Y}]")
            print(f"Target = {data.sTarget} de ID = {data.numId} na Posição = [{data.target.X}][{data.target.Y}]")
            print (f"Quantida de pacotes = {data.qtdPacotes}")
            print(f"\nProc[{data.source.X}][{data.source.Y}] criou a mensagem")
        data.matrizCalor[data.source.Y][data.source.X] += data.qtdPacotes
        # Altera  a coluna
        # identifica qual o melhor caminho a ser seguido pela coluna
        incremento = -1 if data.target.X - data.source.X > 0 and ((data.target.X - data.source.X) > (data.tamMatriz.X-1) / 2) or data.target.X - data.source.X < 0 and abs(data.target.X - data.source.X) <= (data.tamMatriz.X-1) / 2 else 1
        while data.aux.X != data.target.X:
            if data.aux.X == data.tamMatriz.X-1 and incremento == 1 or data.aux.X == 0 and incremento == -1:
                data.aux.X = 0 if data.aux.X == data.tamMatriz.X-1 else data.tamMatriz.X-1
                if rota:
                    print(f"Proc[{data.tamMatriz.X-1-data.aux.X}][{data.source.Y}] enviou a mensagem para o Proc[{data.aux.X}][{data.source.Y}]")
                    print(f"Proc[{data.aux.X}][{data.source.Y}] recebeu a mensagem do Proc[{data.tamMatriz.X-1-data.aux.X}][{data.source.Y}]")
                    if data.source.Y != data.target.Y or data.aux.X != data.target.X:
                        print(f"Proc[{data.aux.X}][{data.source.Y}] NAO e o destino")
            else:
                if rota:
                    print(f"Proc[{data.aux.X}][{data.source.Y}] enviou a mensagem do Proc[{data.aux.X+incremento}][{data.source.Y}]")
                    print(f"Proc[{data.aux.X+incremento}][{data.source.Y}] recebeu a mensagem do Proc[{data.aux.X}][{data.source.Y}]")
                    if data.source.Y != data.target.Y or data.aux.X + incremento != data.target.X:
                        print(f"Proc[{data.aux.X+incremento}][{data.source.Y}] NAO e o destino")
                data.aux.X += incremento
            data.matrizCalor[data.source.Y][data.aux.X] += data.qtdPacotes
        # Altera a linha 
        # identifica qual o melhor caminho a ser seguido pela linha
        incremento = -1 if data.target.Y - data.source.Y > 0 and ((data.target.Y - data.source.Y) > (data.tamMatriz.Y-1) / 2) or data.target.Y - data.source.Y < 0 and abs(data.target.Y - data.source.Y) <= (data.tamMatriz.Y-1) / 2 else 1
        while data.aux.Y != data.target.Y:
            # identifica se precisa fazer a volta na matriz (MESH-3D)
            if data.aux.Y == data.tamMatriz.Y-1 and incremento == 1 or data.aux.Y == 0 and incremento == -1:
                data.aux.Y = 0 if data.aux.Y == data.tamMatriz.Y-1 else data.tamMatriz.Y-1
                if rota:
                    print(f"Proc[{data.target.X}][{data.tamMatriz.Y-1-data.aux.Y}] enviou a mensagem para o Proc[{data.target.X}][{data.aux.Y}]")
                    print(f"Proc[{data.target.X}][{data.aux.Y}] recebeu a mensagem do Proc[{data.target.X}][{data.tamMatriz.Y-1-data.aux.Y}]")
                    if data.aux.Y != data.target.Y:
                        print(f"Proc[{data.target.X}][{data.aux.Y}] NAO e o destino")
            else:
                if rota:
                    print(f"Proc[{data.target.X}][{data.aux.Y}] enviou a mensagem do Proc[{data.target.X}][{data.aux.Y+incremento}]")
                    print(f"Proc[{data.target.X}][{data.aux.Y+incremento}] recebeu a mensagem do Proc[{data.target.X}][{data.aux.Y}]")
                    if data.aux.Y+incremento != data.target.Y:
                        print(f"Proc[{data.target.X}][{data.aux.Y+incremento}] NAO e o destino")
                data.aux.Y += incremento
            data.matrizCalor[data.aux.Y][data.target.X] += data.qtdPacotes
        if rota:
            print(f"Proc[{data.target.X}][{data.target.Y}] e o destino")
            print(f"Proc[{data.target.X}][{data.target.Y}] consumiu a mensagem\n")
            mostraMatriz(data, 1)
    if not rota:
        mostraMatriz(data, 1)


data = Data
data.tamMatriz.X = int(teste1["MPSOC_SIZE_X"])
data.tamMatriz.Y = int(teste1["MPSOC_SIZE_Y"])

data.limiteTasks = int(teste1["TASKS_PER_PROCESSOR"])

crie_matriz(data)
for data.posAplic in teste1["TEST"]:

    nomeAplic = data.posAplic["APP"]
    data.qtd = int(data.posAplic["QTD"])

    with open(f"Applications/{nomeAplic}.json", encoding='utf-8') as meu_json:
        aplic = json.load(meu_json)
    
    data.posPonto = data.ultimoId = data.id = 0
    data.tarefas=[]
    for data.grafoTarefas in aplic["grafo_tarefas"]:
        letra = data.grafoTarefas["tarefa_origem"]
        if (letra not in data.tarefas):
            data.tarefas.append(letra)
        letra = data.grafoTarefas["tarefa_destino"]
        if (letra not in data.tarefas):
            data.tarefas.append(letra)

    for l in range (0, data.qtd):
        for c in range(0, data.limiteTasks):
            distancia(data)
    data.ultimosId.append(data.ultimoId)

for data.posAplic in teste1["TEST"]:

    with open(f"Applications/{nomeAplic}.json", encoding='utf-8') as meu_json:
        aplic = json.load(meu_json)

    for q in (data.ultimosId):
        for data.numId in range(0, q):
            router(data)
        