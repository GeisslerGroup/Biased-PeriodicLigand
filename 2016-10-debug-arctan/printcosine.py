import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("-bias", type=float, default=2500.0, help="bias value for spring constant")
parser.add_argument("-at_lower", type=float, default=-0.75, help="lower limit of order parameter in biased simulation")
parser.add_argument("-at_upper", type=float, default=-0.73, help="upper limit of order parameter in biased simulation")
parser.add_argument("-at_step", type=float, default=0.01, help="step between each consecutive umbrella")
parser.add_argument("-timestep", type=int, default=5000, help="timesteps after which umbrella is moved")
args   = parser.parse_args()

at_range = np.arange(args.at_lower, args.at_upper+args.at_step, args.at_step)
str_out = ""
str_out = str_out + "UNITS ENERGY=kcal/mol\n"
count = 1

for i in range(3840, 6000, 18):
    str_out = str_out + "d{}: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i, i+9)
    count = count + 1

for i in range(8160, 10320, 18):
    str_out = str_out + "d{}: DISTANCE ATOMS={},{} COMPONENTS\n".format(count, i, i+9)
    count = count + 1

for i in range(1, count):
    str_out = str_out + "\nMATHEVAL ...\n"
    str_out = str_out + "LABEL=theta{}\nARG=d{}.x,d{}.y,d{}.z,".format(i, i, i, i)
    str_out = str_out.rstrip(",")
    str_out = str_out + "\nFUNC=atan(z/y)+0.0*x\n"
    str_out = str_out + "PERIODIC={-pi,pi}\n"
    str_out = str_out + "... MATHEVAL\n"

str_out = str_out + "\navgtheta: COMBINE ARG="

for i in range(1, count):
    str_out = str_out + "theta{},".format(i)
str_out = str_out.rstrip(",")

str_out = str_out + " COEFFICIENTS="

for i in range(1, count):
    str_out = str_out + "0.00416667,"
str_out = str_out.rstrip(",")

str_out = str_out + " PERIODIC={-pi,pi}"

str_out = str_out + "\n\nRESTRAINT ARG=avgtheta AT={} KAPPA={} LABEL=restraint\n".format(args.at_lower, args.bias)

# str_out = str_out + "\nPRINT ARG="
# for i in range(1, count):
#     str_out = str_out + "theta{},".format(i)
# str_out = str_out + ",avgtheta STRIDE=10\n"

str_out = str_out + "\nPRINT ARG=" + ",".join(["theta{}".format(i) for i in range(1,count)]) + ",avgtheta STRIDE=10\n"
str_out = str_out.rstrip(",")

print str_out
