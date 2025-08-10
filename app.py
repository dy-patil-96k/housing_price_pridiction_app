from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# loading Model
model = joblib.load('housing_price_model.pkl')

@app.route('/')
def home():
      return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
      # request for json file
      data = request.get_json()
    
      # creating features from json file
      sqft_living = float(data.get('sqft_living'))
      sqft_above = float(data.get('sqft_above'))
      bathrooms = float(data.get('bathrooms'))
      view = float(data.get('view'))
      sqft_basement = float(data.get('sqft_basement'))
      bedrooms = float(data.get('bedrooms'))

      features = pd.DataFrame([[sqft_living, sqft_above, bathrooms, view, sqft_basement, bedrooms]],
                               columns=['sqft_living', 'sqft_above', 'bathrooms', 'view', 'sqft_basement', 'bedrooms'])

       # Reshape the features for prediction
      # features = [features]
    
      # Make prediction
      prediction = model.predict(features)
    
      # Return the prediction as a JSON response
      return jsonify({'predicted_price': prediction[0][0]})

if __name__ == '__main__':
    app.run(debug=True)