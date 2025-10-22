from abc import ABC, abstractmethod

class MemoryStore(ABC):
    @abstractmethod
    def add(self, content: str, embedding: list):
        pass

    @abstractmethod
    def search(self, query: str):
        pass
