# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.log

logger = tornado.log.logging.getLogger()

tornado.log.access_log.setLevel(tornado.log.logging.DEBUG)
tornado.log.app_log.setLevel(tornado.log.logging.DEBUG)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hi Sandeep, Welcome to Tornado Web Framework.\n")

if __name__ == "__main__":
	logger.setLevel(tornado.log.logging.DEBUG)
	application = tornado.web.Application([
		(r"/", MainHandler),
	])
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
