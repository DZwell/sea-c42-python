# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number different nucleotides seen so far.
gc_count = 0
at_count = 0
c_count = 0
g_count = 0
a_count = 0
t_count = 0



# Category of organism
category = ""

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if (bp == 'C'):
        gc_count = gc_count + 1
        c_count = c_count + 1

    elif (bp == 'G'):
        # increment the count of gc
        gc_count = gc_count + 1
        g_count = g_count + 1

    elif (bp == 'A'):
        at_count = at_count + 1
        a_count = a_count + 1

    elif (bp == 'T'):
        at_count = at_count + 1
        t_count = t_count + 1

    elif (bp != 'A' or 'C' or 'G' or 'T'):
        total_count = total_count - 1





# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count
at_gc_ratio = float(a_count + t_count) / float(g_count + c_count)



# Categorizes organisms
if (gc_content > float(.6)):
    category = "high GC content"
elif (gc_content < float(.4)):
    category = "low GC content"
elif (gc_content < float(.6) and gc_content > float(.4)):
    category = "moderate GC content"

# Print the answer
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('A-content:', a_count)
print('T-content:', t_count)
print('G-content:', g_count)
print('C-content:', c_count)
print('Sum Count:', a_count + t_count + g_count + c_count)
print('Total Count:', total_count)
print ("Sequence Length:", len(seq))
print("AT/GC Ratio:", at_gc_ratio)
print("Sequence Length:", len(seq))
print("AT/GC Ratio:", at_gc_ratio)
print("GC Classifcation = ", category)

