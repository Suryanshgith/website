userFile = input("Your File Name:\n") 
try: 
    with open(f"{userFile}","r") as f:
        f.read()
        userWord = input("Word you want to replace:\n")
        with open(f"{userFile}","r") as f:
             content = f.read() 
        if(f"{userWord}" in content): 
            userReplaceWord = input("Word that is going to replace:\n")
            content = content.replace(f"{userWord}",f"{userReplaceWord}")
            with open(f"{userFile}","w") as f: 
                 f.write(content)
        else:
            print(f"There is no {userWord} in {userFile}")
except IOError:
        print(f"There is no file named {userFile}")


 
