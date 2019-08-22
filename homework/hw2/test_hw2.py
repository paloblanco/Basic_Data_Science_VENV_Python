import Rocco_HW2_graph as rg

def test_create_node_dict():
    NODES = r"homework\hw2\handout\wikipedia_small.nodes"
    dict_nodes = rg.create_node_dict(NODES)
    
    assert isinstance(dict_nodes, dict)
    assert dict_nodes[0] == ".NET_Framework"

