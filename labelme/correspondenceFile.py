#
# Copyright (C) 2011 Michael Pitidis, Hussein Abdulwahid.
#
# This file is part of Labelme.
#
# Labelme is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Labelme is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Labelme.  If not, see <http://www.gnu.org/licenses/>.
#

from base64 import b64encode, b64decode
import json
import os.path
import sys

PY2 = sys.version_info[0] == 2


class CorrespondenceFileError(Exception):
    pass

class CorrespondenceFile(object):
    suffix = '.crd'

    def __init__(self, filename=None):
        self.crspdcById = {}
        self.crspdcByName = []
        self.imagePath = [None] * 2
        if filename is not None:
            self.load(filename)

    def load(self, filename):
        try:
            with open(filename, 'rb') as f:
                data = json.load(f)
                imagePath = data['imagePath']
                crspdcById = data['crspdcById']
                crspdcByName = data['crspdcByName']

                # Only replace data after everything is loaded.
                self.crspdcById = crspdcById
                self.crspdcByName = crspdcByName
                self.imagePath = imagePath
        except Exception as e:
            raise CorrespondenceFileError(e)

    def extractCorrespondence(self, shapes):
        self.crspdcById = {}
        for canvasShapes in shapes:
            for shape in canvasShapes:
                # If there is no correspondence, skip it for god's sake
                if len(shape.correspondence) == 0:
                    continue
                self.crspdcById[shape.id] = shape.correspondence


    def save(self, crspdcByName, shapes, imagePath, filename=None):
        self.extractCorrespondence(shapes)
        self.crspdcByName = crspdcByName
        self.imagePath = imagePath
        assert(len(self.imagePath) == 2)
        assert(len(shapes) == 2)
        if filename is None:
            filename = CorrespondenceFile.getCrspdcFileFromNames(imagePath)

        data = dict(
            crspdcById=self.crspdcById,
            crspdcByName=self.crspdcByName,
            imagePath=imagePath
        )
        try:
            with open(filename, 'wb' if PY2 else 'w') as f:
                json.dump(data, f, ensure_ascii=True, indent=2)
        except Exception as e:
            raise CorrespondenceFileError(e)

    @staticmethod
    def isCorrespondenceFile(filename):
        return os.path.splitext(filename)[1].lower() == CorrespondenceFile.suffix

    @staticmethod
    def getCrspdcFileFromNames(filenames):
        assert(len(filenames) == 2)
        path, f1 = os.path.split(filenames[0])
        f1, _ = os.path.splitext(f1)
        _, f2 = os.path.split(filenames[1])
        f2, _ = os.path.splitext(f2)
        f1, f2 = [f2, f1] if f1 > f2 else [f1, f2]
        return path + '/' + f1 + '_' + f2 + CorrespondenceFile.suffix
