class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        shift_counts = collections.Counter()
        for start, end, right in shifts:
            shift_counts[start] += 1 if right else -1 
            if end + 1 < n:                          
                shift_counts[end + 1] += -1 if right else 1
                
        prefix_sum = [0]                             
        shifted_string = ''
        for i in range(n):                         
            cur_shift = prefix_sum[-1] + shift_counts[i]
            prefix_sum.append(cur_shift)
            shifted_char = chr((ord(s[i]) - ord('a') + cur_shift) % 26 + ord('a'))
            shifted_string += shifted_char
        return shifted_string
      
        