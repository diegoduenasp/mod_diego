SHELL=/bin/bash
summary/all.tex: gen
	echo '\summaryRule{Imidazole}{\summaryRuleSpan{out/001_r_0_10300000}{out/001\_r\_0\_10300000}}{\summaryRuleSpan{out/003_r_0_11300100}{out/003\_r\_0\_11300100}}{}{out/004_r_0_constraints.tex}' >> summary/all.tex
	echo '\summaryRule{Inverse Imidazole}{\summaryRuleSpan{out/006_r_1_10300000}{out/006\_r\_1\_10300000}}{\summaryRuleSpan{out/008_r_1_11300100}{out/008\_r\_1\_11300100}}{}{out/009_r_1_constraints.tex}' >> summary/all.tex
summary.pdf: summary/all.tex
	mod_post --mode compileSummary
include summary/MakefileImpl
include summary/MakefileDep
include summary/MakefileAllTarget
include summary/MakefileClean
