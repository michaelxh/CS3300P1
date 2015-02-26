from bs4 import BeautifulSoup as bs
import requests
import re
import sys
import unicodedata
import pickle

def combine_dicts(d1,d2):
    d3 = {}
    for i in d1.keys():
        if not (i in d2):
            d3[i]=d1[i]
    for i in d2.keys():
        if i in d1:
            d3[i]=d1[i]+d2[i]
        else:
            d3[i]=d2[i]
    return d3

def process_episode(ep_name,last_appearances,summs):
    p = requests.get("http://gameofthrones.wikia.com/wiki/"+ep_name).text
    
    #note the nondefault parser
    s = bs(p,"html5lib")
    
    #find all the tags that are useful, note that 'a' gets hyperlinks which is 
    #useful for the characters because all the important ones are hyperlinks to
    #their own pages
    txt = s.find_all(['p',re.compile("^h"),'span','a'])
    stripped_txt = ""
    
    for t in txt:
        stripped_txt= stripped_txt+t.get_text()+"\n"
    
    #find the summary, the min(a,b) is because there are multiple options, and
    #we want the first one
    summary = stripped_txt[stripped_txt.find("Summary\n"):
        min(stripped_txt.find("\nRecap\n") if stripped_txt.find("\nRecap\n")>0 else sys.maxint,
        stripped_txt.find("\nAppearances\n"))]
    #gets rid of nasty unicode that does not take to being a string properly
    summary = unicodedata.normalize('NFKD',summary).encode('ascii','ignore')
    
    summs.append(summary)
    
    #gets rid of \n, images, and punctuation
    summary = re.sub(r'\n',' ',summary)
    summary = re.sub(r'<img.*?>',' ',summary)
    summary = re.sub(r'[^\w\s]|\n',' ',summary)
    
    #find appearances first
    first_appearances = stripped_txt[
        stripped_txt.find("\nFirst\n") if stripped_txt.find("\nFirst\n") > 0 else 
            stripped_txt.find("\nFirst appearances") if stripped_txt.find("\nFirst appearances")>0 else 
                stripped_txt.find("\nFirst Appearances"):
        min(stripped_txt.find("\nDeaths\n") if stripped_txt.find("\nDeaths\n")>0 else sys.maxint,
        stripped_txt.find("\nProduction\nCast") if stripped_txt.find("\nProduction\nCast")>0 else sys.maxint,
        stripped_txt.find("\nProduction\nEdit") if stripped_txt.find("\nProduction\nEdit")>0 else sys.maxint,
        stripped_txt.find("\nDeath\n") if stripped_txt.find("\nDeath\n")>0 else sys.maxint)]
        #max(stripped_txt.find("Deaths\nEdit"),stripped_txt.find("Production\nEdit"))]
    first_appearances = unicodedata.normalize('NFKD',first_appearances).encode('ascii','ignore')
    first_appearances = re.sub(r'<img.*?>',' ',first_appearances)
    summary = re.sub(r'[^\w\s]|\n','',summary)
    first_appearances = [f.split(' ')[0] for f in first_appearances.split("\n") if f!=''and f!='Edit'][1:]
    
    #find deaths
    deaths = stripped_txt[
        min(stripped_txt.find("\nDeaths\n") if stripped_txt.find("\nDeaths\n")>0 else sys.maxint,
        stripped_txt.find("\nDeath\n") if stripped_txt.find("\nDeath\n")>0 else sys.maxint):
        min(stripped_txt.find("\nProduction\nC") if stripped_txt.find("\nProduction\nC")>0 else sys.maxint,
            stripped_txt.find("\nCast\n") if stripped_txt.find("\nCast\n")>0 else sys.maxint,
            stripped_txt.find("\nProduction\nEdit") if stripped_txt.find("\nProduction\nEdit")>0 else sys.maxint)]
    deaths = unicodedata.normalize('NFKD',deaths).encode('ascii','ignore')
    deaths=[d for d in deaths.split("\n") if d!='' and d!='Edit'][1:]
    first_app = {}
    for f in first_appearances:
        first_app[f] = 0
    
    #add new appearances to old set of characters 
    appearances_new = combine_dicts(first_app,last_appearances)
    for a in appearances_new.keys():
        #counts characters in summary text
        appearances_new[a] += summary.count(a+' ')
        
    return(appearances_new,deaths,first_appearances)
    

episodes = ['Winter_is_Coming','The_Kingsroad','Lord_Snow',
            'Cripples,_Bastards_and_Broken_Things','The_Wolf_and_the_Lion',
            'A_Golden_Crown','You_Win_or_You_Die','The_Pointy_End',
            'Baelor','Fire_and_Blood',
            'The_North_Remembers','The_Night_Lands','What_is_Dead_May_Never_Die',
            'Garden_of_Bones','The_Ghost_of_Harrenhal','The_Old_Gods_and_the_New',
            'A_Man_Without_Honor','The_Prince_of_Winterfell','Blackwater',
            'Valar_Morghulis',
            'Valar_Dohaeris', 'Dark_Wings,_Dark_Words','Walk_of_Punishment',
            'And_Now_His_Watch_is_Ended','Kissed_by_Fire','The_Climb',
            'The_Bear_and_the_Maiden_Fair_(episode)','Second_Sons_(episode)',
            'The_Rains_of_Castamere_(episode)','Mhysa',
            'Two_Swords','The_Lion_and_the_Rose','Breaker_of_Chains','Oathkeeper',
            'First_of_His_Name','The_Laws_of_Gods_and_Men','Mockingbird',
            'The_Mountain_and_the_Viper','The_Watchers_on_the_Wall','The_Children']

episode_appearances = []
new_appearances = []
last_app = {}
episode_deaths = []
summs = []
for e in episodes:
    res = process_episode(e,last_app,summs)
    episode_appearances.append(res[0])
    episode_deaths.append(res[1])
    new_appearances.append(res[2])
    last_app=episode_appearances[len(episode_appearances)-1]
pickle.dump(episode_deaths,open('episode_deaths.p','wb'))
pickle.dump(episode_appearances,open('episode_appearances.p','wb'))


    


        
        
        
        

    
    
        



