#!/usr/bin/python

import os
import sys
import gtk
import terminatorlib.plugin as plugin
from terminatorlib.translation import _


# AVAILABLE must contain a list of all the classes that you want exposed
AVAILABLE = ['Session']

class Session(plugin.MenuItem):
    capabilities = ['terminal_menu']
    dialog_action = gtk.FILE_CHOOSER_ACTION_SAVE
    dialog_buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                      gtk.STOCK_SAVE, gtk.RESPONSE_OK)
    def __init__(self):
        plugin.MenuItem.__init__(self)

    def callback(self, menuitems, menu, terminal):
    	item = gtk.MenuItem(_("Save Session"))
    	item.connect("activate", self.save_session, terminal)
    	menuitems.append(item)

    def save_session(self, _widget, Terminal):
		for terminal in Terminal.terminator.terminals:
			print("title", terminal.titlebar.label._label.get_text())
			print("size", terminal.get_size())
			print("rect", terminal.get_allocation())
			print("position", terminal.window.get_position())
			print("=========================")
		for window in Terminal.terminator.windows:
			print(window.title)
			window.split_axis(window.get_children()[0])


