class GroupAnagrams:

    def __init__(self) -> None:
        pass

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

        for key, value in main_dict.items():
            results.append(value)

        return results

def main():
    solution = GroupAnagrams()

    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

main()