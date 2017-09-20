#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档：http://www.cnblogs.com/alex3714/articles/5161349.html
# 散列消息鉴别码，简称HMAC，是一种基于消息鉴别码MAC（Message Authentication Code）的鉴别机制
# 使用HMAC时,消息通讯的双方，通过验证消息中加入的鉴别密钥K来鉴别消息的真伪
# 一般用于网络通信中消息加密，前提是双方先要约定好key,就像接头暗号一样，然后消息发送把用key把消息加密
# 接收方用key ＋ 消息明文再加密，拿加密后的值 跟 发送者的相对比是否相等，这样就能验证消息的真实性，及发送者的合法性了
# hmac为一种对称加密算法，此处可逆；它内部对我们创建 key 和 内容 再进行处理然后再加密

import hmac
# key和text都只能是bytes；要么使用b明确定义bytes类型，此时不支持中文，因为b只支持ASCII码
h = hmac.new(b'adg', b'my name')
print(h.hexdigest())
# 要么使用字串的encode方法将其编码，因为编码的本质就是转换成了bytes类型进行存储
h = hmac.new('adg15栈'.encode(encoding="utf-8"), 'my name is 张无忌'.encode(encoding="utf-8"))
print(h.hexdigest())