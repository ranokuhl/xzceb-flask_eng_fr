from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench/<text_to_translate>")
def englishToFrench(text_to_translate):
    translated_text = request.args.get(text_to_translate)
    # Write your code here
    return translator.english_to_french(translated_text)
    # return "Translated text to French"

@app.route("/frenchToEnglish/<text_to_translate>")
def frenchToEnglish(text_to_translate):
    translated_text = request.args.get('text_to_translate')
    # Write your code here
    return translator.french_to_english(translated_text)
    # return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
