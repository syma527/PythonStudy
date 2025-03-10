"""
============================
Project: rsaproject
Author:柠檬班-海励
Time:2022/9/16 19:28
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
简历
http://testingpai.com/article/1637675445921

pycrypto和crypto是同一个库，crypto在 python 中又被称为pycrypto，它是一个第三方库，但是已经停止更新了，所以不建议大家安装。
pycryptodome是crypto的延伸版本，用法和crypto是一模一样的，可以完全替代crypto。
如果上述方法仍不能解决问题，可以找到 python 下面的\Lib\site-packages，手动将crypto改为Crypto
pip3.8  install pycryptodome
支持pkcs1+pkcs8
#加密分片长度
max_encode_len = 证书key位数/8 - 11

#解密分片长度
max_decode_len=base64.b64decode(msg='无需分段加密后密文')
"""

import traceback
import base64
from Crypto.PublicKey import RSA
#Crypto模块中的pkcs1_v1_5就是pkcs8的格式的秘钥
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_v1_5_Cipher

class RSACrypto(object):
    def __init__(self, private_key=None, public_key=None):
        # 秘钥从文件读取
        self.private_key = RSA.import_key(open('privkeyzj.pem').read())
        self.public_key = RSA.import_key(open('pubkeyzj.pem').read())
        self.max_encode_len,self.max_decode_len=self.choice_channel()

    # 预加密,获取模值
    def choice_channel(self):
        try:
            msg='test'
            models_dict={'64': 512, '128': 1024, "512": 2048}
            pk = PKCS1_v1_5_Cipher.new(key=self.public_key)
            encrypt_text = pk.encrypt(msg.encode())  # 进行加密
            result = base64.b64encode(encrypt_text).decode()  # 加密通过base64进行编码
            decode_str = base64.b64decode(result)
            max_decode_len = len(decode_str)
            key_size=models_dict['{}'.format(max_decode_len)]
            max_encode_len=int(key_size/8-11)
            #print('初始化获取的模值:',max_encode_len,max_decode_len)
            return max_encode_len,max_decode_len
        except Exception as e:
            print(traceback.print_exc(),e)

    # 公钥加密
    # 初始化公钥--初始化加密方法--加密字符串编码encode()--加密方法加密--加密后进行base64编码---完成
    # 公钥分段加密(在用)
    def to_encrypt_section(self,msg):
        try:
            # 加密的 plaintext = max_len 最大长度是 证书key位数/8 - 11, 例如1024 bit的证书，被加密的串最长 1024/8 - 11=117,加密得到的密文长度，却恰恰是密钥的长度
            pk = PKCS1_v1_5_Cipher.new(key=self.public_key)
            if len(msg) <= self.max_encode_len:
                encrypt_text = pk.encrypt(msg.encode())  # 进行加密
                result = base64.b64encode(encrypt_text).decode()  # 加密通过base64进行编码
                return result
            else:
                encrypt_text = []
                for i in range(0, len(msg), self.max_encode_len):
                    cont = msg[i: (i + self.max_encode_len)]
                    encrypt_text.append(pk.encrypt(message=cont.encode()))
                encrypt_data = b''.join(encrypt_text)
                # base64 编码
                result = base64.b64encode(s=encrypt_data).decode()
                return result
        except Exception as e:
            print(traceback.print_exc(),e)

    #分段解密
    def to_decrypt_section(self,msg):
        try:
            decode_str = base64.b64decode(msg)
            decode_msg=PKCS1_v1_5_Cipher.new(key=self.private_key)
            #max_decode_len = 128
            if len(decode_str) <= self.max_decode_len:
                text = decode_msg.decrypt(decode_str, 'DecryptError')
                return text.decode()  # 解密出来的是字节码格式，decodee转换为字符串
            else:
                text = []
                for i in range(0,len(decode_str),self.max_decode_len):
                    cont=decode_str[i: (i + self.max_decode_len)]
                    data = decode_msg.decrypt(ciphertext=cont, sentinel='to_decrypt_section_error')
                    text.append(data)
                decrypt_text=b''.join(text)
                result=decrypt_text.decode()
                return result
        except Exception as e:
            print(traceback.print_exc(),e)

if __name__ == '__main__':
    cl=RSACrypto() #初始化秘钥
    str1='123456'
    decodestr=cl.to_encrypt_section(msg=str1)
    print("加密后：",decodestr)
    str2 = cl.to_decrypt_section(msg=decodestr)
    print("解密后：",str2)



