# OOP-Ex3

_By: Dana Cherchenkov and Gal Cohen._
```
Github pages:

https://github.com/DanaCherchenkov 
https://github.com/Gal25
```

This project is an assignment in an Object Oriented Programming course at Ariel University.\
In the project we were asked to design and implement data structures and algorithms of graphs (directed and weighted) in python. 
The project consists of three parts, first the implementation of a weighted and directed graph with the help of implementation of different interfaces. \
The second part is design the graph and use the algorithms we implemented in the first part and make the graph visual by using of PYGAME library.\
In the third part we will perform a comparison test of the running times. The comparison will be made between the data we received in the previous assignment in JAVA, can be seen at the following link: _https://github.com/Gal25/OOP-Ex2_, and the data we received in this project in Python.\
A detail of the third part is documented in the wiki.\
The project include two different interfaces and five classes. The interfaces are under the SRC PACKAGE which include in the content of all the functions for the implementation of the graph. Moreover there is an implementation of tests for each function in the graph (show under the package ‘tests’).



## Directed weighted graph in Python:
### __Node_Class:__
This simple class representing a node (vertex) on a directed weighted graph.\
In the class can find the main variables and their implementation:

•	Key -  A key that is used to as each node’s ID.\
•	Location -  An object that represent the location of the node.\
•	Wieght – A variable that get the weight of the node, there is an option to update the weight of the vertex,helps in calculating functions in DiGraph and GraphAlgo.\
•	Info –  A variable that get the information of the node by String, there is an option to update the Info of the vertex, helps in calculating functions in DiGraph and GraphAlgo.\
•	Tag- A variable that used by default.\
• E_out - A variable that get the amount of the nodes that connected to (into) other node.\
• E_in - A variable that get the amount of the nodes that connected from other node.


## __DiGraph Class:__
This class implements the interface GraphInterface.\
This class representing  a directional weight graph. Can see the implementation of the graph by using dictionary.\
That is, all the vertices in the graph are seen under a data structure of a dictionary, and each vertex has edges that go in and out of that vertex (these data can also be seen in a dictionary).In the class can find the functions and their implementation:

| __Main Method__ | __Description__ | __Output__ |
| :---------------- | :---------------- | :---------------|
| v_size() | Number of vertices in this graph | Integer |
| e_size() | Number of edges in this graph | Integer |
| get_all_v() | A dictionary of all the nodes in the Graph | Dictionary |
| all_in_edges_of_node(int) | A dictionary of all the nodes connected to (into) node_id | Dictionary |
| all_out_edges_of_node(int) | A dictionary of all the nodes connected from node_id | Dictionary |
| get_mc() | Current version of this graph | Dictionary |
| add_edge(int, int, float) | Adds an edge to the graph | Bool |
| add_node(int, pos: tuple) | Adds a node to the graph | Bool |
| remove_node(int) | Removes a node from the graph | Bool |
| remove_edge(int, int) | Removes an edge from the graph | Bool |





### __More private functions:__
**_getNode(int):_** Method that get the node ID in the dictionary of nodes.




## __GraphAlgo Class:__
This class implements the interface GraphAlgoInterface.\
The class represent an implementation of a Directed (positive) Weighted Graph Theory Algorithms include: init (graph), shortestPath (by the Dijkstra Algorithm), node of center, list of TSP, load from Json file, save from Json file, plot of the grapg.\
In each implementation of an entire graph in this class, it prepares the data of a DiGraph class on which the algorithms work on.
In the class can find the functions and their implementation:


| __Main Method__ | __Description__ | __Output__|
| :---------------- | :---------------- | :-------------|
| get_praph() | The directed graph on which the algorithm works on | GraphInterface |
| load_from_json(str) | Loads a graph from a json file | Bool |
| save_to_json(str) | Saves the graph in JSON format to a file | Bool | 
| shortest_path(int, int) | The shortest path from node id1 to node id2 using Dijkstra's Algorithm | Float, List |
| TSP(List[int]) | Finds the shortest path that visits all the nodes in the list | List[int], Float |
| centerPoint() | Finds the node that has the shortest distance to it's farthest node | Integer, Float |
| plot_graph() | Plots the graph. | None|

  
__More private functions:__
  
**_`algorithm_of_Dijkstra:`_** The function is a helper function for the implementation of the TSP algorithm.\
The function receive a Node, represent the source node. Based on the Dijkstra's algorithm.\
Solves the problem of finding the easiest path from point in graph to destination in weighted graph. It is possible to find using       this algorithm, at this time, the fast paths to all the points in the graph. The algorithm calculates the weights of the nodes with     the desired edges each time and compares them. According to the algorithm we get the path with the lowest weight.\
Link: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm \
_Complexity: (O(V+E)), |V|=number of nodes, |E|=number of edges._




## __More Classes:__
**_main.py:_**  This is a class given in advance by the team, assists in checking the algorithms and coordinating the results.\
**_GUI.py:_** This class implements graphical implementation of all the algorithms from the first part using PYGAME.\
The class contain the functions:
**scale(data, min_screen, max_screen, min_data, max_data):** The function get the scaled data with proportions min_data, max_data
 relative to min and max screen dimensions.
**Setminmax():** This function......
**my_scale(data, x, y):** This function....

  
## _How to run a Graph:_
By the Ex2 class functions and a jar file, can run the Graph.
  
__Running by the commend line__:\
  At first, place the files where we know its location on the computer. The desired files are: one of the JSON files (no matter which one) and the JAR file that we created specifically for the Ex2 main class.\
Example of registering : 
  ```
  c:\'name'\'name'\'name'>java -jar Ex2.jar G1.json
  ```
 At second, inside the window that opens, by select the function load it brings the option to select any JSON file from your comuter, and then do any function that you want.
  
  
 ```
  External Information:
  
  In the src package can find the all tests for all function in this project.
 ```
  
