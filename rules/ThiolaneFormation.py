thiolane_formation = ruleGMLString("""rule [
	ruleID "Thiolane Formation"
	labelType "term"

	left[

                edge [ source 1 target 2 label "=" ]
                edge [ source 8 target 9 label "-" ]
                
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "*" ]
                node [ id 4 label "*" ]
                node [ id 5 label "*" ]
                node [ id 6 label "*" ]
                node [ id 7 label "*" ]
                node [ id 8 label "S" ]
                node [ id 9 label "H" ]
                
                edge [ source 1 target 3 label "-" ]
                edge [ source 1 target 4 label "-" ]
                edge [ source 2 target 5 label "-" ]
                edge [ source 2 target 6 label "-" ]
                edge [ source 8 target 7 label "-" ]
                
	]
	right [
                edge [ source 1 target 2 label "-" ]
                edge [ source 1 target 9 label "-" ]
                edge [ source 2 target 8 label "-" ]
	]

	# make sure 1 isn't bonded to -O,-N,-S to make sure 3 and 4 arent anything other than C/H
        constrainAdj [
                id 1 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" label "S" ]
        ]

        # make sure 8 isn't bonded to -O,-N,-S to make sure 7 isnt anything other than C/H
        constrainAdj [
                id 8 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" label "S" ]
        ]

]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

thiolane_formation.print(p)
