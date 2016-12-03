import numpy as np

ylo = -54.721679678020529
L = -2.0 * ylo
coords = np.genfromtxt('/home/pratima/Biased-PeriodicLigand/2016-11-22-run/solv.xyz')
start = 27
end = start + 22116
replace=False
mol_dat = np.zeros(3)

with open("new.340") as f:
    for t, l in enumerate(f):
        l_arr = l.split()
        if (t >= start and t < end):
            index = int(l_arr[0]) - 1
            mol_dat[0] = float(l_arr[3])
            mol_dat[1] = float(l_arr[4])
            mol_dat[2] = float(l_arr[5])

            if (l_arr[2] == '5' or l_arr[2] == '6'):
                l_arr[3] = coords[index][1]
                l_arr[4] = coords[index][2]
                l_arr[5] = coords[index][3]
#             print l_arr
            print("{} {} {} {} {} {} {} {} {}".format(l_arr[0], l_arr[1], l_arr[2], l_arr[3], l_arr[4], l_arr[5], l_arr[6], l_arr[7], l_arr[8]))
        else:
            print(l.strip())

#         if (l_arr[0] == '5' and not in_mol):
#             in_mol=True
# #             print(l_arr)
#             mol_dat = []
#             mol_dat.append(l_arr)
#         elif (l_arr[0] == '6'):
#             if not in_mol:
#                 raise ValueError("Hit atom type 6 but not in a molecule!")
#             mol_dat.append(l_arr)
#         elif (l_arr[0] == '5' and in_mol):
#             in_mol=False
#             mol_dat.append(l_arr)
#             y_dat = [line[2] for line in mol_dat]
#             if (max(y_dat) - min(y_dat) > 10):
# #                 print(mol_dat)
#                 y_fix = [(y_i + L if y_i < 0 else y_i) for y_i in y_dat]       
#                 mol_fix = [[mol_i[0], mol_i[1], y_i, mol_i[3]] for mol_i, y_i in zip(mol_dat, y_fix)]
#                 mol_dat = mol_fix
#             for line in mol_dat:
# #                 print("{} {:4.5f} {:4.5f} {:4.5f}".format(mol_dat[0], mol_dat[1], mol_dat[2], mol_dat[3]))
#                 print("{} {} {} {}".format(line[0], line[1], line[2], line[3]))
#         else:
#             print(l.strip())

