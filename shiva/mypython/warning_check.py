import sys



x1 = open(sys.argv[1],"r")
x2 = open(sys.argv[2],"r")
count1 = 0
count2 = 0

for line in x1:
    if line.find("warning") != -1:
        count1 += 1
x1.close()

for line in x2:
    if line.find("warning") != -1:
        count2 += 1
x2.close()

print(f"** Old warning count =  {count1}")
print(f"** New warning count =  {count2}")

if count2 > count1:
    print("** New Warnings have been introduced in the new build")
    print("Build is not promoted")
else:
    print("Build is promoted")

