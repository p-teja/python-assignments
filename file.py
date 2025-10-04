a1 = "How long has this been going on?"
print(a1.index('h'))           # 9
print(a1.rindex('o'))          # 33
print(a1.find('been'))         # 17
print(a1.rfind('on'))          # 31
print(a1.replace('going', 'happening 😒'))  # How long has this been happening 😒 on?

a2 = "You've been creepin' 'round on me"
print(a2.index('e'))           # 3
print(a2.rindex('e'))          # 31
print(a2.find('been'))         # 7
print(a2.rfind('on'))          # 28
print(a2.replace("creepin'", 'sneakin 😀'))  # You've been sneakin 😀 'round on me

a3 = "While you're callin' me 'baby'"
print(a3.index('y'))           # 6
print(a3.rindex('y'))          # 29
print(a3.find("callin'"))      # 13
print(a3.rfind('me'))          # 21
print(a3.replace("'baby'", 'darling 💃'))  # While you're callin' me darling 💃

a4 = "How long has this been going on?"
print(a4.index('h'))           # 9
print(a4.rindex('o'))          # 33
print(a4.find('been'))         # 17
print(a4.rfind('on'))          # 31
print(a4.replace('going', 'rolling 🍥'))  # How long has this been rolling 🍥 on?

a5 = "You've been actin' so shady"
print(a5.index('b'))           # 7
print(a5.rindex('y'))          # 28
print(a5.find("actin'"))       # 13
print(a5.rfind('so'))          # 20
print(a5.replace("shady", 'weird 🤔'))  # You've been actin' so weird 🤔

a6 = "I've been feelin' it lately, baby"
print(a6.index('f'))           # 10
print(a6.rindex('y'))          # 31
print(a6.find("lately"))       # 22
print(a6.rfind('baby'))        # 29
print(a6.replace("feelin'", 'vibin 😎'))  # I've been vibin 😎 it lately, baby

a7 = "I'll admit it's my fault"
print(a7.index('m'))           # 16
print(a7.rindex('t'))          # 21
print(a7.find("fault"))        # 19
print(a7.rfind('my'))          # 16
print(a7.replace("fault", 'mistake 😬'))  # I'll admit it's my mistake 😬

a8 = "But you gotta believe me"
print(a8.index('g'))           # 8
print(a8.rindex('e'))          # 23
print(a8.find('believe'))      # 13
print(a8.rfind('me'))          # 21
print(a8.replace("believe", 'trust 🤝'))  # But you gotta trust 🤝 me

a9 = "When I say it only happened once"
print(a9.index('o'))           # 16
print(a9.rindex('e'))          # 32
print(a9.find('happened'))     # 20
print(a9.rfind('once'))        # 29
print(a9.replace("once", 'before ⏳'))  # When I say it only happened before ⏳

a10 = "I tried, and I tried, but you'll never see that"
print(a10.index('t'))          # 2
print(a10.rindex('t'))         # 43
print(a10.find("tried"))       # 2
print(a10.rfind("you'll"))     # 22
print(a10.replace("never", 'always 🫂'))  # I tried, and I tried, but you'll always 🫂 see that

