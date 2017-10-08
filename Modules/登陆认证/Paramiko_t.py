#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档：http://www.cnblogs.com/wupeiqi/articles/5095821.html

# 该模块基于SSH用于连接远程服务器并进行批量管理
# ssh的配置文件：/etc/ssh/sshd_config[配置ssh的端口号；是否允许root用户登陆]


'''
基于用户名密码连接
基于公钥密钥连接
基于用户名密码上传下载
基于公钥密钥上传下载
'''

#**********************************************主机连接登陆*************************************************************

# *************方法一：基于用户名密码连接
'''
import paramiko
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机，自动将相关信息添加到know_hosts文件中
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='c1.salt.com', port=22, username='wupeiqi', password='123')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()
# 关闭连接
ssh.close()
'''

# ************方法二：基于公钥密钥连接

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', pkey=private_key)

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')

transport.close()

#SSHClient 封装 Transport

#**********************************************文件上传下载*************************************************************

# ************方法一：scp命令实现

#scp -rp -P52113 root@192.168.80.128:/tmp

# ************方法二：paramiko模块实现基于用户名密码上传下载

import paramiko

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', password='123')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()

# ************方法三：paramiko模块实现基于公钥密钥上传下载

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()











