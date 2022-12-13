class ContainDuplicates:

    def __init__(self) -> None:
        pass

    def containsDuplicate(self, nums: list[int]) -> bool:
        count_dict = dict()

        i = 0
        while i < len(nums):
            cur = nums[i]

            if cur in count_dict:
                count_dict[cur] = count_dict[cur] + 1
            else:
                count_dict[cur] = 1
            
            i += 1

        
        for key, value in count_dict.items():
            if value > 1:
                return True

        return False

    def containsDuplicate_break_loop(self, nums: list[int]) -> bool:
        count_dict = dict()

        i = 0
        ret = False
        while i < len(nums):
            cur = nums[i]

            if cur in count_dict:
                ret = True
                break
            else:
                count_dict[cur] = 1
            
            i += 1

    

        return ret