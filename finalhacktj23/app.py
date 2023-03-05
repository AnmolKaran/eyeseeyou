from flask import Flask, render_template, request, url_for, flash, redirect
from sqlalchemy import true

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AAAA'

FINAL_LIST = []
curr_correct_val = "E"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/about')    
def about():
    return render_template('about.html')

@app.route('/eyetracker')
def eyetracker():
    return render_template('eyetracker.html')

count=0
l = [[13.125,'/static/images/E.png'],[6.562,'/static/images/F.png'],[6.562,'/static/images/P.png'],[4.594,'/static/images/Z.png'],[4.594,'/static/images/O.png'],[4.594,'/static/images/D.png'],[4.594,'/static/images/L.png'],[4.594,'/static/images/C.png'],[3.28,'static/images/H.png'],[3.28,'static/images/R.png'],[3.28,'static/images/U.png'],[3.28,'static/images/C.png'],[3.28,'static/images/V.png'],[1.9688,'static/images/Y.png'],[1.9688,'static/images/F.png'],[1.9688,'static/images/G.png'],[1.9688,'static/images/U.png'],[1.9688,'static/images/F.png'],[1.3125,'static/images/V.png'],[1.3125,'static/images/C.png'],[1.3125,'static/images/L.png'],[1.3125,'static/images/W.png'],[1.3125,'static/images/Y.png']]
#print(len(l))
@app.route('/snellentest', methods = ['GET','POST'])
def snellentest():
    global count
    global FINAL_LIST
    if(count < len(l)-1):
        if request.method == "POST":
            
            curr_correct_val = l[count][1].split(".")[0][-1]
            #print(curr_correct_val)
            val = request.form.get("userInput")
            val = (val).upper()
            classif = False

            if val == curr_correct_val:
                classif = True
            else:
                classif = False
            FINAL_LIST.append(classif)
            count+=1
            size = l[count][0]
            imgpath = l[count][1]
            data = {"size_mm": size, "image":imgpath}
         
            return render_template('snellentest.html',data = data)    #snellentest1()
         
        size = l[count][0]
        imgpath = l[count][1]
        data = {"size_mm": size, "image":imgpath}
        return render_template('snellentest.html',data = data)
    
    data = {"score":calcScore()}
    FINAL_LIST = []
    count = 0
    return render_template('score.html',data = data)

@app.route('/score', methods = ['GET','POST'])
def score():
    data = {"score":calcScore()}
    return render_template('score.html',data = data)


def corrCount(startind, endind):
    ct=0
    for p in range(startind,endind-1):
        if(FINAL_LIST[p]==True):
            ct+=1
    return ct


def calcScore():
    if FINAL_LIST[0] == False:
        return "20/200"
    if FINAL_LIST[1]== False or FINAL_LIST[2]==False:
        return "2/100"
    t3 = corrCount(3,8)
    t4 = corrCount(8,13)
    t5 = corrCount(13,18)
    t6 = corrCount(18,23)
    if t3>=4:
        if t4>=4:
            if t5>=4:
                if t6>=4:
                    return "20/20"
            return "20/30"
        return "20/50"
    return "20/70"

