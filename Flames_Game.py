def remove_common(p1_l, p2_l):
    for i in range(len(p1_l)):
        for j in range(len(p2_l)):
            if p1_l[i] == p2_l[j]:
                x = p1_l[i]
                p1_l.remove(x)
                p2_l.remove(x)
                return [[p1_l, p2_l], 1]
    return [(p1_l+p2_l), 0]

if __name__ == "__main__":
    print('Welcome to the game of Flames\nA Game where your life can be decided\n')
    p1 = input("Enter your name (full name): ")
    p1 = p1.upper()
    p1 = "".join(p1.split())
    p1_l = list(p1)
    p2 = input("Enter the special name (full name): ")
    p2 = p2.upper()
    p2 = "".join(p2.split())
    p2_l = list(p2)
    flag = 1
    while flag:
        l_ret = remove_common(p1_l, p2_l)
        flag = l_ret[1]
        if flag == 0:
            final = l_ret[0]
            break
        p1_l = l_ret[0][0]
        p2_l = l_ret[0][1]
    count = len(final)
    Flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    ind = 0
    while len(Flames) > 1:
        ind = ((count+ind) % len(Flames)) - 1
        Flames.remove(Flames[ind])
    print(f"Result returned is --> {Flames[0]}\nCongratulations")
    input('\nPress any key to exit....')
