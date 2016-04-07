import xml.etree.ElementTree as ET
import sys

treeEdges = ET.parse(sys.argv[1])

edges = treeEdges.getroot()

vertices = []
arcs = []

for edge in edges:
	vertex_from = ""
	vertex_to = ""
	for vertex in edge:
		if vertex.text not in vertices:
			vertices.append(vertex.text)

		if vertex.tag == "eecs485_from":
			vertex_from = vertex.text
		else:
			vertex_to = vertex.text

	arcs.append(vertex_from + " " + vertex_to)

##### Start output #####

# Vertices
print "*Vertices", len(vertices)
for vertex in vertices:
	# print vertex, hashlib.md5(vertex).hexdigest()
	print vertex, "\"" + vertex + "\""

# Arcs
print "*Arcs", len(arcs) 
for arc in arcs:
	print arc