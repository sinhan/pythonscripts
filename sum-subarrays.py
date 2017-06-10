arr = [1,2,2,2,1,2,3,4,5,5,6,7]
print arr
givenSum = 20
l = len(arr)
currSum = arr[0];
start=0;
end=0;
while end < l:

    if currSum == givenSum:
        print "Found given sum from " + str(start) + " to " + str(end)
        print arr[start:end+1]

    if currSum <= givenSum:
        end += 1;
        if end < l:
            currSum = currSum + arr[end]
    else:
        currSum = currSum - arr[start];
        start += 1
