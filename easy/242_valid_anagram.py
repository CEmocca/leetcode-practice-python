class ValidAnagram:

    def __init__(self):
        pass

    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = dict()

        if len(s) != len(t):
            return False

        i = 0
        while i < len(s):
            if s[i] in anagram_dict:
                anagram_dict[s[i]] = anagram_dict[s[i]] + 1
            else:
                anagram_dict[s[i]] = 1
            i += 1

        j = 0
        while j < len(s):
            if t[j] in anagram_dict:
                anagram_dict[t[j]] = anagram_dict[t[j]] - 1

            j += 1

        for _, value in anagram_dict.items():
            if value > 0:
                return False

        return True