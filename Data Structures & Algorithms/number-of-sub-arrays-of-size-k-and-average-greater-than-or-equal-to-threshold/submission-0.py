class Solution:
   
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        L=0
        total=0

        for R in range(len(arr)):
            total += arr[R]

            if R-L+1 == k:
                count +=1 if total//k>= threshold else 0
                total = total - arr[L]
                L +=1
                
        return count
