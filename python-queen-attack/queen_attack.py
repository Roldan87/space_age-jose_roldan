
def board(wq, bq):
    # COACHES' NOTE: wq, bq? I only know what these mean because of the context, don't depend on the reader's deduction skills but just use full names.
    # COACHES' NOTE: no need for el(if), raising an error returns out of the function
    if wq[0] < 0 or wq[0] > 7:
        raise ValueError("White Queen out of the board bounds")
    elif wq[1] < 0 or wq[1] > 7:
        raise ValueError("White Queen out of the board bounds")
    elif bq[0] < 0 or bq[0] > 7:
        raise ValueError("Black Queen out of the board bounds")
    elif bq[1] < 0 or bq[1] > 7:
        raise ValueError("Black Queen out of the board bounds")
    elif wq[0] == bq[0] and wq[1] == bq[1]:
        raise ValueError("Both Queens cannot share the same location")
    # COACHES' NOTE: same as before, no need for the else check, if you got this far, then you have not triggered any exception
    else:
        # COACHES' NOTE: again, don't use abbreviations for variable names.
        ans = [["_"] * 8 for num in range(8)]
        ans[wq[0]][wq[1]] = "W"
        ans[bq[0]][bq[1]] = "B"
        ans = ["".join(row) for row in ans]
        return ans
    

def can_attack(wq, bq):
    
    # COACHES' NOTE: same comment as before, el(if) is not needed here
    if wq[0] < 0 or wq[0] > 7:
        raise ValueError("White Queen out of the board bounds")
    elif wq[1] < 0 or wq[1] > 7:
        raise ValueError("White Queen out of the board bounds")
    elif bq[0] < 0 or bq[0] > 7:
        raise ValueError("Black Queen out of the board bounds")
    elif bq[1] < 0 or bq[1] > 7:
        raise ValueError("Black Queen out of the board bounds")
    elif wq[0] == bq[0] and wq[1] == bq[1]:
        raise ValueError("Both Queens cannot share the same location")
    else:
        if wq[0] == bq[0]:
            return True
        elif wq[1] == bq[1]:
            return True
        elif abs(wq[0] - bq[0]) == abs(wq[1] - bq[1]):
            return True
        else:
            return False

# COACHES' NOTE: Nice code, but don't abbreviate. Also, typing would be appreciated.
