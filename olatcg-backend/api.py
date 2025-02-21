from flask import Flask, Blueprint
from view.seqAlignmentView import seqAlignmentView
from view.homologySearchView import homologySearchView
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.register_blueprint(seqAlignmentView)
app.register_blueprint(homologySearchView)