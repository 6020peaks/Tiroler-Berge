Tiroler-Berge
=============

This repository contains the source code of the Scrapy-based crawler used to retrieve data from Wikipedia about the existing Tirolean mountains. The resulting data was submitted to the [open4data.at 2016 challenge](http://open4data.at). The same data got the special [ODP-Connect mention](https://www.opendataportal.at/odp-connect-bei-der-open4data-preisverleihung/) in the contest.

Use instructions
----------------
You will need a python environment (version 2.7.12) correctly set up in your machine in order to run this code. In addition you will need to install [Scrapy](http://scrapy.org), if you don't have it yet.

You can run the spider and save the data in JSON format by executing the following command from a terminal:

$ scrapy crawl wiki -o mountains.json
