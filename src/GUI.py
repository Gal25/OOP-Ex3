# init pygame
import json
import math
import os
from types import SimpleNamespace

# import display as display
import pygame as pygame
from pygame import display ,gfxdraw, RESIZABLE
from pygame.color import Color

from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from src.Node import Node

WIDTH, HEIGHT = 1080, 720

pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 20, bold=True)

g = DiGraph()
graph_algo = GraphAlgo(g)
file = '../data/A0.json'

def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen


# get the current directory path
root_path = os.path.dirname(os.path.abspath(__file__))

# load the json file into SimpleNamespace Object

graph_algo.load_from_json(file)

# get data proportions
# min_x = min(graph_algo.graph.nodes, key= graph_algo.graph.getNode(graph_algo.graph.nodes.keys()).location[0]).location[0]
# min_y = min(graph_algo.graph.nodes, key=lambda n: n.location[1]).location[1]
# max_x = max(graph_algo.graph.nodes, key=lambda n: n.pos.x).pos.x
# max_y = max(graph_algo.graph.nodes, key=lambda n: n.pos.y).pos.y
min_x = math.inf
min_y = math.inf
max_x = -math.inf
max_y = -math.inf
# def min():
# for i in range(len(graph_algo.graph.nodes)):
#     min_x = min(graph_algo.graph.nodes, key=graph_algo.graph.getNode(graph_algo.graph.nodes.keys()).location[0]).location[0]
# for i in range(len(graph_algo.graph.nodes)):
#     min_y = min(graph_algo.graph.nodes, key=graph_algo.graph.getNode(i).location[1]).location[1]
# for i in range(len(graph_algo.graph.nodes)):
#     max_x = max(graph_algo.graph.nodes, key=graph_algo.graph.getNode(i).location[0]).location[0]
# for i in range(len(graph_algo.graph.nodes)):
#     max_y = max(graph_algo.graph.nodes, key=graph_algo.graph.getNode(i).location[0]).location[0]

def Setminmax():
    global min_x, min_y, max_x, max_y
    for n in range(graph_algo.graph.v_size()):
        if graph_algo.graph.getNode(n).location[0] < min_x:
            min_x = graph_algo.graph.getNode(n).location[0]
        if graph_algo.graph.getNode(n).location[1] < min_y:
            min_y = graph_algo.graph.getNode(n).location[1]
        if graph_algo.graph.getNode(n).location[0] > max_x:
            max_x = graph_algo.graph.getNode(n).location[0]
        if graph_algo.graph.getNode(n).location[1] > max_y:
            max_y = graph_algo.graph.getNode(n).location[1]


# decorate scale with the correct values


def my_scale(data, x=False, y=False):
    Setminmax()
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)


radius = 15


while(True):
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh screen
    screen.fill(Color(0, 0, 0))

    # draw nodes
    for n in graph_algo.get_graph().get_all_v():
        x = my_scale(graph_algo.graph.getNode(n).location[0], x=True)
        y = my_scale(graph_algo.graph.getNode(n).location[1], y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(graph_algo.graph.getNode(n).key), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

        # draw edges
        for e, d in graph_algo.get_graph().all_out_edges_of_node(n).items():
            # find the edge nodes
            src = next(n for n in graph_algo.get_graph().get_all_v() if graph_algo.graph.getNode(n) == e[graph_algo.get_graph().get_all_v()])
            dest = next(n for n in graph_algo.get_graph().get_all_v() if graph_algo.graph.getNode(n) == d[graph_algo.get_graph().get_all_v()])

            # scaled positions
            src_x = my_scale(src.pos.x, x=True)
            src_y = my_scale(src.pos.y, y=True)
            dest_x = my_scale(dest.pos.x, x=True)
            dest_y = my_scale(dest.pos.y, y=True)

            # draw the line
            pygame.draw.line(screen, Color(61, 72, 126),(src_x, src_y), (dest_x, dest_y))

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

