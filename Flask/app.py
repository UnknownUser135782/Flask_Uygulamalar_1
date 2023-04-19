from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.errorhandler(404)
def error(e):
    return render_template('404.html')

@app.route("/küp_hacmi", methods=['GET','POST'])
def küp_hacmi_bulma():
    if request.method == 'POST':
        küp_kenar = request.form['küp_kenar']
        küp_hacim = float(küp_kenar)**3
        küp_yüzey = float(küp_kenar)*6
        return render_template('küp_hacmi.html', küp_hacim=küp_hacim, küp_yüzey=küp_yüzey)
    return render_template('küp_hacmi.html')

@app.route("/pisagor", methods=['GET','POST'])
def pisagor():
    if request.method == 'POST':
        kenar_1 = request.form['kenar_1']
        kenar_2 = request.form['kenar_2']
        pisagor_sonuç_kare  = float(kenar_1)**2 + float(kenar_2)**2
        pisagor_sonuç = pisagor_sonuç_kare**0.5
        return render_template('pisagor.html', pisagor_sonuç=pisagor_sonuç)
    return render_template('pisagor.html')

@app.route("/sayfa_3")
def sayfa_3():
    return render_template('sayfa_3.html')


if __name__  == "__main__":
    app.run(debug=True)

