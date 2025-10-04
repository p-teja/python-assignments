print(1,2,3,4,5,56,sep="-",end="\n")
print("hello world")
a=12
b=23
print("sum of numbers are",int(a)+int(b))


#formating string FIRST METHOD
print("my name is ravi teja")
print("my name is show man")
# for strings %s
# fro int's %d
#for floating valuess %f
print("my name is %s iam from %s" %('raviteja','ts'))
print("my name is %s my weight is  %d" %('raviteja',56))
print("my name is %s my height is  %f" %('raviteja',5.8))

# formating string SECOND METHOD{.format}
msg="today is {}".format("friday")
print(msg)

# formating string third METHOD  literals

title="kingdom"
hero="VD"
heroin="bhagya"
b=f"the movie name is {title},hero in that is {hero}, and heroin is {heroin}"
print(b)



