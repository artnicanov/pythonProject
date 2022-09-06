import json

def load_candidates():
	"""загружает данные из файла"""
	with open("candidates.json") as file:
		return json.load(file)

def get_all():
	"""показывает всех кандидатов"""
	return load_candidates()

def get_by_pk(pk):
	"""возвращает кандидата по pk"""
	canditates_data = load_candidates()
	for canditate in canditates_data:
		if pk == canditate["pk"]:
			return canditate

def get_by_skill(skill_name):
	"""возвращает кандидата по навыку"""
	canditates_data = load_candidates()
	canditates_list = []
	for canditate in canditates_data:
		if skill_name in canditate["skills"].lower():
			canditates_list.append(canditate)
	return canditates_list


