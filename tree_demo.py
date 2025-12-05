from tree_design import (
    DecisionNode, LeafNode, TreeBuilder, 
    SplittingState, StoppingState, PruningState,
    DepthVisitor, CountLeavesVisitor
)

def run_demo():
    print("\n1. Construção da Árvore")
    
    # Instancia o construtor (Contexto do State)
    builder = TreeBuilder()
    
    # Cria a Raiz
    root = DecisionNode("Raiz: Clima?", "Sol ou Chuva?")
    builder.process_node(root) # Estado padrão: Splitting
    
    # Cria ramos
    node_sol = DecisionNode("Ramo: Sol", "Umidade?")
    node_chuva = DecisionNode("Ramo: Chuva", "Vento?")
    
    # Adiciona filhos
    root.add_child(node_sol)
    root.add_child(node_chuva)
    
    # Simula troca de estados
    builder.set_state(PruningState())
    builder.process_node(node_sol) # Simula poda
    
    builder.set_state(SplittingState()) # Volta a dividir
    
    # Adiciona folhas
    leaf_jogar = LeafNode("Folha: Jogar", "Sim")
    leaf_nao_jogar = LeafNode("Folha: Não Jogar", "Não")
    leaf_talvez = LeafNode("Folha: Talvez", "Depende")
    
    node_sol.add_child(leaf_jogar)
    node_sol.add_child(leaf_nao_jogar)
    node_chuva.add_child(leaf_talvez)
    
    # Finaliza construção
    builder.set_state(StoppingState())
    builder.process_node(root)

    print("\n2. Navegação")
    print("Iterando pela árvore (Pre-Order):")
    
    # Obtém o iterador do nó raiz
    iterator = root.get_pre_order_iterator()
    try:
        while iterator.has_next():
            node = iterator.next()
            tipo = "Decisão" if isinstance(node, DecisionNode) else "Folha"
            print(f" -> {tipo}: {node.name}")
    except StopIteration:
        pass

    print("\n3. Operações Independentes")
    
    # Calcular Profundidade
    print("\n[Executando DepthVisitor]")
    depth_visitor = DepthVisitor()
    total_depth = root.accept(depth_visitor)
    print(f"RESULTADO: Profundidade máxima da árvore: {total_depth}")
    
    # Contar Folhas
    print("\n[Executando CountLeavesVisitor]")
    leaves_visitor = CountLeavesVisitor()
    total_leaves = root.accept(leaves_visitor)
    print(f"RESULTADO: Total de folhas encontradas: {total_leaves}")

if __name__ == "__main__":
    run_demo()