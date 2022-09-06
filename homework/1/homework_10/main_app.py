from flask import Flask
import utils

app = Flask(__name__)

# представление для роута главной страницы
@app.route("/")
def index():
	candidates = utils.get_all()
	candidates_output = ""
	for candidate in candidates:
		candidates_output += candidate["name"] + "\n"
		candidates_output += candidate["position"] + "\n"
		candidates_output += candidate["skills"] + "\n"
		candidates_output += "\n"
	return f"<pre> {candidates_output} </pre>"

# представление для роута кандидата по его номеру
@app.route("/candidates/<int:pk>/")
def candidate_pk(pk):
	candidate = utils.get_by_pk(pk)
	candidate_output = ''
	candidate_output += candidate["name"] + "\n"
	candidate_output += candidate["position"] + "\n"
	candidate_output += candidate["skills"] + "\n"
	candidate_output += "\n"
	return f"""
	<img src={candidate["picture"]}>
	<pre>{candidate_output}</pre>
	"""

# представление для роута кандидата по его навыкам
@app.route("/candidates/<skill_name>/")
def candidate_skills(skill_name):
	candidates = utils.get_by_skill(skill_name.lower()) # вывод не зависит от регистра ввода
	candidate_output = ''
	for candidate in candidates:
		candidate_output += candidate["name"] + "\n"
		candidate_output += candidate["position"] + "\n"
		candidate_output += candidate["skills"] + "\n"
		candidate_output += "\n"
	return f"<pre>{candidate_output}</pre>"

app.run(debug=True, port=5001)