#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max0=0
        for i in arr:
            if i>max0:
                max0=i
                #print(max0)
        
        max1=-1
        for i in arr:
            if i>max1 and i<max0:
                #print(i)
                max1=i
                #print(max1)
        return max1
            
            

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends