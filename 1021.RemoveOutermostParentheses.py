class Solution:
    def removeOuterParentheses(self, S):
        complete_pairs = self.getCompletePairs(list(S))

        output = ""
        for pair in complete_pairs:
            output += "".join(pair[1:-1])
        return output

    def getCompletePairs(self ,arr):
        _stack = []
        pairs = []
        counter = 0

        for p in arr:
            _stack.append(p)
            if p == "(":
                counter +=1
            elif p == ")":
                counter -=1
                if counter == 0:
                    pairs.append(_stack)
                    _stack = []
        return pairs


s = Solution()

print (s.removeOuterParentheses("(()())(())"))


"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and Bare valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:
Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 
Note:
	1. S.length <= 10000
	2. S[i] is "(" or ")"
	3. S is a valid parentheses string
"""
