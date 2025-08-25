#-----------------------------------------------------------
#
# Point Sampling Tool
#
# A QGIS plugin for collecting polygon attributes and raster values from multiple layers at specified sampling points
#
# Copyright (C) 2008-2012  Borys Jurgiel
# based on Carson Farmer's PointsInPoly plugin, Copyright (C) 2008 Carson Farmer
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
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
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------

def classFactory(iface):
    from .Plugin import Plugin
    return Plugin(iface)
