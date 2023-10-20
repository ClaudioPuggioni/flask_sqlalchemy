from app import app
from operator import itemgetter
from flask import request, jsonify
from db import db, User


@app.get("/")
def home():
    return "Hello, world"


@app.post("/users")
def addUser():
    content = request.json
    print(f"content: {content}")
    print(f"content.get('name'): {content.get('name')}")
    print(f"content.get('email'): {content.get('email')}")
    name, email = itemgetter("name", "email")(content)
    newUser = User(name=name, email=email)
    db.session.add(newUser)
    db.session.commit()
    return jsonify({"name": name, "email": email, "id": newUser.id})


@app.get("/users/all")
def allUsers():
    order = request.args.get("order", default=id, type=str)
    print(f"order: {order}")
    retrieved_list = (
        db.session.execute(db.select(User).order_by(getattr(User, order)))
        .scalars()
        .all()
    )
    print(f"retrieved_list: {retrieved_list}")
    return jsonify(
        {
            "result": [
                {"name": user.name, "id": user.id, "email": user.email}
                for user in retrieved_list
            ]
        }
    )
