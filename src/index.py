from graph import Graph, Vertex
from draw import BokehGraph


def main():
    graph = Graph()
    v0 = Vertex("0")
    graph.add_vertex(v0)
    graph.add_vertex("1")
    graph.add_vertex("2")

    graph.add_vertex("3")
    graph.add_vertex("4")
    graph.add_vertex("5")
    graph.add_vertex("6")

    graph.add_edge("0", "1")
    graph.add_edge("5", "1")
    graph.add_edge("7", "5", False)

    bg = BokehGraph(graph)
    # render the graph on the screen
    bg.show()


if __name__ == "__main__":
    main()
