from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    mesaj = ""
    show_dogrulama = False

    if request.method == "POST":
        isim = request.form.get("isim")
        miktar = request.form.get("miktar")

        # Başarısız mesaj ve doğrulama görselini göster
        mesaj = "Başarısız ❌ doğrulama eksik."
        show_dogrulama = True

    return render_template("index.html", mesaj=mesaj, show_dogrulama=show_dogrulama)

@app.route("/dogrulamasayfasi")
def dogrulama():
    return render_template("dogrulamasayfasi.html")

# Render için app.run() gerekmiyor
if __name__ == "__main__":
   
    pass
