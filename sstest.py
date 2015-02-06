import glob, sys
import fnmatch

filenames= sorted(glob.glob('*.txt'))
with open('TESTINGFILE', 'w', errors='ignore') as outfile:
    for fname in filenames:
        with open(fname, 'r', errors='ignore') as infile:
            for line in infile:
                for word in line.split():
                    outfile.write(word)
                    outfile.write(' ')
            outfile.write('\n')    
              
              
          
