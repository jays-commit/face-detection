Face detection software used to detect and authenticate chosen users face.

General Installation Information
face_recognition and face_recognition_models can be installed via pip, but there are quite a few dependencies, which we'll be running through

Installation instruction splits between Windows and Linux for some dependencies, then there is a common part for them.

Windows
Microsoft Visual Studio 2015 or newer (check if build tools are enough): https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/ - download and install
Download and install CMake for Windows: https://github.com/Kitware/CMake/releases/download/v3.16.2/cmake-3.16.2-win64-x64.msi (other options available at: https://cmake.org/download/) During installation check to add CMake to PATH for all users (leave everything else default).


Restart Windows (simply starting new cmd window so it will include changes in PATH should be enough, restart is a safer option though)
pip install --upgrade numpy scipy
Install git client from: https://git-scm.com/download/win


Linux
sudo pip3.7 install --upgrade numpy scipy
Install git client anc cmake: sudo apt-get update && sudo apt-get -y install git cmake

Common
Remaining Python dependencies (use correct pip like sudo pip3, sudo pip3.7 on Linux/MacOS): pip install --upgrade Click Pillow
Installing dlib:
http://dlib.net/release_notes.html, search for cuda to find out supported CUDA versions if GPU acceleration is meant to be used. Currently it supports CUDA 10.1 (for Linux it worked for me with 10.0 too).
pip install dlib or sudo pip3, sudo pip3.7, etc. WARNING - it's going to be compiled and compilation can require a lot of processing power. Be patient.
If we aimed for CUDA, let's now check if it compiled to use CUDA:

> python >>> import dlib >>> dlib.DLIB_USE_CUDA True
Of course for Linux/MacOS we call python3, python3.7, etc.

Installing face_recognition: pip install git+https://github.com/ageitgey/face_recognition
Installing face_recognition_models: pip install git+https://github.com/ageitgey/face_recognition_models

Once you have all of the dependencies and have installed the face_recognition package (pip install face-recognition), we can begin

Create a directory called known_faces, which will house directories of known identities. Inside of known_faces, and name it after the identity youll be detecting  and populate it with different pics of said identity. 
Add a new directory called unknown_faces, which will be populated with pictures you want to make comparisons with.
