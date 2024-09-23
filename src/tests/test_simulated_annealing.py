import pytest
from src.domain.use_cases.solve_tsp import SolveTSP
from src.infrastructure.utils.helpers import calcular_distancia_total

@pytest.fixture
def mock_config():
    return {
        'T0': 1000.0,
        'Tf': 0.001,
        'L': 100,
        'alfa': 0.99
    }

@pytest.fixture
def mock_distance_matrix():
    return [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]

def test_simulated_annealing(mock_distance_matrix, mock_config):
    solver = SolveTSP(mock_distance_matrix, mock_config)
    best_solution, best_cost = solver.execute()
    
    assert sorted(best_solution) == [0, 1, 2, 3], "A solução encontrada deve conter todas as cidades."
    
    assert best_cost > 0, "O custo da solução deve ser maior que zero."
    
    calculated_cost = calcular_distancia_total(mock_distance_matrix, best_solution)
    assert calculated_cost == best_cost, "O custo calculado da solução deve ser igual ao custo retornado."

def test_simulated_annealing_temperature_decrease(mock_distance_matrix, mock_config):
    solver = SolveTSP(mock_distance_matrix, mock_config)
    solver.execute()
    
    assert solver.T < mock_config['T0'], "A temperatura deve diminuir após as iterações."
