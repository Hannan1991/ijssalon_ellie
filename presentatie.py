def presenteer(dictionary, totaal):
 for key, value in dictionary.items():
     print(key, ':', value, 'euro')

 print('=')

 print('totaal :', totaal, 'euro')

mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}

totaal = 50
presenteer(mijn_dict, totaal)