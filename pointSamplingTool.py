# -*- coding: utf-8 -*-

# ***************************************************************************
# Point Sampling Tool
#
# A QGIS plugin for collecting polygon attributes and raster values
# from multiple layers at specified sampling points
#
# Copyright (C) 2008 Borys Jurgiel
# based on Carson Farmer's PointsInPoly plugin, Copyright (C) 2008 Carson Farmer
#
# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************

import os
from builtins import object

from qgis.PyQt.QtCore import (
    QT_VERSION_STR,
    QCoreApplication,
    QLocale,
    QSettings,
    QTranslator,
)
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from . import doPointSamplingTool
from . import resources

QT_VERSION_INT = int(QT_VERSION_STR.split(".")[0])


def exec_dialog(dialog):
    if QT_VERSION_INT <= 5:
        return dialog.exec_()
    else:
        return dialog.exec()


class pointSamplingTool(object):
    def __init__(self, iface):
        self.iface = iface

        if QSettings().value("locale/overrideFlag", type=bool):
            locale = QSettings().value("locale/userLocale")
        else:
            locale = QLocale.system().name()

        locale_path = os.path.join(
            os.path.dirname(__file__),
            "i18n",
            "pointSamplingTool_{}.qm".format(locale[0:2]),
        )

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # create action
        self.action = QAction(
            QIcon(":/plugins/pointSamplingTool/pointSamplingToolIcon.png"),
            QCoreApplication.translate("Point Sampling Tool", "Point Sampling Tool"),
            self.iface.mainWindow(),
        )
        self.action.setWhatsThis(
            QCoreApplication.translate(
                "Point Sampling Tool",
                "Collects polygon attributes and raster values from multiple layers at specified sampling points",
            )
        )
        self.action.triggered.connect(self.run)
        # add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(
            QCoreApplication.translate("Point Sampling Tool", "&Analyses"), self.action
        )

    def unload(self):
        # remove the plugin menu item and icon
        self.iface.removePluginMenu(
            QCoreApplication.translate("Point Sampling Tool", "&Analyses"), self.action
        )
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        # create and show a configuration dialog or something similar
        dialoga = doPointSamplingTool.Dialog(self.iface)
        exec_dialog(dialoga)
