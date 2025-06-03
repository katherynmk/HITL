from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        features = request.form['input_data']
        prediction = model.predict([features])
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
