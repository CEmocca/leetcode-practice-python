class GroupAnagrams:

    def __init__(self) -> None:
        pass

    # Time compelxity = O for loop through all list
    # and n log n for sorted string
    # total = O(m * nlogn)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return []

        main_dict = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in main_dict:
                main_dict[sorted_word].append(word)

            else:
                main_dict[sorted_word] = [word]

        results = []

        for _, value in main_dict.items():
            results.append(value)

        return results

    def groupAnagrams_optimize(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return []

        count_dict = dict()

        for word in strs:
            count_char = [0] * 26
            for char in word:
                ascii = ord(char) - ord('a')
                count_char[ascii] = count_char[ascii] + 1

            new_key = tuple(count_char)
            if new_key in count_dict:
                count_dict[new_key].append(word)
            else:
                count_dict[new_key] = [word]

        result = []

        for _, value in count_dict.items():
            result.append(value)
        return result

                


def main():
    solution = GroupAnagrams()

    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(solution.groupAnagrams_optimize(["eat","tea","tan","ate","nat","bat"]))

main()