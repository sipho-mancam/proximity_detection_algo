import pprint


class ProximityCalculator:
    def __init__(self, x_list:list, o_list:list)->None:
        self.__x_list = x_list
        self.__o_list = o_list

        self.__selected_vertices = []
        self.__selected_indices = []

        self.__graph = [
            {'id':'y', 'edges':{'2':0.20, '3':0.25, '1':0.56, '4':0.8}},
            {'id':'x', 'edges':{'1':0.3, '3':0.5,'2':0.55, '4':0.7}},
            {'id':'A', 'edges':{'4':0.01, '2':0.16, '3':0.25, '1':0.8}},
            {'id':'z', 'edges':{'4':0.02, '2':0.15, '3':0.2, '1':0.7}}
        ]


    def build_distances_graph(self)->None:
        # This method needs to construct a similar graph to the one at the top
        # From a list of nodes and a list of vertices
        # Vertices in this context will mean the O points
        # and Nodes will refer to the X points
        pass
    
    
    def calculate_proximity(self, node:tuple, index):
        vertex , dist, ind = node
        if index == len(self.__graph):
            return (vertex, dist, ind)
        
        current_pointer = self.__graph[index]['edges']
        keys = list(current_pointer.keys())
        if keys[0] != vertex or current_pointer[keys[0]] > dist or (self.__graph[index].get('selected') is not None and self.__graph[index].get('selected')):
            return self.calculate_proximity((vertex, dist, ind), index+1)
        elif current_pointer[keys[0]] < dist:
            return self.calculate_proximity((keys[0], current_pointer[keys[0]], index), index+1)
       

        
    def run(self)->None:
        current_pointer = 0 # The current index on the list
        current_key = 0 # for the selected index, current key

        while len(self.__selected_vertices) < len(self.__graph):
            node = self.__graph[current_pointer]
            edges = list(node['edges'].keys())

            if edges[current_key] in self.__selected_indices:
                current_key += 1
                continue

            res = self.calculate_proximity((edges[current_key], node['edges'][edges[current_key]], current_pointer), current_pointer+1)
            vert, dist, ind = res
            self.__graph[ind]['selected'] = True
            self.__graph[ind]['vertex'] = vert
            self.__selected_indices.append(vert)
            self.__selected_vertices.append(ind)
            
            if ind == current_pointer:
                current_pointer += 1
                if current_key > 0:
                    current_key = 0
            else:
                current_key += 1

        print(self.__graph)


        

res = ProximityCalculator(None, None)

res.run()