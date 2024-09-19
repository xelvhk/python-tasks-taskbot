check_str = input ("Enter the string to check if it is a palindrome: ")
check_str = check_str.casefold ()
rev_str = reversed (check_str)
if list (check_str) == list (rev_str):
    print ("The string is a palindrome.")
else:
    print ("The string is not a palindrome.")
