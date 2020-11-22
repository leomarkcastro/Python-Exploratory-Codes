
import keyword as k

words = ['elif', 'if', 'else', 'juggernaut', 'iskeyword', 'red', 'radio', 'head', 'wolf']

for i in words:
    if k.iskeyword(i):
        print(i, "is a keyword of python")

print (k.kwlist)