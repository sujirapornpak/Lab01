#==========//==========//==========//==========//==========//

# Method 1: import 'old_module_name' as 'new_module_name'
#import module1 as mod  
#mod.fn1(5, 10)

# Method 2: from MODULE_NAME import FUNCTION_NAME
#from module1 import fn1
#fn1(5,10)

#==========//==========//==========//==========//==========//
 
## 1. Check Python version of update module
#try:
    #reload  # Python 2.7
#except NameError:
    #try:
        #from importlib import reload  # Python 3.4+
    #except ImportError:
        #from imp import reload  # Python 3.0 - 3.3

# 2. Update module
#import importlib                
#importlib.reload(mod) # aftr rename module1 as mod

#==========//==========//==========//==========//==========//
##STEP 1.1: Import required python libraries (matplotlib, pandas, numpy).

#%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# fn0: Test function
def fn0(x,y):
	return x+y
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# fn1: Replacing Header with Top Row (i.e., make row 11th to be the header)
def fn1(dataframe,firstrow):
    temp1 = dataframe.iloc[firstrow:,:] #select firstrow = row 11th to the end, every columns
    temp1 = temp1.reset_index(drop=True) # use drop parameter to avoid the old index being added as a column.
    new_header = temp1.iloc[0] # select the first row (old row#11) to be header 
    df4 = temp1[1:] # select the data content from row#1 (exclude row#0 that will be header)
    df4.columns = new_header # set the header row as the df header
    return df4


# fn2: Unique row name (data objects) in given column
def fn2(df4,columnname):
    df5 = df4.groupby(columnname).nunique()
    return df5


# fn3a: Query member names in a given column 
def fn3a(df4,columnname,qugene1):
    df44 = df4[df4[columnname].isin(qugene1)]
    df44 = df44.sort_values(by='donor_id', ascending=True) # sort from low to high ID
    return df44 # Return filtered table
    return np.array(df44['donor_id']) # Return ID listed of filtered row
    return df44['donor_id'].tolist() 
    # How to use function: 
        # tab1 = fn3a(HippoID,'structure_acronym',['HIP'])
     # Ref sort: ## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html


# fn3b: Re-ordering columns in pandas dataframe based on column name ( = sort subject ID in column)
def fn3b(dataframe):
    df1 = dataframe.sort_index(axis=1)
    return df1
# Ref: https://stackoverflow.com/questions/11067027/re-ordering-columns-in-pandas-dataframe-based-on-column-name


# fn3c: Sort value in specific column
def fn3c(dataframe):
    df1 = dataframe.sort_values(by='donor_id', ascending=True) # sort from low to high ID, if =False (high->low)
    return df1 # Return filtered table


# fn3d: Get desired ID from column names (taxa table), and use them to filter ID in rows from patient-metadata table
def fn3d(taxatab,metatab):
    ids=list(taxatab.columns) # get list of desired ID
    ids_md = metatab[metatab['Subject_ID'].isin(ids)] # filter row of metadata table with corresponding ID
    ids_md = ids_md.set_index('Subject_ID') # ##Column 'Subject_ID' turned to be Index
    return ids_md

# fn3e: Add "Group" (Label) to the last column of feature table using "Merge" function()
def fn3e(taxatab,metatab):
    dat = taxatab.merge(metatab[['Subject_ID','Group']],on='Subject_ID',how='inner')
    return dat


# fn4a: Test code for selecting different members in set
def fn4a(t1,t2):
    t3 = []
    for i in list(range(len(t1))): 
        if t1[i] not in t2:
            t3.append(t1[i])
    return t3      
t1 = ['A','B','C']  # default value for t1
t2 = ['A']          # default value for t2


# fn4b: Selecting different members in set
def fn4b(allfea,bestfea):
    nonfea = []
    for i in list(range(len(allfea))):  #len(allfea) = 326
        if allfea[i] not in bestfea: # len(bestfea) = 79
            nonfea.append(allfea[i])
    return len(nonfea)        # 326-79 (best features) = 247 non-sig features (remaining) 


# fn4c: Make new table based on best (14,53,79) features
def fn4c(dataframe,bestfea14):
    SbjID1 = dataframe.iloc[:,0:1] # cut first column into new dataframe
    SbjID2 = SbjID1 # For reuse purpose of first column
    # Test code before for loop script
    # SbjID2['Absiella_dolichum'] = np.array(dataframe['Absiella_dolichum'])
    ## For loop to append columns of 14 best features
    for i in list(range(len(bestfea14))):  #len(bestfea14) = 14, which is a list name, i.e., (['Ali', 'Alist',...])
        SbjID2[bestfea14[i]] = np.array(dataframe[bestfea14[i]])
    return SbjID2


# fn5a: Convert id in integer to string
def fn4d(rnaseq94):
    newlist = []
    for i in range(len(rnaseq94)):
        id = str(rnaseq94[i])
        newlist.append(id)
    return newlist
rnaseq94 = [496100281, 496100288, 496100294, 496100303, 496100304] # default test value as integer