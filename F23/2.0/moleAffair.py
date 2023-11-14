import time

#cheatings
#letters
#increments
#rips

def solveMoleAffair(k,cheatings,letters,rip):
    l, r = 0,cheatings
    while l < r:
        mid = (l+r)//2
        projectedLetters = (mid/2)*(k*(mid+1))-rip*cheatings+rip*mid
        if projectedLetters > letters:
            r = mid
        elif projectedLetters < letters:
            l = mid
        else:
            break
    return (cheatings-mid)

print(solveMoleAffair(2,14,179,3))