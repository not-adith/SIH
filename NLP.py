


import math
import nltk
import os
import sys,string
from nltk.stem import WordNetLemmatizer

def main(indata):
    """Calculate top TF-IDF for a corpus of documents."""

    
    corpus = load_data(indata)

    # Get all words in corpus
    print("Extracting words from corpus...")
    words = set()
    for filename in corpus:
        words.update(corpus[filename])

    # Calculate IDFs
    print("Calculating inverse document frequencies...")
    idfs = dict()
    for word in words:
        f = sum(word in corpus[filename] for filename in corpus)
        idf = math.log(len(corpus) / f)
        idfs[word] = idf

    # Calculate TF-IDFs
    print("Calculating term frequencies...")
    tfidfs = dict()
    for filename in corpus:
        tfidfs[filename] = []
        for word in corpus[filename]:
            tf = corpus[filename][word]
            tfidfs[filename].append((word, tf * idfs[word]))

    # Sort and get top 5 TF-IDFs for each file
    print("Computing top terms...")
    for filename in corpus:
        tfidfs[filename].sort(key=lambda tfidf: tfidf[1], reverse=True)
        tfidfs[filename] = tfidfs[filename][:5]

    # Print results
    outdict={}
    for filename in corpus:
        
        outlist = []
        for term, score in tfidfs[filename]:
            
            outlist.append((term,score))
        outdict[filename]= outlist
    return outdict


def load_data(directory):
    files = dict()
    wordnet_lemmatizer = WordNetLemmatizer()
    nltk.download('wordnet')
    for filename in directory:
        

        # Extract words
        
        contents = [
            word.lower() for word in
            nltk.word_tokenize(directory[filename]) #[filename]
            if word.isalpha()
        ]
        
        for word in contents:
            wordnet_lemmatizer.lemmatize(word)

        

        # Count frequencies
        frequencies = dict()
        for word in contents:
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
        files[filename] = frequencies

    return files




if __name__ == "__main__":
     
    main(sys.argv[1])