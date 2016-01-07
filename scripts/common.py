def keyLength(vertices, direction, diagonal):
	if diagonal == 'define' and direction == 'd':
		return vertices * vertices
	elif diagonal == 'define' and direction == 'u':
		return vertices * (vertices + 1) / 2
	elif direction == 'd':
		return vertices * (vertices - 1)
	elif direction == 'u':
		return vertices * (vertices - 1) / 2
	else:
		sys.stderr.write("invalid input for keyLength: " + vertices + ", " + directedion + ", " + diagonal + "\n")
		sys.exit(1)

def listFromKey(vertices, direction, diagonal, key):
	binary = str(bin(long(key)))[2:]
	length = keyLength(vertices, direction, diagonal)
	return '0' * (length - len(binary)) + binary