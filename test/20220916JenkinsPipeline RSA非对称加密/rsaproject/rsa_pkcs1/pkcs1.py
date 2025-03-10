"""
============================
Project: rsaproject
Author:柠檬班-海励
Time:2022/9/16 19:34
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
前程贷使用的是pkcs1
不分段加密
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
        self.pubkey =rsa.PublicKey.load_pkcs1(pubkey)
        self.privkey=rsa.PrivateKey.load_pkcs1(privkey)
    #加密
    def encode_string(self,string):
        msg = string.encode("utf8")
        encrypt_msg = rsa.encrypt(message=msg,pub_key=self.pubkey)
        print("base64之前：",type(encrypt_msg),encrypt_msg)
        encrypt_msg = base64.b64encode(encrypt_msg)
        print("base64之后：",type(encrypt_msg), encrypt_msg)
        encrypt_msg = encrypt_msg.decode()
        print("decode后：",type(encrypt_msg), encrypt_msg)
        return encrypt_msg
    #解密
    def decode_string(self,encrypt_msg):
        #加密的逆向过程，先对字符串进行encode()，在进行base64.b64decode(encrypt_msg)，在通过rsa模块decrypt
        encrypt_msg = encrypt_msg.encode()
        encrypt_msg = base64.b64decode(encrypt_msg)
        decrypt_str = rsa.decrypt(crypto=encrypt_msg,priv_key=self.privkey)
        new_decrypt_str=decrypt_str.decode(encoding="utf8")
        print("解密后：",new_decrypt_str)
if __name__ == '__main__':
    cl = MyRsa()
    encrypt_msg = cl.encode_string(string="123456")
    cl.decode_string(encrypt_msg=encrypt_msg)


