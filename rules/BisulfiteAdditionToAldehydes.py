bisulfite_addition_to_aldehydes = ruleGMLString("""rule [
	ruleID "Bisulfite Addition to Aldehydes"
	labelType "term"

	left[
                edge [ source 1 target 8 label "=" ]
                edge [ source 2 target 7 label "-" ]
                edge [ source 3 target 7 label "-" ]
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "S" ]
                node [ id 3 label "H" ]
                node [ id 4 label "H" ]
                node [ id 5 label "*" ] #C or H
                node [ id 6 label "O" ]
                node [ id 7 label "O" ]
                node [ id 8 label "O" ]
                node [ id 9 label "O-" ]

                edge [ source 1 target 4 label "-" ]
                edge [ source 1 target 5 label "-" ]
                edge [ source 2 target 6 label "=" ]
                edge [ source 2 target 9 label "-" ]
	]
	right [
                edge [ source 3 target 8 label "-" ]
                edge [ source 2 target 7 label "=" ]
                edge [ source 1 target 2 label "-" ]
                edge [ source 1 target 8 label "-" ]
                
	]

]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

bisulfite_addition_to_aldehydes.print(p)
