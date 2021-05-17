# web_app/routes/email_routes.py

from flask import Blueprint, jsonify

email_routes = Blueprint("email_routes", __name__)

@email_routes.route("/email")
@email_routes.route("/email.json")
def list_books():
    print("EMAIL")
    books = [
        {"id": 1, "title": "Book 1", "year": 1957},
        {"id": 2, "title": "Book 2", "year": 1990},
        {"id": 3, "title": "Book 3", "year": 2031},
    ] # some dummy / placeholder data
    return jsonify(email)
#
#@email_routes.route("/email/<int:book_id>")
#@email_routes.route("/email/<int:book_id>.json")
#def get_book(book_id):
#    print("BOOK...", book_id)
#    book = {"id": book_id, "title": f"Example Book", "year": 2000} # some dummy / placeholder data
#    return jsonify(book)