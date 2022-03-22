import gensim.downloader as api, inspect
from gensim.models.word2vec import Word2Vec


def main():
    corpus = api.load('text8')
    vectoring_model = Word2Vec(corpus)
    print(vectoring_model.wv['tree'])
    


if __name__ == "__main__":
    main()
