
from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)


@pytest.fixture
def mark_person():
    mock_data = {"firstname": "mark", "lastname": "smith", 
         "age": 13, "mark": 73.4}
    return mock_data

@pytest.fixture
def peter_get():
     mock_data = {"firstname": "Peter", "lastname": "Parker", 
         "age": 18, "mark": 93}
     return mock_data

@pytest.fixture
def mark_delete():
    mock_data = mock_data = {"Message": "Student deleted"}
    return mock_data

@pytest.fixture
def mark_update():
    mock_data = mock_data = {"firstname": "mark", "lastname": "smith", 
         "age": 13, "mark": 23}
    return mock_data


def test_create(mocker, mark_person):
    mock_data = mark_person
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data

    mocker.patch.object(client, "post", return_value=mock_response)

    response = client.post(" /create_student",
    json={"firstname": "mark", "lastname": "smith", 
         "age": 13, "mark": 73.4})
    assert response.status_code == 200
    assert response.json() == {"firstname": "mark", "lastname": "smith", 
         "age": 13, "mark": 73.4}

def test_get(mocker, peter_get):

    mock_data = peter_get
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data

    mocker.patch.object(client, "get", return_value=mock_response)

    response = client.get("/get_student",
    params={"name": "Peter"})
    assert response.status_code == 200
    assert response.json() == {"firstname": "Peter", "lastname": "Parker", 
         "age": 18, "mark": 93}


def test_update_student(mocker, mark_update):
    mock_data = mark_update
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data

    mocker.patch.object(client, "put", return_value=mock_response)

    response = client.put("/update_mark",
    params={"name": "mark", "mark": 23})
    
    assert response.status_code == 200
    assert response.json() == {"firstname": "mark", "lastname": "smith", 
         "age": 13, "mark": 23}

def test_delete(mocker, mark_delete):
    mock_data = mark_delete
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data

    mocker.patch.object(client, "delete", return_value=mock_response)


    response = client.delete("/delete_student",
    params={"name": "mark"})
    assert response.status_code == 200
    assert response.json() == {"Message": "Student deleted"}

