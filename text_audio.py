import os
import gtts

f = open("C:\\Users\\91990\\OneDrive\\Desktop\\file.txt")
text = f.read()
#text= "Wellcome to python"
t1 = gtts.gTTS(text=text, lang='en', slow=False)
os.remove("welcome1.mp3")

t1.save("welcome1.mp3")
f.close()
