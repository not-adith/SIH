
from asyncio.windows_events import NULL
from cmath import inf
from lib2to3.pgen2.token import EQUAL
from msilib.schema import File

from tkinter.filedialog import Directory
import string
from numpy import Infinity
from tensorflow.keras import layers

import gensim.downloader as api
from gensim.models.word2vec import Word2Vec


def dicttoclass(imported_data):

    func_return = []
    for web in imported_data:
        web1=webpage()
        web1.name=web
        for i in range(imported_data[web]):
            
                web1.catlist.append(category(cat=imported_data[web][i][0],tfidf=imported_data[web][i][1]))
        
        func_return.append(web1)
    return func_return




#There should be 12 categories
CATEGORIES=('Science','Technology','Political', 'Sports', 'International', 'Environmental', 'Business','Historical', 'Hateful','Misleading','Harmful')
CAT_VECTOR={}
class category:
    def __init__(self,cat,tfidf):
        self.cat=cat
        self.tfidf= tfidf
        self.vector=[]
        self.distance=0.0000
        self.inverse_d=0.0000
        self.percentage=0.000
        self.assignedCAT= NULL

    
class webpage:
    def __init__(self):
        self.name=NULL
        self.catlist=[]
        





#def assign_vector():
    
# def find_distance(category):
#     category.cat
#     vectoring_model.wv.distance



def main(imported_data):
    #input data  to class conversion 
    imported_data= dicttoclass(imported_data)
    # this code needs to change afterwards
    wv = api.load('word2vec-google-news-300')

    # corpus = api.load('text8')
    # vectoring_model = Word2Vec(corpus)
    
    #asigning vector to categories
    for words in CATEGORIES:
        CAT_VECTOR[words]=wv[words]

    #assigning vector to data
    
    for webpage in imported_data:
       
        
        for _ in range(len(webpage.catlist)-1):
            if webpage.catlist[_].cat in wv:
                webpage.catlist[_].vector= wv[webpage.catlist[_].cat]
            else:
                webpage.catlist.remove(webpage.catlist[_])
            # removing the data which is not found
    

    # clustering algo
    for webpage in imported_data:
        for _ in range(len(webpage.catlist)):
            dist=Infinity
            for i in CATEGORIES:
                if webpage.catlist[_].cat in wv and i in wv:
                    distance=wv.distance(webpage.catlist[_].cat,i)
                    if (dist>distance):
                        webpage.catlist[_].distance=distance
                        webpage.catlist[_].assignedCAT=i
                else:
                    webpage.catlist[_].distance=1000
                

    for webpage in imported_data:
        for _ in webpage.catlist:
            product_dist=1
            if (_.distance==0):
                product_dist=(_.distance+1)*product_dist
            else:
                product_dist=_.distance*product_dist
        for _ in webpage.catlist:
            _.inverse_d =product_dist/_.distance
  


    # finding percentage
    for webpage in imported_data:
        sum_invdist_and_tfidf=0
        for categories in webpage.catlist:
            categories.percentage= categories.tfidf*categories.inverse_d
            sum_invdist_and_tfidf+=categories.percentage
    for webpage in imported_data:
        for categories in webpage.catlist:
            categories.percentage= (categories.percentage/sum_invdist_and_tfidf)*100
    

    out={}
    for webpage in imported_data:
        cat_and_percert=[]
        for categories in webpage.catlist:
            cat_and_percert.append((categories.assignedCAT,categories.percentage))
        out[webpage.name]=cat_and_percert
    
    return out 
    #out to be retur.ned






    # finding distance algo
 
    # for webpage in imported_data:
    #     product_dist=1
    #     for category in webpage:
    #         category.distance=vectoring_model.wv.distance(category.cat,category.assignedCAT)
    #         if (category.distance==0):
    #             product_dist=(category.distance+1)*product_dist
    #         else:
    #             product_dist=category.distance*product_dist
    #inverse distance algo
    # for webpage in imported_data:
    #     for category in webpage:
    #         category.inverse_d =product_dist/category.distance
    