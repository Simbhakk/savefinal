import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return """
<center> 
    <h1>Welcome to Save restricted website </h1>
    <p> Hi , If you are able to see this website ,</br> then it means our bot is working perfectly</p>
    <img src="https://graph.org/file/121de3eeefcb047facd3e.jpg" style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://github.com/Simbhakk/none okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 main.py &")
