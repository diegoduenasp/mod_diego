hydroxyketone_degradation = ruleGMLString("""rule [
	ruleID "Hydroxyketone Degradation"
	labelType "term"

	left[

                edge [ source 1 target 6 label "-" ]
                edge [ source 6 target 7 label "-" ]
                edge [ source 8 target 10 label "-" ]
                edge [ source 9 target 10 label "-" ]
                
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "*" ]
                node [ id 4 label "*" ]
                node [ id 5 label "O" ]
                node [ id 6 label "O" ]
                node [ id 7 label "H" ]
                node [ id 8 label "H" ]
                node [ id 9 label "H" ]
                node [ id 10 label "S" ]
                
                edge [ source 1 target 2 label "-" ]
                edge [ source 1 target 4 label "-" ]
                edge [ source 2 target 3 label "-" ]
                edge [ source 2 target 5 label "=" ]
                
	]
	right [
                edge [ source 10 target 1 label "-" ]
                edge [ source 10 target 7 label "-" ]
                edge [ source 6 target 9 label "-" ]
                edge [ source 6 target 8 label "-" ]
	]

	# make sure 2 isn't bonded to -O,-N,-S to make sure 3 isnt anything other than C/H
        constrainAdj [
                id 2 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" label "S" ]
        ]

        # make sure 1 isn't bonded to -N,-S to make sure 4 isnt anything other than C/H
        constrainAdj [
                id 1 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "N" label "S" ]
        ]

]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

hydroxyketone_degradation.print(p)
