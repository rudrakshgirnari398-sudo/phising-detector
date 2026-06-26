from flask import Flask, render_template, request

app = Flask(__name__)

def check_url(url):
    score = 0
    reasons = []

    if "@" in url:
        score += 1
        reasons.append("Contains @ symbol")

    if len(url) > 50:
        score += 1
        reasons.append("URL is too long")

    if "http://" in url:
        score += 1
        reasons.append("Uses HTTP instead of HTTPS")

    suspicious_words = ["login", "verify", "secure", "bank"]

    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious word: {word}")

    if score >= 3:
        return "Phishing Website", reasons
    else:
        return "Safe Website", reasons


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    reasons = []

    if request.method == "POST":
        url = request.form["url"]
        result, reasons = check_url(url)

    return render_template("index.html", result=result, reasons=reasons)


if __name__ == "__main__":
    app.run(debug=True)