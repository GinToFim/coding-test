def solution(my_string):
    my_string = my_string.lower()
    my_string = ''.join(sorted(my_string))
    return my_string