file1 = "this.txt"
file2 = "log.txt"

with open(file1) as f:
    f1 = f.read()
with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Both of the files are identical.")
else:
    print("Both of the files are not identical.")

