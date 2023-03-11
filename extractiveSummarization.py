import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import fasttext
import fasttext.util
import re

ft = fasttext.load_model('cc.hi.300.bin')

def create_sim_mat(sentences):
    
    sim_mat = np.zeros([len(sentences), len(sentences)])
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                sim_mat[i][j] = cosine_similarity(ft.get_sentence_vector(sentences[i]).reshape(1, -1),ft.get_sentence_vector(sentences[j]).reshape(1, -1))
    return sim_mat
    
def get_ranked_sentences(sentences,sim_mat):
    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
    return ranked_sentences

def get_op(text):
    sentences = hindiSentTokenize(text)
    n = int(len(sentences) * 0.3)
    n = 1 if n == 0 else n
    simi_matrix = create_sim_mat(sentences)
    ranked_sentences = get_ranked_sentences(sentences,simi_matrix)
    op=list()
    # Extract top n sentences as the summary
    for i in range(n):
        if ranked_sentences[i][1]:
            op.append(ranked_sentences[i][1])
    return op

def clean_article(articleText):
    articleText = re.sub("http\S+\s*", " ", articleText) # Remove URL
    articleText = re.sub("RT|cc", " ", articleText) # rempve RT and cc
    articleText = re.sub("#\S+", " ", articleText) # remove hashtag
    articleText = re.sub("@\S+", " ", articleText) # rempve mentions
    articleText = re.sub("[%s]" % re.escape('!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~'), " ", articleText) # remove punctuations
    articleText = re.sub("\s+", " ", articleText) # remove extra whitespaces
    return articleText

def hindiSentTokenize(sent):
    cleanText = clean_article(sent)
    splitText = cleanText.split("। ")
    return list(filter(lambda x: len(x) !=0 ,splitText))