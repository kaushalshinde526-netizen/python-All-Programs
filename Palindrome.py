def is_palindrome(s):
    s= s.lower()  # Convert to lowercase    
    left,right=0,len(s)-1  # Initialize pointers
    while left<right:
        if s[left]!=s[right]:  # Compare characters
            return False  # Not a palindrome
        left+=1  # Move left pointer right
        right-=1  # Move right pointer left
    return True
print(is_palindrome("madam"))  # True