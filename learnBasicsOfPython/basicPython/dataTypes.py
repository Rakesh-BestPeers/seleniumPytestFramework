# Python has the following data types built-in by default, in these categories:

# Boolean Type:	bool
print(type(True))
print(type(False))

# Text Type:	str
text='Rakesh'
print(text,type(text))

# Numeric Types:	int, float, complex
x=20
print(x,type(x))

y=2.15
print(y,type(y))

z=11+10j
print(z,type(z))

# Sequence Types:	list, tuple, range
List=[[['Rakesh'],['Singh'],['Thakur']]]
print(List,type(List))

Tuple1 = ('python','java')
Tuple2=(1,2,3,4,5,6,7,8,9,0)
Tuple3=(Tuple1,Tuple2)
print(Tuple3,type(Tuple3))

x=range(5)
for n in x:
    print(n)

# Mapping Type:	dict
Dict={'Name':'Geeks',1:[1,2,3,4]}
print(Dict,type(Dict))

# Set Types:	set, frozenset
set1=set(["Geeks","For","Geeks"])
print(set1,type(set1))