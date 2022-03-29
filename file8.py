with open("this.txt","r") as f:
    f1 = f.read()
with open("copy.txt","w") as f:
    f.write(f1)
