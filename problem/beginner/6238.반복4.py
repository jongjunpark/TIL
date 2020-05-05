sol = ""
for i in range(1,101,1):
    if i%2 != 0:
        sol += "%d, "%i

print(sol[0:193])
