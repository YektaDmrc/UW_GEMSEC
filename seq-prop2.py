
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt

peptides = [None] * 60
for i in range(60):
    peptides[i] = pd.read_csv("./peptide_" + str(i+1) + ".csv")

#for i in range(573):
    #temp = pd.DataFrame(columns = np.arange(12) + 1)
    #for j in range(60):
        #temp = temp.append(peptides[j].loc[:,0])
    #temp.to_csv(path_or_buf = "./props/prop_" + str(i+1) + ".csv")
peptides[0]


# ## Reduced Dataset PCA/FA
# * Add corresponding properties to CSV files for correlation

# In[87]:


import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt

for i in range(1,13):
    #generate DataFrame from csv files of un-standardized data, store in std_data[<location>]
    temp1 = pd.read_csv('transp_location_' + str(i) + '.csv')
    temp1 = temp1.drop(temp1.columns[0],axis=1)
    properties = temp1.columns
    
    temp2 = pd.read_csv('./correlated_props/corr_loc_' + str(i) + '.csv', header = None)
    indices = temp2.iloc[:,0]
    
    corresponding_props = [None] * len(indices)
    for j in range(len(indices)):
        corresponding_props[j] = properties[indices[j] - 1]
    temp2["Properties"] = corresponding_props
    temp2.to_csv(path_or_buf= './correlated_props/corr_loc_' + str(i) + '_text.csv')
temp2.head()


# Next, want to generate a list of indices for properties to keep for each of twelve locations

# In[151]:


for i in range(1,13):
    kept_props = []
    temp = pd.read_csv("./correlated_props/corr_loc_" + str(i) + '.csv', header = None)
    data = pd.read_csv('location_' + str(i) + '.csv')
    indices = temp.iloc[:,0]
    reduced_data = pd.DataFrame(data = None, columns = data.columns)
    for j in range(len(indices)):
        if temp.iloc[j, 1] == 1:
            kept_props.append(indices[j] - 1)
            reduced_data = reduced_data.append(data.iloc[j,:])
    reduced_data.to_csv("./reduced_data/reduced_loc_" + str(i) + ".csv")
reduced_data


# Transform reduced data sets / send to numpy array, perform PCA
# TODO: Export sorted loading scores with data

# In[45]:


import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt

std_data = [None] * 12
# Access: std_data[<location>][<peptide #>][<prop #>]
loading_scores, top_props = [None]*12, [None]*12
pc_table = [None] * 15
pca = PCA()
sorted_scores = [[[None for x in range(100)] for y in range(15)] for z in range(12)]

for i in range(1,13):
    #generate DataFrame from csv files of un-standardized data, store in std_data[<location>]
    temp = pd.read_csv('./reduced_data/reduced_loc_' + str(i) + '.csv')
    temp = temp.drop(temp.columns[0],axis=1)
    temp = temp.drop(temp.columns[0],axis=1)
    temp = temp.transpose()
    temp.columns = temp.iloc[0]
    temp = temp.drop(temp.index[0])
    properties = temp.columns
    
    #some values are NaN or non-finite - fill these values
    temp = temp.fillna(0)
    temp = preprocessing.scale(temp)     #scale values, from dataframe -> ndarray
    std_data[i-1] = temp    #store in numpy array
    
    #erform PCA
    pca.fit_transform(std_data[i-1])
    pca_data = pca.transform(std_data[i-1])
    
    #Create table for each location: Property and loading score for each principal component
    df = pd.DataFrame() #list of properties, text
    df2 = pd.DataFrame() #list of sorted loading scores
    for j in range(15):
        loading_scores[i-1] = pd.Series(pca.components_[j], index = properties)
        sorted_loading_scores = loading_scores[i-1].abs().sort_values(ascending=False)
        top_props[i-1] = sorted_loading_scores[0:len(sorted_loading_scores)].index.values
        df["PC" + str(j+1)] = top_props[i-1]
        sorted_scores[i-1][j] = sorted_loading_scores[:100]
    per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
    df.loc["Percent Variance"] = per_var[:15]
    df.to_csv(path_or_buf = "./PCA_reduced/top_props_perPC_loc_" + str(i) + ".csv")
    #Visualizing which principal components explain most variance
    #labels = ['PC'+str(x) for x in range(1, len(per_var)+1)]
    #plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
    #plt.ylabel('Percentage of explained variance for location ' + str(i))
    #plt.xlabel('Principal component')
    #plt.show()
df.head()


# In[46]:


for i in range(15):
    pc_table[i] = pd.DataFrame(columns = np.arange(100))
    for j in range(1,13):
        temp = pd.read_csv('./reduced_data/reduced_loc_' + str(j) + '.csv')
        temp = temp.drop(temp.columns[0],axis=1)
        temp = temp.drop(temp.columns[0],axis=1)
        temp = temp.transpose()
        temp.columns = temp.iloc[0]
        temp = temp.drop(temp.index[0])
        properties = temp.columns
        
        temp = temp.fillna(0)
        temp = preprocessing.scale(temp)     #scale values, from dataframe -> ndarray
        std_data[j-1] = temp    #store in numpy array

        pca.fit_transform(std_data[j-1])
        pca_data = pca.transform(std_data[j-1])
        
        loading_scores[j-1] = pd.Series(pca.components_[i], index = properties)
        sorted_loading_scores = loading_scores[j-1].abs().sort_values(ascending=False)
        top_props[j-1] = sorted_loading_scores[0:100].index.values
        
        pc_table[i].loc["Location " + str(j)] = top_props[j-1]
    pc_table[i].T.to_csv(path_or_buf="./PCA_reduced/top_props_perloc_PC" + str(i+1) +".csv")
pc_table[0].T.head()


# Now have top properties (text) per location, and per principal component. Also made 12 (location) x 15 (principal components) * 100 (top 100 properties per PC per location) list. Ex. to access the list of top 100 most important properties for first location, considering the first principal component, call sorted_scores[0][0] to retrieve a pd.Series object

# In[41]:


sorted_scores[0][0]


# In[66]:


temp_df = pd.DataFrame()
pc_columns = ["PC" + str(i+1) for i in range(15)]
for i in range(12):
    for j in range(15):
        temp_tuple = list(zip(sorted_scores[i][j].index, sorted_scores[i][j])

