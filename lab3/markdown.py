"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
 4. convert single hashtag to h1 tags
 5. convert double hashtag to h2 tags
 6. convert triple hashtag to h3 tags
 7. convert bq tags
"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  line = re.sub(r'# (.*)', r'<h1>\1</h1>', line)
  return line

def convertH2(line):
  line = re.sub(r'## (.*)', r'<h2>\1</h2>', line)
  return line

def convertH3(line):
  line = re.sub(r'### (.*)', r'<h3>\1</h3>', line)
  return line

def convertbq(line, mode):
  if line[0] == '>':
    if mode == False:
      return '<blockquote>'+line[1:]
      
    else:
      return line[1:]
      
  else:
    if mode == True:
      return '</blockquote>'+line
      
    else:
      return line

bqmode = False
for line in fileinput.input():
  line = line.rstrip() 
  line = convertStrong(line)
  line = convertEm(line)
  line = convertH3(line)
  line = convertH2(line)
  line = convertH1(line)
  line = convertbq(line,bqmode)
  print '<p>' + line + '</p>',
