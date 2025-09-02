thiophene_production = ruleGMLString("""rule [
	ruleID "Thiophene Production"
	labelType "term"

	left[
                edge [ source 1 target 2 label "-" ]
                edge [ source 1 target 12 label "=" ]
                edge [ source 3 target 4 label "-" ]
                edge [ source 4 target 13 label "=" ]
                edge [ source 3 target 9 label "-" ]
                edge [ source 2 target 8 label "-" ]
                edge [ source 10 target 7 label "-" ]
                edge [ source 11 target 7 label "-" ]
                
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "C" ]
                node [ id 3 label "C" ]
                node [ id 4 label "C" ]
                node [ id 5 label "*" ]
                node [ id 6 label "*" ]
                node [ id 7 label "S" ]
                node [ id 8 label "H" ]
                node [ id 9 label "H" ]
                node [ id 10 label "H" ]
                node [ id 11 label "H" ]
                node [ id 12 label "O" ]
                node [ id 13 label "O" ]
                node [ id 14 label "*" ] #C/H
                node [ id 15 label "*" ] #C/H
                edge [ source 2 target 3 label "-" ]
                edge [ source 2 target 5 label "-" ]
                edge [ source 3 target 6 label "-" ]
                edge [ source 1 target 14 label "-" ]
                edge [ source 4 target 15 label "-" ]
	]
	right [
                edge [ source 1 target 2 label "=" ]
                edge [ source 3 target 4 label "=" ]
                edge [ source 1 target 7 label "-" ]
                edge [ source 4 target 7 label "-" ]
                edge [ source 13 target 9 label "-" ]
                edge [ source 13 target 8 label "-" ]
                edge [ source 12 target 10 label "-" ]
                edge [ source 12 target 11 label "-" ]
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

thiophene_production.print(p)
