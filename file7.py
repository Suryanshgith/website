content = "true" 
i = 1

with open("logfile.txt","r") as f:
    while content:
        content = f.readline()
        if("python" in content.lower()):
            print(f"python is present in line number {i}")
        i+= 1
        
