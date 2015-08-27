#!/usr/bin/python -Es
#
# system-config-selinux.py - GUI for SELinux Config tool in system-config-selinux
#
# Dan Walsh <dwalsh@redhat.com>
#
# Copyright 2006-2009 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
import signal
import string
import sys
try:
    import gtk
except RuntimeError, e:
    print "system-config-selinux:", e
    print "This is a graphical application and requires DISPLAY to be set."
    sys.exit (1)

import gtk.glade
import os
import gobject
import gnome
import statusPage
import booleansPage
import loginsPage
import usersPage
import portsPage
import modulesPage
import domainsPage
import fcontextPage
import selinux
##
## I18N
##
PROGNAME="policycoreutils"

import gettext
gettext.bindtextdomain(PROGNAME, "/usr/share/locale")
gettext.textdomain(PROGNAME)
try:
    gettext.install(PROGNAME,
                    localedir="/usr/share/locale",
                    unicode=False,
                    codeset = 'utf-8')
except IOError:
    import __builtin__
    __builtin__.__dict__['_'] = unicode

gnome.program_init("SELinux Management Tool", "5")

version = "1.0"

sys.path.append('/usr/share/system-config-selinux')



##
## Pull in the Glade file
##
if os.access("system-config-selinux.glade", os.F_OK):
    xml = gtk.glade.XML ("system-config-selinux.glade", domain=PROGNAME)
else:
    xml = gtk.glade.XML ("/usr/share/system-config-selinux/system-config-selinux.glade", domain=PROGNAME)

class childWindow:
    def __init__(self):
        self.tabs=[]
        self.xml = xml
        xml.signal_connect("on_quit_activate", self.destroy)
        xml.signal_connect("on_delete_clicked", self.delete)
        xml.signal_connect("on_add_clicked", self.add)
        xml.signal_connect("on_properties_clicked", self.properties)
        xml.signal_connect("on_local_clicked", self.on_local_clicked)
        self.add_page(statusPage.statusPage(xml))
        if selinux.is_selinux_enabled() > 0:
            try:
                self.add_page(booleansPage.booleansPage(xml))
                self.add_page(fcontextPage.fcontextPage(xml))
                self.add_page(loginsPage.loginsPage(xml))
                self.add_page(usersPage.usersPage(xml))
                self.add_page(portsPage.portsPage(xml))
                self.add_page(modulesPage.modulesPage(xml)) # modules
                self.add_page(domainsPage.domainsPage(xml)) # domains
            except ValueError, e:
                self.error(e.message)

        xml.signal_connect("on_quit_activate", self.destroy)
        xml.signal_connect("on_policy_activate", self.policy)
        xml.signal_connect("on_logging_activate", self.logging)
        xml.signal_connect("on_about_activate", self.on_about_activate)

        self.add_menu = xml.get_widget("add_menu_item")
        self.properties_menu = xml.get_widget("properties_menu_item")
        self.delete_menu = xml.get_widget("delete_menu_item")

    def error(self, message):
        dlg = gtk.MessageDialog(None, 0, gtk.MESSAGE_ERROR,
                                gtk.BUTTONS_CLOSE,
                                message)
        dlg.set_position(gtk.WIN_POS_MOUSE)
        dlg.show_all()
        dlg.run()
        dlg.destroy()

    def add_page(self, page):
        self.tabs.append(page)

    def policy(self, args):
        os.spawnl(os.P_NOWAIT, "/usr/share/system-config-selinux/semanagegui.py")
    def logging(self, args):
        os.spawnl(os.P_NOWAIT, "/usr/bin/seaudit")

    def delete(self, args):
        self.tabs[self.notebook.get_current_page()].deleteDialog()

    def add(self, args):
        self.tabs[self.notebook.get_current_page()].addDialog()

    def properties(self, args):
        self.tabs[self.notebook.get_current_page()].propertiesDialog()

    def on_local_clicked(self, button):
        self.tabs[self.notebook.get_current_page()].on_local_clicked(button)

    def on_about_activate(self, args):
        dlg = xml.get_widget ("aboutWindow")
        dlg.run ()
        dlg.hide ()

    def destroy(self, args):
        gtk.main_quit()

    def use_menus(self, use_menus):
        self.add_menu.set_sensitive(use_menus)
        self.properties_menu.set_sensitive(use_menus)
        self.delete_menu.set_sensitive(use_menus)

    def itemSelected(self, selection):
        store, rows = selection.get_selected_rows()
        if store != None and len(rows) > 0:
            self.notebook.set_current_page(rows[0][0])
            self.use_menus(self.tabs[rows[0][0]].use_menus())
        else:
            self.notebook.set_current_page(0)
            self.use_menus(self.tabs[0].use_menus())


    def setupScreen(self):
        # Bring in widgets from glade file.
        self.mainWindow = self.xml.get_widget("mainWindow")
        self.notebook = self.xml.get_widget("notebook")
        self.view = self.xml.get_widget("selectView")
        self.view.get_selection().connect("changed", self.itemSelected)
        self.store = gtk.ListStore(gobject.TYPE_STRING)
        self.view.set_model(self.store)
        col = gtk.TreeViewColumn("",  gtk.CellRendererText(), text = 0)
        col.set_resizable(True)
        self.view.append_column(col)

        for page in self.tabs:
            iter = self.store.append()
            self.store.set_value(iter, 0, page.get_description())
        self.view.get_selection().select_path ((0,))

    def stand_alone(self):
        desktopName = _("Configue SELinux")

        self.setupScreen()

        self.mainWindow.connect("destroy", self.destroy)

        self.mainWindow.show_all()
        gtk.main()

if __name__ == "__main__":
    signal.signal (signal.SIGINT, signal.SIG_DFL)

    app = childWindow()
    app.stand_alone()
