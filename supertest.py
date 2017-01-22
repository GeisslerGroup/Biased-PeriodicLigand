import random

fp=open("tmp.xyz","w")
fp.write("3\n\n")

for i in range(100):
  dec=random.random()
  if dec>0.67:fp.write("N -100 0 0\nO {} 0 0\n N -50 0 0\n\n\n".format(1e-4*i))
  elif dec>0.33:fp.write("N -100 0 0\nO -50 0 0\n N {} 0 0\n\n\n".format(1e-4*i))
  else:fp.write("N 1 0 0\nN -100 0 0\nN -50 0 0\n\n\n")

fp.close()


