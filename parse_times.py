import json
f = open('screen_time_info.txt')
dict = {}
for l in f:
    n = l[0:l.find('-')-1]
    t = int(l[l.find('-')+1:l.find(':')])
    t += int(l[l.find(':')+1:l.find(':')+3])/60.0
    s = l[l.find('('):l.find(';')].split(',')
    e = int(l[l.find(';')+2:l.find(')')])
    dict[n] = {'time':t,'seasons':s,'episodes':e}
to_write = open('screen_time_info.json','wb')
to_write.write(json.dumps(dict))
f.close()
to_write.close()
episode_lengths =[62,56,58,56,55,53,58,59,57,53,
    53,54,53,51,55,54,56,54,55,64,
    55,57,53,54,58,53,59,58,52,64,
    58,52,57,55,53,50,51,52,50,65]
