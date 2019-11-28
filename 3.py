s1,s2 = map(int, input().split())
e1,e2 = map(int, input().split())

sim_height = min(s1, s2)
sim_width = max(s1, s2)
env_height = min(e1, e2)
env_width = max(e1, e2)

if sim_height <= env_height and sim_width <= env_width:
    print("YES")
else:
    print("NO")