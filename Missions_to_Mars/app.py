from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_db"
mongo = PyMongo(app)

@app.route("/")
def index():

    # access information from the database
    mars_data = mongo.db.marsData.find_one()
    print(mars_data)
    return render_template("index.html", mars = mars_data)

@app.route("/scrape")
def scrape():
    # refer to db collection
    mars_table = mongo.db.marsData

    mongo.db.marsData.drop()

    mars_data = scrape_mars.scrape_all()
    # print(mars_data)

    # load dict into MongoDB
    mars_table.insert_one(mars_data)

    # go back to the route
    return redirect("/")


if __name__ == "__main__":
    app.run(port=7000)


