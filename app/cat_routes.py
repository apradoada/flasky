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

# GET /cats/<id>
@cats_bp.route("/<id>", methods=["GET"])
def handle_cat(id):
    cat = validate_cat(id)
    cat_dict = dict(
                id=cat.id, 
                name=cat.name, 
                color=cat.color, 
                personality=cat.personality
            )

    # If we don't specify a status code, Flask will default to 200 OK.
    # We can wrap `cat_dict`` in `jsonify``, but as a dictionary we
    # don't need to for Flask to understand how to format the response.
    return cat_dict

# PUT /cats/<id>
@cats_bp.route("/<id>", methods=["PUT"])
def replace_cat(id):
    cat_data = request.get_json()
    cat_to_update = validate_cat(id)

    cat_to_update.name = cat_data["name"]
    cat_to_update.color = cat_data["color"]
    cat_to_update.personality = cat_data["personality"]
    db.session.commit()

    return make_response(f"Cat {cat_to_update.name} updated", 200)

# DELETE /cats/<id>
@cats_bp.route("/<id>", methods=["DELETE"])
def delete_cat_by_id(id):
    cat_to_delete = validate_cat(id)
    db.session.delete(cat_to_delete)
    db.session.commit()

    message = f"Cat {cat_to_delete.name} deleted"
    return make_response(message, 200)

def validate_cat(id):
    try:
        id = int(id)
    except:
        message = f"cat {id} is invalid"
        abort(make_response({"message": message}, 400))
    
    cat = Cat.query.get(id)

    if not cat:
        message = f"cat {id} not found"
        abort(make_response({"message": message}, 404))

    return cat
