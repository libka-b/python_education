import urllib
import urllib.request as req
import time
import base64

url = "http://192.168.1.1/"

"""for pair in asus_test:# pairs:
    user = pair.get("login")
    password = pair.get("password")
    try:
        request = req.Request(url)
        b64string = base64.encodestrings("%s:%s" % (user, password))
        request.add_header(user_agent, "Authorization", "Basic %s" % b64string)
        result = urllib.urlopen(request)
        if result.getcode() == 200:
            print("login/pass: %s/%s" % (user, password))
    except Exception as e:
        print(e.getcode())"""

logins = [
    "admin",
    "",
    "Admin",
    "Administrator",
    "administrator",
    "root",
    "guest",
    "login",
    "support",
    "sysadmin",
    "tech",
    "user",
    "webadmin"
]

passwords = [
    "123456",
    "12345",
    "1234",
    "letmein",
    "password",
    "private",
    "public",
    "secret"
    ]

pairs = [
    {"login" : "Admin", "password" : "admin"},
    {"login" : "Administrator", "password" : "admin"},
    {"login" : "Administrator", "password" : "smcadmin"},
    {"login" : "User", "password" : "Password"},
    {"login" : "User", "password" : ""},
    {"login" : "Username", "password" : "Password"},
    {"login" : "", "password" : "1234"},
    {"login" : "", "password" : ""},
    {"login" : "", "password" : "admin"},
    {"login" : "adm", "password" : ""},
    {"login" : "admim", "password" : "password"},
    {"login" : "admin2", "password" : "admin"},
    {"login" : "admin2", "password" : "changeme"},
    {"login" : "admin", "password" : "1111"},
    {"login" : "admin", "password" : "1234admin"},
    {"login" : "admin", "password" : "2222"},
    {"login" : "admin", "password" : "Password"},
    {"login" : "admin", "password" : ""},
    {"login" : "admin", "password" : "admin123"},
    {"login" : "admin", "password" : "admin"},
    {"login" : "admin", "password" : "changeme"},
    {"login" : "admin", "password" : "default"},
    {"login" : "admin", "password" : "epicrouter"},
    {"login" : "admin", "password" : "hello"},
    {"login" : "admin", "password" : "netadmin"},
    {"login" : "admin", "password" : "operator"},
    {"login" : "admin", "password" : "password"},
    {"login" : "admin", "password" : "root"},
    {"login" : "admin", "password" : "secure"},
    {"login" : "admin", "password" : "setup"},
    {"login" : "admin", "password" : "sky"},
    {"login" : "admin", "password" : "smcadmin"},
    {"login" : "admin", "password" : "system"},
    {"login" : "admin", "password" : "senha"},
    {"login" : "admin", "password" : "123senha"},
    {"login" : "admin", "password" : "senha123"},
    {"login" : "admin", "password" : "gvt12345"},
    {"login" : "admin", "password" : "Gvt12345"},
    {"login" : "admin", "password" : "DLKT20090202"},
    {"login" : "TMARDLKT93319", "password" : "DLKT93319"},
    {"login" : "ZXDSL", "password" : "ZXDSL"},
    {"login" : "DXDSL", "password" : "DXDSL"},
    {"login" : "ADSL", "password" : "expert03"},
    {"login" : "comcast", "password" : "1234"},
    {"login" : "cusadmin", "password" : "highspeed"},
    {"login" : "customer", "password" : "none"},
    {"login" : "login", "password" : "1111"},
    {"login" : "login", "password" : "admin"},
    {"login" : "login", "password" : "password"},
    {"login" : "manager", "password" : "admin"},
    {"login" : "root", "password" : "1234"},
    {"login" : "root", "password" : "Admin"},
    {"login" : "root", "password" : "admin"},
    {"login" : "smc", "password" : "smcadmin"},
    {"login" : "support", "password" : "supportpw"},
    {"login" : "sysadm", "password" : "sysadm"},
    {"login" : "user", "password" : ""},
    {"login" : "user", "password" : "password"},
    {"login" : "user", "password" : "user"}
    ]

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"

"""for logs in logins:
    for passw in passwords:
        pairs.append({"login" : logs, "password" : passw})"""

asus_test = [
    {"login" : "admin", "password" : "password"},
    {"login" : "admin", "password" : "admin"},
    {"login" : "admin", "password" : "12345"},
    {"login" : "admin", "password" : "root"},
    {"login" : "admin", "password" : "none"}
]

for pair in asus_test:
    time.sleep(2)
    user = pair.get("login")
    password = pair.get("password")
    try:
        password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        top_level_url = url
        password_mgr.add_password(None, top_level_url, user, password)
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        opener = urllib.request.build_opener(handler)
        print("Trying credentials: " + str(user) + ":" + str(password))
        print("Server status: " + str(opener.open(url).getcode()))
        if opener.open(url).getcode() == 200:
            print("login/pass: %s/%s" % (user, password))
        #urllib.request.install_opener(opener)
        opener.close()
    except Exception as e:
        print("Server status: " + str(e.getcode()))
        print("Urllib exception:\n\r" + str(e.info()))

