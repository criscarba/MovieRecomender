from flask import Flask, render_template, request, jsonify
import pickle
import numpy as numpy
import pandas as pd
import yaml

#filename_similarities = parsed_yaml_file[USER]['sim_per_desc_model_metadata_indices']
loaded_model_indices = pickle.load(open('model_metadata_indices.pkl', 'rb'))
#filename_indices = parsed_yaml_file[USER]['sim_per_desc_model_metadata_similarities']
loaded_model_similarities = pickle.load(open('model_metadata_similarities_small.pkl', 'rb'))
#filename_titles = parsed_yaml_file[USER]['sim_per_desc_model_metadata_titles']
loaded_model_titles = pickle.load(open('model_metadata_titles.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('test.html')

@app.route('/predict', methods=['POST'])
def predecir():
	val_to_predict = request.form['pelicula']
	print(val_to_predict)
	prediction = get_recommendations_load_model(val_to_predict)
	return render_template('after.html', data=prediction, target=val_to_predict)
	#prediction = get_recommendations_load_model(val_to_predict)
    #val_to_predict = 'hola'
    #return render_template('after.html', data=prediction, movie=val_to_predict)
    
#Funcion de consumo del modelo
def get_recommendations_load_model(title):
    idx = loaded_model_indices[title]
    sim_scores = list(enumerate(loaded_model_similarities))
    sim_scores = sorted(sim_scores, reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return loaded_model_titles.iloc[movie_indices]

if __name__ == '__main__':
    app.run(debug=True)