from flask import Flask,render_template,url_for,request
import pickle
import pandas as pd

application = Flask(__name__)
app = application


#imprting the pkile file 

model = pickle.load(open('models/diabetes.pkl','rb'))

@app.route('/')

def wel():
    return render_template('welcome.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Fetch the input values from the form
            Pregnancies = float(request.form.get('Pregnancies'))
            Glucose = float(request.form.get('Glucose'))
            BloodPressure = float(request.form.get('BloodPressure'))
            SkinThickness = float(request.form.get('SkinThickness'))
            Insulin = float(request.form.get('Insulin'))
            BMI = float(request.form.get('BMI'))
            DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
            Age = float(request.form.get('Age'))

            # Prepare the data in the same format used for training
            input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]

            # Step 2: Predict using the model
            prediction = model.predict(input_data)

            # Get the prediction result
            result = 'Positive' if prediction[0] == 1 else 'Negative'

            return render_template('home.html', result=result)

        except Exception as e:
            # Print the error message to the terminal/logs for debugging
            print(f"Error: {e}")
            return render_template('home.html', result=f"Error in prediction: {str(e)}")
        
    return render_template('home.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)


    