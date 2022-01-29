nameList = ["Doc","Grumpy","Happy","Sleepy","Bashful","Sneezy","Dopey"]
longest = -1
for name in nameList:
    if len(name) > longest:
        longest = len(name)
        result = name
print(result)
        
    
