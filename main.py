translations = {
   'apple': ['malum', 'pomum', 'popula'],
   'fruit': ['baca', 'bacca', 'popum'],
   'punishment': ['malum', 'multa']
}
newdictionary={
   a:[i for i in translations .keys()
            if a in translations[i]]
           for k,a in translations .items() for a in a
}
print(newdictionary)