import numpy as np

ylo = -70.0
L = -2.0 * ylo
coords = np.genfromtxt('test.txt')
start = 47
end = start + 22116
replace=False
mol_dat = np.zeros(3)

with open("new.351") as f:
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


