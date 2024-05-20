def is_good_turn(x, y):
    return "YES" if x + y > 6 else "NO"


t = int(input())


for _ in range(t):
   
    x, y = map(int, input().split())
    
  
    print(is_good_turn(x, y))
