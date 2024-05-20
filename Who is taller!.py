def taller(X, Y):
    if X < Y:
        return 'B'
    else:
        return 'A'


T = int(input())


for _ in range(T):
  
    X, Y = map(int, input().split())
    
    
    print(taller(X, Y))
