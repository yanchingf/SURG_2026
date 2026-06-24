
from graph import Graph
from graph_decimate import decimate

def do_sdrg(graph, show=False):

    curr = graph.search()
    count = 1

    while graph.search() != None:
        decimate(graph, curr)

        if show:
            print(f"Iteration {count} : Decimated {curr}")

        curr = graph.search()
        count += 1

    return