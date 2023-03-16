def bigger_is_greater(w):
    n = len(w)
    for i in range(n-2, -1,-1):
        if w[i] < w[i+1]:
            break
    else:
        return "no answer"
    
    for j in range(n-1, i,-1):
        if w[j] > w[i]:
            break

    w = list(w)
    w[i], w[j] = w[j], w[i]
    w[i+1:] = reversed(w[i+1:])
    return "".join(w)
