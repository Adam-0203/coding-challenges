def tower_hanoi(n,begin="begin",inter="inter",end="end"):
    if n == 1 : 
        print(f"move from {begin:5} to {end:5}")
        return

    tower_hanoi(n-1,begin,end,inter)
    print(f"move from {begin:5} to {end:5}")
    tower_hanoi(n-1,inter,begin,end)


tower_hanoi(3)
