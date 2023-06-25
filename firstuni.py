def firstUniqueChar(s):
    char_count={}
    ## count the occurrences of each character in the string
    for char in s:
        char_count[char]=char_count.get(char,0)+1
        for i in range(len(s)):
            if char_count[s[i]]==1:
                return i
            return -1