import glob, sys
import fnmatch

filenames= sorted(glob.glob('*.txt'))
with open('TRAININGFILE', 'w', errors='ignore') as outfile:
    for fname in filenames:
      with open(fname, 'r', errors='ignore') as infile:
         
            if fnmatch.fnmatch(fname, '*HAM.*'):
              
               outfile.write('HAM ')
               for line in infile:
                   for word in line.split():
                       outfile.write(word)
                       outfile.write(' ')
               outfile.write('\n')
              
            elif fnmatch. fnmatch(fname, '*SPAM.*'):
               outfile.write('SPAM ')
               
               for line in infile:
                   for word in line.split():
                       outfile.write(word)
                       outfile.write(' ')
               outfile.write('\n')

            elif fnmatch. fnmatch(fname, '*POS.*'):
               outfile.write('POS ')
               
               for line in infile:
                   for word in line.split():
                       outfile.write(word)
                       outfile.write(' ')
               outfile.write('\n')
         
            elif fnmatch. fnmatch(fname, '*NEG.*'):
               outfile.write('NEG ')
               
               for line in infile:
                   for word in line.split():
                       outfile.write(word)
                       outfile.write(' ')
               outfile.write('\n')
