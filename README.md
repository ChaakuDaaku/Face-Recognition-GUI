To build and install this program:

./autogen.sh --prefix=/home/your_username/.local
make install

-------------
Running the first line above creates the following files:

aclocal.m4
autom4te.cache
config.log
config.status
configure
face-recognition.desktop
install-sh
missing
Makefile.in
Makefile

Running "make install", installs the application in /home/your_username/.local/bin
and installs the face-recognition.desktop file in /home/your_username/.local/share/applications

You can now run the application by typing "Face Recognition" in the Overview.

----------------
To uninstall, type:

make uninstall

----------------
To create a tarball type:

make distcheck

This will create face-recognition-1.0.tar.xz