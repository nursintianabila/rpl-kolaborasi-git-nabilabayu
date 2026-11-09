from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


def salam_waktu(jam):
    if 4 <= jam <= 10:
        return "Selamat pagi"
    if 11 <= jam <= 14:
        return "Selamat siang"
    if 15 <= jam <= 17:
        return "Selamat sore"
    return "Selamat malam"


@app.route("/", methods=["GET", "POST"])
def beranda():
    # Ambil nama hanya setelah formulir dikirim.
    nama = request.form.get("nama", "").strip() if request.method == "POST" else ""
    sekarang = datetime.now()
    waktu_server = sekarang.strftime("%d-%m-%Y %H:%M:%S")
    salam = salam_waktu(sekarang.hour)
    return render_template(
        "index.html", nama=nama, salam=salam, waktu_server=waktu_server
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)