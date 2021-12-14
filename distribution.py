import random
from numpy.random import choice as choice_numpy
import numpy

artifacts = ('sands','goblet','circlet','flower','plume')
mainstats = {
    'sands' : ( ('hp%'  , 'atk%','def%' ,'er%'  ,'em'), #Type
                (26.68  ,26.68  ,26.68  ,10     ,10  )),#Weight
    'goblet': ( ('hp%'  ,'atk%' ,'def%' ,'pyro' ,'electro'  ,'cryo' ,'hydro'    ,'anemo',   'geo'   ,'physical'     ,'em'),
                (21.25  ,21.25  ,20     ,5      ,5          ,5      ,5          ,5          ,5      ,5              ,2.5)),
    'circlet':( ('hp%'  ,'atk%' ,'def%' ,'cr%'  ,'cd%'  ,'heal%'    ,'em'),
                (22     ,22     ,22     ,10     ,10     ,10         ,2.5)),
    'flower': ( ('hp',''),(100,0)),
    'plume':  ( ('atk',''),(100,0))
}
substats = {
    ('sands','hp%'):    (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),  # Type
                         (15    ,15     ,15     ,0      ,10     ,10     ,10     ,10     ,7.5    ,7.5  )),       # Weight
    ('sands','atk%'):   (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                         (15    ,15     ,15     ,10     ,0      ,10     ,10     ,10     ,7.5    ,7.5  )),
    ('sands','def%'):   (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                         (15    ,15     ,15     ,10     ,10     ,0      ,10     ,10     ,7.5    ,7.5  )),                        
    ('sands','er%'):    (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                         (15    ,15     ,15     ,10     ,10     ,10     ,0      ,10     ,7.5    ,7.5  )),
    ('sands','em'):     (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                         (15    ,15     ,15     ,10     ,10     ,10     ,10     ,0      ,7.5    ,7.5  )),
      
    ('goblet','hp%'):    (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (15    ,15     ,15     ,0      ,10     ,10     ,10     ,10     ,7.5    ,7.5  )),
    ('goblet','atk%'):   (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (15    ,15     ,15     ,10     ,0      ,10     ,10     ,10     ,7.5    ,7.5  )),
    ('goblet','def%'):   (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (15    ,15     ,15     ,10     ,10     ,0      ,10     ,10     ,7.5    ,7.5  )),                        
    ('goblet','er%'):    (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (15    ,15     ,15     ,10     ,10     ,10     ,0      ,10     ,7.5    ,7.5  )),
    ('goblet','em'):     (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (15    ,15     ,15     ,10     ,10     ,10     ,10     ,0      ,7.5    ,7.5  )),
    ('goblet','pyro'):   (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (13.64 ,13.64  ,13.64  ,9.09   ,9.09   ,9.09   ,9.09   ,9.09   ,6.82  ,6.82  )),
    ('goblet','electro'):(('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (13.64 ,13.64  ,13.64  ,9.09   ,9.09   ,9.09   ,9.09   ,9.09   ,6.82  ,6.82  )),
    ('goblet','cryo'):   (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (13.64 ,13.64  ,13.64  ,9.09   ,9.09   ,9.09   ,9.09   ,9.09   ,6.82  ,6.82  )),
    ('goblet','hydro'):  (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (13.64 ,13.64  ,13.64  ,9.09   ,9.09   ,9.09   ,9.09   ,9.09   ,6.82  ,6.82  )),
    ('goblet','anemo'):  (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (13.64 ,13.64  ,13.64  ,9.09   ,9.09   ,9.09   ,9.09   ,9.09   ,6.82  ,6.82  )),
    ('goblet','geo'):    (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (13.64 ,13.64  ,13.64  ,9.09   ,9.09   ,9.09   ,9.09   ,9.09   ,6.82  ,6.82  )),
   ('goblet','physical'):(('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                          (13.64 ,13.64  ,13.64  ,9.09   ,9.09   ,9.09   ,9.09   ,9.09   ,6.82  ,6.82  )),

    ('circlet','hp%'):    (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                           (15    ,15     ,15     ,0      ,10     ,10     ,10     ,10     ,7.5    ,7.5  )),
    ('circlet','atk%'):   (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                           (15    ,15     ,15     ,10     ,0      ,10     ,10     ,10     ,7.5    ,7.5  )),
    ('circlet','def%'):   (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                           (15    ,15     ,15     ,10     ,10     ,0      ,10     ,10     ,7.5    ,7.5  )),                        
    ('circlet','cr%'):    (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                           (14.63 ,14.63  ,14.63  ,9.76   ,9.76   ,9.76   ,9.76   ,9.76   ,0      ,7.32  )),
    ('circlet','cd%'):    (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                           (14.63 ,14.63  ,14.63  ,9.76   ,9.76   ,9.76   ,9.76   ,9.76   ,7.32   ,0  )),
    ('circlet','heal%'):  (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                           (13.64 ,13.64  ,13.64  ,9.09   ,9.09   ,9.09   ,9.09   ,9.09   ,6.82   ,6.82  )),
    ('circlet','em'):     (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                           (15    ,15     ,15     ,10     ,10     ,10     ,10     ,0      ,7.5    ,7.5  )),
    
    ('flower','hp'):      (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                           (0     ,15.79 ,15.79   ,10.53  ,10.53  ,10.53  ,10.53  ,10.53  ,7.89   ,7.89  )),
    ('plume','atk'):      (('hp'  ,'atk'  ,'def'  ,'hp%'  ,'atk%' ,'def%' ,'er%'  ,'em'   ,'cr%'  ,'cd%'      ),
                           (15.79 ,0      ,15.79  ,10.53 ,10.53   ,10.53  ,10.53  ,10.53  ,7.89   ,7.89  )),
}


stats_distribution = {
    'hp':   (209.13 , 239.00, 268.88, 298.75),  # Type : (possible values)
    'atk':  (13.62  , 15.56 , 17.51 , 19.45 ),
    'def':  (16.20  , 18.52 , 20.83 , 23.15 ),
    'hp%':  (4.08   , 4.66  , 5.25  , 5.83  ),
    'atk%': (4.08   , 4.66  , 5.25  , 5.83  ),
    'def%': (5.10   , 5.83  , 6.56  , 7.29  ),
    'em':   (16.32  , 18.65 , 20.98 , 23.31 ),
    'er%':  (4.53   , 5.18  , 5.83  , 6.48  ),
    'cr%':  (2.72   , 3.11  , 3.50  , 3.89  ),
    'cd%':  (5.44   , 6.22  , 6.99  , 7.77  )
}


def normalize(probs):
    # Changes weights so probability for numpy.choice
    prob_factor = 1 / sum(probs)
    return [prob_factor * p for p in probs]

def generate_artifact():
    item = random.choice(artifacts)
    # Roll main stat of item
    mainstat = random.choices(mainstats[item][0],mainstats[item][1])   
    subst_tpl = substats[(item,mainstat[0])]
    norm_probs = normalize(subst_tpl[1])

    # Roll substats types
    picked_substats = choice_numpy(subst_tpl[0],4,p=norm_probs,replace=False)
    
    stat_values = {}
    for stat in picked_substats:
        # Roll for initial values of stats
        stat_values[stat]=random.choice(stats_distribution[stat])

    # Roll for number of start substats (in practice number of rolls for substats)
    rolls_count = random.choices((4,5),(80,20))[0]
    for _ in range(rolls_count):
        stat_to_upgrade = random.choice(picked_substats)
        stat_values[stat_to_upgrade] += random.choice(stats_distribution[stat_to_upgrade])
    
    # Add item to list of farmed items
    return (item,mainstat[0],stat_values,picked_substats[:rolls_count-2])

def top_from_set_of_runs(n):
    # Returns dictionary of items. If best item did not drop, don't return that element
    top_set = {}

    #Generate list of all dropped items from dunegon.
    farmed_items=[]
    for _ in range(n):
        # Find how many items dropped in run
        items = 1 + random.choices((0,1),(93.5,6.5))[0]
        for _ in range(items):
            farmed_items.append(generate_artifact())

    circlet_cd =  [x[2]['cr%'] for x in farmed_items if x[0]=='circlet' and 'cd%' in x[1] and 'cr%' in x[2]]
    max_cr_cirlet_cd = max( circlet_cd,default=None )
    if max_cr_cirlet_cd :
        top_set['circlet_cd']=max_cr_cirlet_cd*2
    

    circlet_cr =  [x[2]['cd%'] for x in farmed_items if x[0]=='circlet' and 'cr%' in x[1] and 'cd%' in x[2]]
    max_cd_cirlet_cr = max( circlet_cr,default=None )
    if max_cd_cirlet_cr :
        top_set['circlet_cr']=max_cd_cirlet_cr

    feather_top = [ x[2]['cd%']+ x[2]['cr%']*2 for x in farmed_items if x[0]=='feather' and 'cr%' in x[2] and 'cd%' in x[2] ]
    max_feather = max(feather_top,default=None)
    if max_feather :
        top_set['feather']=max_feather

    flower_top = [ x[2]['cd%']+ x[2]['cr%']*2 for x in farmed_items if x[0]=='flower' and 'cr%' in x[2] and 'cd%' in x[2] ]
    max_flower = max(flower_top,default=None)
    if max_flower :
        top_set['flower']=max_flower

    # Goblet, Sands

    
    goblet_top = [ x[2]['cd%']+ x[2]['cr%']*2 for x in farmed_items if x[0]=='goblet' and x[1] in ('pyro' ,'electro'  ,'cryo' ,'hydro'    ,'anemo',   'geo'   ,'physical') and 'cr%' in x[2] and 'cd%' in x[2] ]
    max_goblet = max(goblet_top,default=None)
    if max_goblet :
        top_set['goblet']=max_goblet


    sands_top = [ x[2]['cd%']+ x[2]['cr%']*2 for x in farmed_items if x[0]=='sands' and x[1] in ('atk%') and 'cr%' in x[2] and 'cd%' in x[2] ]
    max_sands = max(sands_top,default=None)
    if max_sands :
        top_set['sands']=max_sands

    return top_set

# Now its good time to average the max outputs
def averaging_runs(tries_ammount=10000,runs_in_set=120):
    cumulative_stats = {}
    for _ in range(tries_ammount):
        best_items = top_from_set_of_runs(runs_in_set)
        for item in best_items.items():
            if item[0] not in cumulative_stats:
                cumulative_stats[item[0]]={'sum':0,'count':0}
            cumulative_stats[item[0]]['sum'] += item[1]
            cumulative_stats[item[0]]['count'] += 1

    for item in cumulative_stats:
        count = cumulative_stats[item]['count']
        avg_val = cumulative_stats[item]['sum']/count
        print (f'Item : {item} , average_value: {avg_val:{10}.{4}}, time actually got item in set of run : {count} per {tries_ammount} tries')



    
averaging_runs()
