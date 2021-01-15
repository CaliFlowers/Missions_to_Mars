from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/MarsDB")


@app.route("/")
def home():

    Mars_data = mongo.db.collection.find_one()
    print(Mars_data)

    return render_template("index.html", vacation = Mars_data)


@app.route("/scrape")
def scrape():

    Mars_data = scrape_mars.scrape_info()
    mongo.db.collection.update({}, Mars_data, upsert=True)
    return redirect("/")
    
    if __name__ == "__main__":
        app.run(debug=True)