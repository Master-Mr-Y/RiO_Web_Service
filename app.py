from flask import Flask , render_template , request , jsonify
import time
import genai
import os
# AI section

def worrior(qurry):
    
    replay_msg = genai.engine(qurry)
    
    return replay_msg

# Flask section

web = Flask(__name__)

@web.route("/")

def intro():
    
    return render_template("intro.html")
@web.route("/index" , methods=["GET","POST"])
def main():
    
    if request.method == "POST":
        
        user = request.form["user"]
        
        sam = worrior(user)
        
        return jsonify({
            
              "results" : sam
        })
    
    return render_template("index.html")

if __name__ =="__main__":
    port = int(os.environ.get("PORT",5000))
    web.run(host="0.0.0.0",port=port)
    
    
