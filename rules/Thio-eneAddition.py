thioene_addition = ruleGMLString("""rule [
	ruleID "Thio-ene Addition"
	labelType "term"

	left[
                edge [ source 1 target 2 label "=" ]
                edge [ source 3 target 4 label "-" ]   
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "S" ]
                node [ id 4 label "H" ]
                node [ id 5 label "*" ]
                node [ id 6 label "*" ]
                node [ id 7 label "*" ]
                node [ id 8 label "*" ]
                node [ id 9 label "*" ]
                edge [ source 3 target 9 label "-" ]
                edge [ source 1 target 5 label "-" ]
                edge [ source 1 target 6 label "-" ]
                edge [ source 2 target 7 label "-" ]
                edge [ source 2 target 8 label "-" ]		
	]
	right [
                edge [ source 1 target 3 label "-" ]
                edge [ source 1 target 2 label "-" ]
                edge [ source 2 target 4 label "-" ]
	]
	constrainAdj [
		id 9 op "=" count 0
		nodeLabels [ label "O" label "N" label "S" ]
		edgeLabels [ label "-" ]
	]
]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

thioene_addition.print(p)
