"""
1. given an amount x.
2.minimum coins required to make that amount.
Note : Consider indian coin system
"""
#1,2,5,10

d = {10:10,5:5,2:2,1:1}
x = int(input("Enter amount:"))

def coin(x):
    if(x == 0):
        return
    maxvalue = max(d)
    if d.get(x):
        return 1
    else:
        count = 0
        while(x>0):
            if x >= maxvalue:
               
                x = x - maxvalue
                
                count += 1
            else:
                
                del d[maxvalue]
                maxvalue = max(d)
                
        return count
    
print("num:",coin(x))
