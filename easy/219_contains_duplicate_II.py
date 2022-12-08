class ContainDuplicatesII:

    def __init__(self) -> None:
        pass

    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        i = 0
        count_dict = dict()
        while i < len(nums):
            if nums[i] in count_dict:

                if abs(count_dict[nums[i]] - i) <= k:
                    return True
            
            count_dict[nums[i]] = i

            i += 1

        
        return False
            