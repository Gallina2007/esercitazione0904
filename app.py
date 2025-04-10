from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route("/")
def profilo():
    df = pd.read_csv("profilo.csv")
    dati = df.iloc[0].to_dict()
    return render_template("profilo.html", dati=dati)


@app.route("/modifica", methods=["GET", "POST"])
def modifica():
    if request.method == "POST":
        nuovo_profilo = {
            "Nome": request.form["nome"],
            "Cognome": request.form["cognome"],
            "Scuola": request.form["scuola"],
            "Hobby": request.form["hobby"]
        }
        df = pd.DataFrame([nuovo_profilo])
        df.to_csv("profilo.csv", index=False)
        return redirect(url_for('index'))
    df = pd.read_csv("profilo.csv")
    dati = df.iloc[0].to_dict()
    return render_template("modifica.html", dati=dati)  




if __name__ == '__main__':
    app.run(debug=True) 