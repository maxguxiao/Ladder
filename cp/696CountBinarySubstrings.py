"""Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""
#O(N^2)
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
        	return 0
        else:
        	o = self.findAllSubStr(s)
        	return o
        
    def check(self, s):
        strlist = [int(x) for x in s]
        n = len(strlist)
        first_half = strlist[:(n/2)]
        second_half = strlist[(n/2):]
        if n % 2 == 0:
            if (sum(first_half) == 0 and sum(second_half) == n/2) or (sum(first_half) == n/2 and sum(second_half) == 0):
                return 1
            else:
                return 0
        else:
            return 0
    
    def findAllSubStr(self, s):
    	"""
    	:type s: str
    	:rtype: list[str]
    	"""
    	return sum([self.check(s[i:j]) for i in range(len(s)) for j in range(i+1,len(s)+1,1)])


#O(N)
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        o = []
        count = 1
        for i in range(len(s)-1):
            if s[i+1] != s[i]:
                o.append(count)
                count = 1
            else:
                count += 1
        o.append(count)
        return sum([min(o[i],o[i+1]) for i in range(len(o)-1)])



#O(N)
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 0
        count = 1
        out = 0
        for i in range(len(s)-1):
            if s[i+1] != s[i]:
                if prev > 0:
                    out += min(count, prev)
                    prev = count
                    count = 1
                else:
                    prev = count
                    count = 1
            else:
                count += 1
        out += min(count, prev)
        return out