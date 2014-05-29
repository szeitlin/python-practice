tabby_cat = "\tI'm tabbed in." #\t just means tab (indent)
persian_cat = "I'm split\non a line." #this include a newline call in the middle (I find it hard to read)
backslash_cat = "I'm \\ a \\ cat." #\\ lets you use the \ symbol (escapes the function call and uses it as a character in a string)

fat_cat = """
I'll do a list:
\t* Cat food #this just means tab and put an asterisk
\t* Fishies
\t* Catnip\n\t* Grass #this is just a smart-ass way of putting two things on one line, to show you can
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
