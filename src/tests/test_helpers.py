import pytest
from src.infrastructure.utils.helpers import calcular_distancia_total, obter_vizinhos

@pytest.fixture
def mock_distance_matrix():
    return [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]

def test_calcular_distancia_total(mock_distance_matrix):
    itinerario = [0, 1, 3, 2]

    total_distance = calcular_distancia_total(mock_distance_matrix, itinerario)
    
    expected_distance = 2 + 4 + 12 + 15
    
    assert total_distance == expected_distance, f"A distância total deve ser {expected_distance}."

def test_obter_vizinhos():
    solucao = [0, 1, 2, 3]
    
    vizinhos = obter_vizinhos(solucao)
    
    expected_neighbors_count = 6
    assert len(vizinhos) == expected_neighbors_count, "O número de vizinhos gerados está incorreto."
    
    for vizinho in vizinhos:
        assert sorted(vizinho) == [0, 1, 2, 3], "Os vizinhos devem conter todas as cidades."

def test_vizinhos_diferentes():
    solucao = [0, 1, 2, 3]
    vizinhos = obter_vizinhos(solucao)
    
    for vizinho in vizinhos:
        assert vizinho != solucao, "Os vizinhos gerados devem ser diferentes da solução original."
