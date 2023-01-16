import json

if __name__ == '__main__':
    with open("data/my_persons.json", "r") as fh:
        persons = json.load(fh)

    print(f"We already have {len(persons)} in our db")
    for i in range(3):
        name = input("Name: ")
        per_id = input("id: ")
        year = input("year: ")
        persons.append({
            'name': name,
            'id': per_id,
            'year': year
        })
    with open("data/my_persons.json", "w") as fh:
        json.dump(persons, fh)