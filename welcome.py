from flask import Flask, render_template, jsonify
from flask import request
import csv
import requests
from key import key
import imghdr
import filereader
app = Flask(__name__)


@app.route("/json_submit", methods=["POST"])
def writeTocsv():
	time = request.form['time']
	date = request.form['date']
	crime = request.form['crime']
	addr = request.form['addr']
	print time, date, crime
	fieldnames =['date','time','crime','addr']
	with open('crime.csv','a') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)

            # writerow() will write a row in your csv file
            writer.writerow({'date': date, 'time': time,'crime':crime,'addr':addr})
	return render_template('layout.html')

@app.route("/", methods=["GET"])
def retreive():
    return render_template('layout.html') 

@app.route("/hi", methods=["GET"])
def retreive1():
	lat,lang,crimeID = filereader.read_file()
	
	return render_template('test.html',lat=lat,lang = lang,crimeID=crimeID) 


@app.route("/sendRequest/<string:query>")
def results(query):
	search_payload = {"key":key, "query":query}
	search_req = requests.get(search_url, params=search_payload)
	search_json = search_req.json()

	photo_id = search_json["results"][0]["photos"][0]["photo_reference"]

	photo_payload = {"key" : key, "maxwidth" : 500, "maxwidth" : 500, "photoreference" : photo_id}
	photo_request = requests.get(photos_url, params=photo_payload)

	photo_type = imghdr.what("", photo_request.content)
	photo_name = "static/" + query + "." + photo_type

	with open(photo_name, "wb") as photo:
		photo.write(photo_request.content)

	return '<img src='+ photo_name + '>'


if __name__ ==  "__main__":
    app.run(debug=True)