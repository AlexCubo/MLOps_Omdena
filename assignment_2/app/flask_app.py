#import modules
from area_of_field import area_in_acres
from flask import Flask, Request, request, jsonify
import json

#instantiate a flask object
app = Flask('__name__')

@app.route('/',methods = ['GET','POST'])
def get_input():
    ''' A Flask app to take inputs and invoce arear_in_acres
        module function and returns acres'''
    #packet = request.get_json()
    packet = request.get_json()
    length = packet['length']
    width = packet['width']
    area_acres = area_in_acres(length, width)
    #return jsonify(area_acres)
    return jsonify('length (feet):{}'.format(packet['length']),
                    'width (feet):{}'.format(packet['width']),
                    'area (acres):{}'.format(area_acres))#"Some other new String"

#main driver function
if __name__=='__main__':
    app.run(debug=True)
