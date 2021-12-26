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
This class implements the interface GraphAlgoInterface.\
This class representing  a directional weight graph. Can see the implementation of the graph by using dictionary.\
That is, all the vertices in the graph are seen under a data structure of a dictionary, and each vertex has edges that go in and out of that vertex (these data can also be seen in a dictionary).In the class can find the functions and their implementation:

| __Main Method__ | __Description__ | __Output__ |
| :---------------- | :---------------- |
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




__More private functions:__

**_getNode(int):_** Method that get the node ID in the dictionary of nodes.




## __DWGraph_Algo Class:__
This class implements the interface DirectedWeightedGraphAlgorithm.\
The class represent an implementation of a Directed (positive) Weighted Graph Theory Algorithms include: colne (copy), init (graph), isConnected (strongly),  double shortestPathDist, list shortestPath, node of center, list of TSP, load a Json file, save a Json file.\
The implementation according to the data structures of Hash map (the value of the Hash map is based on the same data structure).


| __Main Method__ | __Description__ |
| :---------------- | :---------------- |
| DWGraph_Algo() | Default constructor |
| DWGraph_Algo(DirectedWeightedGraph| Constructor |
| init(DirectedWeightedGraph g) | init the graph on which this set of algorithms operates on |
| getGraph() | underlying graph of which specific class works|
| copy() | Computes a deep copy of this weighted graph |
| isConnected() | true if there is a valid path from each node to each other node |
| shortestPathDist(int src, int dest) | representing the shortest distance between first node(source) and second node (destination), us the Dijkstra algorithm (return double of the distance) |
| shortestPath(int src, int dest) | representing the shortest distance between first node(source) and second node (destination), us the Dijkstra algorithm (return list of the nodes)|
| center() | finds the NodeData which minimizes the max distance to all the other nodes |
| tsp(List<NodeData>) | computes a list of consecutive nodes which go over all the nodes in cities |
| save(String file) | saves the json file that is a directed weighted graph to the given |
| load(String file) | this function implement the load of a graph to this graph algorithm |

  
__More private functions:__
  
•	**_`algorithm_of_Dijkstra:`_** The function receive a NodeData. The function based on the Dijkstra's algorithm.
    Solves the problem of finding the easiest route from point in graph to destination in weighted graph. It is possible to find using       this algorithm, at this time, the fast paths to all the points in the graph. The algorithm calculates the weights of the nodes with     the desired edges each time and compares them. According to the algorithm we get the path with the lowest weight.\
    Link: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm \
    _Complexity: (O(V+E)), |V|=number of nodes, |E|=number of edges._\
Returns an array of doubles that representing the shortest path to each node (the indexs on the array representing the nodes ID).\
•	**_`toString():`_** The function receive a graph and by the library in java represent the graph as a string.\
•	**_`reset_weight():`_** This function re – update the weight of the all nodes in the graph.\
• **_`findTheLongestPathInDijkstra(NodeDate):`_** This function receive a NodeData (vertex). Its realization is carried out according to the      result obtained from the Dijksrta algorithm, depending on the result we will go over the array and choose the longest path from all      the short ones and return the destination (node) that occurred with the longest path. This function helps to find the center of the      graph.\
•	**_`upSideDownGraph():`_** This function creates a new graph that will be the graph in the opposite direction of the existing graph.\
• **_`BFS(DirectedWeightedGraph, NodeData):`_** This function checks if there is a path that passes through all the vertices.\
• **_`BFS_isConnected(DirectedWeightedGraph graph, NodeData N):`_** This function checks whether the graph is connected ,uses the BFS           algorithm.\
__Link to the algorithm BFS: https://en.wikipedia.org/wiki/Breadth-first_search.__ \
• **_`changeTags():`_** This function re-update all the tags of the nodes in the graph to be -1 (NOT VISITED).\
• **_`graphJsonDeserializer implements JsonDeserializer<DWGraph>:`_** This class implements the Json Deserializer to allow you to load the Jason file. 

  
## GUI PACKAGE
In this part of the project can see the graphical implementation of all the interfaces from the first part. Using JAVA SWING which is a part of Java Foundation Classes (JFC) that is used to create window-based applications.\
There is use of the JFrame and JPanel class. With the help of the functions given within the libreries and the corresponding implementation for them, we will get an overall picture of the graph.\
There is a menuBar where we can choose which JSON file is selected to load or to save, and in addition there is the use of the functions of the class DWGrapg_Algo and once we select the implementation of one of them is seen directly on the graph.\
The JSON files contain different graphs and range from G1 to G3.
In addition, we will see from the following table the runtimes for multi-vertices and edges (which are not in these classes):

For the demo we will select the _center()_ function to see the running time:
  
| __Json File__ | __Running Time__|
| :-------------| :---------------: |
| 1000.json | 1 sec 556 ms |
| 10000.json |6 minutes 1 sec 334 ms |
| 100000.json |timeout |
  
 For the demo we will select the _isConnected()_ function to see the running time:
| __Json File__ | __Running Time__|
| :-------------| :---------------: |
| 1000.json | 1 sec 884 ms |
| 10000.json |2 sec 209 ms |
| 100000.json |1 sec 792 ms |


  
  
## _Algorithmic classes:_
### __MyFrame Class:__
  This class is extends of JFrame and have implements of ActionListener.\
  This class creates the window where the graph will appear.\
  The options:
  
  ```
  Select file:
  • load
  • save
  ```
  ```
  Functions of the Algorithms:
  • isConnected
  • shortestPathDist
  • shortestPath
  • center
  • TSP
  ```
  ```
  Functions on the graph:
  • Remove_node
  • Remove_edge
  • Edd_node
  ```

  
###  __MyPanel Class:__
This class is extends of JPanel.\
This class implements the full explanation of the actions and how they are actually performed on the graph.\
For example, different response to mouse uses, setting the graph size in the window, maintaining appropriate proportions of the graph when opening the file, and more.\
By select one of the functions under the "Functions of the Algorithms" in the menuBar, can see the implementation of the functions:
  
  __`select isConnected:`__ A window will pop up stating whether the graph is connected or not.\
  __`select shortestPathDist:`__  A window will open, in which it will be possible to write down the choice of destination and the source of the nodes. Between them we will get the shortest path (return a numerical answer).\
  __`select shortestPath:`__  A window will open, in which it will be possible to write down the choice of destination and the source of the nodes. Between them we will get the shortest path (return a string of nodes and will seen a red line on the graph represents the shortestPath).\
  __`select center:`__ A window will pop up stating the center the specific graph.\
  __`select TSP:`__ A window will open, in which it will be possible to write down the path that you want after clicking `OK`. In every time that you select a node, needs to click `OK`. After finishing selecting the nodes write `Exit` and then can see the path marked on the graph (with red line).
  
 
  
By select one of the functions under the "Functions on the graph" in the menuBar, can see the implementation of the functions:\
__`select Remove_node`__ - A window will open, in which it will be possible to write down the choice of which node would you like to delete.\
__`select Remove_edge`__ - A window will open, in which it will be possible to write down the choice of which edge would you like to delete (select a src and dest).\
PAY ATTENTION! The graph shown is a weighted directed graph so must pay attention to the direction of the edges. There is a possibility that between two nodes there is an edge in the direction of one node and a second edge in the direction of a second node, so if one of them is deleted, the difference is not visually visible, but in practice the rib is deleted (to delet completly the edge you will to do the action - Remove_edge twice, first from source node to destination node and second from the destination node to source node.\
__`select Add_node`__ - A window will open, in which it will be possible to write down the choice of which node you woulde like to add and in which location.
  
  
  
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
  
