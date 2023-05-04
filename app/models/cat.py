from app import db

class Cat(db.Model):
    id = db.Column(
            db.Integer, 
            primary_key=True, 
            autoincrement=True)
    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    personality = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "color": self.color,
                "personality": self.personality
                }
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name = data_dict["name"],
            color = data_dict["color"],
            personality = data_dict["personality"]
        )
    
        # return dict(
        #         id=self.id, 
        #         name=self.name, 
        #         color=self.color, 
        #         personality=self.personality
        #     )


# class Cat:
#     def __init__(self, id, name, color, personality):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.personality = personality

#     def to_dict(self):
        # return dict(
        #     id=self.id, 
        #     name=self.name, 
        #     color=self.color, 
        #     personality=self.personality
        # )

# cats = [ 
#     Cat(1, "Luna", "grey", "naughty"), 
#     Cat(2, "Orange Cat", "orange", "antagonistic"),
#     Cat(3, "Big Ears", "grey and white", "sleepy")
# ]