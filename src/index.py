from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/data')
def about():
    return render_template("dataT.html")


@app.route('/tabla-casos-continente')
def table1():
    return render_template("tCasCon.html")


@app.route('/tabla-muertes-continente')
def table2():
    return render_template("tMueCon.html")


@app.route('/tabla-muertes-paises-no-pobres')
def table3():
    return render_template("tMueNPobres.html")


@app.route('/tabla-muertes-paises-pobres')
def table4():
    return render_template("tMuePobres.html")


@app.route('/tabla-casos-colombia')
def table5():
    return render_template("tCasCol.html")


@app.route('/tabla-muertes-colombia')
def table6():
    return render_template("tMueCol.html")


if __name__ == '__main__':
    app.run(debug=True)
