#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: OriganizeFile.py
#
#           USAGE:
#
#   DESCRIPTION: Using the shutil and os modules, make a program that organizes the files in a specified directory
#                By classifying them into folders of music, pdfs, images, etc
#
#       OPTIONS: ----
#  REQUIREMENTS: ----
#          BUGS: ----
#         NOTES: ----
#        AUTHOR: Chyi Yaqing
#  ORGANIZATION:
#       VERSION: 0.1.0
#       CREATED: 04/24/2017
#      REVISION: ----
#      Copyright © 2017 Chyi Yaqing
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software FOundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAB PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#===================================================================

import argparse
import arrow
import os
import subprocess
import sys

VERSION = 'Classifier 2.0'
DIRCONFFILE = '.classifier.conf'
PLATFORM = sys.platform
OS = os.name

if PLATFORM == 'darwin':
    CONFIG = os.path.join(os.path.expenduser('~'), '.classifier-master.conf')
elif PLATFORM == 'win32' or OS == 'nt':
    CONFIG = os.path.join(os.getenv('userprofile'), 'classifier-master.conf')
elif PLATFORM == 'linux' or PLATFORM == 'linux2' or OS == 'posix':
    CONFIG = os.path.join(os.getenv('HOME'), '.classifier-master.conf')
else:
    CONFIG = os.path.join(os.getcwd(), '.classifier-master.conf')

def main():
    Classifier()

class Classifier:
    """
    All format lists were taken from wikipedia, not all of them were added due to extensions
    not being exclusive to one format such as webm, or raw
    Audio           -       https://en.wikipedia.org/wiki/Audio_file_format
    Images          -       https://en.wikipedia.org/wiki/Image_file_formats
    Video           -       https://en.wikipedia.org/wiki/Video_file_format
    Documents       -       https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions
    """

    def __init__(self):
        self.description = "Organize files in your directory instantly,by classifying them into different folders"
        self.parser = argparse.ArgumentParser(description=self.description)

        self.parser.add_argument("-v", "--version", action='store_true',
                                help="show version, filename and exit")

        self.parser.add_argument("-et", "--edittypes", action='store_true',
                                help="Edit the list of types and formats")

        self.parser.add_argument("-t", "--types", action='store_true',
                                help="Show the current list of types and formats")

        self.parser.add_argument("-rst", "--reset", action='store_true',
                                help="Reset the default Config file")

        """
        self.parser.add_argument("-r", "--recursive", action='store_true',
                                help="Recursively search your source directory. " +
                                "WARNING: Ensure you use the correct path as this " +
                                "Will move all files from your selected types.")
        """

        self.parser.add_argument("-st", "--specific-types", type=str, nargs='+',
                                help="Move all file extensions, given in the args list, " +
                                    "in the current directory into the Specific Folder")

        self.parser.add_argument("-sf", "--specifc-folder", type=str,
                                help="Folder to move Specific File Type")

        self.parser.add_argument("-o", "--output", type=str,
                                help="Main directory to put organized folders")

        self.parser.add_argument("-d", "--directory", type=str,
                                help="The directory whose files to classify")

        self.parser.add_argument("-dt", "--date", action='store_true',
                                help="Organize files by creation date")

        self.parser.add_argument("-df", "--dateformat", type=str,
                                help="set the date format using YYYY, MM or DD")

        self.args = self.parser.parse_args()
        self.dateformat = 'YYYY-MM-DD'
        self.formats = {}
        self.dirconf = None
        self.checkconfig()
        self.run()

    def create_default_config(self):
        with open(CONFIG, "w") as conffile:
            conffile.write("IGNORE: part, desktop\n" +
                            "Music: mp3, aac, flac, ogg, wma, m4a, aiff, wav, amr\n" +
                            "Videos: flv, ogv, avi, mp4, mpg, mpeg, 3gp, mkv, ts, webm, vob, wmv\n" +
                            "Pictures: png, jpeg, gif, jpg, bmp, svg, webp, psd, tiff\n" +
                            "Archives: rar, zip, 7z, gz, bz2, tar, dmg, tgz, xz, iso, cpio\n" +
                            "Documents: txt, pdf, doc, docx, odf, xls, xlsv, xlsx, " +
                                        "ppt, pptx, ppsx, odp, odt, ods, md, json, csv\n" +
                            "Books: mobi, epub, chm\n" +
                            "DEBPackages: deb\n" +
                            "Programs: exe, msi\n" +
                            "RPMPackages: rpm")
        print("CONFIG file created at: "+CONFIG)

    def checkconfig(self):
        """
        create a default config if not available
        """
        if not os.path.isdir(os.path.dirname(CONFIG)):
            os.makedirs(os.path.dirname(CONFIG))
        if not os.path.isfile(CONFIG):
            self.create_default_config()

        with open(CONFIG, 'r') as file:
            for items in file:
                spl = items.replace('\n', '').split(':')
                key = spl[0].replace(" ","")
                val = spl[1].replace(" ","")
                self.formats[key] = val
        return

    def moveto(self, filename, form_folder, to_folder):
        from_file = os.path.join(from_folder, filename)
        to_file = os.path.join(to_folder, filename)
        # to move only files, not folders
        if not to_file == from_file:
            print('moved: ' + str(to_file))
            if os.path.isfile(from_file):
                if not os.path.exists(to_folder):
                    os.makedirs(to_folder)
                os.rename(from_file, to_file)
        return

    def classify(self, formats, output, directory):
        for file in os.listdir(directory):
            tmpbreak = False
            # set up a config per folder
            if not file == DIRCONFFILE and os.path.isfile(os.path.join(directory, file)):
                filename, file_ext = os.path.splitext(file)
                file_ext = file_ext.lower().replace('.','')
                if 'IGNORE' in self.formats:
                    for ignored in self.formats['IGNORE'].replace('\n', '').split(','):
                        if file_ext == ignored:
                            tmpbreak = True
                if not tepbreak:
                    for folder, ext_list in list(formats.items()):
                        # never move files in the ignore list
                        if not folder == 'IGNORE':
                            folder = os.path.join(output, folder)
                            # make sure we are passing a list to the extension checker
                            if type(ext_list) == str:
                                ext_list = ext_list.split(',')
                            for
