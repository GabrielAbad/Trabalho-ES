from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    """
    Classe base abstrata para todos os nós da árvore.
    """
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def accept(self, visitor):
        """
        Permite que operações externas sejam executadas neste nó.
        """
        pass


class DecisionNode(Node):
    """
    Representa um nó interno que contém filhos.
    """
    def __init__(self, name: str, condition: str):
        super().__init__(name)
        self.condition = condition
        self.children: List[Node] = []

    def add_child(self, child: Node):
        """
        Adiciona um nó filho à lista de filhos.
        """
        self.children.append(child)
        print(f"Nó '{child.name}' adicionado ao pai '{self.name}'.")


class LeafNode(Node):
    """
    Representa um nó folha (resultado final/predição).
    """
    def __init__(self, name: str, value: any):
        super().__init__(name)
        self.value = value
