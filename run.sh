#!/bin/bash

biaslist=$(seq -0.80 0.05 -0.25)

for bias in ${biaslist}
do
	python printcosine.py -bias 2500.0 -at ${bias} > cosine.plu
	lmp_plumed -in in.long -log log.${bias}.lammps
	mv dump.340 dump_files/dump.340.${bias}
	mv log.${bias}.lammps log_files/
done
