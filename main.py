#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello world"

@app.route("/login/get",methods=["GET"])
def login_using_get():
	user = request.args.get("user",None)
	pas = request.args.get('pass',None)
	return verify_credentials(user,pas)
		
@app.route("/login/post",methods = ["POST"])
def login_using_post():
	user = request.form.get("user",None)
	pas = request.form.get('pass',None)
	return verify_credentials(user,pas)
	
def verify_credentials(user:str,pas:str) -> str:
	if user and pas and user==app.config["user"] and pas==app.config["pass"]:
		return "Login succeeded",200
	else:
		return "Login failed",403
	
if __name__=="__main__":
	import argparse
	parser = argparse.ArgumentParser(description="Server for testing password attacks - hydra",exit_on_error=True,add_help=False,
	epilog="#POST /login/post\n#GET /login/get\n\nuser=^USER^&pass=^PASS^")
	parser.add_argument("--help",action="help",help="Show this help mesage and exit")
	parser.add_argument("host",nargs="?",help="Address for hosting the server - %(default)s",default="127.0.0.1")
	parser.add_argument("port",nargs="?",help="Port to listen at - %(default)s",type=int,default=8000)
	parser.add_argument("-u","--username",help="Login username - %(default)s",default="admin",metavar="USER",)
	parser.add_argument("-p","--password",help="Login password - %(default)s",default="dommy",metavar="PASS")
	args = parser.parse_args()
	app.config["user"]=args.username
	app.config["pass"]=args.password
	app.run(host=args.host,port=args.port,debug=False)
