'''
A GUI program to run Face Recognition algorithm using OPENCV 3.
This will be run on a Raspberry Pi Zero with a 3.5" 480x 320 Touch Screen.
It made using GTK+3
GUI consist of 4 buttos:
1) To Test the camera
2) To Gather and Label the person
3) Train the data
4) To Recognise
'''

import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from subprocess import call


class SelectionView(Gtk.Window):
    """ Window class which contains the button elements """
    def __init__(self):
        Gtk.Window.__init__(self, title= "Select an Action")
        #Setting the window size
        self.set_default_size(360, 300)
        #Setting the window position
        self.set_position(Gtk.WindowPosition.CENTER)
        #Window should not be resizable
        self.set_resizable(resizable = False)
        self.connect("destroy", Gtk.main_quit)

        #Test Camera button
        test_button = Gtk.Button()
        test_button.set_label("Test")
        test_button.connect("clicked", self.test_clicked)

        #Gather Button
        gather_button = Gtk.Button()
        gather_button.set_label("Gather")
        gather_button.connect("clicked", self.gather_clicked)

        #Train Button
        train_button = Gtk.Button()
        train_button.set_label("Train")
        train_button.connect("clicked", self.train_clicked)

        #Recognise Button
        recog_button = Gtk.Button()
        recog_button.set_label("Recognise")
        recog_button.connect("clicked", self.recog_clicked)

        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_column_homogeneous(True)
        grid.set_row_spacing(5)
        grid.set_row_homogeneous(True)
        grid.attach(test_button, 0, 0, 1, 4)
        grid.attach(gather_button, 1, 0, 1, 4)
        grid.attach(train_button, 0, 4, 1, 4)
        grid.attach(recog_button, 1, 4, 1, 4)

        self.add(grid)

        self.show_all()

    def test_clicked(self, button):
        print("Test Clicked")
        call(["python ./src/test_camera.py"])


    def gather_clicked(self, button):
        print("Gather Clicked")   
        call(["python ./src/data_gathering.py"])


    def train_clicked(self, button):
        print("Train Clicked")   
        call(["python ./src/trainer.py"])

    def recog_clicked(self, button):
        print("Recognition Clicked")    
        call(["python ./src/recognizer.py"])

if __name__ == "__main__":
    SelectionView()
    Gtk.main()
