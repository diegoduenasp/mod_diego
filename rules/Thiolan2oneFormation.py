thiolan2one_formation = ruleGMLString("""rule [
	ruleID "Thiolan-2-one Formation"
	labelType "term"

	left[

                edge [ source 12 target 14 label "-" ]
                edge [ source 4 target 11 label "-" ]
                
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "C" ]
                node [ id 4 label "C" ]
                node [ id 5 label "*" ]
                node [ id 6 label "*" ]
                node [ id 7 label "*" ]
                node [ id 8 label "*" ]
                node [ id 9 label "*" ]
                node [ id 10 label "*" ]
                node [ id 11 label "*" ]
                node [ id 12 label "S" ]
                node [ id 13 label "O" ]
                node [ id 14 label "H" ]
                
                edge [ source 1 target 12 label "-" ]
                edge [ source 1 target 2 label "-" ]
                edge [ source 2 target 3 label "-" ]
                edge [ source 3 target 4 label "-" ]
                edge [ source 4 target 13 label "=" ]
                edge [ source 1 target 5 label "-" ]
                edge [ source 1 target 6 label "-" ]
                edge [ source 2 target 7 label "-" ]
                edge [ source 2 target 8 label "-" ]
                edge [ source 3 target 9 label "-" ]
                edge [ source 3 target 10 label "-" ]
                
	]
	right [
                edge [ source 4 target 12 label "-" ]
	]

        # make sure 1 isn't bonded to -O,-N to make sure 5 and 6 arent anything other than C/H
        constrainAdj [
                id 1 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" ]
        ]

]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

thiolan2one_formation.print(p)

