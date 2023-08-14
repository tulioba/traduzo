from flask import Blueprint, render_template, request

# from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    # if request.method == "GET":
    #     languages = LanguageModel.list_dicts()
    # print(languages)
    # return render_template("index.html", languages=languages)
    languages = LanguageModel.list_dicts()
    print(languages)
    return render_template("index.html", languages=languages)


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
