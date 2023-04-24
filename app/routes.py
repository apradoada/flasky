from flask import Blueprint, jsonify, abort, make_response

class Cat:
    def __init__(self, id, name, color, personality):
        self.id = id
        self.name = name
        self.color = color
        self.personality = personality

    def to_dict(self):
        return dict(
            id=self.id, 
            name=self.name, 
            color=self.color, 
            personality=self.personality
        )

cats = [ 
    Cat(1, "Luna", "grey", "naughty"), 
    Cat(2, "Orange Cat", "orange", "antagonistic"),
    Cat(3, "Big Ears", "grey and white", "sleepy")
]

bp = Blueprint("cats", __name__, url_prefix="/cats")

# GET /cats
@bp.route("", methods=["GET"])
def handle_cats():
    results = []
    for cat in cats: 
        results.append(cat.to_dict())

    return jsonify(results)

# GET /cats/<id>
@bp.route("/<id>", methods=["GET"])
def handle_cat(id):
    cat = validate_cat(id)

    return cat.to_dict()

def validate_cat(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"cat {id} is invalid"}, 400))
    
    for cat in cats:
        if cat.id == id:
            return cat
    
    abort(make_response({"message":f"cat {id} not found"}, 404))
