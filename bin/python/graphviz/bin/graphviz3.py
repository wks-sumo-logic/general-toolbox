#!/usr/bin/env python3

from graphviz import Digraph

dot = Digraph()
dot.node('A', 'category')
dot.node('B', 'parse')
dot.node('C', 'count')
dot.node('D', 'transpose')
dot.edges(['AB', 'BC', 'CD', 'DA'])
print(dot.source)
dot.render(view=True)
