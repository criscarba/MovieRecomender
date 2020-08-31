from flask import Flask, render_template, request, jsonify
import pickle
import numpy as numpy
import pandas as pd
#import yaml

#USER = 'CRISTIAN'
#a_yaml_file = open("links.yml")
#parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

#Lectura de los Modelos
#filename_similarities = parsed_yaml_file[USER]['sim_per_desc_model_metadata_indices']
#loaded_model_indices = pickle.load(open(filename_similarities, 'rb'))
#filename_indices = parsed_yaml_file[USER]['sim_per_desc_model_metadata_similarities']
#loaded_model_similarities = pickle.load(open(filename_indices, 'rb'))
#filename_titles = parsed_yaml_file[USER]['sim_per_desc_model_metadata_titles']
#loaded_model_titles = pickle.load(open(filename_titles, 'rb'))

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('movie_index.html')

@app.route('/predict', methods=['POST'])
def predecir():
	#val_to_predict = request.form['pelicula']
	#prediction = get_recommendations_load_model(val_to_predict)
    val_to_predict = 'hola'
    prediction = 'prediccion'
	return render_template('movie_prediction.html', data=prediction, target=val_to_predict)

#Funcion de consumo del modelo
#def get_recommendations_load_model(title):
#    idx = loaded_model_indices[title]
#    sim_scores = list(enumerate(loaded_model_similarities[idx]))
#    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#    sim_scores = sim_scores[1:31]
#    movie_indices = [i[0] for i in sim_scores]
#    return loaded_model_titles.iloc[movie_indices]


if __name__ == '__main__':
    app.run(debug=True)