# 🎯 IMG Capture

A full-stack Python Flask application that captures user media (camera) and redirects to a specified URL. The application features a beautiful UI with custom fonts and provides a command-line interface for easy management.

## ✨ Features

- **Media Capture**: Automatically requests camera permission and captures images
- **Instant Redirect**: Redirects users to a specified URL after capture
- **Beautiful UI**: Modern design with custom Orbitron font and gradient backgrounds
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Easy Management**: Command-line interface with 4 main options
- **Image Storage**: Saves captured images in `captured_img` folder with timestamps

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

### How It Works

1. **Launch the server** (Option 1)
2. **Open your browser** and go to `http://localhost:5000`
3. **Allow camera access** when prompted
4. **Image is captured** and saved automatically
5. **User is redirected** to the specified URL

## 📁 File Structure

```
imgcapture/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── config.json        # Configuration file (auto-generated)
├── captured_img/      # Directory for saved images
└── templates/
    └── index.html     # Web interface template
```

## 🔧 Configuration

The application automatically creates a `config.json` file that stores:
- `redirect_url`: The URL to redirect to after capture
- `first_launch`: Whether this is the first time running the app

## 🎨 UI Features

- **Custom Font**: Uses Orbitron font for a futuristic look
- **Gradient Background**: Beautiful purple gradient background
- **Glass Morphism**: Modern glass-like container design
- **Responsive**: Works on desktop and mobile devices
- **Loading Animations**: Smooth loading spinners and transitions

## 🔒 Privacy & Permissions

- The application requests camera permission from the user
- Images are saved locally in the `captured_img` folder
- No data is sent to external servers
- Camera stream is stopped immediately after capture

## 🛠️ Technical Details

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Media Capture**: HTML5 MediaDevices API
- **Image Format**: PNG with timestamped filenames
- **Cross-platform**: Uses platform-specific commands for folder opening

## 📸 Image Storage

Images are saved with the format: `capture_YYYYMMDD_HHMMSS.png`

Example: `capture_20231201_143022.png`

## 🚨 Troubleshooting

### Camera Access Issues
- Make sure your browser supports camera access
- Check if camera permissions are enabled in your browser
- Try refreshing the page if permission is denied

### Server Issues
- Make sure port 5000 is not in use
- Check if Flask is properly installed
- Ensure you're running the script from the correct directory

### Folder Opening Issues
- On Windows: Uses `explorer`
- On macOS: Uses `open`
- On Linux: Uses `xdg-open`

## 📝 License

This project is open source and available under the MIT License.

---

**Made with ❤️ using Python Flask and modern web technologies**