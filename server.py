import requests
from flask import Flask, render_template
from time import sleep

app = Flask(__name__)

def get_latitude_longitude(robot_id):
    url = f'http://espia:strongpiopio042@52.161.96.125:3001/robot.log?{robot_id}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        parts = data.split(',')
        
        if len(parts) >= 4:
            latitude = float(parts[2])
            longitude = float(parts[3])
            return latitude, longitude
        else:
            return None, None
    else:
        return None, None

@app.route('/')
def index():
    robot_data = []
    
    for robot_id in range(1010, 1098):
        latitude, longitude = get_latitude_longitude(robot_id)
        if latitude is not None and longitude is not None:
            robot_data.append((robot_id, latitude, longitude))

    return render_template('index.html', robot_data=robot_data)

@app.route('/update')
def update():
    robot_data = []
    robots = [1010,1014,1017,1023,1024,1025,1026,1028,1031,1033,1041,1043,1044,1046,1048,1049,1050,1051,1060,1061,1062,1068,1069,1070,1071,1097,1098]
    for robot_id in robots:
        latitude, longitude = get_latitude_longitude(robot_id)
        if latitude is not None and longitude is not None:
            robot_data.append({"robot_id": robot_id, "latitude": latitude, "longitude": longitude})

    return {"robot_data": robot_data}


if __name__ == '__main__':
    while True:
        app.run()
        sleep(1)
