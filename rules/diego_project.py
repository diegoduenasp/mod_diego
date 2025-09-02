AmmoniumionOligo = [ruleGMLString("""rule [
    ruleID "Ammonium ion oligomerization"
    left [
        edge [ source 1 target 3 label "=" ]
        edge [ source 7 target 11 label "-" ]
    ]
    context [
        node [ id 1 label "C" ]
        node [ id 2 label "C" ]
        node [ id 3 label "O" ]
        node [ id 4 label "O" ]
        node [ id 5 label "H" ]
        node [ id 6 label "H" ] # there need to be at least 2 alpha-H on one of the carbonyls
        node [ id 7 label "N" ]
        node [ id 8 label "H" ]
        node [ id 9 label "H" ]
        node [ id 10 label "H" ]
        node [ id 11 label "H" ]
        edge [ source 1 target 2 label "-" ]
        edge [ source 1 target 5 label "-" ]
        edge [ source 2 target 4 label "=" ]
        edge [ source 2 target 6 label "-" ]
        edge [ source 7 target 8 label "-" ]
        edge [ source 7 target 9 label "-" ]
        edge [ source 7 target 10 label "-" ]
    ]
    right [
        edge [ source 1 target 3 label "-" ] # convert O into OH
        edge [ source 3 target 11 label "-" ]
    ]
]
""")]
# The rule below does beta elimination in the same step, try to not do that

inv_AmmoniumionOligo = [ruleGMLString("""rule [
    ruleID "Inverse Ammonium ion oligomerization"
    left [
        edge [ source 1 target 3 label "-" ] # convert O into OH
        edge [ source 3 target 11 label "-" ]
    ]
    context [
        node [ id 1 label "C" ]
        node [ id 2 label "C" ]
        node [ id 3 label "O" ]
        node [ id 4 label "O" ]
        node [ id 5 label "H" ]
        node [ id 6 label "H" ] # there need to be at least 2 alpha-H on one of the carbonyls
        node [ id 7 label "N" ]
        node [ id 8 label "H" ]
        node [ id 9 label "H" ]
        node [ id 10 label "H" ]
        node [ id 11 label "H" ]
        edge [ source 1 target 2 label "-" ]
        edge [ source 1 target 5 label "-" ]
        edge [ source 2 target 4 label "=" ]
        edge [ source 2 target 6 label "-" ]
        edge [ source 7 target 8 label "-" ]
        edge [ source 7 target 9 label "-" ]
        edge [ source 7 target 10 label "-" ]
    ]
    right [
        edge [ source 1 target 3 label "=" ]
        edge [ source 7 target 11 label "-" ]
    ]
]
""")]
