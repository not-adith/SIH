
import crawlerfinal
import NLP
import Clustering
import sys

def main(query):
    # text1 =os.system("python crawler.py https://en.wikipedia.org/wiki/Fruit")
    crawlerout= crawlerfinal.main(query)
   
    # print(crawlerout)
    NLPout= NLP.main(crawlerout)
    #print(NLPout)
    Clusteringout=Clustering.main(NLPout)

    #print(Clusteringout)
 
# need to write the steming algo tooooo



if __name__ == "__main__":
    
    main(sys.argv[1])