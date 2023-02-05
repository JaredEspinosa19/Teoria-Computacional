import pydot

graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="white")

###

graph.add_edge(pydot.Edge("Z0","Z0", label=""))
#gripa A
graph.add_edge(pydot.Edge("Z0","a1", label="g"))
graph.add_edge(pydot.Edge("a1","a2", label="r"))
graph.add_edge(pydot.Edge("a2","a3", label="i"))
graph.add_edge(pydot.Edge("a3","a4", label="p"))
graph.add_edge(pydot.Edge("a4","a5", label="a"))
#Contagio b
graph.add_edge(pydot.Edge("Z0","b1", label="c"))
graph.add_edge(pydot.Edge("b1","b2", label="o"))
graph.add_edge(pydot.Edge("b2","b3", label="n"))
graph.add_edge(pydot.Edge("b3","b4", label="t"))
graph.add_edge(pydot.Edge("b4","b5", label="a"))
graph.add_edge(pydot.Edge("b5","b6", label="g"))
graph.add_edge(pydot.Edge("b6","b7", label="i"))
graph.add_edge(pydot.Edge("b7","b8", label="o"))
#distancia c
graph.add_edge(pydot.Edge("Z0","c1", label="d"))
graph.add_edge(pydot.Edge("c1","c2", label="i"))
graph.add_edge(pydot.Edge("c2","c3", label="s"))
graph.add_edge(pydot.Edge("c3","c4", label="t"))
graph.add_edge(pydot.Edge("c4","c5", label="a"))
graph.add_edge(pydot.Edge("c5","c6", label="n"))
graph.add_edge(pydot.Edge("c6","c7", label="c"))
graph.add_edge(pydot.Edge("c7","c8", label="i"))
graph.add_edge(pydot.Edge("c8","c9", label="a"))
#calentura d
graph.add_edge(pydot.Edge("Z0","d1", label="c"))
graph.add_edge(pydot.Edge("d1","d2", label="a"))
graph.add_edge(pydot.Edge("d2","d3", label="l"))
graph.add_edge(pydot.Edge("d3","d4", label="e"))
graph.add_edge(pydot.Edge("d4","d5", label="n"))
graph.add_edge(pydot.Edge("d5","d6", label="t"))
graph.add_edge(pydot.Edge("d6","d7", label="u"))
graph.add_edge(pydot.Edge("d7","d8", label="r"))
graph.add_edge(pydot.Edge("d8","d9", label="a"))
#covid e
graph.add_edge(pydot.Edge("Z0","e1", label="c"))
graph.add_edge(pydot.Edge("e1","e2", label="o"))
graph.add_edge(pydot.Edge("e2","e3", label="v"))
graph.add_edge(pydot.Edge("e3","e4", label="i"))
graph.add_edge(pydot.Edge("e4","e5", label="d"))
#cansancio f
graph.add_edge(pydot.Edge("Z0","f1", label="c"))
graph.add_edge(pydot.Edge("f1","f2", label="a"))
graph.add_edge(pydot.Edge("f2","f3", label="n"))
graph.add_edge(pydot.Edge("f3","f4", label="s"))
graph.add_edge(pydot.Edge("f4","f5", label="a"))
graph.add_edge(pydot.Edge("f5","f6", label="n"))
graph.add_edge(pydot.Edge("f6","f7", label="c"))
graph.add_edge(pydot.Edge("f7","f8", label="i"))
graph.add_edge(pydot.Edge("f8","f9", label="o"))
# cubrebocas g

graph.add_edge(pydot.Edge("Z0","g1", label="c"))
graph.add_edge(pydot.Edge("g1","g2", label="u"))
graph.add_edge(pydot.Edge("g2","g3", label="b"))
graph.add_edge(pydot.Edge("g3","g4", label="r"))
graph.add_edge(pydot.Edge("g4","g5", label="e"))
graph.add_edge(pydot.Edge("g5","g6", label="b"))
graph.add_edge(pydot.Edge("g6","g7", label="o"))
graph.add_edge(pydot.Edge("g7","g8", label="c"))
graph.add_edge(pydot.Edge("g8","g9", label="a"))
graph.add_edge(pydot.Edge("g9","g10", label="s"))

#dolor

graph.add_edge(pydot.Edge("Z0","h1", label="d"))
graph.add_edge(pydot.Edge("h1","h2", label="o"))
graph.add_edge(pydot.Edge("h2","h3", label="l"))
graph.add_edge(pydot.Edge("h3","h4", label="o"))
graph.add_edge(pydot.Edge("h4","h5", label="r"))

graph.write_png("3.png")