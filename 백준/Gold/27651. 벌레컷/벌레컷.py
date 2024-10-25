n = int(input().rstrip()) 
arr = list(map(int, input().rstrip().split()))  
sums = [0]
for a in arr:
    sums.append(sums[-1] + a) 
del sums[0]  
result = 0  
for y in range(1, n - 1):
    stomSum = sums[-1] - sums[y]  

    start = 0
    end = y - 1 

    if start == end:
        if sums[0] < stomSum < sums[y] - sums[0]:
            result += 1
    else:
        cnt = 0
        already = 0
        while start <= end:
            mid = (start + end) // 2 
            if sums[mid] < stomSum < sums[y] - sums[mid]:
                result += mid + 1 - already  
                already = mid + 1
                start = mid + 1
            else:
                end = mid - 1
print(result)  
