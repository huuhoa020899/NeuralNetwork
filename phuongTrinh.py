
from http.server import HTTPServer,BaseHTTPRequestHandler
import cgi
import math
import UCLN
from Giaipt import GiaiPhuongTrinh
from random import randint
class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path =="/":
            self.path ="/phuongTrinh.html"
        try:
            f = open(self.path[1:]).read()
            self.send_response(200,"--Access successful--")
        except:
            f ="Not found"
            self.send_error(404,"Not found")
        self.end_headers()
        self.wfile.write(bytes(f,"utf-8"))
    def do_POST(self):
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
                                environ={"REQUEST_METHOD": "POST", "CONTENT_TYPE": self.headers["Content-type"]})
        self.send_response(200, "--Access successful--")
        self.end_headers()
        global a,b,c,delta,d,dem,tong,giaithua
        a= int(form.getvalue("a"))
        b= int(form.getvalue("b"))

        def UCLN(a, b):
            while (a != b):
                if a > b:
                    a = a - b
                else:
                    b = b - a
            return a

        def SearchMax(b):
            #n = int(input("Enter n:"))
            a = []
            for i in range(b):
                a.append(randint(-100, 100))
            print(a)
            x=max(a)
            return x

        def BCNN(a, b):
            return (a*b)/UCLN(a,b)

        def KTSNT(x):
            #x = int(input("enter x:"))
            dem = 0
            for i in range(1, x + 1):
                if x % int(i) == 0:
                    dem = dem + 1;
                if dem > 2:
                    break
            if dem == 2:
                return "N la so nguyen to"
            else:
                return " N k la so nguyen to"

        def Tong(n):
            tong = 0
            #n = int(input("Enter n:"))
            for i in range(n + 1):
                tong = tong + i
            return tong
        #c= float(form.getvalue("c"))
        #d= int(form.getvalue("d"))
        #if a==0:
        #   if b==0:
        #       msg="phuong trinh da cho vo nghiem"
        #    else:
        #        msg="phuong trinh co 1 nghiem:%f"%(float(-c/b))
        #else:
        #    delta=b*b-4*a*c
        #    if (delta > 0):
        #       x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        #        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        #        msg="phuong trinh co 2 nghiem phan biet x1=%f x2=%f"%(x1,x2)
        #    elif (delta == 0):
        #        x1 = (-b / (2 * a));
        #        msg="phuong trinh co 1 nghiem kep x=%f"%(x1)
        #    else:
        #       msg="phuong trinh vo nghiem"
        #while (a != b):
        #    if a > b:
        #        a = a - b
        #    else:
        #        b = b - a
        #msg="%f"%(a)
        #tong=0
        #for i in range(a):
        #    tong=tong+i
        #msg="%d"%(tong)
        #giaithua=1
        #for i in range(1,a):
        #    giaithua=giaithua*i
        #msg="Giai Thua: %d "%(giaithua)
        #dem = 0
        #for i in range(1, a + 1):
        #    if a % int(i) == 0:
        #        dem = dem + 1;
        #    if dem > 2:
        #        break
        #if dem == 2:
        #    msg="N la so nguyen to"
        #else:
        #    msg=" N k la so nguyen to"
        #if a == 0:
        #    if b == 0:
        #        msg = "Phuong trinh vo so nghiem"
        #    else:
        #        msg = "Phuong trinh vo nghiem."
        #else:
        #    x = -b / a
        #   msg = "Nghiem cua phuong trinh %f" % (x)
        msg = "TinhTong:%d "%(int(Tong(a)))

        self.wfile.write(bytes(msg,"utf-8"))
if __name__ == '__main__':
    HOST='localhost'
    PORT =8000
    ADD=(HOST,PORT)
    http_sv=HTTPServer(ADD,Server)
    try:
        print ("Server started http://%s:%s" %(HOST, PORT))
        http_sv.serve_forever()
    except:
        print("Error!")
