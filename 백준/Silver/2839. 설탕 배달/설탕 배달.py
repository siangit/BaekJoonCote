N = int(input())

def sugar(N):
    fivekg_bags, five_mod =divmod(N,5)
    if five_mod ==0:
        print(fivekg_bags)
        return
    
    while fivekg_bags >= 0:
        threekg_bags,three_mod =divmod(five_mod,3)
        if three_mod ==0:
            print(fivekg_bags+threekg_bags)
            return
        fivekg_bags -= 1
        five_mod += 5

    else:
        print(-1)

sugar(N)
