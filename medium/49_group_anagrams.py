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
    
    def group_anagrams_neetcode_2nd(self, strs: list[str]) -> list[list[str]]:

        groups = {}
            
        for word in strs:
            char_occupy = [0] * 26  # array to keep number of each chars between A-Z [0-25]
            for char in word:
                to_index = ord(char) - 97 # 97 is ASCII code of A
                char_occupy[to_index] = char_occupy[to_index] + 1

            key = ""
            for i, num in enumerate(char_occupy):
                if num == 0:
                    continue
                key += f'{chr(i + 97)}{num}'

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]


        ans = []
        for _, values in groups.items():
            ans.append(values)

        return ans

                


def main():
    solution = GroupAnagrams()

    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(solution.groupAnagrams_optimize(["eat","tea","tan","ate","nat","bat"]))
    print(solution.group_anagrams_neetcode_2nd(["eat","tea","tan","ate","nat","bat"]))

main()