class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        final_list = []
        num1_ptr = 0
        num2_ptr = 0
        for _ in range(m+n):
            if num1_ptr >= m:
                break
            elif num2_ptr >= n:
                break
            elif(nums1[num1_ptr] <= nums2[num2_ptr]):
                print("nums1[num1_ptr] <= nums2[num2_ptr]")
                final_list.append(nums1[num1_ptr])
                num1_ptr += 1
            else:
                final_list.append(nums2[num2_ptr])
                print("nums1[num1_ptr] <= nums2[num2_ptr] except condition")
                num2_ptr += 1
        if num1_ptr < m:
            print("came here at numptr1 = ", num1_ptr)
            final_list = final_list + nums1[num1_ptr:m]
        else:
            print("came here at numptr2 = ", num2_ptr)
            final_list = final_list + nums2[num2_ptr:n]
        if (m+n)%2 == 0:
            return (final_list[int((m+n)/2) - 1] + final_list[int((m+n)/2)])/2
        else:
            return final_list[int((m+n+1)/2) - 1]

new_ques = Solution
m = new_ques.findMedianSortedArrays(new_ques,[1,2],[3,4])
print(m)

# [1,2,3,4,6,8]