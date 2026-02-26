from flask import Flask, jsonify, send_from_directory, request
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')

@app.route('/api/apps')
def get_apps():
    # Сервер сам определит свой адрес (например, https://my-market.onrender.com)
    domain = request.host_url.rstrip('/') 
    
    apps_data = [
        {
            "id": 1,
            "title": "Minecraft",
            "developer": "Mojang",
            "price": "Free",
            "icon_url": f"{domain}/files/mc.png",
            "apk_url": f"{domain}/files/mc.apk"
        },
        {
            "id": 2,
            "title": "Cut The Rope",
            "developer": "ZeptoLab",
            "price": "Free",
            "icon_url": f"{domain}/files/cut.png",
            "apk_url": f"{domain}/files/cut.apk"
        }
    ]
    return jsonify({"data": apps_data})

@app.route('/files/<path:filename>')
def serve_files(filename):
    return send_from_directory(FILES_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
