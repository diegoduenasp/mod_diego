ketone_additionII = ruleGMLString("""rule [
	ruleID "Ketone Addition II"
	labelType "term"

	left[
                edge [ source 1 target 7 label "=" ]
                edge [ source 5 target 8 label "-" ]
                edge [ source 6 target 9 label "-" ]
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "C" ]
                node [ id 4 label "C" ]
                node [ id 5 label "S" ]
                node [ id 6 label "S" ]
                node [ id 7 label "O" ]
                node [ id 8 label "H" ]
                node [ id 9 label "H" ]
                node [ id 10 label "C" ] #C
                node [ id 11 label "C" ] #C
                node [ id 12 label "*" ]
                node [ id 13 label "*" ]
                node [ id 14 label "*" ] #C/H
                node [ id 15 label "*" ] #C/H
                node [ id 16 label "*" ] #C/H
                node [ id 17 label "*" ] #C/H
                edge [ source 1 target 10 label "-" ]
                edge [ source 1 target 11 label "-" ]
                edge [ source 5 target 2 label "-" ]
                edge [ source 2 target 3 label "-" ]
                edge [ source 3 target 4 label "-" ]
                edge [ source 4 target 6 label "-" ]
                edge [ source 3 target 12 label "-" ]
                edge [ source 3 target 13 label "-" ]
                edge [ source 2 target 14 label "-" ]
                edge [ source 2 target 15 label "-" ]
                edge [ source 4 target 16 label "-" ]
                edge [ source 4 target 17 label "-" ]
	]
	right [
                edge [ source 1 target 5 label "-" ]
                edge [ source 1 target 6 label "-" ]
                edge [ source 8 target 7 label "-" ]
                edge [ source 9 target 7 label "-" ]     
	]

	# make sure 2 isn't bonded to -O,-N to make sure 14 and 15 arent anything other than C/H
        constrainAdj [
                id 2 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" ]
        ]
        
        # make sure 4 isn't bonded to -O,-N to make sure 16 and 17 arent anything other than C/H
        constrainAdj [
                id 4 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" ]
        ]
	
        
]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

ketone_additionII.print(p)
