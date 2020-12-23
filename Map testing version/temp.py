from Map import all_maps

lst = []
for mp in all_maps:
    lst.append(mp.key)

lst2 = ['4HOTL', '4TOWN', 'LHOM4', '4SHOP', 'WORLD', 'TOWER', '1TWR1', '1TWR2', 'MNTN-', 'MNUP1', '2CAVE', '3TOWN', 'LHOM3', '3HOTL', '3SHOP', '2TOWN', 'LHOM2', '2HOTL', '2SHOP', 'HTOWN', 'LHOM1', 'HOUSE', '1CAVE', '1CVL1', 'MNUP2', '2CVL1', 'MNUP3', '2CVL2']

diff = []
for mp in lst:
    if mp not in lst2:
        diff.append(mp)

print(diff)