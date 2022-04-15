**String methods:**  

**capitalize()** Converts the first character to upper case  
**casefold()** Converts string into lower case  
**center()** Returns a centered string  
**count()** Returns the number of times a specified value occurs in a string  
**encode()** Returns an encoded version of the string  
**endswith(**) Returns true if the string ends with the specified value  
**expandtabs()** Sets the tab size of the string  
**find()** Searches the string for a specified value and returns the position of where it was found  
**format()** Formats specified values in a string  
**format_map()** Formats specified values in a string  
**index()** Searches the string for a specified value and returns the position of where it was found  
**isalnum()** Returns True if all characters in the string are alphanumeric  
**isalpha()** Returns True if all characters in the string are in the alphabet   
**isascii()** Returns True if all characters in the string are ascii characters  
**isdecimal()** Returns True if all characters in the string are decimals  
**isdigit()** Returns True if all characters in the string are digits  
**isidentifier()** Returns True if the string is an identifier  
**islower()** Returns True if all characters in the string are lower case  
**isnumeric()** Returns True if all characters in the string are numeric  
**isprintable()** Returns True if all characters in the string are printable  
**isspace()** Returns True if all characters in the string are whitespaces  
**istitle()** Returns True if the string follows the rules of a title  
**isupper()** Returns True if all characters in the string are upper case  
**join()** Converts the elements of an iterable into a string  
**ljust()** Returns a left justified version of the string  
**lower()** Converts a string into lower case  
**lstrip()** Returns a left trim version of the string  
**maketrans()** Returns a translation table to be used in translations  
**partition()** Returns a tuple where the string is parted into three parts  
**replace()** Returns a string where a specified value is replaced with a specified value  
**rfind()**	 Searches the string for a specified value and returns the last position of where it was found  
**rindex()** Searches the string for a specified value and returns the last position of where it was found  
**rjust()** Returns a right justified version of the string  
**rpartition()** Returns a tuple where the string is parted into three parts  
**rsplit()** Splits the string at the specified separator, and returns a list  
**rstrip()** Returns a right trim version of the string  
**split()** Splits the string at the specified separator, and returns a list  
**splitlines()** Splits the string at line breaks and returns a list  
**startswith()** Returns true if the string starts with the specified value  
**strip()** Returns a trimmed version of the string  
**swapcase()** Swaps cases, lower case becomes upper case and vice versa  
**title()** Converts the first character of each word to upper case  
**translate()** Returns a translated string  
**upper()** Converts a string into upper case  
**zfill()** Fills the string with a specified number of 0 values at the beginning  

**Handy built-in functions**  
When you don’t need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the repr() or str() functions. 
* The str() function is meant to return representations of values which are fairly human-readable, while repr() is meant to generate representations which can be read by the interpreter.
* You also have format(). The format() method formats the specified value(s) and insert them inside the string’s placeholder {}.
```python
x=20 
y=400
repr((x, y, ('spam', 'eggs')))
str((x, y, ('spam', 'eggs')))           
 
 print('{0} and {1}'.format('spam', 'eggs'))   
 print('{1} and {0}'.format('‘spam’', '‘eggs’'))
```