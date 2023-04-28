from flask import Blueprint, jsonify, abort, make_response, request
from app.models.cat import Cat
from app import db

cats_bp = Blueprint("cats", __name__, url_prefix="/cats")

# POST /cats
@cats_bp.route("", methods=["POST"])
def create_cat():
    request_body = request.get_json()
    new_cat = Cat(
        name=request_body["name"],
        color=request_body["color"],
        personality=request_body["personality"],
    )

    db.session.add(new_cat)
    db.session.commit()

    message = f"Cat {new_cat.name} successfully created"
    return make_response(message, 201)

# GET /cats
@cats_bp.route("", methods=["GET"])
def get_all_cats():
    cats = Cat.query.all()
    results = []
    for cat in cats: 
        results.append(
            dict(
                id=cat.id, 
                name=cat.name, 
                color=cat.color, 
                personality=cat.personality
            )
        )

    return jsonify(results)

# # GET /cats/<id>
# @bp.route("/<id>", methods=["GET"])
# def handle_cat(id):
#     cat = validate_cat(id)

#     return cat.to_dict()

# def validate_cat(id):
#     try:
#         id = int(id)
#     except:
#         abort(make_response({"message":f"cat {id} is invalid"}, 400))
    
#     for cat in cats:
#         if cat.id == id:
#             return cat
    
#     abort(make_response({"message":f"cat {id} not found"}, 404))
