import random
import math
from src.infrastructure.utils.helpers import calcular_distancia_total, obter_vizinhos

class SolveTSP:
    def __init__(self, distance_matrix, config):
        self.distance_matrix = distance_matrix
        self.T = config['T0']
        self.Tf = config['Tf']
        self.L = config['L']
        self.alfa = config['alfa']

    def execute(self):
        S = random.sample(range(len(self.distance_matrix)), len(self.distance_matrix))
        best_solution = S
        best_cost = calcular_distancia_total(self.distance_matrix, S)
        
        while self.T > self.Tf:
            for _ in range(self.L):
                S_linha = random.choice(obter_vizinhos(S))
                delta_custo = calcular_distancia_total(self.distance_matrix, S_linha) - calcular_distancia_total(self.distance_matrix, S)
                
                if delta_custo < 0 or random.random() < math.exp(-delta_custo / self.T):
                    S = S_linha
                
                custo_atual = calcular_distancia_total(self.distance_matrix, S)
                if custo_atual < best_cost:
                    best_solution = S
                    best_cost = custo_atual
            
            self.T *= self.alfa
        
        return best_solution, best_cost
