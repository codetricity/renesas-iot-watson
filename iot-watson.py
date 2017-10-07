import json

with open('iot.json') as json_data:
    d = json.load(json_data)
    sensor_data = (d['with'][0]['content']['sensors'])
    watson_data = "\"The current temperature in Fahrenheit is " + \
        str(sensor_data['TemperatureF']) + ". "
    watson_data += "Sound level is " + str(sensor_data['SoundLevel']) + ".\""
    # print(watson_data)
    watson_file = open('watson.dat', 'w')
    watson_file.write(watson_data)
