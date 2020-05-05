T = int(input())
for t in range(1,T+1):
    st = input()
    i = len(st)
    a = "..#.."
    a_1 = ".#.."
    b = ".#.#."
    b_1 = "#.#."
    print(a,end='')
    print(a_1*(i-1))
    print(b,end='')
    print(b_1*(i-1))
    print(f"#.{st[0]}.#",end='')
    for j in range(1,len(st)):
        print(f".{st[j]}.#",end='')
    print()
    print(b,end='')
    print(b_1*(i-1))
    print(a,end='')
    print(a_1*(i-1))