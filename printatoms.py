import numpy as np
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser(description="")
parser.add_argument("mode", choices=["A","B"], type=str, help="Mode for atoms")
args   = parser.parse_args()

str_out = ""

if args.mode == "A":
    for atom in range(3991, 5999, 18):
        str_out = str_out + "{},".format(atom)


if args.mode == "B":
    for atom in range(3997, 5999, 18):
        str_out = str_out + "{},".format(atom)

str_out = str_out.rstrip(",")
print str_out
