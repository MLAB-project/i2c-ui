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


clients = []
Sensors = []
Outputs = []
GlobData = ["name"]

class hello(tornado.web.RequestHandler):
    def get(self):
        return render.touch()


class var(tornado.web.RequestHandler):
    def get(self, name):
        print "VAR get", name
        if str(name) == "json":
            json="?("
            print Sensors
            project = h5py.File(GlobData[0]+'.hdf5', 'a')
            for sens in Sensors:
                table = np.array(project[sens][:])
                json += '{"'+str(sens)+'":{"sensor":"'+str(sens)+'", "pointStart":'+str(float(table[0][1]))+',"pointInterval":'+str(1)+',"data":['
                for row in table:
                    json += str(float(row[2]))+', '
                json += ']'
                json += '},'
            json += '});'
            self.write( json )

        elif str(name) in Sensors:
            project = h5py.File(GlobData[0]+'.hdf5', 'a')
            table = np.array(project[str(name)][:])
            '''
            json="?("
            json += '{"'+str(name)+'":{"sensor":"'+str(name)+'", "pointStart":'+str(float(table[0][1]))+',"pointInterval":'+str(1)+',"data":['
            for row in table:
                json += str(float(row[2]))+', '
                print
            json += ']'
            json += '},'
            json += '});'
            '''
            self.write( str(table) )

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
        self.render("templates/baseW.html", title=str(sys.argv[0])+" "+ str(', '.join(map(str, Sensors))) + "I, "+ str(', '.join(map(str, Outputs))) + "O", data=[Sensors, Outputs])

def send_to_all_clients(msg):
    for client in clients:
        try:
            client.write_message(msg)
        except Exception, e:
            print "client " + str(client) + " is unreacheable"

class streamer(tornado.websocket.WebSocketHandler):

    def open(self):
        print("WebSocket opened")
        l_sensors = "$hello;"+str(len(Sensors))+";"
        for x in Sensors:
            l_sensors = l_sensors + ( x +";" )
        print l_sensors
        self.write_message(l_sensors)
        clients.append(self)

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed", self)
        try:
            clients.remove(self)
        except Exception, e:
            raise e
    

class MlabVisualiser(tornado.web.Application):
    def __init__(self, projectName="ProjectLog", LocalWebTime=1, filedivide=0):
        global GlobData
        GlobData[0] = projectName
        #GlobData[1] = LocalWebTime*60
        self.projectName = projectName
        self.projectCallbacks = {}
        self.project = h5py.File(self.projectName+'.hdf5', 'a', userblock_size=1024*filedivide)
        self.lastWrite = time.time()
        self.lastNewFile = time.time()
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
        val = self.projectCallbacks[SensorLabel]()
        table = np.append(table,[[table.shape[0], time.time(), val]], axis=0)
        self.project[SensorLabel].resize(table.shape)
        self.project[SensorLabel][:,:]=table
        self.project.flush()
        return val

    def getSensors(self):
        return self.projectCallbacks.keys()

    def ThreadMeasure(self, parent, input, output, delay, repeat):
            SensorLabels = sorted(input)
            OutputLabels = sorted(output)
            global Sensors
            Sensors = SensorLabels
            status = True
            print "run"
            loop = 0
            while status:
                if repeat == 0 or repeat >= loop:
                    if parent.lastWrite+delay/1000.0 <= time.time():
                        newtime=time.time()
                        for SensorLabel in SensorLabels:
                            id = SensorLabels.index(SensorLabel)
                            val = parent.getValue(SensorLabel)
                            send_to_all_clients(str("$rtdt")+";"+str(SensorLabel)+";"+str(newtime)+";"+str(val)+";"+str(id))
                            parent.lastWrite = time.time()
                            loop =+ 1

    def run(self, input=[], output=[], delay=1000, repeat=1):
        thr = threading.Thread(target=self.ThreadMeasure, args=(self, input, output, delay, repeat))
        thr.setDaemon(True)
        thr.start()
        print "tohle je za threading"


    def startWeb(self):
        self.listen(8888)
        tornado.ioloop.IOLoop.current().start()

