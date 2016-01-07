#!/usr/bin/python

import sys
import common

# def keyLength(vertices, direction, diagonal):
# 	if diagonal == 'define' and direction == 'd':
# 		return vertices * vertices
# 	elif diagonal == 'define' and direction == 'u':
# 		return vertices * (vertices + 1) / 2
# 	elif direction == 'd':
# 		return vertices * (vertices - 1)
# 	elif direction == 'u':
# 		return vertices * (vertices - 1) / 2
# 	else:
# 		sys.stderr.write("invalid input for keyLength: " + vertices + ", " + directedion + ", " + diagonal + "\n")
# 		sys.exit(1)

# def listFromKey(vertices, direction, diagonal, key):
# 	binary = str(bin(int(key)))[2:]
# 	length = keyLength(vertices, direction, diagonal)
# 	return '0' * (length - len(binary)) + binary

if len(sys.argv) != 9:
	sys.stderr.write("expecting 8 arguments:\n")
	sys.stderr.write("  got: " + str(sys.argv[1:]) + "\n")
	sys.stderr.write("  1: number of vertices\n")
	sys.stderr.write("  2: direction [d,u]\n")
	sys.stderr.write("  3: diagonal [define,*]\n")
	sys.stderr.write("  4: names to use [index,char,none]\n")
	sys.stderr.write("  5: label\n")
	sys.stderr.write("  6: caption\n")
	sys.stderr.write("  7: type [key,list]\n")
	sys.stderr.write("  8: definition (depending on type)\n")
	sys.stderr.write("     key: number\n")
	sys.stderr.write("     list: list of entries (sep by ,)\n")
	sys.exit(1)

vertices=int(sys.argv[1])
direction=sys.argv[2]
diagonal=sys.argv[3]
names_=sys.argv[4]
label=sys.argv[5]
caption=sys.argv[6]
type_=sys.argv[7]
definition=sys.argv[8]

if not type_ in ['key', 'list']:
	sys.stderr.write("invalid type given: " + type_ + ", expecting 'key' or 'list'\n")
	sys.exit(1)

if not direction in ['d', 'u']:
	sys.stderr.write("invalid direction given: " + direction + ", expecting 'd' or 'u'\n")
	sys.exit(1)

if not names_ in ['index', 'char', 'none']:
	sys.stderr.write("invalid names given: " + names_ + ", expecting 'index' or 'char' or 'none'\n")
	sys.exit(1)

if names_ == 'index':
	names = range(0,vertices)
elif names_ == 'char':
	names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if type_ == 'key':
	elements = list(common.listFromKey(vertices, direction, diagonal, definition))
else:
	elements=definition.split(',')


sep='\t&\t'
headrule='\\hline'
end='\t\\\\'

if names_ == 'none':
	header = '\\begin{tabular}{'+ 'c' * vertices +'}'
else:
	header = '\\begin{tabular}{r|'+ 'c' * vertices +'}'

footer = '\\end{tabular}'

if not (label == '' and caption == ''):
	header = '\\begin{table}\n\\centering\n' + header
	footer = footer + "\n\\caption{' + caption + '}\n\\label{' + label + '}\n\\end{table}"


print header
if not names_ == 'none':
	for j in range(0,vertices):
		sys.stdout.write(sep+str(names[j]))
	print end
	print headrule

if direction == 'd':

	index=0
	for i in range(0,vertices):
		if not names_ == 'none':
			sys.stdout.write(str(names[i]))
		for j in range(0,vertices):
			if i == j and not names_ == 'none' and not diagonal == 'define':
				sys.stdout.write(sep)
			if i == j and not diagonal == 'define':
				sys.stdout.write(diagonal)
			else:
				sys.stdout.write(sep+elements[index])
				index += 1
		print end

else:

	index=0
	for i in range(0,vertices):
		if not names_ == 'none':
			sys.stdout.write(str(names[i]))
		for j in range(0,vertices):
			if j < i or (i == j and not names_ == 'none' and not diagonal == 'define'):
				sys.stdout.write(sep)
			if j == i:
				if not diagonal == 'define':
					sys.stdout.write(diagonal)
				else:
					sys.stdout.write(sep+elements[index])
					index += 1
			elif j > i:
				sys.stdout.write(sep+elements[index])
				index += 1
		print end

print footer
