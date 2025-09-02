thiolane_formationB = ruleGMLString("""rule [
	ruleID "Thiolane Formation B"
	labelType "term"

	left[

                edge [ source 3 target 4 label "=" ]
                edge [ source 12 target 13 label "-" ]
                
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
                node [ id 13 label "H" ]
                
                edge [ source 1 target 12 label "-" ]
                edge [ source 1 target 2 label "-" ]
                edge [ source 2 target 3 label "-" ]
                edge [ source 1 target 5 label "-" ]
                edge [ source 1 target 6 label "-" ]
                edge [ source 2 target 7 label "-" ]
                edge [ source 2 target 8 label "-" ]
                edge [ source 3 target 9 label "-" ]
                edge [ source 4 target 10 label "-" ]
                edge [ source 4 target 11 label "-" ]
                
	]
	right [
                edge [ source 3 target 4 label "-" ]
                edge [ source 3 target 13 label "-" ]
                edge [ source 4 target 12 label "-" ]
	]

	# make sure 4 isn't bonded to -O,-N,-S to make sure 10 and 11 arent anything other than C/H
        constrainAdj [
                id 4 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" label "S" ]
        ]

        # make sure 3 isn't bonded to -O,-N,-S to make sure 9 isnt anything other than C/H
        constrainAdj [
                id 3 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" label "S" ]
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

thiolane_formationB.print(p)
