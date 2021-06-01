class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenth = 1
        if len(s) <= 1:
            return len(s)
        # # 这句没有用
        # elif len(s)>5*10**4:
        #     return False
        else:
            for i in range(len(s)):
                for j in range(len(s) - 1, i, -1):
                    s1 = s[i:j + 1]
                    p = True
                    for k in s1:
                        if s1.count(k) > 1:
                            p = False
                            break
                    if p == True:
                        index = j
                        break
                    else:
                        index = i

                if index - i + 1 > lenth:
                    lenth = index - i + 1
                if lenth >= len(s) - i:
                    break
            return lenth


def main():
    s = ""
    print(Solution().lengthOfLongestSubstring(s))
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
