#!/bin/bash

# mpiexec -np 6 ~/local/lammps-plumed-2Apr13/src/lmp_openmpi -in in_new.340

biaslist=$(seq 25000 5000 75000)
at=-0.262

for bias in ${biaslist}
do
	python printcosine.py -bias ${bias} -at ${at }> cosine.plu
	lmp_plumed -in in.long -log log${bias}.lammps
	cp dump.340 dump.340.${bias}
done
