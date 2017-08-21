import re
import igraph
#IN_FILE = "repo-gru.cflow"
IN_FILE = "opencv.cflow"
with open(IN_FILE) as f:
    tree = list(f)

parent = None
graph = igraph.Graph(directed=True)
for line in tree: 
    #Check if it's a 0-level function (caller/parent function)
    if line[0] != " ":
        regex = re.match("^(.+)?\(\)", line)
        parent = regex.groups()[0]
        graph.add_vertex(parent)
    else: 
        #It is a 1-level function (called by the parent)
        regex = re.match("^\s{4}(.+)?\(\)", line)
        called = regex.groups()[0]
        graph.add_vertex(called)
        graph.add_edge(parent, called)

print("Done generating graph")
print("Starting plotting algorithm")
igraph.plot(graph, "img.png")
#find . -iname "*.c" | xargs cflow -m asdfasdf --depth=2 
