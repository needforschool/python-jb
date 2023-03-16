import json

movie = {
    "title": "La reine des neiges",
    "author": "Disney",
    "year": 2013,
    "characters": [
        "Anna",
        "Elsa",
        "Kristoff",
        "Olaf",
        "Sven"
    ]
}

print(json.dumps(movie))