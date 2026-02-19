from flask import Flask, request, render_template, url_for, redirect
from data_loader import CSV_Loader
import pickle
import numpy as np

app = Flask(__name__)

loader = CSV_Loader()
model = pickle.load(open('models/RandomForestModel.sav', 'rb'))
scaler =pickle.load(open('models/Scaler.sav', 'rb'))

@app.route("/")
def home():
    
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def get_city():
    if request.method == 'POST':
        city = request.form['city']
    return redirect(url_for('get_form_values', city=city))

@app.route('/forms/<city>', methods=['POST', 'GET'])
def get_form_values(city):
    # return f"<h1>{city}</h1>"
    if city in ['delhi', 'mumbai', 'pune']:
        city = city.capitalize()
    print(city)
    locations = loader.get_location(city)
    locations.sort()
    return render_template('form.html', locations=locations, city=city)

@app.route('/predictions', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        # print(request.form)
        numRooms = float(request.form['numRooms'])
        numBathrooms = float(request.form['numBathrooms'])
        numBalconies = float(request.form['numBalconies'])
        coordinates = loader.get_coordinates(request.form['city'],request.form['location'])
        houseSize = float(request.form['houseSize'])
        securityDeposit = float(request.form['securityDeposit'])
        configuration = int(request.form['configuration'])
        houseType = int(request.form['houseType'])
        negotiation = int(request.form['negotiation'])
        furnishing = int(request.form['furnishing'])
        data = [numRooms, coordinates['lat'], coordinates['lon'], numBathrooms, numBalconies, houseSize, securityDeposit, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        data[7+configuration] = 1
        data[9+ houseType] = 1
        data[15 + negotiation] = 1
        print(furnishing)
        data[17 + furnishing] = 1
        
        data = np.array(data)
        prediction = round(model.predict(scaler.transform(data.reshape(1,-1)))[0])
        
        return render_template('index.html', prediction=[prediction])
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=False)
