from flask import Flask, render_template

app = Flask(__name__)

mahsulotlar = ["Noutbuk", "Telefon", "Planshet", "Quloqchin", "Kamera"]

@app.route("/")
def home():
    return render_template("index.html", mahsulotlar=mahsulotlar)

@app.route("/mahsulot/<int:indeks>")
def mahsulot_detail(indeks):
    if 0 <= indeks < len(mahsulotlar):
        return render_template("detail.html", mahsulot=mahsulotlar[indeks])
    else:
        return render_template("detail.html", mahsulot=None)

if __name__ == "__main__":
    app.run(debug=True)
