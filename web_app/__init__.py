from flask import Flask

app = Flask(__name__)

# when someone visits the home page in the browser 
# trigger "home" function to display this message 

@app.route('/')
def home():
    return "THIS IS THE HOME PAGE"



if __name__ == '__main__':

    app.run(debug=True)