def can_go_on_ride(x, h):
    return "YES" if x >= h else "NO"


t = int(input())


for _ in range(t):
   
    x, h = map(int, input().split())
    
   
    print(can_go_on_ride(x, h))
