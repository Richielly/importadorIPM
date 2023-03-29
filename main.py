import time
import fdb
import configparser
import script
from bottle import get, post, route, run, debug, template, request, static_file, error

cfg = configparser.ConfigParser()
cfg.read('cfg.ini')