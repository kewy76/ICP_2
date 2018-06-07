# Kate Williams
# 6/7/2018

infile = open("input", "r")
outfile = open("output", "w")

count = 0

for line in infile:
    outfile.write(line)
    count += 1

outfile.write("\n" + str(count))

infile.close()
outfile.close()