def calcular_distancia_total(matriz, itinerario):
    distancia_total = 0.0
    for i in range(len(itinerario) - 1):
        cidade_a = itinerario[i]
        cidade_b = itinerario[i + 1]
        distancia_total += matriz[cidade_a][cidade_b]
    
    distancia_total += matriz[itinerario[-1]][itinerario[0]]
    return distancia_total

def obter_vizinhos(solucao):
    vizinhos = []
    for i in range(len(solucao)):
        for j in range(i + 1, len(solucao)):
            vizinho = solucao[:]
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            vizinhos.append(vizinho)
    return vizinhos

def ler_matriz_distancias(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    
    matriz = []
    for linha in linhas:
        valores = linha.split()
        matriz.append([float(valor) for valor in valores])
    
    return matriz