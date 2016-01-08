#!/usr/bin/python

import sys
import common

if len(sys.argv) != 10:
	sys.stderr.write("expecting 9 arguments:\n")
	sys.stderr.write("  got: " + str(sys.argv[1:]) + "\n")
	sys.stderr.write("  1: number of vertices\n")
	sys.stderr.write("  2: direction [d,u]\n")
	sys.stderr.write("  3: diagonal [define,weight,*]\n")
	sys.stderr.write("  4: names to use [index,char,none]\n")
	sys.stderr.write("  5: label\n")
	sys.stderr.write("  6: caption\n")
	sys.stderr.write("  7: type [key,list]\n")
	sys.stderr.write("  8: definition (depending on type)\n")
	sys.stderr.write("     key: number\n")
	sys.stderr.write("     list: list of entries (sep by ,)\n")
	sys.stderr.write("  9: placement [line,circle]\n")
	sys.exit(1)

vertices=int(sys.argv[1])
direction=sys.argv[2]
diagonal=sys.argv[3]
names_=sys.argv[4]
label=sys.argv[5]
caption=sys.argv[6]
type_=sys.argv[7]
definition=sys.argv[8]
placement=sys.argv[9]

if not type_ in ['key', 'list']:
	sys.stderr.write("invalid type given: " + type_ + ", expecting 'key' or 'list'\n")
	sys.exit(1)

if not direction in ['d', 'u']:
	sys.stderr.write("invalid direction given: " + direction + ", expecting 'd' or 'u'\n")
	sys.exit(1)

if not names_ in ['index', 'char', 'none']:
	sys.stderr.write("invalid names given: " + names_ + ", expecting 'index' or 'char' or 'none'\n")
	sys.exit(1)

if not placement in ['line', 'circle']:
	sys.stderr.write("invalid placement given: " + placement + ", expecting 'line' or 'circle'\n")
	sys.exit(1)

if names_ == 'index':
	names = range(0,vertices)
elif names_ == 'char':
	names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if type_ == 'key':
	elements = list(common.listFromKey(vertices, direction, diagonal, definition))
else:
	elements=definition.split(',')

# print "\\documentclass{standalone}\\usepackage{tikz}\\begin{document}"

if not (label == '' and caption == ''):
	print "\\begin{figure}"

weights = [None] * vertices
if diagonal == 'weight':
	index = 0
	for i in range(0,vertices):
		for j in range(0,vertices):
			if direction == 'u' and i > j:
				continue
			if i == j:
				weights[i] = elements[index]
			index += 1

if placement == 'line':
	print "\\begin{tikzpicture}"
	print "\\def \\n {" + str(vertices) + "}"
	print "\\def \\radius {5cm}"
	print "\\def \\margin {8}"
	print "\\foreach \\s in {1,...,\\n}"
	print "{"
	print "  \\node[draw, circle] at (0,) {v$\s$};"
	#print "  \\draw[->, >=latex] ({360/\\n * (\\s - 1)+\\margin}:\\radius)"
	#print "    arc ({360/\\n * (\\s - 1)+\\margin}:{360/\\n * (\\s)-\\margin}:\\radius);"
	print "}"
	print "\\end{tikzpicture}"
elif placement == 'circle':
	r = 3
	print "\\begin{tikzpicture}"
	print "\\def \\radius {3cm}"
	for i in range(0,vertices):
		pos = (-i * 360 / vertices + 90) % 360
		if weights[i] == None or weights[i] == '':
			print "\\draw (%d:%s) node[circle,draw] (v%d) {%s};" % (pos, r, i, str(names[i]))
		else:
			print "\\draw (%d:%s) node[circle,draw,label=%s] (v%d) {%s};" % (pos, r, weights[i], i, str(names[i]))
	index = 0
	for i in range(0,vertices):
		for j in range(0,vertices):
			if i == j and diagonal == 'weight':
				index += 1
				continue
			if i == j and not diagonal == 'define':
				continue
			if i > j and direction == 'u':
				continue
			if not (elements[index] == '0' or elements[index] == ' ' or elements[index] == '' or elements[index] == None):
				edgeLabel = "" if (elements[index] == "1") else (" node [fill=white] {%s}" % elements[index])
				if direction == 'u':
					print "\\path[-] (v%d) edge [thick] %s (v%d);" % (i, edgeLabel, j)
				else:
					print "\\path[->] (v%d) edge [bend left, thick] %s (v%d);" % (i, edgeLabel, j)
			index += 1
	print "\\end{tikzpicture}"

if not (label == '' and caption == ''):
	print "\\caption{" + caption + "}"
	print "\\label{" + label + "}"
	print "\\end{figure}"

# print "\\end{document}"
