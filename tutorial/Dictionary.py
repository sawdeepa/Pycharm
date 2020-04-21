d={'H':'Hydrogen','O':'Oxygen'}
print(type(d))
print(d.keys())
print(d.values())
print(d.items())
print(d['H'])
print(d.get('H'))
d['C']='Carbon'
print (d)
del d['H']
print (d)