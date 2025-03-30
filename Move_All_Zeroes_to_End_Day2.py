# User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr):
        
        count = 0
        # Traverse the array and swap non-zero elements to the front
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1




if __name__ == '__main__':
    tc = int(input("Enter number of test cases: "))
    while tc > 0:
        arr = list(map(int, input("Enter array elements separated by space: ").strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        print("Modified Array:", *arr)
        print("~")
        tc -= 1
