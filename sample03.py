# sun 16:33 modified
# Sun 16:36 modified
# Numbers
def pattern(n):
    x=0
    for i in range(0,n):
        x=x+1
        for j in range(0,i+1):
            print(x,end=" ")
        print("\r")
    
pattern(9)



