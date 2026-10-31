# file handling
# file handling allows python to read,write,create and delete files

# file modes
# mode  meaning         If file doesn't exist       existing content
#  "r"  Read(default)       FileNotFoundError               kept
#  "w"  write               creates it                      Erased
#  "a"  append(add to end)  creates it                      kept(adds at end)                          
#  "x"  create only         creates it                      Error if file Exists
#  "r+" Read and write      Error                           kept

# add b for binary files(images,pdfs): "rb","wb"
# w wipes the file the moment you opens it
# tell : to say cursor at which position i.e character
# seek : to bring cursor to the position we need
# cursor position is very important
# eof means end of the file
# always use "with" statements for automatic file closure
# close files properly if not using "with"
# if text files has emojis or special characters add (encoding=utf-8)
# "t"-since text mode is default we don't mention it as 'rt','wt','at'
