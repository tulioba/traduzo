import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    # text_to_test = [
    #     {
    #         {
    #             "text_to_translate": "Hello, I like videogame",
    #             "translate_from": "en",
    #             "translate_to": "pt",
    #         },
    #         {
    #             "text_to_translate": "Do you love music?",
    #             "translate_from": "en",
    #             "translate_to": "pt",
    #         },
    #     }
    # ]

    history = HistoryModel.list_as_json()
    result = json.loads(history)

    # assert result == text_to_test

    assert len(result) == 2
    assert result[0]["text_to_translate"] == "Hello, I like videogame"
    assert result[0]["translate_from"] == "en"
    assert result[0]["translate_to"] == "pt"
    assert result[1]["text_to_translate"] == "Do you love music?"
    assert result[1]["translate_from"] == "en"
    assert result[1]["translate_to"] == "pt"
