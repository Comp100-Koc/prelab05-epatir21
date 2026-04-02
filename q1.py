def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    
    longest_palindrom=''
    palindrom_word=''
    
    if len(s)<2:
        return ''
    
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
        
            if s[i:j]==s[i:j][::-1]:
                palindrom_word=s[i:j]
                if len(palindrom_word)>len(longest_palindrom):
                    longest_palindrom=palindrom_word
    
    if len(longest_palindrom)>=2:
       return longest_palindrom
   
    else:
        return ''
    
    
    
print(longest_palindromic_substring("baabaad"))
   
    
    