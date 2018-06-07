# Kate Williams
# 6/7/2018

infile = open("input", "r")
outfile = open("output", "w")

tempString = ""

i = 0

for line in infile:
    tempString = line
    for char in tempString:
        i += 1
    outfile.write(tempString + ", " + str(i) + "\n")
    i = 0

infile.close()
outfile.close()