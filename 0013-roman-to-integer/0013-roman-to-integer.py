class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

        answer = roman_dict[s[-1]]
        size = len(s) - 2
        while size >= 0 :
            if roman_dict[s[size]] < roman_dict[s[size+1]]:
                answer -= roman_dict[s[size]]
            else:
                answer += roman_dict[s[size]]
            size -=1
        return answer