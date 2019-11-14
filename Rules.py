import pandas as pd

def check_emails(u,v):
	if df.loc[u,"email"]==df.loc[v,"email"]:
		return True
	return False

def check_venue(u,v):
	if df.loc[u,"venue"]==df.loc[v,"venue"]:
		return True
	return False

def check_coauthors(u,v):
	u_co=df.loc[u,"coauthors"]
	v_co=df.loc[v,"coauthors"]
	for i in u_co:
		if i in v_co:
			return True
	return False

def check_citation(u,v):
	u_cited=df.loc[u,"citation"]
	v_cited=df.loc[v,"citation"]
	for i in u_cited:
		if i not in v_co:
			return False
	return True

def check_MIandSubject(u,v):
	u_MI=df.loc[u,"MI"]
	v_MI=df.loc[v,"MI"]
	u_sub=df.loc[u,"subject"]
	v_sub=df.loc[v,"subject"]
	return u_MI==v_MI and u_sub==v_sub

#Still to Write
def check_name(u,v):
	u_author=df.loc[u,"name"]
	v_author=df.loc[v,"name"]
	return u_author==v_author

def check_self_citation(u,v):
	if not check_name(u,v):
		return False
	if (u in df.loc[v,"citation"]) or (v in df.loc[u,"citation"]):
		return True
	return False

def isPositive(u,v):
	

def Find(par,u):
	if par[u]==u:
		return u
	return par[u]=Find(par,par[u])

def Union(par,u,v):
	u=Find(par,u)
	v=Find(par,v)
	if u!=v:
		par[u]=v
