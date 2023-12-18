import sys
import os

#get the number of arguments passed to the python script
def getargcount():
 return len(sys.argv)

# get details of arguments passed to script
def debug_getargdetails():

  # total arguments
  n = len(sys.argv)
  print("Total arguments passed:", n)
  
  # Arguments passed
  print("\nName of Python script:", sys.argv[0])
  
  print("\nArguments passed:", end = " ")
  for i in range(1, n):
    print(sys.argv[i], end = " ")

  print("\nthe number of args: " + str(getargcount()))


# read the file
def readfile(filename):
  filedata = open(filename,'r',encoding="utf8")
  return filedata

# read the file and return the lines of data in the file as a list
def readfilegetdata(filename):
  filedatastr = []
  try:
    # open the file
    #filedata = open(filename,'r')
    filedata = open(filename,'r',encoding="utf8")
    
    # get the lines of data
    filedatastr = filedata.readlines()
    filedata.close()
  except:
    print("\n Error occured during read file")
  #finally:
    #print("\n")

  return filedatastr

def readstreamorfileandgetdata(filename,mode):
  if mode=="file":
    return readfilegetdata(filename)
  elif mode=="stdin":
    return sys.stdin.readlines()

# get the file size
def getfilesize(filename,method):
  if method=="file":
    filedata = readfile(filename)
    # get the cursor positioned at end
    filedata.seek(0, os.SEEK_END)
    # get the current position of cursor
    return filedata.tell()
  elif method=="stdin":
    return len(sys.stdin.read())

# get the number of lines in the file
def getfilenolines(linesinfile):
  #linesinfile = readfilegetdata(filename)
  lines = len(linesinfile)
  # debug print("size of: " + str(sys.getsizeof(linesinfile)) + "\n")
  return lines

# get the number of words in the file
def getnumberofwords(linesinfile):
  #linesinfile = readfilegetdata(filename)
  numberoflines = len(linesinfile)
  numberofwords = 0
  for line in range(0, numberoflines-1):
    wordsinline = len(linesinfile[line].split())
    numberofwords = numberofwords + wordsinline

  return numberofwords

# get the number of char in the file
def getnumberofchar(linesinfile):
  #linesinfile = readfilegetdata(filename)
  numberoflines = len(linesinfile)
  numberofchar = 0
  for line in range(0, numberoflines-1):
    linedata = linesinfile[line]
    charsinline = len(linedata)
    numberofchar = numberofchar + charsinline

  return numberofchar
  
# return the 2nd arg that was passed to the script
def getarg2():
  return sys.argv[1]

# return the 3rd arg that was passed to the script
def getarg3():
   return sys.argv[2]

# process different functions of the script based on arg
def processarg():
  # set the output to blank for default
  opsmethod = ""
  # get the number of arguments passed to the script
  numberofargs = getargcount()
  
  # determine the operation based on the 2nd arg
  arg2 = getarg2()
  if arg2.startswith("-"):
    if arg2=="-c":
       opsmethod = "ops_filesize"
    elif arg2=="-l":
       opsmethod = "ops_linesinfile"
    elif arg2=="-w":
       opsmethod = "ops_wordsinfile"
    elif arg2=="-m":
       opsmethod = "ops_charsinfile"
  else:
    opsmethod = "ops_all"
  
  #determine the input type based on the 2nd arg/3rd arg - if 
  if numberofargs == 3:
    inputmethod = "input_file"
  elif numberofargs == 2:
    if arg2.startswith("-"):
      inputmethod = "stdin"
    else:
      inputmethod = "input_file"
  
  return inputmethod + "_" + opsmethod

# perform the operation based on argument
def performops(opsmethod):
  # set the output to blank for default
  output = ""
  method = ""
  filename = ""
  # based on the method determine if file or stdin and set it to a property
  # also determine where to get the filename from
  if opsmethod.startswith("input_file"):
    method = "file"
    if getargcount()==2:
      filename = getarg2()
    elif getargcount()==3:
      filename = getarg3()
  elif opsmethod.startswith("stdin"):
    method = "stdin"
  
  # peform the operation based on the ops method
  if opsmethod=="input_file_ops_all":
    output = str(getfilenolines(readstreamorfileandgetdata(filename,method))) + " "
    output = output + str(getnumberofwords(readstreamorfileandgetdata(filename,method))) + " "
    output = output + str(getfilesize(filename,method))
  elif opsmethod.endswith("ops_filesize"):
    output = getfilesize(filename,method)
  elif opsmethod.endswith("ops_linesinfile"):
    output = getfilenolines(readstreamorfileandgetdata(filename,method))
  elif opsmethod.endswith("ops_wordsinfile"):
    output = getnumberofwords(readstreamorfileandgetdata(filename,method))
  elif opsmethod.endswith("ops_charsinfile"):
    output = getnumberofchar(readstreamorfileandgetdata(filename,method))

  print(output, " ",filename)
  
# main method
def main():
  # debug get the argument details
  # debug_getargdetails()
  opsmethod = processarg()
  performops(opsmethod)
  

# call the main method to start execution of the script
main()