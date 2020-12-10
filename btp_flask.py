import os
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)


# Read all data into global dataframe
DF = pd.read_csv('static/final.csv')
DF['STATE'] = DF['STATE'].str.upper()
DF['STATION CODE'] = DF['STATION CODE'].astype('int32')
DF['WQI'] = DF['WQI'].round(3)


@app.route('/', methods = ['GET'])
def main():
    return render_template('index.html')


@app.route('/wqi', methods=['GET'])
def wqi():
    states = DF['STATE'].unique()
    return render_template('wqi.html', states=states)


@app.route('/stations/<state>', methods=['GET'])
def get_stations(state):
    stations = DF.loc[DF['STATE'] == state, ['STATION CODE', 'LOCATIONS']].sort_values(by=['STATION CODE'])
    stations.reset_index(inplace=True, drop=True)
    return jsonify({'stations': stations.to_dict('index')})


@app.route('/wqi/<station_code>', methods=['GET'])
def get_wqi(station_code):
    wqi = DF.loc[DF['STATION CODE'] == int(station_code), 'WQI'].values[0]
    return jsonify({"WQI": wqi})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
