#plagiarism detector using python
from difflib import SequenceMatcher
with open('t1.txt') as one_file,open('t2.txt') as two_file:
    data_file1= one_file.read()
    data_file2= two_file.read()
    matches= SequenceMatcher(None,data_file1,data_file2).ratio()
    print("plagiarized content is :",matches)