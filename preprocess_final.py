import sklearn as sk
import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.stats import norm
from sklearn.metrics.pairwise import cosine_similarity as cosine
import random


# In[2]:


def diff_gaussian(year1, year2, var=3.408):
    return norm(0,var).pdf(abs(year2-year1))*(1/norm(0,var).pdf(0))


# In[3]:


data = pd.read_csv('~/datamining/DBLP_labeled_data .tsv', sep='\t')


# In[4]:


data.head()


# In[5]:


title_list = [i for i in data["Title"]]


# In[6]:


vectorizer = TfidfVectorizer()


# In[7]:


title_vectors = vectorizer.fit_transform(title_list)


# In[8]:


print(title_vectors[0])


# In[9]:


venue_list = [i for i in data["Venue"]]


# In[10]:


venue_list[0]


# In[11]:


venue_vectors = vectorizer.fit_transform(venue_list)


# In[12]:


print(venue_vectors[0])


# In[13]:


author_list_old = [i for i in data["Coauthors"]]
author_list = []

for i in author_list_old:
    authors = i.split('|')
    author = authors[0]
    author_names = author.split()
    first_name = author_names[0]
    middle_name = author_names[1]
    authors[0] = first_name[0] + " " + middle_name[0] + " " + " ".join(k for k in author_names[2:])
    author_list.append(" ".join(j for j in authors))
# In[14]:


#author_list = [i.replace('|',' ') for i in author_list]


# In[15]:


author_list = [i.replace('.','') for i in author_list]


# In[16]:


author_list[0]


# In[17]:


author_vectors = vectorizer.fit_transform(author_list)


# In[18]:


X = []
y = []
for i in range(1000):
    if i%100==0:
            print(i)
    for j in range(i):
        if data.loc[i,"Unique Author ID"] == data.loc[j, "Unique Author ID"]:
            y.append(1)
        else:
            y.append(0)
        similarity_vector = []
        similarity_vector.append(cosine(author_vectors[i], author_vectors[j])[0][0])
        similarity_vector.append(cosine(title_vectors[i], title_vectors[j])[0][0])
        similarity_vector.append(cosine(venue_vectors[i], venue_vectors[j])[0][0])
        similarity_vector.append(diff_gaussian(data["Year"][i], data["Year"][j]))
        X.append(similarity_vector)


# In[ ]:


print(len(data.index))
