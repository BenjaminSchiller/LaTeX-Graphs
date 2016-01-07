#!/bin/bash

function example {
	echo ""
	echo "\\FloatBarrier"
	echo "\\begin{figure}[!htb]\\centering"
	echo "\\begin{minipage}[b]{.99\\textwidth}\\begin{verbatim}"
	echo "./adjacencyMatrix.py [or ./tikzGraph.py] \\"
	echo "    \"$1\" \"$2\" \"$3\" \\"
	echo "    \"$4\" \"$5\" \"$6\" \\"
	echo "    \"$7\" \"$8\" [\"$9\"]"
	echo ""
	echo "\\end{verbatim}\\end{minipage}"
	
	echo "\\begin{minipage}[b]{.49\textwidth} \\resizebox {1.0\\textwidth} {!} {"
	../scripts/tikzGraph.py "$1" "$2" "$3" "$4" "" "" "$7" "$8" "$9"
	echo "} \\caption{$6} \\label{fig:$5} \\end{minipage}"
	echo "\\hfill"
	echo "\\begin{minipage}[b]{.49\textwidth} \\resizebox {1.0\\textwidth} {!} {"
	../scripts/adjacencyMatrix.py "$1" "$2" "$3" "$4" "" "" "$7" "$8"
	echo "} \\caption{$6} \\label{tab:$5} \\end{minipage}"
	
	echo "\\end{figure}"
}

echo "\\documentclass{article}\\usepackage{graphicx}\\usepackage{placeins}\\usepackage{tikz}\\begin{document}"

# for i in $(seq 0 200 5000); do
# 	example 20 u - char "fig:example-$i" "example-$i" key $i circle
# done

example 4 d - char "ex1" "directed clique" list '1,1,1,1,1,1,1,1,1,1,1,1' circle
example 6 d - char "ex2" "directed ring" list '1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0' circle
example 4 u - char "ex3" "undirected clique" list '1,1,1,1,1,1' circle
example 6 u - char "ex4" "undirected ring" list '1,0,0,0,1,1,0,0,0,1,0,0,1,0,1' circle
example 5 u - index "ex5" "undirected pentagram" list '1,1,1,1,1,1,1,1,1,1' circle
example 12 u - index "ex6" "undirected clock" list '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1' circle

echo "\\end{document}"