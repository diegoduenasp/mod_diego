hydrogen_sulfide_additionII = ruleGMLString("""rule [
	ruleID "Hydrogen Sulfide Addition to Aldehydes II"
	labelType "term"

	left[
                edge [ source 1 target 5 label "=" ]
                edge [ source 2 target 6 label "=" ]
                edge [ source 7 target 12 label "-" ]
                edge [ source 7 target 13 label "-" ]
                edge [ source 8 target 15 label "-" ]
                edge [ source 9 target 17 label "-" ]
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "*" ]
                node [ id 4 label "*" ]
                node [ id 5 label "O" ]
                node [ id 6 label "O" ]
                node [ id 7 label "S" ]
                node [ id 8 label "S" ]
                node [ id 9 label "S" ]
                node [ id 10 label "H" ]
                node [ id 11 label "H" ]
                node [ id 12 label "H" ]
                node [ id 13 label "H" ]
                node [ id 14 label "H" ]
                node [ id 15 label "H" ]
                node [ id 16 label "H" ]
                node [ id 17 label "H" ]
                edge [ source 1 target 3 label "-" ]
                edge [ source 2 target 4 label "-" ]
                edge [ source 1 target 10 label "-" ]
                edge [ source 2 target 11 label "-" ]
                edge [ source 8 target 14 label "-" ]
                edge [ source 9 target 16 label "-" ]
	]
	right [
                edge [ source 1 target 7 label "-" ]
                edge [ source 1 target 8 label "-" ]
                edge [ source 2 target 7 label "-" ]
                edge [ source 2 target 9 label "-" ]
                edge [ source 5 target 12 label "-" ]
                edge [ source 5 target 13 label "-" ]
                edge [ source 6 target 15 label "-" ]
                edge [ source 6 target 17 label "-" ]
	]

	# make sure 1 isn't bonded to -O,-N,-S to make sure 3 isnt anything other than C/H
        constrainAdj [
                id 1 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" label "S" ]
        ]

        # make sure 2 isn't bonded to -O,-N,-S to make sure 4 isnt anything other than C/H
        constrainAdj [
                id 2 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" label "S" ]
        ]
]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

hydrogen_sulfide_additionII.print(p)
