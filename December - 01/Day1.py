
for loop in range(int(input())):
    l = list(map(str, input().split()))
    ans = ''
    for i in l:
        ans += chr(int(i , 16))
    print(ans)