with open("logfile.txt","r") as f:
    logfile = f.read()
    if("Python" in logfile):
        print("It contains word python.")
    else:
        print("It doesn't contains word python.")

