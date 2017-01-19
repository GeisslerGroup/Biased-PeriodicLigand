import numpy as np

in_mol=False
zb0 = 0.0
zb1 = 81.0040
# dump = np.genfromtxt('/home/pratima/Biased-PeriodicLigand/2017-01-13-run/dump.stripped')

with open("dump.stripped") as f:
    for t,l in enumerate(f):
        l_arr = l.split()
#         print(l_arr)
        l_arr[1] = float(l_arr[1])
        l_arr[2] = float(l_arr[2])
        l_arr[3] = float(l_arr[3])
        if (l_arr[0] == '2' and l_arr[2] > 0 and not in_mol):
            in_mol=True
            mol_dat = []
            mol_dat.append(l_arr)
        elif (l_arr[0] == '2' and l_arr[2] > 0 and in_mol):
            mol_dat.append(l_arr)
        elif (l_arr[0] == '1' and l_arr[2] > 0):
            if not in_mol:
                raise ValueError("Hit atom type 1 but not in a molecule!")
            mol_dat.append(l_arr)
            in_mol=False
#             print mol_dat
            y0 = mol_dat[0][2]
            z0 = mol_dat[0][3]
            y1 = mol_dat[9][2]
            z1 = mol_dat[9][3]
            y_vec = y1 - y0
            z_vec = (z1 - z0) / (zb1 - zb0)
            z_vec = (z_vec - round(z_vec)) * (zb1 - zb0)
            th = -np.arctan(z_vec / y_vec)
            if (th > 0.7):
                mol_dat[0] == '8'
#             print("fixed!")
            for line in mol_dat:
                print("{} {} {} {}".format(line[0], line[1], line[2], line[3]))
        else:
            print(l.strip())

