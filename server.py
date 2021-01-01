# coding: utf-8

import os
import sys

import cherrypy

from app import application

class Server:

    def main(self):
        # Get current directory
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
        except:
            current_dir = os.path.dirname(os.path.abspath(sys.executable))
        # disable autoreload
        cherrypy.engine.autoreload.unsubscribe()
        # activate logger
        cherrypy.config.update({'log.access_file': "access.log", 'log.error_file': "server.log", 'log.screen': True, })
        # Static content config
        static_config = {
            '/': {'tools.staticdir.root': current_dir, 'tools.staticdir.on': True, 'tools.staticdir.dir': './content'}}
        # Mount static content handler
        cherrypy.tree.mount(application.Application(), '/', static_config)
        cherrypy.tree.mount(self, '/shutdown', {'/': {}})
        # suppress traceback-info
        cherrypy.config.update({'request.show_tracebacks': False})
        # Start server
        cherrypy.engine.start()
        cherrypy.engine.block()

    @cherrypy.expose
    def index(self):
        cherrypy.engine.exit()

if __name__ == '__main__':
    server = Server()
    server.main()