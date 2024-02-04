class ProductOfArrayExceptSelf:

    def __init__(self) -> None:
        pass


    def productExceptSelf(self, nums: list[int]) -> list[int]:
        num_len = len(nums)
        prefix = [0] * num_len
        postfix = [0] * num_len

        i = 0
        while i < num_len:
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]
            i += 1
        
        j = num_len - 1

        while j >= 0:
            if j == num_len - 1:
                postfix[j] = nums[j]
            else:
                postfix[j] = postfix[j + 1] * nums[j]
            
            j -= 1

        k = 0
        while k < num_len:
            if k == 0:
                nums[k] = postfix[k + 1]
            elif k == num_len - 1:
                nums[k] = prefix[k - 1]
            else:
                nums[k] = prefix[k - 1] * postfix[k + 1]
            
            k += 1

        return nums

    def productExceptSelf_optimize_space(self, nums: list[int]) -> list[int]:
        nums_len = len(nums)
        result = [0] * nums_len

        i = 0

        prefix = 1
        while i < nums_len:
            result[i] = prefix
            prefix = nums[i] * prefix 
            i += 1

        postfix = 1
        j = nums_len - 1
        while j >= 0:
            result[j] = postfix * result[j]
            postfix = postfix * nums[j]
            j -= 1

        return result
    
    def product_except_self_neetcode_2nd(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        
        prefix = 1
        i = 0
        while i < len(nums):
            ans[i] = prefix
            prefix = prefix * nums[i]
            i += 1
            
        j = len(nums) - 1
        postfix = 1
        while j >= 0:
            ans[j] = postfix * ans[j]
            postfix = postfix * nums[j]
            j -= 1
            
        return ans

def main():
    solution = ProductOfArrayExceptSelf()
    print(solution.productExceptSelf([1,2,3,4]))
    print(solution.productExceptSelf_optimize_space([1,2,3,4]))

main()