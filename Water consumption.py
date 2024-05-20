def followed_advice(x):
    return "YES" if x >= 2000 else "NO"


t = int(input())


for _ in range(t):
 
    x = int(input())
    
    
    print(followed_advice(x))

