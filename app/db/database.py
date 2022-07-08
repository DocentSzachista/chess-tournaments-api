import json

db = { "tournaments":
    [
        {
            "name": "eksallibur",
            "tempo": "rapid",
            "city": "Wroclaw",
            "country_state":  "DS",
            "tournament_state": "planned"
        },
        {
            "name": "eksallibur",
            "tempo": "blitz",
            "city": "Wroclaw",
            "country_state":  "DS",
            "tournament_state": "planned"
        },
        {
            "name": "eksalliburs",
            "tempo": "classic",
            "city": "Wroclaw",
            "country_state":  "DS",
            "tournament_state": "planned"
        }
    ]
}

def read_db(key)->list:
    return db[key]