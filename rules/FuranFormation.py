furan_production = ruleGMLString("""rule [
	ruleID "Furan Production"
	labelType "term"

	left[
                edge [ source 1 target 2 label "-" ]
                edge [ source 1 target 9 label "=" ]
                edge [ source 3 target 4 label "-" ]
                edge [ source 4 target 10 label "=" ]
                edge [ source 2 target 7 label "-" ]
                edge [ source 3 target 8 label "-" ]
                
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "C" ]
                node [ id 4 label "C" ]
                node [ id 5 label "*" ]
                node [ id 6 label "*" ]
                node [ id 7 label "H" ]
                node [ id 8 label "H" ]
                node [ id 9 label "O" ]
                node [ id 10 label "O" ]
                node [ id 11 label "*" ] #C/H
                node [ id 12 label "*" ] #C/H
                edge [ source 2 target 3 label "-" ]
                edge [ source 2 target 5 label "-" ]
                edge [ source 3 target 6 label "-" ]
                edge [ source 1 target 11 label "-" ]
                edge [ source 4 target 12 label "-" ]
	]
	right [
                edge [ source 1 target 2 label "=" ]
                edge [ source 3 target 4 label "=" ]
                edge [ source 1 target 9 label "-" ]
                edge [ source 4 target 9 label "-" ]
                edge [ source 7 target 10 label "-" ]
                edge [ source 8 target 10 label "-" ]
	]
	
	# make sure 1 isn't bonded to -O,-N,-S to make sure 14 isnt anything other than C/H
        constrainAdj [
                id 1 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" label "S" ]
        ]
        
        # make sure 4 isn't bonded to -O,-N,-S to make sure 15 isnt anything other than C/H
        constrainAdj [
                id 4 op "=" count 0
                edgeLabels [ label "-" ]
                nodeLabels [ label "O" label "N" label "S" ]
        ]
        
]""")

p = GraphPrinter()
p.withColour = True
p.withIndex = True

furan_production.print(p)
