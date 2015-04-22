#!/usr/bin/python

import os
import sys
import gtk
import terminatorlib.plugin as plugin
from terminatorlib.translation import _
import pprint


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
		item = gtk.MenuItem(_("Session"))
		submenu = gtk.Menu()
		saveItem = gtk.MenuItem("Save")
		saveItem.connect("activate", self.save_session, terminal)
		loadItem = gtk.MenuItem("Load")
		loadItem.connect("activate", self.load_session, terminal)
		spawnItem = gtk.MenuItem("Recursive spawn")
		spawnItem.connect("activate", self.recursive_spawn, terminal)
		submenu.append(saveItem)
		submenu.append(loadItem)
		submenu.append(spawnItem)
		item.set_submenu(submenu)
		menuitems.append(item)

	def load_session(self, _widget, Terminal):
		pass

	def get_relevant_data(self, terminal):
		return {
			"title": 	str(terminal.titlebar.label._label.get_text()),
			"size":  	str(terminal.get_size()),
			"rect": 	str(terminal.get_allocation()),
			"pos": 		str(terminal.window.get_position()),
			"cwd": 		str(terminal.get_cwd())
		}

	def recursive_save(self, node):
		class_string = node.__class__.__name__
		if class_string == "VPaned" or class_string == "HPaned":
			return { "node_type": class_string, "children": [self.recursive_save(child) for child in node.get_children()] }
		else:
			return { "node_type": class_string, "element": self.get_relevant_data(node) }

	def save_session(self, _widget, Terminal):
		win = Terminal.terminator.windows[0]
		open_list = win.get_children()
		pprint.pprint(self.recursive_save(win.get_children()[0]))

	def recursive_spawn(self, _widget, Terminal):
		win = Terminal.terminator.windows[0]
		open_list = win.get_children()
		while len(open_list) > 0:
			child = open_list.pop()
			class_string = child.__class__.__name__
			if class_string == "VPaned" or class_string == "HPaned":
				open_list = open_list + child.get_children()
			else:
				child.get_parent().split_axis(child)
