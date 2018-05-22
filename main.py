#!user/bin/python
# -*- coding: utf-8 -*-
import urllib2, base64
import requests
import json
import unicodedata
import sys
from datetime import datetime, timedelta
from urllib2 import urlopen,base64
#Here import my own libs
from tokensTeamWork import *
from teamworkcreateatask import *
from verifyconnectedtime import *
reload(sys)

########################################################################################################################
##                                                                                                                    ##
##                                                                                                                    ##
##                                              main                                                                  ##
##                                                                                                                    ##
##                                                                                                                    ##
########################################################################################################################


verifyConnectedTime()
