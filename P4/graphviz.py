import pydot

graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="white")

# Add nodes
#Rojos
# graph.add_node(pydot.Node("1", shape="circle",color="red"))
# graph.add_node(pydot.Node("3", shape="circle",color="red"))
# graph.add_node(pydot.Node("5", shape="circle",color="red"))
# graph.add_node(pydot.Node("7", shape="circle",color="red"))
# graph.add_node(pydot.Node("9", shape="circle",color="red"))
# graph.add_node(pydot.Node("11", shape="circle",color="red"))
# graph.add_node(pydot.Node("13", shape="circle",color="red"))
# graph.add_node(pydot.Node("15", shape="circle",color="red"))
# graph.add_node(pydot.Node("15", shape="circle",color="red"))
# #Negros
graph.add_node(pydot.Node("2", shape="circle",color="red", bgcolor="red"))
# graph.add_node(pydot.Node("4", shape="circle",color="black"))
# graph.add_node(pydot.Node("6", shape="circle",color="black"))
# graph.add_node(pydot.Node("8", shape="circle",color="black"))
# graph.add_node(pydot.Node("10", shape="circle",color="black"))
# graph.add_node(pydot.Node("12", shape="circle",color="black"))
# graph.add_node(pydot.Node("14", shape="circle",color="black"))
# graph.add_node(pydot.Node("16", shape="circle",color="black"))


# Add edges
# my_edge = pydot.Edge("a", "b", color="black")
# graph.add_edge(my_edge)
# Or, without using an intermediate variable:
graph.add_edge(pydot.Edge("1", "2", color="black"))
graph.add_edge(pydot.Edge("2", "4", color="black"))
graph.add_edge(pydot.Edge("2", "5", color="black"))
graph.add_edge(pydot.Edge("2", "5", color="black"))



graph.write_png("output.png")