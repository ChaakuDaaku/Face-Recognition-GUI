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

        #Detect Face button
        detect_button = Gtk.Button()
        detect_button.set_label("Detect")
        detect_button.connect("clicked", self.detect_clicked)

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

        #Created a Grid to arrange 4 buttons
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_column_homogeneous(True)
        grid.set_row_spacing(5)
        grid.set_row_homogeneous(True)
        grid.attach(test_button, 0, 0, 1, 2)
        grid.attach_next_to(detect_button, test_button, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(gather_button, test_button, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(train_button, gather_button, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(recog_button, detect_button, Gtk.PositionType.RIGHT, 2, 2)

        #Now we add the Grid to Window
        self.add(grid)

        #Show the Window
        self.show_all()

    def test_clicked(self, button):
        """ Click Event function for Test Button """
        print("Test Clicked")
        call(["python", "./src/test_camera.py"])

    def detect_clicked(self, button):
        """ Click Event function for Detect Button """
        print("Detect Clicked")
        call(["python", "./src/face_detection.py"])

    def gather_clicked(self, button):
        """ Click Event function for Test Button """
        InputWindow().on_button_clicked(self)
        print("Gather Clicked")   

    def train_clicked(self, button):
        """ Click Event function for Test Button """
        print("Train Clicked")   
        call(["python", "./src/trainer.py"])

    def recog_clicked(self, button):
        """ Click Event function for Test Button """
        print("Recognition Clicked")    
        call(["python", "./src/recognizer.py"])

class InputDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Face ID", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150, 100)

        label = Gtk.Label("Assign an ID for the person")
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("eg. 1")

        box = self.get_content_area()
        box.add(label)
        box.add(self.entry)
        self.show_all()

class InputWindow(Gtk.Window):
    def on_button_clicked(self, widget):
        dialog = InputDialog(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            global face_id
            face_id = dialog.entry.get_text()
            print(face_id)
            call(["python", "./src/data_gathering.py"])

        
        elif response == Gtk.ResponseType.CANCEL:
            print("You cancelled the operation")

        dialog.destroy()
    

if __name__ == "__main__":
    SelectionView()
    Gtk.main()
