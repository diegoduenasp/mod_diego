hydrogen_sulfide_additionIII = ruleGMLString("""rule [
	ruleID "Hydrogen Sulfide Addition to Aldehydes III"
	labelType "term"

	left[

                edge [ source 1 target 10 label "=" ]
                edge [ source 2 target 11 label "=" ]
                edge [ source 3 target 12 label "=" ]

                edge [ source 7 target 16 label "-" ]
                edge [ source 7 target 17 label "-" ]
                edge [ source 8 target 18 label "-" ]
                edge [ source 8 target 19 label "-" ]
                edge [ source 9 target 20 label "-" ]
                edge [ source 9 target 21 label "-" ]
                
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "C" ]
                node [ id 4 label "H" ] #
                node [ id 5 label "H" ] #
                node [ id 6 label "H" ] #
                node [ id 7 label "S" ]
                node [ id 8 label "S" ]
                node [ id 9 label "S" ]
                node [ id 10 label "O" ]
                node [ id 11 label "O" ]
                node [ id 12 label "O" ]
                node [ id 13 label "H" ]
                node [ id 14 label "H" ]
                node [ id 15 label "H" ]
                node [ id 16 label "H" ]
                node [ id 17 label "H" ]
                node [ id 18 label "H" ]
                node [ id 19 label "H" ]
                node [ id 20 label "H" ]
                node [ id 21 label "H" ]

                
                edge [ source 1 target 4 label "-" ]
                edge [ source 1 target 13 label "-" ]
                edge [ source 2 target 5 label "-" ]
                edge [ source 2 target 14 label "-" ]
                edge [ source 3 target 6 label "-" ]
                edge [ source 3 target 15 label "-" ]
                
	]
	right [
                edge [ source 1 target 7 label "-" ]
                edge [ source 1 target 8 label "-" ]
                edge [ source 2 target 7 label "-" ]
                edge [ source 2 target 9 label "-" ]
                edge [ source 3 target 8 label "-" ]
                edge [ source 3 target 9 label "-" ]
                edge [ source 10 target 16 label "-" ]
                edge [ source 10 target 17 label "-" ]
                edge [ source 11 target 18 label "-" ]
                edge [ source 11 target 19 label "-" ]
                edge [ source 12 target 20 label "-" ]
                edge [ source 12 target 21 label "-" ]
	]

	# make sure 1 isn't bonded to -O,-N to make sure 4 isnt anything other than C/H
        constrainAdj [
                id 1 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" ]
        ]

        # make sure 2 isn't bonded to -O,-N to make sure 5 isnt anything other than C/H
        constrainAdj [
                id 2 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" ]
        ]

        # make sure 3 isn't bonded to -O,-N to make sure 6 isnt anything other than C/H
        constrainAdj [
                id 3 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" ]
        ]
]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

hydrogen_sulfide_additionIII.print(p)
