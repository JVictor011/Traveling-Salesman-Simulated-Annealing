class SolutionWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_solution(self, itinerario, distancia):
        with open(self.file_path, 'w') as f:
            f.write(f"Melhor Itinerário: {itinerario}\n")
            f.write(f"Distância: {distancia}\n")
