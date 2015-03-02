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

episode_deaths=[['Waymar Royce', 'Gared', 'Will', 'Jon Arryn'], 
                ['Catspaw assassin', 'Mycah', 'Lady'], [], 
                ['Hugh'], ['Kurleket', 'Willis Wode', 'Jory Cassel', 'Wyl', 'Heward'], 
                ['Stiv', 'Wallen', 'Vardis Egen', 'Viserys Targaryen'], 
                ['Robert Baratheon', 'Varly'], 
                ['Vayon Poole', 'Septa Mordane', 'Syrio Forel', 'Mago', 'Jafer Flowers', 'Othor', 'Stableboy'], 
                ['Eddard Stark', 'Qotho'], ['Rhaego', 'Drogo', 'Mirri maz Duur'], 
                ['Cressen', 'Barra'], ['Rakharro'], ['Yoren', 'Lommy Greenhands'], 
                ['Rennick', 'Lannister guardsman', 'Tortured prisoner', 'Stafford Lannister'], 
                ['Renly Baratheon', 'Emmon Cuy', 'Robar Royce', 'The Tickler'], 
                ['Rodrik Cassel', 'High Septon', 'Amory Lorch', 'Drennan', 'Irri'], 
                ['Alton Lannister', 'Torrhen Karstark', 'the Thirteen', 'The Spice King', 'Silk King', 'Copper King', 'Billy', 'Jack'],    
                ['Borba', 'Harker', 'Stonesnake'], ['Matthos Seaworth', 'Mandon Moore'], 
                ['Maester', 'Luwin', 'Doreah', 'Xharo Xoan Daxos', 'Qhorin Halfhand', 'Pyat Pree', 'Tom'], [], 
                ['Hoster Tully'], ['Master Torturer'], ['Bannen', 'Craster', 'Jeor Mormont', 'Kraznys mo Nakloz', 'Greizhen mo Ullhor'], 
                ['Willem Lannister', 'Martyn Lannister', 'Karstark lookout', 'Rickard Karstark'], 
                ['Ros'], [], ['Mero', 'Prendahl na Ghezn', 'White Walker'], 
                ['Old man', 'Orell', 'Talisa Maegyr', 'Wendel Manderly', 'Grey Wind', 'Robb Stark', 'Joyeuse Erenford', 'Catelyn Stark'], 
                ['Frey soldier #1', 'Frey soldier #2'], ['Lowell', 'Polliver'], 
                ['Tansy', 'Axell Florent', 'Joffrey Baratheon'], 
                [' Dontos Hollard', 'Guymon', "Olly's mother", 'Oznak zo Pahl'], 
                ['Great Master 1'], ['Mutineers', 'Karl', 'Rast', 'Locke'], [], 
                ['Dying man', 'Biter', 'Rorge', 'Lysa Arryn'], 
                ['Kegs', 'Black Jack Bulwer', 'Mully', "Mole's Town whore", 'Ralf Kenning', 'Adrack Humble', 'Oberyn Martell'], 
                ['Dongo', 'Smitty', 'Pypar', 'Thenn Warg', 'Styr of Thenn', 'Ygritte', 'Mag Mar Tun Doh Weg', 'Grenn', 'Cooper', 'Donnel Hill'], 
                ['Zalla', 'Jojen Reed', 'Shae', 'Tywin Lannister']]

episode_ratings=[8.6,8.4,8.2,8.3,8.6,8.7,8.8,8.5,9.1,9.0,
                 8.3,8.0,8.3,8.2,8.2,8.5,8.3,8.2,9.4,9.0,
                 8.3,8.0,8.3,9.2,8.4,8.1,8.0,8.4,9.8,8.5,
                 8.8,9.6,8.4,8.3,8.1,9.5,8.7,9.4,9.0,9.3]
    

episode_lengths =[62,56,58,56,55,53,58,59,57,53,
                  53,54,53,51,55,54,56,54,55,64,
                  55,57,53,54,58,53,59,58,52,64,
                  58,52,57,55,53,50,51,52,50,65]


episode_info = []
num = 1
cumulative = 0
for e,e2,r,l in zip(episode_deaths,episode_appearances,episode_ratings,episode_lengths):
    total = 1.0
    cumulative += l
    episode_info.append({'episode':num,'deaths':[],'rating':r,'time':cumulative})
    for a in e2:
        total += e2[a]
    for d in e:
        n = d.split(' ')[0]
        if d =='Jon Arryn':
            n = 'Jon Arryn'
        episode_info[-1]['deaths'].append({'name':d})
    num += 1
f = open('episode_info.json','w')
f.write(json.dumps(episode_info))
f.close()
