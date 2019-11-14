import pandas as pd
import Rules as R
import itertools
#df contains the articles 

def Result(par,i,j):
	if Find(par,i)==Find(par,j):
		return 1
	return 0

n=len(df.index)
par=[i for i in range(n)]
for i in range(n):
	for j in range(n):
		if R.isPositive(i,j):
			R.Union(par,i,j)

rows=itertools.product(df.iterrows(),df.iterrows())
X=pd.DataFrame(left.append(right) for (_,left),(_,right) in rows)
y=pd.DataFrame(Result(par,i,j) for (i,_),(j,_) in rows)
l=[],leng=0
for (i,_),(j,_) in rows:
	if not check_name(i,j):
		l+=leng
	leng+=1
X.reset_index(drop=True)
y.reset_index(drop=True)
X.drop(l,axis=0,inplace=True)
y.drop(l,axis=0,inplace=True)
X.reset_index(drop=True)
y.reset_index(drop=True)