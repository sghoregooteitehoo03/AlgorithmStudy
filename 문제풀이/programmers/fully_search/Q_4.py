def solution(brown, yellow):
    total = brown + yellow

    for h in range(3, total):
        if total % h == 0:
            w = total // h
            if w >= h:
                if (w - 2) * (h - 2) == yellow:
                    return [w, h]