import heapq


class vertex:
    def __init__(self, id, visited):
        self.id = id
        self.visited = visited


class edge:
    def __init__(self, weight, visited, src, dest):
        self.weight = weight
        self.visited = visited
        self.src = src
        self.dest = dest

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight


class graph:
    g = []  # vertices
    e = []  # edges

    def __init__(self, g, e):
        self.g = g
        self.e = e

    # This method returns the vertex with a given id if it
    # already exists in the graph, returns NULL otherwise
    def vertex_exists(self, id):
        for i in range(len(self.g)):
            if self.g[i].id == id:
                return self.g[i]
        return None

    # This method generates the graph with v vertices
    # and e edges
    def generate_graph(self, vertices, edges):
        # create vertices
        for i in range(vertices):
            v = vertex(i + 1, False)
            self.g.append(v)

        # create edges
        for i in range(len(edges)):
            src = self.vertex_exists(edges[i][1])
            dest = self.vertex_exists(edges[i][2])
            e = edge(edges[i][0], False, src, dest)
            self.e.append(e)

    def find_min_spanning_tree(self):
        weight = 0
        heap = []
        heapq.heapify(heap)
        for e in self.e:
            heapq.heappush(heap, e)
        count = len(self.g) - 1
        while count > 0 and heap:
            next_min_edge = heapq.heappop(heap)

            if not next_min_edge.dest.visited:
                next_min_edge.src.visited = True
                next_min_edge.dest.visited = True
                weight += next_min_edge.weight
                count -= 1
        return weight

    def print_graph(self):
        for i in range(len(self.g)):
            print(str(self.g[i].id) + " " + str(self.g[i].visited) + "\n")

        for i in range(len(self.e)):
            print(str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "[" + str(self.e[i].weight) + ", " + str(
                self.e[i].visited) + "]  ")

        print("\n")

    def get_graph(self):
        res = ""
        for i in range(len(self.e)):
            if (i == len(self.e) - 1):
                res += "[" + str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "]"
            else:
                res += "[" + str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "],"
        return res

    def print_mst(self, w):
        print("MST")
        for i in range(len(self.e)):
            if self.e[i].visited == True:
                print(str(self.e[i].src.id) + "->"
                      + str(self.e[i].dest.id))

        print("weight: " + str(w))
        print("\n")


v1 = vertex(id=1, visited=False)
v2 = vertex(id=2, visited=False)
v3 = vertex(id=3, visited=False)
v4 = vertex(id=4, visited=False)
v5 = vertex(id=5, visited=False)

e1 = edge(weight=1, src=v1, dest=v3, visited=False)
e2 = edge(weight=1, src=v1, dest=v2, visited=False)
e3 = edge(weight=2, src=v2, dest=v3, visited=False)
e4 = edge(weight=3, src=v2, dest=v4, visited=False)
e5 = edge(weight=2, src=v4, dest=v5, visited=False)
e6 = edge(weight=3, src=v3, dest=v5, visited=False)

g = graph(g=[v1, v2, v3, v4, v5], e=[e1, e2, e3, e4, e5, e6])

print(g.find_min_spanning_tree())
