with open("poem.txt","r") as f:
    poem = f.read()

if("twinkle" in poem):
    print("Yes,it contains twinkle")
else:
    print("No,it doesn't contain twinkle")
