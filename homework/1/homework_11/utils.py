import json


def load_candidates_from_json():
	"""возвращает список всех кандидатов"""
	path = "candidates.json"
	with open(path) as file:
		return json.load(file)

def get_candidate(candidate_id):
	"""возвращает одного кандидата по его id"""
	for candidate in load_candidates_from_json():
		if candidate_id == candidate["id"]:
			return candidate

def get_candidates_by_name(candidate_name):
	"""возвращает кандидатов по имени"""
	candidates_list = []
	for candidate in load_candidates_from_json():
		if candidate_name.lower() in candidate["name"].lower():
			candidates_list.append(candidate)
	return candidates_list

def get_candidates_by_skill(skill_name):
	"""возвращает кандидатов по навыку"""
	candidates_list = []
	for candidate in load_candidates_from_json():
		if skill_name.lower() in candidate["skills"].lower().split(", "):
			candidates_list.append(candidate)
	return candidates_list
