#with_formaldehyde = True

#Including these files using MOD's include() so that MOD's functions are callable in them
include("main.py")

#Initial Reactants
#thiolactone = smiles("C1(CCCCS1)=O", "Thiolactone")

#thioacetic_acid = smiles("CC(=O)S", "Thioacetic Acid")
#ethylene = smiles("C=C", "Ethylene")
#methanethiol = smiles("CS", "Methanethiol")
#hydrogen_cyanide = smiles("C(SC)=N", "Hydrogen Cyanide")
#water = smiles("O", name="Water")
#thio = smiles("C(CCCCS)(O)=O", "thio")
#bisulfite = smiles("OS(=O)[O-]", "Bisulfite")
#formaldehyde = smiles("C=O", "Formaldehyde")


#Testing Glucose/Threose + H2S

#open_glucose = smiles("O=CC(O)C(O)C(O)C(O)C(O)", "Open Chain Glucose")
#threose = smiles("C(C(C(CO)O)O)=O", "Threose")
#hydrogen_sulfide = smiles("S", "Hydrogen Sulfide")
water = smiles("O", name="Water")
ammonia = smiles("N", name="Ammonia")
#glyoxal = smiles("C(=O)C(=O)", "Glyoxal")
#aa = smiles("[H][N]([H])([H])[H]", "Ammonium ion")
#cyanamide = smiles("N=C=N", "Cyanamide")
#acetone = smiles("CC(=O)C", "Acetone")

xylose = smiles("OC1COC(O)C(O)C1O", "Xylose")
#nhcl = smiles("[H][N](Cl)(Cl)(Cl)Cl", "NHCl4")
#koh = smiles("O[K]", "KOH")
#dextrose = smiles("OCC1OC(O)C(O)C(O)C1O" , "Dextrose")

# Number of generations we want to perform
generations = 8

dg = DG(graphDatabase=inputGraphs,
	labelSettings=LabelSettings(LabelType.Term, LabelRelation.Specialisation))


subset = inputGraphs
universe = []
# dump initial reactants as part of "G0"
write_gen_output(subset, generation=0, reaction_name="test6")


with dg.build() as b:
	for gen in range(generations):
		start_time = time.time()
		print(f"Starting round {gen+1}")
		res = b.execute(addSubset(subset) >> addUniverse(universe) >> strat, verbosity=2)
		end_time = time.time()
		print(f"Took {end_time - start_time} seconds to complete round {gen+1}")
		print(f'Products in generation {gen+1}:', len(res.subset))
		subset, universe = res.subset, res.universe
		#export_to_neo4j(dg_obj = dg, generation_num = gen)
		write_gen_output(subset, gen+1, reaction_name="test6")
	print('Completed')
dg.print()

# Dump the dg so it can be loaded again quickly without having to generate it from scratch.

f = dg.dump()
print("Dump file: ", f)


"""
Starting round 1)
Took 0.03515958786010742 seconds to complete round 1
Products in generation 1: 1
Starting round 2
Took 0.006894111633300781 seconds to complete round 2
Products in generation 2: 1
Starting round 3
Took 0.02248096466064453 seconds to complete round 3
Products in generation 3: 10
Starting round 4
Took 0.4581747055053711 seconds to complete round 4
Products in generation 4: 50
Starting round 5
Took 6.265398979187012 seconds to complete round 5
Products in generation 5: 282


Starting round 6
Took 978.2353045940399 seconds to complete round 6
Products in generation 6: 2254
Completed
Dump file:  out/056_DG.dg
End of code from 'test4.py'
"""