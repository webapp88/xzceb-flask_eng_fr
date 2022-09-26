from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french(english_text):
    """english to french translation"""
    frenchtranslation=language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return frenchtranslation.get("translations")[0].get["translation"]


@app.route("/french_to_english")
def french_to_english(french_text):
    """frensh to english translation"""
    englishtranslation=language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return englishtranslation.get("translations")[0].get["translation"]


@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
