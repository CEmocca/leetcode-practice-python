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

def main():
    solution = TopKFrequentElelments()
    print(solution.topKFrequent([3,0,1,0], 1))

main()