import sys
input = sys.stdin.readline


while True :
    try  :
        n = int(input())
    except :
        break
    
    result = '1'
    
    while True :
        if int(result) % n == 0 :
            print(len(result))
            break
        
        result += '1'
    