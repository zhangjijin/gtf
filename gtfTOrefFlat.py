# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:46:07 2019

@author: jijin
"""

from gtfparse import read_gtf
import pandas as pd
import csv
df = read_gtf("C:\\Users\\jijin\\Desktop\\IWGSC_v1.1_LC_20170706.gtf")#数据位置
df = pd.DataFrame(df)
gene_name_1 = df['gene_name']
gene_name_2 = set(gene_name_1)
gene_name = list(gene_name_2)


refFlat=pd.DataFrame(columns = ['name','chrom','strand','txstart','txend','cdsstart','cdsend','exoncount','exonStarts','exonEnds'])


for i in range(0,len(gene_name)):
    list0=['a','b','c','d','e','f','g','h','i','k']
    list0[0]=gene_name[i]
    
    feature = []
    feature_1=pd.DataFrame(columns=[])
    count = 0
    m=0
    feature_1=pd.DataFrame(columns =['1','2','3'])
    for j in range(0,df.shape[0]):
        appendele = []
        
        if df.iloc[j,10] == gene_name[i]:
            m =m+1
            #feature_1=pd.DataFrame(columns =['1','2','3'])           
            feature_1.loc[m]=[str(df.iloc[j,2]),int(df.iloc[j,3]),int(df.iloc[j,4])]
            #feature_1=feature_1.append(appendele)
            #appendele=[str(df.iloc[j,2]),int(df.iloc[j,3]),int(df.iloc[j,4])]
            
            #feature_1=feature_1.append(appendele)
            #feature_2=feature_1.T
            #feature_2.columns =['1','2','3']
            feature=list(feature_1["1"])#选取第0行
            list0[1]=df.iloc[j,0]
            
            list0[2]=df.iloc[j,6]
        #elif df.iloc[j,10] != gene_name[i]:
            #m=0
            list0[7]=feature.count("exon")
            exon1=''
            exon2=''      
            
            if '5UTR' in feature :
                list0[3]  = df.iloc[j,3]-1
                list0[5] =df.iloc[j,4]
            elif '5UTR' not in feature:
                list0[3] = '.'
                list0[5] ='.'
            if '3UTR' in feature:
                list0[4] = df.iloc[j,4]
                list0[6] =df.iloc[j,3]-1
            elif '3UTR' not in feature:
                list0[4] = '.'
                list0[6] ='.'
            
                
                    
            for k in range(0,len(feature)):
                if feature_1.iloc[k,0]=='exon':
                    exon1=exon1+str(feature_1.iloc[k,1])+','
                    exon2=exon2+str(feature_1.iloc[k,2])+','
             
                    list0[8] = exon1
                    list0[9] = exon2
       # with open ("refFlat.csv","a") as csvfile :
            #writer = csv.writer(csvfile)
            #writer.writerow(list0)#写入csv文件代码
    refFlat.loc[i]=list0#写入数据框

