"""*************************************
Created By Vecsei Gabor
Blog: https://gaborvecsei.wordpress.com/
Email: vecseigabor.x@gmail.com
https://bitbucket.org/gaborvecsei/
*************************************"""

"""
Lists the most frequent words in a text file.
The words in the black list file don't count.

Run the program like this:
python Most_Frequent_Words.py <your_text_file> <your_black_list_file>
"""

import re
from collections import Counter
import sys

"""
Open the text files.
text.txt conatins the text where you would like
to count the word frequencies
blackList.txt contains the black listed words, we don't count them
"""
text = sys.argv[1]
blackList = sys.argv[2]
with open(text) as f:
    text = f.read()
with open(blackList) as f:
    blackList = f.read()

"""Find all of the words with a regular expression"""
blackListWords = re.findall(r'\w+', blackList)
words = re.findall(r'\w+', text)
"""We need only the first 20000 words"""
words = words[0:20000]
"""Change every word to upper case"""
capWords = [word.upper() for word in words]
capBlackListWords = [blword.upper() for blword in blackListWords]
"""
We don't need the words from the black list so we filter them out
http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
"""
capWords = [ w for w in capWords if w not in capBlackListWords ]
"""Count the actual presence"""
wordCounts = Counter(capWords)
"""
List the words to the console in key - value format
The Key is the word what occure once, the Value is the
number of occurrence

We will need only the top 100 words
"""
for key, value in wordCounts.most_common(100):
	print'\n'
	print key, value