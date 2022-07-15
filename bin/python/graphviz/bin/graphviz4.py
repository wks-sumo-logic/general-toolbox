#!/usr/bin/env python3

import os
import sys
from graphviz import Digraph

dot = Digraph()
filename="/Users/wschmidt/Downloads/sample4.gv"
dot = Digraph(name="sample4", filename=filename, format="pdf", encoding="utf-8")
dot.node('A', 'category')
dot.node('B', 'parse')
dot.node('C', 'count')
dot.node('D', 'transpose')
dot.edges(['AB', 'BC', 'CD'])
print(dot.source)
dot.save()
dot.render(filename=filename, view=0, cleanup=1)
