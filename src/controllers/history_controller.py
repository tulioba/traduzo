from flask import Blueprint, jsonify
from src.models import history_model

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/history", methods=["GET"])
def list_hostory():
    return jsonify(history_model.list_history()), 200
