# uniteAllTextFilesInOne
This script unites all the text files in a directory an join them in one file, puting a new line for each file added

This script must be placed at the same directory with all files you want to join
and it will generate a new file called 'uniqueFile.txt' (with all the files of the directory inside)

Example:

File1.txt
'Content 1'

File2.txt
'Content 2'

File3.txt
'Content 3'

After run, the script will make a new text file:

uniqueFile.txt

'Content 1

 Content 2
 
 Content 3'

OBSERVATIONS:
#Tested at Windows (Python 3.11.2) and Xubuntu (Python 3)
In Windows, the script is writing the files in alphanumeri order (according the file name), but in Linux is writing in reverse order
