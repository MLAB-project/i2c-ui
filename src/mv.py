#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
#logging.basicConfig(level=logging.DEBUG) 

import time
import datetime
import sys
import os
from pymlab import config
import h5py
import numpy as np
import time
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket


class hello(tornado.web.RequestHandler):
    def get(self):
        return render.touch()


class var(tornado.web.RequestHandler):
    def get(self, name):
        print "VAR get", name
        if str(name) == "json":
            json="?("
            sensors = self.get_argument("sens", default='', strip=False).split(",")
            print sensors
            project = h5py.File("test"+'.hdf5', 'a')
            for sens in sensors:
                table = np.array(project[sens][:])
                json += '{"'+str(sens)+'":{"sensor":"'+str(sens)+'", "pointStart":'+str(float(table[0][1]))+',"pointInterval":'+str(1)+',"data":['
                for row in table:
                    json += str(float(row[2]))+', '
                json += ']'
                json += '},'
            json += '});'
            self.write( json )

        else:
            print str(name)
            return name


class  ver(tornado.web.RequestHandler):
    def get(self, name):
        if name == "project" or name == "0":
            return renderView.ProjectOverView()
        elif name == "start":
            return renderView.ProjectOverView()
        elif name == "sens":
            print "sensor page"
            return renderView.ProjectGraphView()
        else:
            return "Err"


class image(tornado.web.RequestHandler):
    def get(self, name):
        ext = name.split(".")[-1] # Gather extension
        return open('src/media/%s'%name,"rb").read()


class javascript(tornado.web.RequestHandler):
    def get(self, name):
        ext = name.split(".")[-1] # Gather extension
        print "JAVASCRIPT:::", name
        return open('src/js/%s'%name,"rb").read()


class graph(tornado.web.RequestHandler):
    def get(self, name=None):
        self.render("templates/baseW.html", title="My title", data=[])


class streamer(tornado.websocket.WebSocketHandler):

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")
    
    '''
    application = tornado.web.Application([
        (r"/", bla),
        (r'/var/(.+)', var),
        (r'/ver/(.+)', ver),
        (r'/rt/(.+)', streamer),
        (r'/rt/', streamer),
        (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': './src/media/'}),
        (r'/javascript/(.*)',tornado.web.StaticFileHandler, {'path': './src/js/'}),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': '.'}),
        (r'/bla/(.*)', bla)
    ])
    '''

class MlabVisualiser(tornado.web.Application):
    def __init__(self, projectName):
        self.lastWrite = time.time()
        self.projectName = projectName
        self.projectCallbacks = {}
        self.project = h5py.File(self.projectName+'.hdf5', 'a')
        handlers = [
            (r"/", graph),
            (r'/var/(.+)', var),
            (r'/ver/(.+)', ver),
            (r'/rt/(.+)', streamer),
            (r'/rt/', streamer),
            (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': './src/media/'}),
            (r'/javascript/(.*)',tornado.web.StaticFileHandler, {'path': './src/js/'}),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': '.'}),
            (r'/graph/(.*)', graph)
        ]
        tornado.web.Application.__init__(self, handlers)
        

    def addDataset(self, SensorLabel, valueName, valueCallback):
        try:
            dset = self.project.create_dataset(SensorLabel, (0,3), maxshape=(None, None))
        except Exception, e:
            print e
        self.projectCallbacks[SensorLabel] = valueCallback

    def getValue(self, SensorLabel):
        table = np.array(self.project[SensorLabel][:])
        table = np.append(table,[[table.shape[0], time.time(), self.projectCallbacks[SensorLabel]()]], axis=0)
        self.project[SensorLabel].resize(table.shape)
        self.project[SensorLabel][:,:]=table
        self.project.flush()

    def getSensors(self):
        return self.projectCallbacks.keys()

    
    def ThreadMeasure(self, parent, SensorLabels, delay, repeat):
            status = True
            print "run"
            loop = 0
            while status:
                if repeat == 0 or repeat >= loop:
                    if parent.lastWrite+delay/1000.0 <= time.time():
                        for SensorLabel in SensorLabels:
                            parent.getValue(SensorLabel)
                            parent.lastWrite = time.time()
                            loop =+ 1

    def run(self, dataNames, delay=1000, repeat=1):
        thr = threading.Thread(target=self.ThreadMeasure, args=(self, dataNames, delay, repeat))
        thr.setDaemon(True)
        thr.start()
        print "tohle je za threading"


    def startWeb(self):
        self.listen(8888)
        tornado.ioloop.IOLoop.current().start()

