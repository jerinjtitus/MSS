# -*- coding: utf-8 -*-
"""

    mslib.msui.mscolab
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Window to display authentication and project details for mscolab


    To better understand of the code, look at the 'ships' example from
    chapter 14/16 of 'Rapid GUI Programming with Python and Qt: The
    Definitive Guide to PyQt Programming' (Mark Summerfield).

    This file is part of mss.

    :copyright: Copyright 2019- Shivashis Padhi
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from mslib.msui.mss_qt import QtGui, QtWidgets, QtCore
from mslib.msui.mss_qt import ui_mscolab_window as ui
from mslib.msui import MissionSupportSystemDefaultConfig as mss_default
from mslib.msui.icons import icons
from mslib.msui import flighttrack as ft
from mslib.msui import topview, sideview, tableview
from mslib.msui import socket_control as sc

import logging
import requests
import json
import fs


class MSSMscolabWindow(QtWidgets.QMainWindow, ui.Ui_MSSMscolabWindow):
    """PyQt window implementing mscolab window
    """
    name = "Mscolab"
    identifier = None
    viewCloses = QtCore.pyqtSignal(name="viewCloses")

    def __init__(self, parent=None):
        """Set up user interface
        """
        super(MSSMscolabWindow, self).__init__(parent)
        self.setupUi(self)
        self.widget_2.hide()
        self.setWindowIcon(QtGui.QIcon(icons('64x64')))
        # if token is None, not authorized, else authorized
        self.token = None
        self.loginButton.clicked.connect(self.authorize)
        self.logoutButton.clicked.connect(self.logout)
        self.topview.clicked.connect(self.open_topview)
        self.sideview.clicked.connect(self.open_sideview)
        self.tableview.clicked.connect(self.open_tableview)
        self.save_ft.clicked.connect(self.save_wp_mscolab)

        # int to store active pid
        self.active_pid = None
        # store active_flight_path here as object
        self.waypoints_model = None
        # store a reference of window in class
        self.open_windows_mscolab = []
        # connection object to interact with sockets
        self.conn = None
        # to store tempfile name
        self.fname_temp = ""

    def authorize(self):
        emailid = self.emailid.text()
        password = self.password.text()
        data = {
            "email": emailid,
            "password": password
        }
        r = requests.post(mss_default.mscolab_server_url + '/token', data=data)
        if r.text == "False":
            # popup that wrong credentials
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('Oh no, your credentials were incorrect.')
            pass
        else:
            # remove the login modal and put text there
            json_ = json.loads(r.text)
            self.token = json_["token"]
            self.label.setText("logged in as: " + json_["user"]["username"])
            self.widget_2.show()
            self.widget.hide()

            # add projects
            data = {
                "token": self.token
            }
            r = requests.get(mss_default.mscolab_server_url + '/projects', data=data)
            json_ = json.loads(r.text)
            projects = json_["projects"]
            self.add_projects_to_ui(projects)

            # create socket connection here
            self.conn = sc.ConnectionManager(self.token)

    def add_projects_to_ui(self, projects):
        for project in projects:
            project_desc = project['path'] + " (" + project["access_level"] + ")"
            widgetItem = QtWidgets.QListWidgetItem(project_desc, parent=self.listProjects)
            widgetItem.p_id = project["p_id"]
            self.listProjects.addItem(widgetItem)
        self.listProjects.itemActivated.connect(self.set_active_pid)

    def set_active_pid(self, item):
        # set active_pid here
        self.active_pid = item.p_id

        # set active flightpath here
        data = {
            "token": self.token,
            "p_id": self.active_pid
        }
        r = requests.get(mss_default.mscolab_server_url + '/get_project', data=data)
        ftml = json.loads(r.text)["content"]
        data_dir = fs.open_fs(mss_default.data_dir)
        data_dir.writetext('tempfile_mscolab.ftml', ftml)
        fname_temp = fs.path.combine(mss_default.data_dir, 'tempfile_mscolab.ftml')
        self.fname_temp = fname_temp
        self.waypoints_model = ft.WaypointsTableModel(filename=fname_temp)

        # change font style for selected
        font = QtGui.QFont()
        for i in range(self.listProjects.count()):
            self.listProjects.item(i).setFont(font)
        font.setBold(True)
        item.setFont(font)

    def open_topview(self):
        # showing dummy info dialog
        if self.active_pid == None:
            return
        view_window = topview.MSSTopViewWindow(model=self.waypoints_model, parent=self.listProjects)
        view_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        view_window.show()

    def open_sideview(self):
        # showing dummy info dialog
        if self.active_pid == None:
            return
        view_window = sideview.MSSSideViewWindow(model=self.waypoints_model, parent=self.listProjects)
        view_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        view_window.show()

    def open_tableview(self):
        # showing dummy info dialog
        if self.active_pid == None:
            return
        view_window = tableview.MSSTableViewWindow(model=self.waypoints_model, parent=self.listProjects)
        view_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        view_window.show()

    def logout(self):
        # delete token and show login widget-items
        self.token = None
        # delete active-project-id
        self.active_pid = None
        # clear projects list here
        self.widget_2.hide()
        self.widget.show()
        # clear project listing
        self.listProjects.clear()
        # disconnect socket
        if self.conn != None:
            self.conn.disconnect()
            self.conn = None

    def save_wp_mscolab(self):
        if self.active_pid != None:
            # to save to temp file
            xml_text = self.waypoints_model.save_to_mscolab()
            # to emit to mscolab
            self.conn.save_file(self.token, self.active_pid, xml_text)

    def setIdentifier(self, identifier):
        self.identifier = identifier

    def closeEvent(self, event):
        self.conn.disconnect()