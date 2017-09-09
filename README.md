# ConceptNet-Interface-by-Python

This is a simple interface library to ConceptNet ( conceptnet.io ) by Python.

To use it :

1 - You need install Requests library (http://docs.python-requests.org/en/master/).
2 - Import it to your project.

--------------------------------------------------------------------------------------------------

The class Edge have five attributes {StartNode, EndNode, Relation, Weight, SurfaceText} which represent the edge retrieved from ConceptNet.

Functions :


1 - GetAllEdges(node_label,MinWeight,MaxNumOfEdges,LabelIsStartOnly) return a list of edges (of class Edge) connected to the given node.

- The retrieved edges have Weight greater than or equal MinWeight.
- The number of retrieved edges is less than or equal MaxNumOfEdges.
- IF the flag LabelIsStartOnly is true, the the retrieved edges have the given node as Start node.



2 - GetEdges(start_label,end_label,MinWeight,MaxNumOfEdges) return a list of edges (of class Edge) connected between the given 2 nodes.



3 - GetEdgesEnd(start_label,relation,MinWeight,MaxNumOfEdges) return a list of edges (of class Edge) have the given start and relation.



4 - GetEdgesStart(end_label,relation,MinWeight,MaxNumOfEdges) return a list of edges (of class Edge) have the given end and relation.



5 - GetDistRelations(edges) take a list of edges (of class Edge) and return a list of distinct relations (list of string).



6 - GetEdgesByRelation(edges,relation) take a list of edges (of class Edge) and return edges have the given relation.
