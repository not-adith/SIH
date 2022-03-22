
from lib2to3.pgen2.token import EQUAL
from msilib.schema import File
import sys
import os,string, math, nltk, csv
from tkinter.filedialog import Directory

#print("jai shree ramm")

# fuctions available 
# load file (file)
# tokenization(document)
# compute_idfs(document)

def load_Text(directory,file):
    dict ={}
    with open(os.path.join(directory,file),encoding="utf-8") as f:
            text= f.read()
            dict[f]= text 
    return dict




def load_Webpage(resource_url):
    dict={}
    # we can save the file with differnt name which would be meaningfull so that that can be directly given to blockchain
    dict[resource_url]=nltk.data.retrieve(resource_url, filename=None, verbose=True)
    return dict



def tokenize(document):
    a= nltk.tokenize.word_tokenize(document)
    for words in range(len(a)) :
        a[words]=a[words].lower()
         
    a = [x for x in a if x not in string.punctuation and x not in nltk.corpus.stopwords.words("english")]

    return a
    

def compute_idfs(documents):
    IDF = {}
    num_of_doc = len(documents)
    all_words= []
    for value in documents.values():
        for word in value:
            if word not in all_words:
                all_words.append(word) 
    
    for words in all_words:
        f = sum(words in documents[filename] for filename in documents)
        idf = math.log(num_of_doc / f)
        IDF[words] = idf
    return IDF





def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: py NLP.py dataset_type data_set.")
    data_type=sys.argv[1]
    print("Loading data...")
    if data_type == 'T':
        corpus = load_Text(sys.argv[2])
    elif data_type == 'W':
        corpus = load_Webpage(sys.argv[2])
    else:
        sys.exit("Data set type invalid.")
    
    print("Extracting words from corpus...")
    #getting the words in the corpus
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
    
    print("Calculating term frequencies...")
    tfidfs = dict()
    for filename in corpus:
        tfidfs[filename] = []
        for word in corpus[filename]:
            tf = corpus[filename][word]
            tfidfs[filename].append((word, tf * idfs[word]))
    
    print("Computing top terms...")
    for filename in corpus:
        tfidfs[filename].sort(key=lambda tfidf: tfidf[1], reverse=True)
        tfidfs[filename] = tfidfs[filename][:5]
    
    # saving and showing output
    filename= "out.csv"
    with open(filename,'w' ) as csvfile:
        csvwriter= csv.DictWriter(csvfile,fieldnames={'Filename','Term','Score'}) 
        csvdict={} 
        for filename in corpus:
            for term, score in tfidfs[filename]:
                print(f"    {term}: {score:.4f}")
                csvdict[filename][term]=score
        csvwriter.writeheader()
        csvwriter.writerows(csvdict)
    csvfile.close()

if __name__ == "__main__":
    main()