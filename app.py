from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "hello flask"
'''
 it means running app.py from command line (main entry) 
'''
if __name__=="__main__":
    app.run()
