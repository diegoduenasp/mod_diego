thiolactone_formation = ruleGMLString("""rule [
	ruleID "Thiolactone Formation"
	labelType "term"

left[
                edge [ source 1 target 3 label "-" ]
                edge [ source 6 target 5 label "-" ]
	]
	context [
                node [ id 1 label "C" ]
                node [ id 2 label "O" ]
                node [ id 3 label "O" ]
                node [ id 4 label "H" ]
                node [ id 5 label "H" ]
                node [ id 6 label "S" ]
                node [ id 7 label "*" ]
                edge [ source 1 target 2 label "=" ]
                edge [ source 1 target 7 label "-" ]
                edge [ source 3 target 4 label "-" ]
                edge [ source 6 target 7 label "-" ]
                
	]
	right [
                edge [ source 3 target 5 label "-" ]
                edge [ source 1 target 6 label "-" ]
	]
]""")
