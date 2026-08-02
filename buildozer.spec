[app]

# (str) Title of your application
title = SampleApp

# (str) Package name
package.name = nfsApk

# (str) Package domain (needed for android/ios packaging)
package.domain = org.novfensec

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = images/*.png

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Secure, fully updated package dependency list for KivyMD 2.0+
requirements = python3, kivy==2.3.1, https://github.com, exceptiongroup, asynckivy, asyncgui, materialyoucolor, android, materialshapes

# (str) Presplash and Icon configurations 
# NOTE: Missing file errors bypass korar jonno default config use kora holo
# presplash.filename = %(source.dir)s/images/presplash.png
# icon.filename = %(source.dir)s/images/favicon.png

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API - Stable production API target for 2026 deployment
android.api = 35

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (bool) Enable AndroidX support. Required for dynamic theme libraries.
android.enable_androidx = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Full name including package path of the Java class that implements Android Activity
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
