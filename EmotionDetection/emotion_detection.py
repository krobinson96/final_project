import requests
import json

def emotion_detector(data):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputJson = { "raw_document": { "text": data } }
    response = requests.post(url = URL, json = inputJson, headers = Headers)
    formatted_response = json.loads(response.text)

    anger = formatted_response["emotionPredictions"][0]['emotion']['anger']
    disgust = formatted_response["emotionPredictions"][0]['emotion']['disgust']
    fear = formatted_response["emotionPredictions"][0]['emotion']['fear']
    joy = formatted_response["emotionPredictions"][0]['emotion']['joy']
    sadness = formatted_response["emotionPredictions"][0]['emotion']['sadness']
    
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    highest_emotion = max([anger, disgust, fear, joy, sadness])
    dominant_emotion = emotions[[anger, disgust, fear, joy, sadness].index(highest_emotion)]

    myobj = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}
    
    return myobj