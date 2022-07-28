# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2017 Tijme Gommers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re

import pkg_resources


class PackageHelper:
    """The Package class contains all the package related information (like the version number).

    Attributes:
        __name (str): Cached package name.
        __description (str): Cached package description.
        __alias (str): Cached package alias.
        __version (str): Cached package version number (if initialized).

    """

    __name = "Not Your Average Web Crawler"

    __description = "A web crawler that gathers more than you can imagine."

    __alias = "nyawc"

    __version = None

    def __init__(self,
                 name: str = "Not Your Average Web Crawler",
                 description: str = "A web crawler that gathers more than you can imagine.",
                 alias: str = "nyawc",
                 version: str = None):
        self.__name = name
        self.__description = description
        self.__alias = alias
        self.__version = version

    @staticmethod
    def get_name():
        """Get the name of this package.

        Returns:
            str: The name of this package.

        """

        return PackageHelper.__name

    @staticmethod
    def get_description():
        """Get the description of this package.

        Returns:
            str: The description of this package.

        """

        return PackageHelper.__description

    @staticmethod
    def get_alias():
        """Get the alias of this package.

        Returns:
            str: The alias of this package.

        """

        return PackageHelper.__alias

    @staticmethod
    def get_version():
        """Get the version number of this package.

        Returns:
            str: The version number (marjor.minor.patch).

        Note:
            When this package is installed, the version number will be available through the
            package resource details. Otherwise this method will look for a ``.semver`` file.

        Note:
            In rare cases corrupt installs can cause the version number to be unknown. In this case
            the version number will be set to the string "Unknown".

        """

        if PackageHelper.__version:
            return PackageHelper.__version

        PackageHelper.__version = "Unknown"

        # If this is a GIT clone without install, use the ``.semver`` file.
        try:
            PackageHelper.__version = '1.9'
            return PackageHelper.__version
        except Exception as e:
            print(e)

        # If the package was installed, get the version number via Python's distribution details.
        try:
            distribution = pkg_resources.get_distribution(PackageHelper.get_alias())
            if distribution.version:
                PackageHelper.__version = distribution.version
            return PackageHelper.__version
        except Exception as e:
            print(e)

        return PackageHelper.__version

    @staticmethod
    def rst_to_pypi(contents):
        """
        Convert the given GitHub RST to PyPi RST contents (since some RST directives are not available in PyPi).

        Args:
            contents (str): The GitHub compatible RST contents.

        Returns:
            str: The PyPi compatible RST contents.

        """

        # The PyPi description does not support the SVG file type.
        contents = contents.replace(".svg?pypi=png.from.svg", ".png")

        # Convert ``<br class="title">`` to a H1 title
        asterisks_length = len(PackageHelper.get_name())
        asterisks = "*" * asterisks_length
        title = asterisks + "\n" + PackageHelper.get_name() + "\n" + asterisks

        contents = re.sub(r"(\.\. raw:: html\n)(\n {2,4})(<br class=\"title\">)", title, contents)

        # The PyPi description does not support raw HTML
        contents = re.sub(r"(\.\. raw:: html\n)((\n {2,4})([A-Za-z\d<> =\"/])*)*", "", contents)

        return contents
