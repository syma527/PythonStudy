"""
============================
Project: rsaproject
Author:柠檬班-海励
Time:2022/9/16 19:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
#加密分片长度
max_encode_len = 证书key位数/8 - 11

#解密分片长度
max_decode_len=base64.b64decode(msg='无需分段加密后密文')

#加密的 plaintext = max_len 最大长度是 证书key位数/8 - 11
例如1024 bit的证书，被加密的串最长 1024/8 - 11=117,加密得到的密文长度，却恰恰是密钥的长度

"""
import rsa
import base64

class MyRsa:
    def __init__(self):
        privkey = """
        -----BEGIN RSA PRIVATE KEY-----
        MIIBOwIBAAJBAJBWZJsSrhwDmtjZkq0hsS0ZSa7JJPvo5gfybdHnRLuZa9jGwfBh
        sXFFCJYnZabjQLJ1oPbQ1f7jwbS1WDxI9FkCAwEAAQJABkvuiaFP/SLfH3SmZG0i
        2I/Q2hImTeMEHfaiedS37wjwFCjtK12O73ZviLjtpeFyWHcoqEkAhxTvZZfpGNWs
        vQIjAMrsJdBGRb3IFktM6+JF6aHAsUPp2Py7tYo++R241U/kAm8CHwC2F1jyw0Lb
        o1v/t2dDq6U1/TbpcnfqUI5zzw6HubcCIi2LJM2DCCIZJ0/NOt/1GwOv0NlSQd4v
        bwZRLe5Kzq14mkcCHkmlQ7pbssy2U10nRkKeR2GAmhbszwcbsaGxGsVWHQIiE6tW
        fSyhJt5DtrAhwkbZwRqWFjovii5QSSzuBmFztnt8VA==
        -----END RSA PRIVATE KEY-----
        """
        pubkey = """
        -----BEGIN RSA PUBLIC KEY-----
        MEgCQQCQVmSbEq4cA5rY2ZKtIbEtGUmuyST76OYH8m3R50S7mWvYxsHwYbFxRQiW
        J2Wm40CydaD20NX+48G0tVg8SPRZAgMBAAE=
        -----END RSA PUBLIC KEY-----
        """
        #加载秘钥对象
        self.pubkey =rsa.PublicKey.load_pkcs1(pubkey)
        self.privkey=rsa.PrivateKey.load_pkcs1(privkey)
        #预加密计算模长
        self.max_encode_len,self.max_decode_len = self.choice_channel()

    #预加密，获取模长
    def choice_channel(self):
        msg = "test".encode()
        models_dict={'64':512,'128':1024,"512":2048}
        #加密，获取bytes类型的秘钥长度
        encrypt_msg = rsa.encrypt(message=msg, pub_key=self.pubkey)
        max_decode_len = len(encrypt_msg)
        print("解密模长：", max_decode_len)
        key_size = models_dict['{}'.format(max_decode_len)]
        max_encode_len = int(key_size/8-11)
        print("加密模长：",max_encode_len)
        return max_encode_len,max_decode_len

    #加密
    def encode_string(self,string):
        msg = string.encode()
        encrypt_msg = rsa.encrypt(message=msg,pub_key=self.pubkey)
        encrypt_msg = base64.b64encode(encrypt_msg)
        encrypt_msg = encrypt_msg.decode()
        return encrypt_msg

    #解密
    def decode_string(self,encrypt_msg):
        #加密的逆向过程，先对字符串进行encode()，在进行base64.b64decode(encrypt_msg)，在通过rsa模块decrypt
        encrypt_msg = base64.b64decode(encrypt_msg)
        decrypt_str = rsa.decrypt(crypto=encrypt_msg,priv_key=self.privkey)
        new_decrypt_str=decrypt_str.decode()
        print("解密结果：",new_decrypt_str)
        return new_decrypt_str

    #分段加密
    def section_encode(self,msg):
        if len(msg) <= self.max_encode_len:
            print("不需要进行分段加密")
            encode_string = self.encode_string(string=msg)
            print("加密结果：", encode_string)
            return encode_string
        else:
            print("需要分段加密")
            encode_text = []
            for i in range(0,len(msg),self.max_encode_len):
                #需要加密的字符串进行切片
                section_text = msg[i:(i+self.max_encode_len)]
                section_text = section_text.encode()
                #分段加密
                encode_str = rsa.encrypt(message=section_text, pub_key=self.pubkey)
                encode_text.append(encode_str)
            #拼接加密后的bytes数据
            encode_bytes = b"".join(encode_text)
            encode_string = base64.b64encode(s=encode_bytes)
            encode_string = encode_string.decode()
            print("分段加密结果：",encode_string)
            return encode_string

    #分段解密
    def section_decode(self,msg):
        decode_str = msg.encode()
        decode_str = base64.b64decode(decode_str)
        if len(decode_str) <= self.max_decode_len:
            print("不需要分段解密")
            decode_string = self.decode_string(encrypt_msg=msg)
            print("解密结果：",decode_string)
            return decode_string
        else:
            print("需要分段加密")
            decode_text=[]
            for i in range(0,len(decode_str),self.max_decode_len):
                section_text = decode_str[i:(i + self.max_decode_len)]
                decrypt_str = rsa.decrypt(crypto=section_text, priv_key=self.privkey)
                decode_text.append(decrypt_str)
            decode_byte = b"".join(decode_text)
            decode_string = decode_byte.decode()
            print("解密结果：",decode_string)
            return decode_string

if __name__ == '__main__':
    cl = MyRsa()
    test_str = "dsdffasdfdsdffasdfasdfdsdffasdfasdfdsdffasdfasdfdsdffasdfasdfdsdffasdfasdfdsdffasdfasdfdsdffasdfasdfdsdff"
    res = cl.section_encode(msg=test_str)
    cl.section_decode(msg=res)


