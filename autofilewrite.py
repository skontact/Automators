import os,numpy,sys
import errno, fileinput
pp = os.getcwd()

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
def writestuff(f,file,j):
	f.write("\nWriting in"+file+str(j)+"th file")
	for k in range(0,11):
		f.write("\n\t new line of words"+"line number:"+str(k))

def write_if_file_exists(file,more):
	for j in range(0,5):
		if os.path.isfile(file+str(j+1)+".doc")!=True:   
			print "Creating file in:"+file+str(j+1)+".doc to write first time or overwrite"
			f=open(file+str(j+1)+".doc",'w')
			writestuff(f,file,j)
		elif more=="Y":
			print "Opening file:"+file+str(j+1)+".doc to write more"
			f=open(file+str(j+1)+".doc",'a')
			writestuff(f,file,j)
		else:
			pass
def search_replace(file,word,new):
	if os.path.isfile(file):
	   for line in fileinput.input([file], inplace=True):
	   		line = line.replace(word,new)
	   		sys.stdout.write(line)

# Make new directory if does not exist
# Write more if you want or just enter to pass
for i in range(1,10):
	A = "mkfodder"+str(i)
	make_sure_path_exists(A)
	sys.path.append(A)
	#print sys.path
	Check = raw_input("Check more folders? Enter Y:")
	if Check=="Y":
		more=raw_input("Enter Y to write more:")
		write_if_file_exists(A+"/ex",more)
	else:
		print "Done..."
		break
# Enter folder name and file name

A = raw_input("Enter folder name: \n")
fn = raw_input("Enter file  Name: \t") 
# If you want multiple files you need a for loop
# Put this file in folder with those files
#  for i in range(5):
		# w = raw_input("What word?:")
		# n = raw_input("New word?:")
		# search_replace(A+"/"+fn+str(i),w,n)
		# File2conv = raw_input("Enter file to convert: ")
# search_replace(A+"/"+fn,w,n)
# Enter word to replace and new word
w = raw_input("What word?:")
n = raw_input("New word?:")
search_replace(A+"/"+fn,w,n)
# Replace to Specific Folder
# os.chdir(pp+"/mkfodder1")
# File2conv = raw_input("Enter file to convert: ")
# convert2pdf(File2conv)





	


