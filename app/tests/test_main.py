from fastapi.testclient import TestClient
import pytest

from ..main import app
from ..db import database

client = TestClient(app)


@pytest.fixture 
def tournament_db():
    return database.read_db("tournaments")

@pytest.mark.parametrize("index,status_code",[ (0, 200), (1, 200), (4, 404), (3, 404) ])
def test_retrieve_single_row(index, status_code):
    resp = client.get(f"/tournaments/{index}")
    assert resp.status_code == status_code

def test_retrieve_tournaments(tournament_db):
    resp = client.get("/tournaments")
    
    assert resp.status_code == 200
    assert tournament_db == resp.json()


def test_post_tournament():
    resp = client.post("/tournaments", 
    {
        "name": "chess international 2022 in Wroclaw",
        "city": "Wrocław",
        "address": "Krajowa 8",
        "tempo": "classic",
        "countryState": "DS",
        "startDate": "10.08.2022",
        "endDate": "10.08.2022"
    }
)
    assert resp.status_code == 200