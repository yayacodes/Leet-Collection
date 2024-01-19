class Strings(object):


        def reverseString(self, s):
                """
                :type s: List[str]
                :rtype: None Do not return anything, modify s in-place instead.
                """
        #         i = 0
        #         j = len(s) - 1
                
        #         while i < j:
        #             temp = s[i]
        #             s[i] = s[j]
        #             s[j] = temp
        #             i+=1
        #             j-=1
                
                rev_string = s.reverse()


        def firstUniqChar(self, s):
                """
                :type s: str
                :rtype: int
                """
                char_count = {}
                for c in s:
                        if c in char_count:
                                char_count[c] += 1
                        else:
                                char_count[c] = 1
                for index in range(len(s)):
                        if char_count[s[index]] == 1:
                                return index
                return -1



if __name__ == '__main__':
    strs = Strings()
    print(strs.firstUniqChar("loveleetcode"))