def string_iter(str):
  """ Looks like they want you to return a string that contains each stem, i.e. 
  char 1, char12, char123.
  
  >>> string_iter('Code') 
  'CCoCodCode'

  had to test it to figure out the +1 was required, still kinda surprised it works.

"""
  
  newstring = ""
  
  for i in range(len(str)+1):
      for j in range(0,i):
          newstring+=str[j]

  return newstring 
