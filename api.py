"""
This API will be handling the voice and triggering the Neural network.
"""
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import wget
import inference_api
import os
import transcribe
import stetomono
import time

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



class AudioLink(Resource):       
    def post(self):
        print('received {}'.format(request.json))
        url = request.json["audio"]
        if os.path.exists("audio.wav"):
            os.remove("audio.wav")
        print('beggening download of {}'.format(url))
        wget.download(url, "audio.wav") # please remember to change this with a subprocess
        print('downloaded succesfully')
        print('cleaning')
        p = os.popen('python3 silenceremover.py 3 audio.wav') # creats cleaned.wav
        time.sleep(8)

        inference_api.main(False) # PLEASE CHANGE THIS HORRINDOUS THING INTO A SUBPROCESS AND DELETE THAT ABOMINATION
        print('done with the NN')
        # print('converting to mono')
        # try:
        #     stetomono.to_mono()
        # except:
        #     return('can\'t convert to mono for some reason.')
        
        print(p.read())
        print('transcribing')
        # try:
        transcription = transcribe.transcribe_file('cleaned.wav')
        # except:
        #     return('Please choose a file with a sample rate of an 8000 multiplication (16000,32000), reverting to last cached audio')

        return("Transcription : " + transcription)

api.add_resource(AudioLink, '/al') # This endpoint receives a direct wav URL

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5333, debug=True)
