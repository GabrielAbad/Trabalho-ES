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


class BuilderState(ABC):
    """
    Define a interface comum para todos os estados de construção.
    """
    @abstractmethod
    def execute(self, builder, node: Node):
        pass


class TreeBuilder:
    """
    Gerencia o estado atual da construção e executa ações nos nós.
    """
    def __init__(self):
        self._state = SplittingState()

    def set_state(self, state: BuilderState):
        """
        Permite a transição de estados (ex: de Splitting para Stopping).
        """
        print(f"Transição de Estado: {type(self._state).__name__} -> {type(state).__name__}")
        self._state = state

    def process_node(self, node: Node):
        """
        Delega a ação para o estado atual.
        """
        self._state.execute(self, node)


class SplittingState(BuilderState):
    """
    Simula a lógica de encontrar a melhor divisão (split) para um nó.
    """
    def execute(self, builder, node: Node):
        print(f"Calculando ganho de informação para o nó '{node.name}'...")
        if isinstance(node, DecisionNode):
            print(f"O nó '{node.name}' está pronto para receber filhos.")
        else:
            print(f"O nó '{node.name}' é uma folha e não pode ser dividido.")


class StoppingState(BuilderState):
    """
    Simula a verificação de critérios de parada (ex: profundidade máxima).
    """
    def execute(self, builder, node: Node):
        print(f"Verificando critérios de parada para '{node.name}'...")
        print("Critério atingido. Este ramo não crescerá mais.")


class PruningState(BuilderState):
    """
    Simula a remoção de nós para evitar overfitting.
    """
    def execute(self, builder, node: Node):
        print(f"Avaliando complexidade do nó '{node.name}'...")
        print("Poda simulada: Reduzindo ramos desnecessários.")


class TreeIterator(ABC):
    """
    Define a interface para os iteradores.
    """
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class PreOrderIterator(TreeIterator):
    """
    Percorre a árvore em ordem Pré-Ordem (Raiz, Esquerda, Direita).
    Utiliza uma pilha (stack) para gerenciar os nós a serem visitados.
    """
    def __init__(self, root: Node):
        self._stack = []
        if root:
            # Inicializa a pilha com a raiz
            self._stack.append(root)

    def has_next(self):
        """
        Verifica se ainda há nós a serem visitados.
        """
        return bool(self._stack)

    def next(self):
        """
        Retorna o próximo nó na sequência Pré-Ordem.
        """
        if not self.has_next():
            raise StopIteration("Não há mais nós na árvore.")

        node = self._stack.pop()
        
        print(f"Visitando nó: {node.name}")
        if isinstance(node, DecisionNode):
            for child in reversed(node.children):
                self._stack.append(child)
        
        return node

def get_pre_order_iterator(self):
    """
    Retorna uma instância do nosso iterador.
    """
    return PreOrderIterator(self)

Node.get_pre_order_iterator = get_pre_order_iterator