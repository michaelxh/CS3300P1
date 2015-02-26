import pickle
import json
episode_appearances = pickle.load(open("episode_appearances.p"))
episode_deaths = pickle.load(open("episode_deaths.p"))
for e in episode_appearances:
    e['Lannister']=0
    if 'Black' in e: 
        e['Black'] =0
    if 'The' in e:
        e['The'] = 0
    e['Jon Arryn'] = 7

episode_ratings=[8.6,8.4,8.2,8.3,8.6,8.7,8.8,8.5,9.1,9.0,
                 8.3,8.0,8.3,8.2,8.2,8.5,8.3,8.2,9.4,9.0,
                 8.3,8.0,8.3,9.2,8.4,8.1,8.0,8.4,9.8,8.5,
                 8.8,9.6,8.4,8.3,8.1,9.5,8.7,9.4,9.0,9.3]
    
episode_info = []
num = 1
for e,e2,r in zip(episode_deaths,episode_appearances,episode_ratings):
    total = 1.0
    episode_info.append({'episode':num,'deaths':[],'rating':r})
    for a in e2:
        total += e2[a]
    for d in e:
        n = d.split(' ')[0]
        if d =='Jon Arryn':
            n = 'Jon Arryn'
        episode_info[-1]['deaths'].append({'name':d,
            'mentions':(e2[n] if n in e2 else 0)/total})
    num += 1
f = open('episode_info.json','w')
f.write(json.dumps(episode_info))
f.close()
