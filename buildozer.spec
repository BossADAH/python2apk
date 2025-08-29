
[app]

# (str) Title of your application
title = PortScan Lite

# (str) Package name (all lowercase, no spaces)
package.name = portscanlite

# (str) Package domain (reverse domain style, unique)
package.domain = pot.SCAN.ai

# (str) Source code where your main.py lives
source.dir = .

# (str) The main .py file
source.main = main.py

# (str) Version of your app
version = 1.0.0

# (list) Application requirements
# You can add more libraries separated by commas
requirements = python3,kivy

# (str) Entry point for Kivy
fullscreen = 0

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
#fullscreen = 0

# (list) Permissions your app might need
android.permissions = INTERNET

# (str) Application icon (put your .png in the project root and name it icon.png)
#icon.filename = %(source.dir)s/icon.png

# (str) Presplash screen (optional)
#presplash.filename = %(source.dir)s/presplash.png

# (list) Presplash background color (R,G,B) between 0-1
# Example: 1,1,1 for white
presplash_color = 1,1,1

# (str) Supported android API (don’t change unless you know why)
android.api = 31

# (str) Minimum API your app will support
android.minapi = 21

# (str) Android SDK/NDK versions
android.sdk = 20
android.ndk = 25b

# (str) Android entry point, don’t touch
entrypoint = org.kivy.android.PythonActivity

# (bool) Indicate if you want to include SDL2
osx.kivy_version = 2.3.0

# (str) App theme (just leave default unless you customize UI)
android.theme = '@android:style/Theme.NoTitleBar'

# (bool) If True, the app is built in debug mode
debug = 1

# (bool) If True, logcat will show logs while running
log_level = 2

# (list) Supported platforms
# (don’t change unless you want to build for iOS/macOS)
supported_platforms = android

[buildozer]

# (str) Path to build directory
build_dir = .buildozer

# (str) Path to where compiled packages (APKs) go
bin_dir = bin
