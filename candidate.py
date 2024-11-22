import random
def candidate(n):
    if n <=0:
        raise ValueError("n should be a number")
    candidates=list(range(1,1+n))
    random.shuffle(candidates)
    x=1
    while len(candidates)>1:
        candidates.pop(x)
        x=(x+1)%len(candidates)
    return candidates[0]
try:
    n=int(input("enter a number"))
    winner=candidate(n)
    print(f"number of winner:{winner}")
except ValueError as v:
    print(v)