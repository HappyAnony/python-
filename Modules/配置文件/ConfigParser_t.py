#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档：http://www.cnblogs.com/alex3714/articles/5161349.html
# 用于生成和修改常见配置文档
# python 3.x 版本中为 configparser
# python 2.X 版本中为 ConfigParser

'''生成配置文件
import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
   config.write(configfile)

'''

'''读取配置文件
import configparser
config = configparser.ConfigParser()
config.sections()
config.read('example.ini')
print(config.sections())
print('bitbucket.org' in config)
print('bytebong.com' in config)
print(config['bitbucket.org']['User'])
print(config['DEFAULT']['Compression'])
topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(topsecret['host port'])

for key in config['bitbucket.org']:
	print(key)

print(config['bitbucket.org']['ForwardX11'])
'''
#'''增删改查
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('i.cfg')

# ########## 读 ##########
# secs = config.sections()
# print secs
# options = config.options('group2')
# print options

# item_list = config.items('group2')
# print item_list

# val = config.get('group1','key')
# val = config.getint('group1','key')

# ########## 改写 ##########
# sec = config.remove_section('group1')
# config.write(open('i.cfg', "w"))

# sec = config.has_section('wupeiqi')
# sec = config.add_section('wupeiqi')
# config.write(open('i.cfg', "w"))


# config.set('group2','k1',11111)
# config.write(open('i.cfg', "w"))

# config.remove_option('group2','age')
# config.write(open('i.cfg', "w"))
#'''