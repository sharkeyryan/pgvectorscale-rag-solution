from pydantic import BaseModel, Field

class Dog(BaseModel):
    name: str
    breed: str
    color: str
    gender: str
    age: int

kona = Dog(
    name = "Kona",
    breed = "Foodle",
    color = "Auburn",
    gender = "Female",
    age = 16
)

print(kona.name)

