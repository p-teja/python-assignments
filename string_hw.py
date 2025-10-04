#index()  
s = "Thappu chesinappudu nene baadha paduthanu" 
print(s.index('T'))  # 0 
print(s.index('c'))  # 7 
print(s.index('a'))  # 18 
print(s.index('n'))  # 27 
print(s.index('i'))  # ValueError (not found)

s = "Sweet Memory" 
print(s.index('e', -6, -1))  # 9  
print(s.index('r', -5, -1))  # 11  
print(s.index('o', -4, -1))  # 10  
print(s.index('y', -3, -1))  # 12  
print(s.index('M', -10, -1))  # 6  

#rindex
s = "Kalusina taruvatha ee hrudayam lo alochanalu maaripoyayi"
print(s.rindex('a'))  # 54 
print(s.rindex('n'))  # 52 
print(s.rindex('v'))  # 24 
print(s.rindex('i'))  # 49 
print(s.rindex('l'))  # 39  

#find
s = "Manasu chinnadi kaani feeling peru pedha"
print(s.find('M'))  # 0 
print(s.find('c'))  # 7 
print(s.find('d'))  # 13 
print(s.find('g'))  # 35 
print(s.find('x'))  # -1  

s = "Weekend vibe lo relax chesthunna"
print(s.count('e', -30, -1))  # 3 
print(s.find('x', -5))  # -1  

#rfind
s = "Oka chinna mistake ni marchipovadam manchi gurthulu isthundi"
print(s.rfind('a'))  # 51 
print(s.rfind('i'))  # 48 
print(s.rfind('z'))  # -1 
print(s.rfind("oka"))  # -1  
print(s.rfind("manchi"))  # 37 
print(s.rfind("a", 0, 20))  # 12  

#count
s = "Manasu lo emotions ni artham cheskoni decisions teesukovali"
print(s.count('a'))  # 3 
print(s.count('o'))  # 4 
print(s.count('r'))  # 1 
print(s.count('u'))  # 2 
print(s.count('z'))  # 0  

#replace  
s = "happy coding" 
print(s.replace('coding', 'learning'))  # happy learning 
print(s)

#Assignment  
s1 = "Manchi vishayam ki oka break kuda avasaram"
print(s1.replace("break", "pause"))  # Manchi vishayam ki oka pause kuda avasaram  

s2 = "Naaku kavalsina confidence naku dorakali"
print(s2.replace("confidence", "belief"))  # Naaku kavalsina belief naku dorakali  

s3 = "Oka baga telisina person ni kalavadaniki oka scope undali"
print(s3.replace("person", "partner"))  # Oka baga telisina partner ni kalavadaniki oka scope undali  

s4 = "Nuvvu entry ichinappudu prema ardham aindhi"
print(s4.replace("prema", "trust"))  # Nuvvu entry ichinappudu trust ardham aindhi  

s5 = "Prema lo kastalu unte andam untundi"
print(s5.replace("kastalu", "struggles"))  # Prema lo struggles unte andam untundi  
