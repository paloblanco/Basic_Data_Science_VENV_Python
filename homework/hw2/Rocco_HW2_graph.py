#%%
import networkx as nx

GRAPH = r"homework\hw2\handout\wikipedia_small.graph"
NODES = r"homework\hw2\handout\wikipedia_small.nodes"
#%%
from typing import Dict

def create_node_dict(node_path: str) -> Dict[int,str]:
    with open(NODES,'r',errors='replace') as f:
        list_nodes = f.read().splitlines()
    
    dict_nodes = {ix:each for ix,each in enumerate(list_nodes)}
    return dict_nodes

DICT_NODES = create_node_dict(NODES)
DICT_NODES_REVERSE = {v:k for k,v in DICT_NODES.items()}

#%%

def create_digraph(filename: str) -> nx.DiGraph:
    # G: nx.DiGraph = nx.DiGraph()
    G = nx.read_adjlist(filename)
    return G
    


#%%
