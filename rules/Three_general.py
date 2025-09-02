three_general = ruleGMLString("""rule [
	ruleID "Three General"
	labelType "term"

	left[
                edge [ source 3 target 5 label "-" ]
                edge [ source 4 target 6 label "-" ]
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "S" ]
                node [ id 4 label "S" ]
                node [ id 5 label "H" ]
                node [ id 6 label "H" ]
                node [ id 7 label "*" ] #C/H
                node [ id 8 label "*" ] #C/H
                node [ id 9 label "*" ] #C/H
                node [ id 10 label "*" ] #C/H
                node [ id 11 label "*" ]
                
                edge [ source 1 target 11 label "-" ]
                edge [ source 11 target 2 label "-" ]
                edge [ source 3 target 1 label "-" ]
                edge [ source 4 target 2 label "-" ]
                edge [ source 1 target 7 label "-" ]
                edge [ source 1 target 8 label "-" ]
                edge [ source 2 target 9 label "-" ]
                edge [ source 2 target 10 label "-" ]
	]
	right [
                edge [ source 3 target 4 label "-" ]
                edge [ source 5 target 6 label "-" ]
	]

	# make sure 1 isn't bonded to -O,-N to make sure 7 and 8 arent anything other than C/H
        constrainAdj [
                id 1 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" ]
        ]
        
        # make sure 2 isn't bonded to -O,-N to make sure 9 and 10 arent anything other than C/H
        constrainAdj [
                id 2 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" ]
        ]
        
]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

three_general.print(p)
