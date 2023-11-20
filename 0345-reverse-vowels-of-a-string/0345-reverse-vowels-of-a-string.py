class Solution(object):
    def reverseVowels(self, s):
        answer = list(s) # n
        vowels = [] #n
        idxs = [] #n

        for i in range(len(s)): #n
            if s[i].lower() in 'aeiou':
                vowels.append(s[i])
                idxs.append(i)

        p1 = len(vowels) - 1
        p2 = 0

        while p2 < len(idxs) and p1 >= 0: #n
            answer[idxs[p2]] = vowels[p1]
            p1 -= 1
            p2 += 1

        return ''.join(answer) #n
        