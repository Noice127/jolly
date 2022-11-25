from flask import Flask, render_template
import random

app = Flask('app')

#Christmas Songs
a = "https://www.youtube.com/embed/yXQViqx6GMY"
b = "https://www.youtube.com/embed/bwNV7TAWN3M"
c="https://www.youtube.com/embed/LUjn3RpkcKY"
d="https://www.youtube.com/embed/uOJWI5RAOyY"
e="https://www.youtube.com/embed/j-_1-uJ6Ml4"
f="https://www.youtube.com/embed/HTCFi4l3nkY"
g="https://www.youtube.com/embed/F1itSKJLWQY"
h="hhttps://www.youtube.com/embed/hLf0-lro8X8"
i="https://www.youtube.com/embed/xvHQO9LT6ZI"
j="https://www.youtube.com/embed/4vx6MeuSHw4"
k="https://www.youtube.com/embed/5vyMuxxLsD0"
l="https://www.youtube.com/embed/AaQa2jfoWE8"
m="https://www.youtube.com/embed/sE3uRRFVsmc"
n="https://www.youtube.com/embed/73UqDX_quk0"
o = "https://www.youtube.com/embed/JnS7fDiw34Q"
p = "https://www.youtube.com/embed/nlR0MkrRklg"
q = "https://www.youtube.com/embed/EM2Fnp_qnE8"
r = "https://www.youtube.com/embed/3ZT9_H4-hbM"
s = "https://www.youtube.com/embed/KZk8XkV-jGM"
t = "https://www.youtube.com/embed/eQ1r761EhWA"
u = "https://www.youtube.com/embed/A4zBSnMhvI0"
v = "https://www.youtube.com/embed/iJfjZeiRi3g"
w = "https://www.youtube.com/embed/QArOV1bsISo"
x = "https://www.youtube.com/embed/nI9Bg38BKCk"
y = "https://www.youtube.com/embed/bMjlK8DYf1g"
z = "https://www.youtube.com/embed/aAkMkVFwAoo"

#array of songs 
youtube = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]


christmas = random.choice(youtube)
  
@app.route('/')
def home():
  return render_template('index.html', christmas=christmas)
  
  

app.run(host='0.0.0.0', port=8080)
