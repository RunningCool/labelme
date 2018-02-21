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

import six


class CorrespondenceFileError(Exception):
    pass

class CorrespondenceFile(object):
    suffix = '.json'

    def __init__(self, filename=None):
        self.crspdcById = [{}] * 2
        self.crspdcByPoints = {}
        self.imagePath = [None] * 2
        if filename is not None:
            self.load(filename)

    def load(self, filename):
        try:
            with open(filename, 'rb') as f:
                data = json.load(f)
                imagePath = data['imagePath']
                crspdcById = data['crspdcById']
                crspdcByPoints = data['crspdcByPoints']

                # Only replace data after everything is loaded.
                self.crspdcById = crspdcById
                self.crspdcByPoints = crspdcByPoints
                self.imagePath = imagePath
        except Exception as e:
            raise CorrespondenceFileError(e)

    def save(self, filename, shapes, imagePath, imageData,
            lineColor=None, fillColor=None):
        try:
            with open(filename, 'wb') as f:
                if six.PY3:
                    imageData = b64encode(imageData.encode('utf-8'))
                elif six.PY2:
                    imageData = b64encode(imageData)
                else:
                    raise RuntimeError('Unsupported Python version.')
                json.dump(dict(
                    shapes=shapes,
                    lineColor=lineColor, fillColor=fillColor,
                    imagePath=imagePath,
                    imageData=imageData),
                    f, ensure_ascii=True, indent=2)
        except Exception as e:
            raise CorrespondenceFileError(e)

    @staticmethod
    def isCorrespondenceFile(filename):
        return os.path.splitext(filename)[1].lower() == CorrespondenceFile.suffix
