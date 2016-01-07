# LaTeX-Graphs

In this repo, we provide python scripts for generating graph-related LaTeX code.

## Python version

The scripts have been tested with python version 2.7.10 on Mac Os X 10.11.2 but should work with any python version.

## Repo structure

The python scripts are all located in `scripts/`. Some examples of their usage can be found in `examples/`.

## Scripts

Here, we give a description of how the scripts can be used:

### AdjacencyMatrix.py

This scripts can be used to generate LaTeX code for visualizing an adjacency matrix.
In total, 8 arguments are required.

	expecting 8 arguments:
	  1: number of vertices
	  2: direction [d,u]
	  3: diagonal [define,*]
	  4: names to use [index,char,none]
	  5: label
	  6: caption
	  7: type [key,list]
	  8: definition (depending on type)
	     key: number
	     list: list of entries (sep by ,)

The first argument determines the size of the graph.

The second argument determines its direction: (d) for directed and (u) for undirected.
For undirected graphs, no entries are output below the diagonal.

The third argument determines weather the values for the diagonal (loops) should be specified (using the keyword *define*) in the definition argument or if they can be omited there and should all be same (any other value).
This is useful when dealing with simple graphs (without loops).
Then, the values on the diagonal can all be defined at once, e.g., `-` or ` `.

With the fourth parameter, the names to be used for the first row/column can be specified: *index* creates a list `0,1,2,...`, *char* results in `a,b,c,...`, and *none* removes the first row / line.

The fifth and sixth argument specify the label an caption that is added to the LaTeX output.

The last two arguments determine how the entries of the adjacency matrix are defined and what their values are.
For the type *list*, the values of the adjacency matrix (potentially excluding the diagonal, for undirected graphs excluding the values below the diagonal) are expected as a list separated by `,`.
This list is simply a concatenation of the rows of the adjacency matrix (potentially excluding the diagonal and/or the values below).
For the type *key*, a single number is expected as config which corresponds to the binary representation of the adjacency matrix, i.e., 0 or 1 for each edge as described in the following.
For example, the key `13` is interpreted as `0,0,0,0,0,1,0,1,1` for an directed graph of size 3 and `45` is interpreted as `0,0,0,1,0,1,0,1,1`.

Some basic examples are given here, for more examples we refer to `examples/`.

	./AdjacencyMatrix.py 4 u - index tab:example1 'example adjacency matrix 1' list '1,3,-2,,0,1'

\begin{table}
\centering
\begin{tabular}{r|cccc}
	&	0	&	1	&	2	&	3	\\
\hline
0	&	-	&	1	&	3	&	-2	\\
1	&		&	-	&		&	0	\\
2	&		&		&	-	&	1	\\
3	&		&		&		&	-	\\
\end{tabular}
\caption{example adjacency matrix 1}
\label{tab:example1}
\end{table}

	./AdjacencyMatrix.py 3 d ' ' char tab:example2 'example adjacency matrix 2' list '1,3,-2,,0,1'

\begin{table}
\centering
\begin{tabular}{r|ccc}
	&	a	&	b	&	c	\\
\hline
a	&	-	&	1	&	3	\\
b	&	-2	&	-	&		\\
c	&	0	&	1	&	-	\\
\end{tabular}
\caption{example adjacency matrix 2}
\label{tab:example2}
\end{table}

	./AdjacencyMatrix.py 3 d 'define' char tab:example3 'example adjacency matrix 3' list '1,0,3,-2,0,0,1,5,9'



	./AdjacencyMatrix.py 4 d '-' char tab:example4 'example adjacency matrix 4' list '0,1,1,1,0,1,1,1,0,0,1,0'

\begin{table}
\centering
\begin{tabular}{r|cccc}
	&	a	&	b	&	c	&	d	\\
\hline
a	&	-	&	0	&	1	&	1	\\
b	&	1	&	-	&	0	&	1	\\
c	&	1	&	1	&	-	&	0	\\
d	&	0	&	1	&	0	&	-	\\
\end{tabular}
\caption{example adjacency matrix 2}
\label{tab:example2}
\end{table}

### TikZGraph.py

This script can be used to generate the LaTeX code for generating a TikZ graph.
It expects 9 arguments.
The first 8 arguments are the same as for `AdjacencyMatrix.py`.

	todo: add examples here