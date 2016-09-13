import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("-bias", type=float, default=2500.0, help="bias value for spring constant")
parser.add_argument("-at", type=float, default=-0.262, help="average value of order parameter in biased simulation")
args   = parser.parse_args()

str_out = ""
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
    str_out = str_out + "\nFUNC=atan(sqrt(x*x+z*z)/y)\n"
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

str_out = str_out + "\n\nRESTRAINT ARG=avgtheta AT={} KAPPA={} LABEL=restraint\n\nPRINT ARG=avgtheta STRIDE=10\n".format(args.at, args.bias)

str_out = str_out.rstrip(",")
print str_out
