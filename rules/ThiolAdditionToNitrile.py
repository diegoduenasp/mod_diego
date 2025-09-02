thiol_addition_to_nitrile = ruleGMLString("""rule [
	ruleID "Thiol Addition to Nitrile"
	labelType "term"

	left[
                edge [ source 3 target 4 label "-" ]
                edge [ source 1 target 2 label "#" ]   
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "N" ]
                node [ id 3 label "S" ]
                node [ id 4 label "H" ]
                node [ id 5 label "*" ]
                node [ id 6 label "*" ]
                edge [ source 3 target 6 label "-" ]
                edge [ source 1 target 5 label "-" ]
                		
	]
	right [
                edge [ source 1 target 2 label "=" ]
                edge [ source 1 target 3 label "-" ]
                edge [ source 4 target 2 label "-" ]
	]
]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

thiol_addition_to_nitrile.print(p)
