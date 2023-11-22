import json
from candidate import Candidate


def load_candidates_from_json(filename: str) -> list[Candidate]:
    arr = []
    data = None
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        id = item['id']
        name = item['name']
        picture = item['picture']
        position = item['position']
        gender = item['gender']
        age = item['age']
        skills = item['skills']
        arr.append(Candidate(id, name, picture, position, gender, age, skills))
    return arr


def get_candidate(candidate_id: int, arr: list[Candidate]) -> Candidate:

    for item in arr:
        if item.id == candidate_id:
            return item


def get_candidates_by_name(candidate_name: str, arr: list[Candidate]) -> list[Candidate]:
    ret_arr = []

    for item in arr:
        if candidate_name.lower() in item.name.lower():
            ret_arr.append(item)
    return ret_arr


def get_candidates_by_skill(skill_name: str, arr: list[Candidate]) -> list[Candidate]:
    ret_arr = []

    for item in arr:
        if skill_name.lower() in item.skills.lower():
            ret_arr.append(item)
    return ret_arr
