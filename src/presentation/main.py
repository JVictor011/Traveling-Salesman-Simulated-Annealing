import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.application.simulated_annealing_service import SimulatedAnnealingService
from src.infrastructure.repositories.distance_matrix_repository import DistanceMatrixRepository
from src.infrastructure.repositories.solution_writer import SolutionWriter

def main():
    config = {
        'T0': 1000.0,
        'Tf': 0.001,
        'L': 100,
        'alfa': 0.99
    }
    
    caminho_arquivo_distancias = 'data/fri26_d.txt'
    caminho_arquivo_resultados = 'data/fri26_s.txt'

    distance_repo = DistanceMatrixRepository(caminho_arquivo_distancias)
    solution_writer = SolutionWriter(caminho_arquivo_resultados)
    
    sa_service = SimulatedAnnealingService(distance_repo, solution_writer)
    sa_service.run(config)

if __name__ == "__main__":
    print("Iniciando o Simulated Annealing...")
    main()