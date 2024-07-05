[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = mdabidhossain.xyz

# (str) Source code directory
source.dir = .

# (list) Source files to include (support for globbing)
source.include_exts = py,png,jpg,kv,csv

# (list) Application requirements
requirements = python3==3.10.11,hostpython3==3.10.11,kivy,pandas

# (str) App version
version = 1.0

# (str) Icon of the application
# icon.filename = path/to/your/icon.png

# (list) Application permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Android architecture to build for, can be one of: armeabi-v7a, arm64-v8a, x86, x86_64
# android.arch = armeabi-v7a

# (str) Android NDK version to use
android.ndk = 19c

# (int) Android API to use
android.api = 29

# (str) Android SDK version to use
android.sdk = 29

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) Application permissions
android.permissions = INTERNET

# (str) Android App orientation (landscape, portrait or all)
android.orientation = portrait

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (str) Android build process (android_new, android_gradle)
android.build_mode = release
