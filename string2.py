#method related to string

text="helloworld"
text_upper=text.upper()

print("The data in uppercase is",text_upper)

text_lower=text.lower()

print("the data in lowercase is",text_lower)

name="RajGopal"
newname=name.strip()
print("the data without space is",newname)
Ispace=name.Istrip()
print("the data without space is",Ispace)
rspace=name.rstrip()
print("the data without space is ",rspace)

#str.replace(old,new): this method replaces all occurences of the "old" substring
#with the "new" substring in the string.

sentences= "I like apples, and I like pineapple."
new_sentence= sentence.replace("like," "love")
print(new_sentence)
#"I love apples, and I love"pineapple."


