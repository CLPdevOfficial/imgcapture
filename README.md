# 🎯 IMG Capture

A bsic stack Python Flask application that captures user media (camera) and redirects to a specified URL. 

## 🚀 Installation

1. **Clone or download the project**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📱 Usage

### First Time Setup
When you run the application for the first time, it will ask you to:
1. Enter a URL to redirect to after capture
2. The URL will be saved for future use

### Main Menu Options

Run the application:
```bash
python app.py
```

You'll see a menu with 4 options:

1. **Launch application (start server)** - Starts the Flask server
2. **Open saved images folder** - Opens the `captured_img` directory
3. **Change redirect URL** - Update the URL to redirect to
4. **Exit** - Close the application
5. 
## 🔧 Configuration

The application automatically creates a `config.json` file that stores:
- `redirect_url`: The URL to redirect to after capture
- `first_launch`: Whether this is the first time running the app

## 🔒 Privacy & Permissions

- The application requests camera permission from the user
- Images are saved locally in the `captured_img` folder
- No data is sent to external servers
- Camera stream is stopped immediately after capture
- Always use this ETHICALLY 

## 📸 Image Storage

Images are saved with the format: `capture_YYYYMMDD_HHMMSS.png`

Example: `capture_20231201_143022.png`

## 📝 License



**Made using flask**
