from src.domain.use_cases.solve_tsp import SolveTSP
from src.infrastructure.repositories.solution_writer import SolutionWriter

class SimulatedAnnealingService:
    def __init__(self, distance_matrix_repo, solution_writer: SolutionWriter):
        self.distance_matrix_repo = distance_matrix_repo
        self.solution_writer = solution_writer

    def run(self, config):
        solver = SolveTSP(self.distance_matrix_repo.get_matrix(), config)
        best_solution, best_cost = solver.execute()
        self.solution_writer.write_solution(best_solution, best_cost)
        print(f"Melhor Itinerário: {best_solution}\nDistância: {best_cost}")
        return best_solution, best_cost
