
import os, json
import traceback
import sys
from flask import render_template
from flask import request
from flask import Markup
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask import Flask, jsonify, make_response

from sloBertCommaPredictor import mark_up_placed_text_2, insert_commas
from lectorize_word_t5 import correct_word_mistakes

### because of local problem with m1 mac
#import os
#
#os.environ['KMP_DUPLICATE_LIB_OK']='True'
###

app = Flask(__name__, instance_relative_config=True)

app.config.from_object("postavljalec_vejic.config.Config")
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Zahtevek(db.Model):
    __tablename__ = 'zahtevek'

    id = db.Column(db.Integer, primary_key=True)
    stavek = db.Column(db.String())
    postavljen_stavek = db.Column(db.String())
    status_postavitve = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime())

    def __init__(self, stavek, postavljen_stavek, status_postavitve):
        self.stavek = stavek
        self.postavljen_stavek = postavljen_stavek
        self.status_postavitve = status_postavitve
        self.timestamp = datetime.now()

    def __repr__(self):
        return '<id {}>'.format(self.id)

if __name__ == "__main__":
    sys.setdefaultencoding('utf-8')
    app.run()

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def indexVejice():
    """
    Render the homepage.
    """
    if request.method == "GET":
        return render_template("postavljalec_vejic/index.html", poved="", originPoved="", sklanjajBesede=True, wrstniRedBesed=False, notCorrectNames=False)

    try:
        if not request.form.get("wo"):
            indexses_markup_vejice, vejice_opremljen_stavek = insert_commas(request.form.get("body"))
            print("postavljen_stavek: ", vejice_opremljen_stavek)
            print("indexses_markup_vejice: ", indexses_markup_vejice)

        if request.form.get("wo"):
            model_result = correct_word_mistakes(request.form.get("body"), True, request.form.get("sklanjaj"), True, request.form.get("names")) #request.form.get("names")
        else:
            model_result = correct_word_mistakes(vejice_opremljen_stavek, True, request.form.get("sklanjaj"), False, request.form.get("names"), indexses_markup_vejice)
            
            print("got result ")
        postavljen_stavek = ""

        
        if model_result[1] == 0:
            
            #postavljen_stavek = postavljen_stavek #model_result[0]
            # print("marking text up")
            # print("model_result[0]: ", model_result[0])
            # print("vejice_opremljen_stavek: ", vejice_opremljen_stavek)
            
            postavljen_stavek = model_result[0]
        else:
            postavljen_stavek = "Prišlo je do težave. Prosimo poizkusite ponovno."
    except Exception as e: 
        print(e)
        postavljen_stavek = "We've encountered an error, please try again. Probably one of entered sentences is too long."
    
    lastRowId = -1
    try:
        new_zahtevek = Zahtevek(stavek=request.form.get("body"), postavljen_stavek=postavljen_stavek, status_postavitve=0)
        
        db.session.add(new_zahtevek)
        db.session.commit()
        db.session.refresh(new_zahtevek)
        lastRowId = new_zahtevek.id
    except Exception:
        #traceback.print_exc()
        print("")

    sklanjaj = request.form.get("sklanjaj") != None
    wo = request.form.get("wo") != None
    names = request.form.get("names") != None
    
    
    return render_template("postavljalec_vejic/index.html", poved=Markup(postavljen_stavek), originPoved=request.form.get("body"), insertedRowId=str(lastRowId), sklanjajBesede=sklanjaj, wrstniRedBesed=wo, notCorrectNames=names)

@app.route("/postavi_vejice", methods=["POST"])
def postaviVejice():
    """
    Render the homepage.
    """
    
    besedilo = request.json.get("besedilo")
    popravljeno_besedilo = ""
    response_status = 500
    response = None
    
    if len(besedilo) < 3000:
        try:
            #popravljeno_besedilo = insert_commas(besedilo, True)
            popravljeno_besedilo = correct_word_mistakes(besedilo)[0]
            response_status = 200
        except Exception as e: 
            print(e)
            popravljeno_besedilo = "We've encountered an error, please try again. Probably one of entered sentences is too long."
            response_status = 500
    else:
        popravljeno_besedilo = "Žal ste vnesli predolgo besedilo."
        response_status = 400
        
    response = make_response(
    jsonify(
            { 
                "izvirnoBesedilo": besedilo,
                "popravljenoBesedilo": popravljeno_besedilo
            }
        ),
        response_status,
    )
    response.headers["Content-Type"] = "application/json"
        
    return response

@app.route("/google557336f80a7298db.html", methods=["GET"])
def googleDb():
    return render_template("google557336f80a7298db.html", poved="", originPoved="")

@app.route("/likeDislikeMarkedText", methods=["PUT"])
def likeDislikeMarkedText():
    id = request.form.get("markedTextId")
    ocena = request.form.get("textScore")

    zahtevek_za_ocenit = Zahtevek.query.get_or_404(id)

    try:
        zahtevek_za_ocenit.status_postavitve = ocena
        db.session.add(zahtevek_za_ocenit)
        db.session.commit()
    except Exception:
        traceback.print_exc()
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'} 

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

def queueAllZahtevki():

    zahtevki = Zahtevek.query.all()
    results = [
        {
            "stavek": zahtevek.stavek,
            "status_postavitve": zahtevek.status_postavitve
        } for zahtevek in zahtevki
    ]

    return results

# @app.route("/about", methods=["GET"])
# def aboutPageVejice():
#     """
#     Render the about page.
#     """
#     print("render about page")

#     return render_template("postavljalec_vejic/about.html")

# @app.route("/kolofon", methods=["GET"])
# def kolofonPageVejice():
#     """
#     Render the kolofon page.
#     """
#     print("render kolofon page")

#     return render_template("postavljalec_vejic/kolofon.html")

# @app.route("/arhivRazlicic", methods=["GET"])
# def arhivRazlicicPageVejice():
#     """
#     Render the arhiv razlicic page.
#     """
#     print("render arhiv razlicic page")

#     return render_template("postavljalec_vejic/arhivRazlicic.html")
