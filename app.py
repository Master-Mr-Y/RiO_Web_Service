from flask import Flask , render_template , request , jsonify
import time
import genai
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

web.run(debug=True)
    
    