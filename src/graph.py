class Vertex:
    def __init__(self, label, color="gray", **pos):
        self.label = label
        self.pos = pos
        self.color = color
        self.edges = set()

    '''
    def __repr__(self):
        return str(self.label)
    '''

    # Use the str method instead
    def __str__(self):
        if not self.pos:
            pos = dict(x=None, y=None)
        else:
            pos = self.pos
        return "Vartex is {}, position at ({}, {}), color is {} and has edges  {}".format(self.label, pos['x'], pos['y'], self.color, self.edges)


class Graph:
    def __init__(self):
        self.vertices = {}

    # we can see what properties are on the Graph
    def __str__(self):
        return str(self.vertices)

    def add_edge(self, start, end, bidirectional=True):
        """ And an edge (default bidirectional) between two vertices"""

        # Change this so that if not in vertices, just add it
        '''
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Vertices to connect not in graph!")
        self.vertices[start].add(end)
        '''
        # using the key, if we are passed an object just get the key

        if isinstance(start, Vertex):
            start = start.label

        if isinstance(end, Vertex):
            end = end.label

        # add start if not in vertices
        if start not in list(self.vertices.keys()):
            self.add_vertex(Vertex(start))

        # add end if not in vertices
        if end not in list(self.vertices.keys()):
            self.add_vertex(Vertex(end))

        self.vertices[start].edges.add(self.vertices[end])
        if bidirectional:
            self.vertices[end].edges.add(self.vertices[start])

    def add_vertex(self, vertex):

        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)

        if vertex.label in self.vertices:
            raise Exception("Error: adding vertex that alredy exists")
        # rip these lines out, deal with them when adding edges
        '''
        if not set(edges).issubset(self.vertices):
            raise Exception("Error: cannot have edge to nonexistent vertices")
        self.vertices[vertex] = set(edges)
        '''
        self.vertices[vertex.label] = vertex

    # Create a random graph
    """
    def randomize(self, width, height, pxBox, probability=0.6):
        count = 0
        # Build a grid of verts
        grid = []
        for y in range(height):
            row = []
            for x in range(width):
                v = Vertex('t0', x=200, y=200)
                # v.value = 'v' + x + ',' + y;
                v.value = 'v' + str(count)
                count += 1
                row.append(v)
            grid.append(row)

        # Go through the grid randomly hooking up edges
        for y in range(height):

            for x in range(width):
                # Connect down
                if (y < height - 1):
                    if (random.randrange(100) < probability):
                        self.connectVerts(grid[y][x], grid[y + 1][x])
                # Connect right
                if (x < width - 1):
                    if (random.randrange(100) < probability):
                        self.connectVerts(grid[y][x], grid[y][x + 1])

        # Last pass, set the x and y coordinates for drawing
        boxBuffer = 0.8
        boxInner = pxBox * boxBuffer
        boxInnerOffset = (pxBox - boxInner) // 2

        '''
        for y in range(height):
            for x in range(width):
                grid[y][x].pos['x'] = int(
                    x * pxBox + boxInnerOffset + random.uniform(0, 1) * boxInner),
                grid[y][x].pos['y'] = int(
                    y * pxBox + boxInnerOffset + random.uniform(0, 1) * boxInner)
        '''
        for y in range(height):
            for x in range(width):
                grid[y][x].pos['x'] = int(
                    (x * pxBox + boxInnerOffset + (random.uniform(0, 1)) * boxInner))
                grid[y][x].pos['y'] = int(
                    (y * pxBox + boxInnerOffset + (random.uniform(0, 1)) * boxInner))

        # Finally, add everything in our grid to the vertexes in this Graph
        for y in range(height):
            for x in range(width):
                self.vertexes.append(grid[y][x])

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=60, y=140)
        debug_vertex_3 = Vertex('t3', x=400, y=340)
        debug_vertex_4 = Vertex('t4', x=200, y=90)
        debug_vertex_5 = Vertex('t5', x=100, y=240)
        debug_vertex_6 = Vertex('t6', x=300, y=40)

        debug_edge_1 = Edge(debug_vertex_2)  # 1 -> 2,  index 0 -> index 1
        debug_vertex_1.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_2)
        # 3 -> 2, index 2 ->  index 1
        debug_vertex_3.edges.append(debug_edge_2)

        debug_edge_5 = Edge(debug_vertex_5)  # 4 -> 5 index 3 -> index 4
        debug_vertex_4.edges.append(debug_edge_5)

        # start=[0, 2, 3], end=[1,1, 4]
        self.vertexes.extend(
            [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4, debug_vertex_5, debug_vertex_6])

    def bfs(self, start):
        random_color = '#' + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        queue = []
        found = []
        queue.append(start)
        found.append(start)

        start.color = random_color

        while (len(queue) > 0):
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color

            queue.pop(0)  # TODo look at collections.dequeue
        return found

    # Get the connected components
    def get_connected_components(self):
        # Connected Components
        # Go to the next unfound vertex in graph vertexes and call BFS on it
        # Go to step 1 until we get to the end of the array(loop)

        searched = []

        for vertex in self.vertexes:
            if vertex not in searched:
                searched.append(self.bfs(vertex))

        return searched
    """
