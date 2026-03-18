def test_get_all_cats_with_no_records(client):
    #Act
    response = client.get("/cats")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_cats_with_one_record(client, one_cat):
    #Act
    response = client.get("/cats")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "MOrty",
        "color": "Orange",
        "personality": "rechargeable"
    }]

def test_get_one_cat_succeeds(client, one_cat):
    #Act
    response = client.get("/cats/1")
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "MOrty",
        "color": "Orange",
        "personality": "rechargeable"
    }

def test_create_one_cat(client):
    #Act
    response = client.post("/cats", json={
        "name": "Ash and Alder",
        "color": "Grey and Tawny",
        "personality": "Stinker and Bouncy" 
    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Ash and Alder",
        "color": "Grey and Tawny",
        "personality": "Stinker and Bouncy" 
    }