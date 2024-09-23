from src.infrastructure.utils.helpers import ler_matriz_distancias

class DistanceMatrixRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_matrix(self):
        return ler_matriz_distancias(self.file_path)
