## domainsPage.py - show selinux domains
## Copyright (C) 2009 Red Hat, Inc.

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

## Author: Dan Walsh
import string
import gtk
import gtk.glade
import os
import commands
import gobject
import sys
import seobject
import selinux
from semanagePage import *;
from sepolicy import get_all_entrypoint_domains

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

class domainsPage(semanagePage):
    def __init__(self, xml):
        semanagePage.__init__(self, xml, "domains", _("Process Domain"))
        self.domain_filter = xml.get_widget("domainsFilterEntry")
        self.domain_filter.connect("focus_out_event", self.filter_changed)
        self.domain_filter.connect("activate", self.filter_changed)

        self.store = gtk.ListStore(gobject.TYPE_STRING, gobject.TYPE_STRING)
        self.view.set_model(self.store)
        self.store.set_sort_column_id(0, gtk.SORT_ASCENDING)
        col = gtk.TreeViewColumn(_("Domain Name"), gtk.CellRendererText(), text = 0)
        col.set_sort_column_id(0)
        col.set_resizable(True)
        self.view.append_column(col)
        self.store.set_sort_column_id(0, gtk.SORT_ASCENDING)
        col = gtk.TreeViewColumn(_("Mode"), gtk.CellRendererText(), text = 1)
        col.set_sort_column_id(1)
        col.set_resizable(True)
        self.view.append_column(col)
        self.view.get_selection().connect("changed", self.itemSelected)

        self.permissive_button = xml.get_widget("permissiveButton")
        self.enforcing_button = xml.get_widget("enforcingButton")

        self.domains=get_all_entrypoint_domains()
        self.load()

    def get_modules(self):
        modules=[]
        fd=os.popen("semodule -l")
        mods = fd.readlines()
        fd.close()
        for l in mods:
            modules.append(l.split()[0])
        return modules

    def load(self, filter=""):
        self.filter=filter
        self.store.clear()
        try:
            modules=self.get_modules()
            for domain in self.domains:
                if not self.match(domain, filter):
                    continue
                iter = self.store.append()
                self.store.set_value(iter, 0, domain)
                t = "permissive_%s_t" % domain
                if t in modules:
                    self.store.set_value(iter, 1, _("Permissive"))
                else:
                    self.store.set_value(iter, 1, "")
        except:
            pass
        self.view.get_selection().select_path ((0,))

    def itemSelected(self, selection):
        store, iter = selection.get_selected()
        if iter == None:
            return
        p = store.get_value(iter, 1) == _("Permissive")
        self.permissive_button.set_sensitive(not p)
        self.enforcing_button.set_sensitive(p)

    def deleteDialog(self):
        # Do nothing
        return self.delete()

    def delete(self):
        selection = self.view.get_selection()
        store, iter = selection.get_selected()
        domain = store.get_value(iter, 0)
        try:
            self.wait()
            status, output = commands.getstatusoutput("semanage permissive -d %s_t" % domain)
            self.ready()
            if status != 0:
                self.error(output)
            else:
                domain = store.set_value(iter, 1, "")
                self.itemSelected(selection)

        except ValueError, e:
            self.error(e.args[0])

    def propertiesDialog(self):
        # Do nothing
        return

    def addDialog(self):
        # Do nothing
        return self.add()

    def add(self):
        selection = self.view.get_selection()
        store, iter = selection.get_selected()
        domain = store.get_value(iter, 0)
        try:
            self.wait()
            status, output = commands.getstatusoutput("semanage permissive -a %s_t" % domain)
            self.ready()
            if status != 0:
                self.error(output)
            else:
                domain = store.set_value(iter, 1, _("Permissive"))
                self.itemSelected(selection)

        except ValueError, e:
            self.error(e.args[0])
