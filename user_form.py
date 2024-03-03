from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/form')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Process form data
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        phone_number = request.form['phone_number']

        # Perform any additional processing here

        # Redirect to the main Streamlit page
        return redirect('http://localhost:8501')

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
