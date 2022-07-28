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
from nyawc.Options import Options
from nyawc.QueueItem import QueueItem
from nyawc.helpers.URLHelper import URLHelper
from nyawc.http.Request import Request


class BaseScraper(object):
    """The BaseScraper can be used to create other scrapers.

    Attributes:
        options: The settings/options object.
        queue_item: The queue item containing the response to scrape.

    """

    def __init__(self, options: Options, queue_item: QueueItem):
        """Construct the HTMLSoupLinkScraper instance.

        Args:
            options: The settings/options object.
            queue_item: The queue item containing a response the scrape.

        """

        self.options = options
        self.queue_item = queue_item

    def derived_get_requests(self):
        """
        Get all the new requests that were found in the response.

        Returns:
            list: A list of new requests that were found.

        """
        ...

    def get_requests(self) -> list[Request]:
        """Get all the new requests that were found in the response.

        Returns:
            list: A list of new requests that were found.

        """

        requests = self.derived_get_requests()

        for request in requests:
            request.url = URLHelper.remove_hash(request.url)

        return requests
