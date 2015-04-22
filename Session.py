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
    	item = gtk.MenuItem(_("DUMB"))
    	menuitems.append(item)

