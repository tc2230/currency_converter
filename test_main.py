from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_example_input():
    source = "USD"
    target = "JPY"
    amount = "1,525" # with separator
    response = client.get(f"/convert_currency?source={source}&target={target}&amount={amount}")
    assert response.status_code == 200
    assert response.json() == {"msg": "successful", "amount": "170,496.53"}

def test_amount_without_separator():
    source = "USD"
    target = "JPY"
    amount = "1525" # without separator
    response = client.get(f"/convert_currency?source={source}&target={target}&amount={amount}")
    assert response.status_code == 200
    assert response.json() == {"msg": "successful", "amount": "170,496.53"}

def test_amount_with_decimal():
    source = "USD"
    target = "TWD"
    amount = "10.125" # with decimal 
    response = client.get(f"/convert_currency?source={source}&target={target}&amount={amount}")
    assert response.status_code == 200
    assert response.json() == {"msg": "successful", "amount": "308.40"}

def test_invalid_source():
    source = "DUNE" # invalid source
    target = "USD"
    amount = "1,525" 
    response = client.get(f"/convert_currency?source={source}&target={target}&amount={amount}")
    assert response.status_code == 200
    assert response.json() == {"msg": "failed: Unrecognized curreny option", "amount": None}

def test_invalid_target():
    source = "TWD"
    target = "AGEFACTORY" # invalid target
    amount = "1,525" 
    response = client.get(f"/convert_currency?source={source}&target={target}&amount={amount}")
    assert response.status_code == 200
    assert response.json() == {"msg": "failed: Unrecognized curreny option", "amount": None}

def test_invalid_separator():
    source = "TWD"
    target = "JPY"
    amount = "10,200,33.1234" # invalide thousand separator
    response = client.get(f"/convert_currency?source={source}&target={target}&amount={amount}")
    assert response.status_code == 200
    assert response.json() == {"msg": "failed: Invalid input amount", "amount": None}

def test_invalid_character():
    source = "USD"
    target = "JPY"
    amount = "1e525-" # invalid character
    response = client.get(f"/convert_currency?source={source}&target={target}&amount={amount}")
    assert response.status_code == 200
    assert response.json() == {"msg": "failed: Invalid input amount", "amount": None}

def test_negative_amount():
    source = "USD"
    target = "JPY"
    amount = "-1,525" # negative
    response = client.get(f"/convert_currency?source={source}&target={target}&amount={amount}")
    assert response.status_code == 200
    assert response.json() == {"msg": "failed: Invalid input amount", "amount": None}

def test_zero_heading():
    source = "USD"
    target = "JPY"
    amount = "0234.123" # zero heading
    response = client.get(f"/convert_currency?source={source}&target={target}&amount={amount}")
    assert response.status_code == 200
    assert response.json() == {"msg": "failed: Invalid input amount", "amount": None}