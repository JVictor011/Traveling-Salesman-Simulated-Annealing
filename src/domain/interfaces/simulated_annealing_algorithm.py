from abc import ABC, abstractmethod

class SimulatedAnnealingAlgorithm(ABC):
    @abstractmethod
    def execute(self):
        pass
