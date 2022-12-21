from bottle import Bottle, template #run, #route, #template,
import pyjokes

app = Bottle()

@app.route('/')
def home():
    joke = pyjokes.get_joke()
    return template('home', joke = joke)




app.run(debug=True, reloader=True)