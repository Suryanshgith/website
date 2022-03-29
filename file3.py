for i in range(1,21):
   with open(f"table{i}","w") as f:
        for num in range(1,11):
            f.write(f"{i}*{num}={i*num}")
        if(num!=10):
            f.write("\n")
            
         
        

