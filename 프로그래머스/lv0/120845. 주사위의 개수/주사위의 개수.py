def solution(box, n):
    w, l, h = box
    return (w // n) * (l // n) * (h // n) 