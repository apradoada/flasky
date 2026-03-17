from ..db import db
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    personality: Mapped[str]
    caretaker_id: Mapped[Optional[int]] = mapped_column(ForeignKey("caretaker.id"))
    caretaker: Mapped[Optional["Caretaker"]] = relationship(back_populates="cats")

    def to_dict(self):
        result = {
            "id": self.id, 
            "name": self.name, 
            "color": self.color,
            "personality": self.personality,
        }

        if self.caretaker_id:
            result.update({
                "caretaker_id": self.caretaker_id,
                "caretaker": self.caretaker.name
            })

        return result
    
    @classmethod
    def from_dict(cls, cat_data):
        return cls(name=cat_data["name"],
                    color=cat_data["color"],
                    personality=cat_data["personality"],
                    caretaker_id=cat_data.get("caretaker_id", None)
        )