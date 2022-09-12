from flask import Flask, request, render_template
import utils

app = Flask(__name__)



@app.route('/')
def index():
	candidates = utils.load_candidates_from_json()
	return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:id>')
def candidate_single(id):
	candidate = utils.get_candidate(id)
	return render_template('single.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def candidate_by_name(candidate_name):
	candidates = utils.get_candidates_by_name(candidate_name)
	candidates_len = len(candidates)
	return render_template('search.html', candidates=candidates, candidates_len=candidates_len)

@app.route('/skill/<skill_name>')
def candidate_by_skill(skill_name):
	candidates = utils.get_candidates_by_skill(skill_name)
	candidates_len = len(candidates)
	return render_template('skill.html', candidates=candidates, candidates_len=candidates_len, skill_name=skill_name)

app.run()