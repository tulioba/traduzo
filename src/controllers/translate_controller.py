from flask import Blueprint, render_template, request

from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        languages = LanguageModel.list_dicts()
        return render_template("index.html", languages=languages)
    elif request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        languages = LanguageModel.list_dicts()
        translated = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text_to_translate)

        return render_template(
            "index.html",
            translated=translated,
            translate_from=translate_from,
            translate_to=translate_to,
            languages=languages,
        )

    # languages = LanguageModel.list_dicts()
    # return render_template("index.html", languages=languages)


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    languages = LanguageModel.list_dicts()
    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        translated=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        languages=languages,
    )
