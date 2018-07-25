from graph import Graph
from draw import BokehGraph


def main():
    graph = Graph()

    # graph.debug_create_test_data()
    graph.create_vertices_and_edges(10)
    graph.get_connected_components()
    bg = BokehGraph(graph)
    # render the graph on the screen
    bg.show()


if __name__ == "__main__":
    main()
