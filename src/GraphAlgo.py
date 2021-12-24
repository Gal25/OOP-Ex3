import heapq
import json
import math
import random
from heapq import heappop, heappush
from queue import PriorityQueue
from typing import List

from src import Node
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
import matplotlib.pyplot as plt





class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.graph = graph



    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph


    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
       """
        try:
            g = DiGraph()
            with open(file_name, "r") as file:
                g_load = json.load(file)
                for node in g_load["Nodes"]:
                    if "pos" in node and len(node["pos"]) != 0:
                        pos = []
                        posS = node["pos"].split(',')
                        for i in posS:
                            pos.append(float(i))
                        g.add_node(node["id"], tuple(pos))
                    else:
                        x = random.uniform(0, 100)
                        y = random.uniform(0, 100)
                        g.add_node(node["id"], (x, y, 0))
                for edge in g_load["Edges"]:
                    g.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = g
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            dict = {'Edges': [], 'Nodes': []}
            for key, node in self.graph.get_all_v().items():
                dict['Nodes'].append({'pos': str(str(node.getLocation()[0]) + ',' + str(node.getLocation()[1]) + ',' + str(node.getLocation()[2])), 'id': key})

            for src in self.graph.get_all_v().keys():
                for dest, w in self.graph.all_out_edges_of_node(src).items():
                    dict['Edges'].append({'src': src, 'w': w, 'dest': dest})

            with open(file_name, 'w') as file:
                json.dump(dict, fp=file, indent=4)
                return True
        except Exception as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
            """
            Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
            @param id1: The start node id
            @param id2: The end node id
            @return: The distance of the path, a list of the nodes ids that the path goes through
            Example:
    #      >>> from GraphAlgo import GraphAlgo
    #       >>> g_algo = GraphAlgo()
    #        >>> g_algo.addNode(0)
    #        >>> g_algo.addNode(1)
    #        >>> g_algo.addNode(2)
    #        >>> g_algo.addEdge(0,1,1)
    #        >>> g_algo.addEdge(1,2,4)
    #        >>> g_algo.shortestPath(0,1)
    #        (1, [0, 1])
    #        >>> g_algo.shortestPath(0,2)
    #        (5, [0, 1, 2])
            Notes:
            If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
            More info:
            https://en.wikipedia.org/wiki/Dijkstra's_algorithm
            """
            queue = []  # this heapq will have 2 values in index: (distance, node)
            all_nodes = self.graph.get_all_v().keys()

            the_list = {id1: [id1]}
            visited = {}
            value = {}

            # if the vertex does not exists in the list of nodes in current graph
            if id1 not in all_nodes:
                return float('inf'), []

            heappush(queue, (0, id1))
            while queue:
                (dist, ver) = heappop(queue)
                value[ver] = dist

                for key, edge in self.graph.all_out_edges_of_node(ver).items():
                    curr = value[ver] + edge
                    if key not in visited:
                        visited[key] = curr
                        heappush(queue, (curr, key))
                        if ver not in the_list:
                            the_list[ver] = [ver]
                        the_list[key] = the_list[ver] + [key]

                if ver in value:
                    continue  # already searched this node.
                if ver == id2:
                    break

            visited[id1] = 0
            if id2 in value and id2 in the_list:
                return value[id2], the_list[id2]
            return float('inf'), []

    def dijkstra(self, src : Node):

        for i in range(len(self.graph.nodes)):
            self.graph.nodes[i].setWeight(math.inf)

        src.setTag(0)
        src.setWeight(0)
        # distances = {i: math.inf for i in self.graph.nodes.keys()}
        previous_node = {src: -1}
        q = []
        heapq.heappush(q, src)
        while q:
            node_src = q[0]
            # node_src = self.graph.nodes[v]
            if node_src.getTag() != 1:
                for u, w in self.graph.all_out_edges_of_node(node_src.getkey()).items():
                    node_dest = self.graph.nodes[u]
                    if node_dest.getWeight() > node_src.getWeight() + w:
                        node_dest.setWeight(node_src.getWeight() + w)
                        previous_node[u] = node_src
                        q.append(node_dest)
                        # heapq.heappush(q, node_dest)
                src.setTag(1)



    # def TSP(self, node_lst: List[int]) -> (List[int], float):
    #     """
    #     Finds the shortest path that visits all the nodes in the list
    #     :param node_lst: A list of nodes id's
    #     :return: A list of the nodes id's in the path, and the overall distance
    #     """
    #     current_temp = []
    #     cities_list = []
    #     min_path = math.inf
    #     cities_list_temp = []
    #     min_path_temp = 0
    #     for i in range(len(node_lst)):
    #         first_time = False
    #         cities_list_temp.clear()
    #         cities_temp = node_lst.copy()
    #         min_path_temp = 0
    #         curr_node_index = i
    #         location = i
    #         while len(cities_temp) > 1:
    #             key = cities_temp[location]
    #             cities_temp.remove(key)
    #             self.dijkstra(self.graph.nodes[key])
    #             min_value = math.inf
    #             for j in range(len(cities_temp)):
    #                 x = self.graph.nodes[cities_temp[j]].weight
    #                 if min_value > x:
    #                     min_value = self.graph.nodes[cities_temp[j]].weight
    #                     curr_node_index = cities_temp[j]
    #                     location = j
    #             if min_value == math.inf:
    #                 break
    #             min_path_temp += min_value
    #             current_temp = self.shortest_path(key, curr_node_index)[1]
    #
    #             if first_time:
    #                 current_temp.pop(0)
    #             first_time = True
    #             cities_list_temp.extend(current_temp)
    #
    #         if min_path > min_path_temp:
    #             cities_list.clear()
    #             cities_list = cities_list_temp.copy()
    #             min_path = min_path_temp
    #
    #     return cities_list, min_path

    # def TSP(self, node_lst: List[int]) -> (List[int], float):
    #     TSP = List[int]
    #     tempTSP = List[int]
    #     best_w = math.inf
    #     cities = List[int]
    #     while cities:
    #         curr = self.graph.nodes[cities]
    #         tempTSP.clear()
    #         tempTSP = pathCheker(tempTSP, node_lst,curr)
    #         temp_w = self.w_cheker(tempTSP)
    #         if  temp_w < best_w:
    #             best_w = temp_w
    #             TSP.clear()
    #             TSP.extend(tempTSP)
    #
    #     return TSP
    #
    #
    # def w_cheker(self ,tempTSP : List):
    #     if len(tempTSP) == 0:
    #         return math.inf
    #     sum= 0
    #     for i in range(len(self.graph.nodes)):
    #         sum += self.graph.edges[i].w
    #     return sum
    #
    # def pathCheker(self ,tempTSP:List, node_lst: List, curr: Node):
    #     if len(tempTSP) == len(node_lst):
    #         return tempTSP
    #
    #     while range(len(self.graph.edges)) :

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        TSP = []
        TSP_temp = []
        # curr = node_lst.__getitem__(0)
        minNode = 0
        minDist = math.inf
        for i in range(len(node_lst)):
            if len(node_lst) == 0:
                break
            first_time = False
            TSP_temp.clear()
            temp_copy = node_lst.copy()
            curr = temp_copy[i]
            loc = i
            while len(temp_copy) > 1:
                min_value = math.inf
                key = temp_copy[loc]
                temp_copy.remove(key)

                for j in range(len(temp_copy)):
                    if min_value > self.shortest_path(key, curr)[0]:
                        min_value = self.shortest_path(key, curr)[0]
                        curr = temp_copy[j]
                        loc = j

                minNode += min_value
                current_path = self.shortest_path(key, curr)[1]
                if first_time:
                    current_path.pop(0)
                first_time = True
                TSP_temp.extend(current_path)
            if minDist > minNode:
                TSP.clear()
                TSP = TSP_temp.copy()
                minDist = minNode

        return TSP , minDist

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        center_path = math.inf
        center = None
        for i in range(self.graph.sizeNodes):
            temp = 0
            for j in range(self.graph.sizeNodes):
                path = self.shortest_path(i, j)[0]
                if temp < path:
                    temp = path
            if temp < center_path:
                center_path = temp
                center = self.graph.get_all_v()[i]

        return center.getkey(), center_path

    def plot_graph(self) -> None:
            """
            Plots the graph.
            If the nodes have a position, the nodes will be placed there.
            Otherwise, they will be placed in a random but elegant manner.
            we used with the implement in the Amichai's tirgul
            @return: None
            """
            for v in self.graph.get_all_v().values():
                if v.getLocation() is None:
                    x = random.uniform(0, 100)
                    y = random.uniform(0, 100)
                    pos = (x, y, 0)
                    v.setLocation(pos)
                x, y, z = v.getLocation()
                plt.plot(x, y, markersize=4, marker='o', color='blue')
                plt.text(x, y, str(v.getkey()), color="red", fontsize=12)

                for d, w in self.graph.all_out_edges_of_node(v.getkey()).items():
                    node = self.graph.nodes[d]
                    if node.getLocation() is None:
                        v = random.uniform(0,100)
                        e = random.uniform(0,100)
                        pos = (v, e, 0)
                        node.setLocation(pos)
                    v, e, z = node.getLocation()
                    plt.annotate("", xy=(x, y), xytext=(v, e), arrowprops=dict(arrowstyle="<-"))

            plt.show()


