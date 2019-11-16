# -*- coding: UTF-8 -*-



import logging



logging.basicConfig(level=logging.DEBUG,
                    filename='my.log',
                    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')


logger=logging.getLogger(__name__)

msg='DeBug information'
logger.debug(msg)

msg='测试正常'
logger.debug(msg)
msg='运行正常'
logger.info(msg)
msg='警告，运行错误'
logger.warning(msg)
msg='严重警告，可能无法运行'
logger.error(msg)
msg='系统崩溃'
logger.critical(msg)

def mylog():
