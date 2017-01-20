import numpy as np
import random

in_mol=False
zb0 = 0.0
zb1 = 81.0040
n_atoms = 22116
mol_dat = []
# even=False
Rnum_O = 240 * 18
Rnum_He = 240 * 18
O_used = 0
He_used = 0

print "{}\nComment line".format(n_atoms + Rnum_He)

with open("dump.stripped") as f:
    for t,l in enumerate(f):
#         if ((t/22116)%2 == 0):
#             even=True
#         else:
#             even=False
#         print "quicktest {}".format(even)

        l_arr = l.split()
#         print(l_arr)
        l_arr[1] = float(l_arr[1])
        l_arr[2] = float(l_arr[2])
        l_arr[3] = float(l_arr[3])
        if (l_arr[0] == '2' and l_arr[2] > 0 and not in_mol):
            in_mol=True
#             mol_dat = []
            mol_dat.append(l_arr)
        elif (l_arr[0] == '2' and l_arr[2] > 0 and in_mol):
            mol_dat.append(l_arr)
        elif (l_arr[0] == '1' and l_arr[2] > 0):
            if not in_mol:
                raise ValueError("Hit atom type 1 but not in a molecule!")
            mol_dat.append(l_arr)
            in_mol=False
            y0 = mol_dat[0][2]
            z0 = mol_dat[0][3]
            y1 = mol_dat[9][2]
            z1 = mol_dat[9][3]
            y_vec = y1 - y0
            z_vec = (z1 - z0) / (zb1 - zb0)
            z_vec = (z_vec - round(z_vec)) * (zb1 - zb0)
            th = -np.arctan(z_vec / y_vec)
            th = random.random()
#             print y0, z0, y1, z1, y_vec, z_vec, th
            if (th > 0.5):
                for line in mol_dat:
    # 		    if (line[0]!="8"):print "w to r {}".format(t)
                    print("O {} {} {}".format(line[1], line[2], line[3]))
                    O_used = O_used + 1
            else:
                for line in mol_dat:
# 		    if (line[0]!="2"):print "r to w {}".format(t)
                    print("He {} {} {}".format(line[1], line[2], line[3]))
                    He_used = He_used + 1
            mol_dat=[]
        else:
            print(l.strip())

        if ((t%22116) == 0 and t != 0):
            O_left = Rnum_O - O_used
            He_left = Rnum_He - He_used
            for i in xrange(O_left):
                print "O -140 -140 -140"
            for i in xrange(He_left):
                print "He -140 -140 -140"
            O_used = 0
            He_used = 0
            print "{}\nComment line".format(n_atoms + Rnum_O)

        if t == 22116 * 200:
            exit(0)

