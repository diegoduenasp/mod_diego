ketone_additionI = ruleGMLString("""rule [
	ruleID "Ketone Addition I"
	labelType "term"

	left[
                edge [ source 1 target 8 label "=" ]
                edge [ source 4 target 6 label "-" ]
                edge [ source 5 target 7 label "-" ]
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "C" ]
                node [ id 4 label "S" ]
                node [ id 5 label "S" ]
                node [ id 6 label "H" ]
                node [ id 7 label "H" ]
                node [ id 8 label "O" ]
                node [ id 9 label "C" ] #C
                node [ id 10 label "C" ] #C
                node [ id 11 label "*" ]
                node [ id 12 label "*" ]
                node [ id 13 label "*" ]
                node [ id 14 label "*" ]
                edge [ source 1 target 9 label "-" ]
                edge [ source 1 target 10 label "-" ]
                edge [ source 2 target 11 label "-" ]
                edge [ source 2 target 12 label "-" ]
                edge [ source 2 target 4 label "-" ]
                edge [ source 2 target 3 label "-" ]
                edge [ source 3 target 13 label "-" ]
                edge [ source 3 target 14 label "-" ]
                edge [ source 3 target 5 label "-" ]

	]
	right [
                edge [ source 1 target 4 label "-" ]
                edge [ source 1 target 5 label "-" ]
                edge [ source 8 target 6 label "-" ]
                edge [ source 8 target 7 label "-" ]
	]
        
]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

ketone_additionI.print(p)
