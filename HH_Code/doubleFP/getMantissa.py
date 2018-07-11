import csv, math, collections
with open('dt01FP.txt') as f:
    read = csv.reader(f, delimiter='\t')
    bla = [(math.frexp(float(i[0])), float(i[2]),
            float.hex(math.frexp(float(i[0]))[0])) for i in read]


c = collections.Counter((j[0][0] for j in bla))
print([(int(i[0]*32), i[1]) for i in c.most_common()])
