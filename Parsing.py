data='from stepen.marquad@uct.ac.za Sat Jan 5 09:14:16 2008'
atpa=data.find('@')
print(atpa)
appos= data.find(' ', atpa)
print(appos)
host=data[atpa+1:appos]
print(host)