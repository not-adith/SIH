
from asyncio.windows_events import NULL
from lib2to3.pgen2.token import EQUAL
from msilib.schema import File
import sys
import os,string, math, nltk, csv
from tkinter.filedialog import Directory
import string
from tensorflow.keras import layers

import gensim.downloader as api, inspect
from gensim.models.word2vec import Word2Vec


print("jai shree ramm")

#There should be 12 categories
CATEGORIES=("Crime","Curruption","Gang-war","Cyber warfare")
CAT_VECTOR={}
class category:
    def __init__(self,cat,tfidf):
        self.cat= cat
        self.tfidf= tfidf
        self.vector=[]
        self.distance=0.0000
        self.inverse_d=0.0000
        self.percentage=0.00000
        self.assignedCAT= NULL

    
class webpage:
    def __init__(self,cat1,cat2,cat3,cat4,cat5):
        self.cat1 =cat1
        self.cat2 =cat2
        self.cat3 =cat3
        self.cat4 =cat4
        self.cat5 =cat5



def import_data():
    # TODO import data function and arranging in dict
    print("jai shree ram")
    return dict
#def assign_vector():
    
# def find_distance(category):
#     category.cat
#     vectoring_model.wv.distance

def inverse_distance():

    print("jai shree ramm")



def main():
    imported_data= import_data(sys.argv[1])

    # TODO import word to vector model
    # this code needs to change afterwards
    corpus = api.load('text8')
    vectoring_model = Word2Vec(corpus)

    #asigning vector to categories
    for words in CATEGORIES:
        CAT_VECTOR[words]=vectoring_model.wv[words]

    #assigning vector to data
    for webpage in imported_data:
        webpage.cat1.vector= vectoring_model.wv[webpage.cat1.cat]
        webpage.cat2.vector= vectoring_model.wv[webpage.cat2.cat]
        webpage.cat3.vector= vectoring_model.wv[webpage.cat3.cat]
        webpage.cat4.vector= vectoring_model.wv[webpage.cat4.cat]
        webpage.cat5.vector= vectoring_model.wv[webpage.cat5.cat]
    

    # clustering algo

    # TODO CLustering algo



    # finding distance algo
 
    for webpage in imported_data:
        product_dist=1
        for category in webpage:
            category.distance=vectoring_model.wv.distance(category.cat,category.assignedCAT)
            if (category.distance==0):
                product_dist=(category.distance+1)*product_dist
            else:
                product_dist=category.distance*product_dist
    #inverse distance algo
    for webpage in imported_data:
        for category in webpage:
            category.inverse_d =product_dist/category.distance
    
    # finding percentage

    for webpage in imported_data:
        sum_invdist_and_tfidf=0
        for category in webpage:
            category.percentage= category.tfidf*category.inverse_d
            sum_invdist_and_tfidf+=category.percertage
    for webpage in imported_data:
        for category in webpage:
            category.percentage= (category.percentage/sum_invdist_and_tfidf)*100
    

    out={}
    for webpage in import_data:
        cat_and_percert=[]
        for category in webpage:
            cat_and_percert.append((category.assignedCAT,category.percentage))
        out[webpage]=cat_and_percert

    return out 
    #out to be retruned