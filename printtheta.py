import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("-bias", type=float, default=2500.0, help="bias value for spring constant")
parser.add_argument("-lower", type=float, default=-0.75, help="lower limit of order parameter in biased simulation")
parser.add_argument("-upper", type=float, default=-0.25, help="upper limit of order parameter in biased simulation")
parser.add_argument("-step", type=float, default=0.05, help="step between each consecutive umbrella")
parser.add_argument("-timestep", type=int, default=5000, help="timesteps after which umbrella is moved")
args   = parser.parse_args()

# at_range = np.arange(args.lower, args.upper+args.step, args.step)
steps = ((args.upper - args.lower) / args.step) + 1.0
steps = np.ceil(steps)
at_range = np.zeros(steps)
for i in np.arange(steps):
    at_range[i] = args.lower + args.step * i

str_out = ""
str_out = str_out + "UNITS ENERGY=kcal/mol\n"

count = 1

for i in range(3840, 6000, 18):
    str_out = str_out + "d{}1: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+5, i+12)
    str_out = str_out + "d{}2: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+6, i+13)
    str_out = str_out + "d{}3: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+7, i+14)
    str_out = str_out + "d{}4: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+8, i+15)
    str_out = str_out + "d{}5: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+9, i+16)
    str_out = str_out + "d{}6: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+10, i+17)
    str_out = str_out + "d{}7: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+11, i+18)
    count = count + 1

for i in range(8160, 10320, 18):
    str_out = str_out + "d{}1: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+5, i+12)
    str_out = str_out + "d{}2: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+6, i+13)
    str_out = str_out + "d{}3: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+7, i+14)
    str_out = str_out + "d{}4: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+8, i+15)
    str_out = str_out + "d{}5: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+9, i+16)
    str_out = str_out + "d{}6: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+10, i+17)
    str_out = str_out + "d{}7: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i+11, i+18)
    count = count + 1

for i in range(1, count):
    for j in range(1, 8):
        str_out = str_out + "\nMATHEVAL ...\n"
        str_out = str_out + "LABEL=theta{}{}\nARG=d{}{}.y,d{}{}.z,".format(i, j, i, j, i, j, i, j)
        str_out = str_out.rstrip(",")
        str_out = str_out + "\nFUNC=atan(y/x)\n"
        str_out = str_out + "PERIODIC={-pi,pi}\n"
        str_out = str_out + "... MATHEVAL\n"

str_out = str_out + "\navgtheta: COMBINE ARG="

for i in range(1, count):
    for j in range(1, 8):
        str_out = str_out + "theta{}{},".format(i, j)
str_out = str_out.rstrip(",")

str_out = str_out + " COEFFICIENTS="

coeff = 1/(240*7.0)
for i in range(1, count):
    for j in range(1, 8):
        str_out = str_out + "{:1.9f},".format(coeff)
str_out = str_out.rstrip(",")

str_out = str_out + " PERIODIC={-pi,pi}"

# str_out = str_out + "\n\nRESTRAINT ARG=avgtheta AT={} KAPPA={} LABEL=restraint\n\nPRINT ARG=avgtheta STRIDE=10\n".format(args.at, args.bias)

str_out = str_out + "\n\nMOVINGRESTRAINT ...\n"
str_out = str_out + "  ARG=avgtheta\n"
for i in range(len(at_range)):
    str_out = str_out + "  STEP{}={} AT{}={} KAPPA{}={}\n".format(i, i*args.timestep, i, at_range[i], i, args.bias)
str_out = str_out + "... MOVINGRESTRAINT\n"

str_out = str_out + "\nPRINT ARG=avgtheta STRIDE=10\n"


str_out = str_out.rstrip(",")
print str_out
