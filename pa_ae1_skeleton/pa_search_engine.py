# -*- coding: utf-8 -*-

"""
Module: 
pa_search_engine

About:
Implements functions used by a directory search engine

SOME FUNCTIONS OR THEIR SKELETONS HAVE BEEN PROVIDED
HOWEVER, YOU ARE FREE TO MAKE ANY CHANGES YOU WANT IN THIS FILE
AS LONG AS IT REMAINS COMPATIBLE WITH main.py and tester.py
"""

#%% ---------------------------------------------------------------------------
# Required Imports
#------------------------------------------------------------------------------
import string
from timeit import default_timer as timer
import os

#%%----------------------------------------------------------------------------
def dict_to_file(di, fi):
    with open(fi, "w") as f:
        for key, value in di.items():
            f.write("%s:%s\n" % (key, value))

#%%----------------------------------------------------------------------------
def print_result(result):
    """
    Print result (all docs with non-zero weights)
    """
    print("# Search Results:")
    count = 0
    for val in result: 
        if val[1] > 0: 
            print(val[0])
            count += 1
    print(count, " results returned")

#%%----------------------------------------------------------------------------
def crawl_folder(folder
                ,forward_index
                ,invert_index
                ,term_freq
                ,inv_doc_freq
                ,doc_rank
                ):
    """"
    Crawls a given folder, and runs the indexer on each file
    """
    
    total_docs = 0
    for file in os.scandir(folder):
        if file.is_file():
            total_docs += 1
            index_file(file.name, file.path, forward_index, invert_index, term_freq, doc_rank)

    # with invert_index calculated, we can calculate the inv_doc_freq of each unique word
    # where inv_doc_freq = number of documents with the word / total number of documents
    for word in invert_index.keys():
        inv_doc_freq[word] = len(invert_index[word])/total_docs
        
#%%----------------------------------------------------------------------------
def sanitize_word(word):
    """
    Removes all non ascii characters from a given word 
    ^ does this mean remove all non-ascii characters from a word or only keep alphanumeric characters?
    """    
    new_word = ''
    word = word.lower()
    new_word = ''.join(filter(str.isalnum, word))

    return(new_word)

#%%----------------------------------------------------------------------------
def parse_line(line):
    """    
    Parses a given line, 
    removes whitespaces, splits into list of sanitize words
    Uses sanitize_word()
    
    HINT: Consider using the "strip()" and "split()" function here
    
    """    
    list_of_words = []
    for word in line.strip().split():
        sanitized_word = sanitize_word(word)
        if sanitized_word and sanitized_word != '':
            list_of_words.append(sanitized_word)   
    return(list_of_words)

#%%----------------------------------------------------------------------------
def extract_file_lines(filepath):
    lines = []
    with open(filepath, 'r', encoding="utf-8") as f:
        for line in f:
            sanitized_line = parse_line(line)
            if sanitized_line: #check if the line is not empty
                for word in sanitized_line:
                    lines.append(word)
                #lines.append(sanitized_line)
    return(lines)

#%%----------------------------------------------------------------------------
def invert_index_to_file(word, filename, invert_index):
    if word not in invert_index:
            invert_index[word] = []
    if filename not in invert_index[word]:
        invert_index[word].append(filename) # can maybe clean this up

#%%----------------------------------------------------------------------------
def term_freq_to_file(word, individual_word_count):
    
        if word in individual_word_count:
            individual_word_count[word] += 1
        else:
            individual_word_count[word] = 1
        

#%%----------------------------------------------------------------------------

def index_file  (filename
                ,filepath
                ,forward_index
                ,invert_index
                ,term_freq
                ,doc_rank
                ):
    """    
    Given a file, index it by calculating its:
        forward_index
        term_freq
        doc_rank
        and update the invert_index (which is calculated across all files)

        the parameters forward_index, invert_index, term_freq, doc_rank are all dictionaries to be populated 
    """ 
    start = timer()
    file_words = extract_file_lines(filepath) #might want to change the name of this function as it extracts words not lines
   
    forward_index[filename] = file_words
    doc_rank[filename] = 1 / len(file_words)


    term_freq[filename] = {}
    individual_word_count = {}
    for word in file_words:
        invert_index_to_file(word, filename, invert_index) 
        
        term_freq_to_file(word, individual_word_count)
        term_freq[filename][word] = individual_word_count[word] / len(file_words)

    
    end = timer()
    print("Time taken to index file: ", filename, " = ", end-start)
    return filename, filepath, forward_index, invert_index, term_freq ,doc_rank
    
    #print(f"Invert Index {filename}: ", invert_index)
    #print("Term Frequency" , term_freq)
    #print(individual_word_count)
    #print(len(file_words))

#%%----------------------------------------------------------------------------

def search  (search_phrase
             ,forward_index
             ,invert_index
             ,term_freq
             ,inv_doc_freq
             ,doc_rank    
             ):
    """    
    For every document, you can take the product of TF and IDF 
    for term of the query, and calculate their cumulative product. 
    Then you multiply this value with that documents document-rank 
    to arrive at a final weight for a given query, for every document. 
    """
    
    query_words = parse_line(search_phrase)
    result = {}
    for filename in forward_index.keys():
        result[filename] = 0
        for word in query_words:
            result[filename] += term_freq[filename][word] * inv_doc_freq[word]
        
        result[filename] *= doc_rank[filename]
    
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    # this will return a list of tuples, with the first element being the filename and the second element being the weight
    # the lambda function sorts the list of tuples by the second element in the tuple, which is the weight
    # the reverse=True argument sorts the list in descending order
      

    return(sorted_result)