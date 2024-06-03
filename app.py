from flask import Flask, jsonify,render_template,request
from database import all_invoice

app = Flask(__name__)



@app.route("/")
def homepage():
    invoice =  all_invoice()
    return render_template("home.html",invoice=invoice)





if __name__ == "__main__":
    app.run(debug=True)