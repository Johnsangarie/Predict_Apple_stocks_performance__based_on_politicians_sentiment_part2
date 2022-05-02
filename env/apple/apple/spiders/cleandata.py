import pandas as pd   # give us access to panda
import spacy          # give us access to spacy library

import csv             # give us full access to working with csv files








nlp = spacy.load('en_core_web_lg')    # load the large model of BERT

def load_file(path):
  '''this function enables us to read our corpus which is a csv file and remove all empty rows'''
  data = pd.read_csv(path, encoding='utf-8')       #read the csv file
  data.dropna(how = "all", inplace = True)
  return data                                      # return the text
file_path ="C:\\Users\\sangariej\\Desktop\\projectone1\\env\\apple\\corpus.csv"

df = load_file(file_path)
df.columns
text = df.Text                        # focus on the texts in the file.

remove_empty_cols= text.dropna()       # remove all empty rows










#text = df.Text
apple_sen = []                         #create an empty list
for i in remove_empty_cols:              # form a for loop
    if "stocks"  in i :                 # check if colums contains the word stock
      apple_sen.append(i)               # append only colums with stocks keyword on them because we already know the data has apple on them.













def seperate_punc(apple_sen):
  '''This function enables us to tokenize the strings and remove extrenous characters'''
  return [ token.text.lower() for  token in nlp(apple_sen)       # tokenize string
  if token.text not in '()/-,{}~\n \xa0 \u2009 \u2032 \u2032']    #remove non needed characters

clean_text = [' '.join(seperate_punc(i)) for i in apple_sen]       # put result in a list


string_clean_textt= ' '.join([str(item) for item in clean_text])   # convert back to string for writing in a new file call readme.txt




with open('C:\\Users\\sangariej\\Desktop\\projectone1\\readme.txt', 'w', encoding="utf-8") as f: # open the file
  f.write(string_clean_textt)    # write on the file







