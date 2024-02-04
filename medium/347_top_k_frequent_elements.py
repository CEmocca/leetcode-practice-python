class TopKFrequentElelments:

    def __init__(self) -> None:
        pass

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count_dict = dict()

        for num in nums:
            if num in count_dict:
                count_dict[num] = count_dict[num] + 1

            else:
                count_dict[num] = 1

        result = []

        if len(count_dict) <= k:
            return count_dict.keys()

        for key, _ in sorted(count_dict.items(), key = lambda item: item[1], reverse= True):
            if len(result) < k:
                result.append(key)
            else:
                break

        return result
    
    def top_k_frequent_neetcode_2nd(self, nums: list[int], k: int) -> list[int]:
        have_seen = {}
        
        for num in nums:
            if num in have_seen:
                have_seen[num] = have_seen[num] + 1
            else:
                have_seen[num] = 1
                
        ans = []
        for key, value in have_seen.items():
            ans.append((value, key))
            
        return map(lambda x: x[1], sorted(ans, reverse=True)[:k])

def main():
    solution = TopKFrequentElelments()
    print(solution.topKFrequent([3,0,1,0], 1))

main()