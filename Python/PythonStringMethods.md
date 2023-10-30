Python's built-in String Manipulation methods : 

<str>.capitalize()
Returns a copy of the string <str> with its first character capitalized.

<str>.find(sub[,start[,end]]) 
Returns the lowest index in the string <str> where the substring sub is found within the slice range of start and end. Returns -1 if sub is not found.

<str>.isalnum()
Returns True if the characters in the string <str> are alphanumeric (alphabets or numbers) and there is at least one character, False otherwise.

<str.isalpha()
Returns True if all characters in the string <str> are alphabetic and there is at least one character, False otherwise.

<str.isdigit()
Returns True if all characters in the string <str> are digit. There must be at least one digit, otherwise it returns False.

<str>.isspace()
Returns True if there are only whitespaces characters in the strings <str>. There must be at least one character. It returns False otherwise.

<str>.islower()
Returns True if all cased characters in the string <str> are lowercase. There must be at least one cased character, otherwise it returns False.

<str>.isupper()
Tests wheather all cased characters in the string <str> are uppercase and requires that there be at least onr cased character. Returns True if so and False otherwise.

<str>.istitle()
Returns True if the string <str> is in title case. Title case is any text with most of the first letters of each word capitalised e.g., "I Love Coding" string <str> is in title case.

<str>.lower()
Returns a copy of the string <str> converted to lowercase.

<str>.upper()
Returns a copy of the string <str> converted to uppercase.

<str>.title()
Returns a titlecased version of the string <str> where words start with an uppercase character and remaining characters are lowercase.

<str>.startswith(prefix[,start[,end]]) 
Returns True if the string <str> starts with an argument prefix, otherwise return False.

<str>.endswith(suffix[,start[,end]]) 
Returns True if the string <str> ends with an argument prefix, otherwise return False.

<str>.swapcase()
Returns a copy of the string <str> with uppercase characters converted to lowercase and vice-versa.

<str>.partition(sep)
Splits the string <str> at the first occurence occurence of argument sep, and returns a 3-tuple containing the part before the separater, the separater itself, and the part after the separator.
If the separator is not found, it returns a 3-tuple containing the string itself, followed by two empty string

<str>.count(sub[,start[,end]])
Returns the number of non-overlapping occurences of substring sub in the range [start,end] of the given string <str>. The start and end are optional arguments and if not given , the whole string is considered for finding and counting the given substring sub.

<str>.lstrip([chars])
Returns a copy of the string <str> with leading characters removed. If used without any argument, it removes the leading whitespaces.

<str>.rstrip([chars])
Returns a copy of the string <str> with trailing characters removed. If used without any argument, it removes the leading whitespaces.

