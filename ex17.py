from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do this on one line, how?
#in_file = open(from_file)
indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
#from_file.close()