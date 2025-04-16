class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adj_list = {}

    def add_edge(self, v, w):
      
        if v not in self.adj_list:
            self.adj_list[v] = []
       
        if w not in self.adj_list:
            self.adj_list[w] = []
       
        self.adj_list[v].append(w)
       
        self.adj_list[w].append(v)

    def display(self):
       
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.display()

