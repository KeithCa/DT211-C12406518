def palindrome(num):
    if num[::-1] == num:
       return True
    else:
       return False
print palindrome('please')