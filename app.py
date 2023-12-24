# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 12:29:34 2023

@author: DELL
"""

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the recommendation data
df_result = pd.read_csv('MovieRecommendations.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    search_movie = request.form['movie']
    list_result = df_result[df_result['title'] == search_movie]

    if not list_result.empty:
        recommendations = list_result.iloc[0, 7:11].values
        return render_template('index.html', recommendations=recommendations, movie=search_movie)
    else:
        return render_template('index.html', recommendations=["Movie not found in the recommendations."])

if __name__ == '__main__':
    app.run(debug=True)
