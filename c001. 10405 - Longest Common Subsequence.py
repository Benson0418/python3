"""

time complexity O(n²)

space complexity O(n)
"""
while True:
    try:
        s1=input()
        s2=input()
    except:
        break
    n1=len(s1)
    n2=len(s2)
    dp=[0]*(n2+1)
    for i in range(1,n1+1):
        dp_prev=dp[:]
        for j in range(1,n2+1):
            if s1[i-1]==s2[j-1]:
                dp[j]=dp_prev[j-1]+1
            else:
                dp[j]=max(dp[j-1],dp[j])
    print(dp[n2])
