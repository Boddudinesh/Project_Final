import matplotlib
import os
import pandas as pd
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
from flask import Flask,render_template,request
from threading import Lock


app=Flask(__name__)
lock = Lock()
files=[]

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

@app.route('/result',methods=['GET','POST'])
def get_plot():
    with lock:
        k=request.form['reg']
        r=k.strip()
        r=r.lower()
        dep=r[4:6].upper()
        cnt = 0
        sub = 0
        gt = 0
        y=0
        ch = r[3:6]
        ch2 = r[:3]
        img_list = []
        mar=[]
        ranks_t = []
        x_ax = []
        y_ax = []
        sems = []
        links=[]
        total_m = []
        total_s = []
        g = []
        c = []
        percent=[]
        plt.rcParams['figure.figsize'] = (9, 5)
        ma=pd.read_excel("static/GeneratedLinks.xlsx")
        if ch == "acs":
            flag = 1
        elif ch == "acm":
            flag = 2
        elif ch == "ait":
            flag = 3
        elif ch == "acb":
            flag = 4
        elif ch == "ads":
            flag = 5
        elif ch == "aei":
            flag = 6
        elif ch == "aec":
            flag = 7
        elif ch == "ace":
            flag = 8
        elif ch == "ame":
            flag = 9
        elif ch == "aee":
            flag = 10

        if ch2 == "y20" or ch2 == "l21":
            num = 7
            y = 4
        elif ch2 == "y21" or ch2 == "l22":
            num = 5
            y = 3
        elif ch2 == "y22" or ch2 == "l23":
            num = 3
            y = 2

        try:
            for i in range(1, num):
                try:
                    if flag == 1:
                        df = pd.read_csv(f"Departments//CSE//CSE-{y}.{i}.csv")
                    elif flag == 2:
                        df = pd.read_csv(f"Departments//AIML//AIML-{y}.{i}.csv")
                    elif flag == 3:
                        df = pd.read_csv(f"Departments/IT/IT-{y}.{i}.csv")
                    elif flag == 4:
                        df = pd.read_csv(f"Departments//CB//CB-{y}.{i}.csv")
                    elif flag == 5:
                        df = pd.read_csv(f"Departments//DS//DS-{y}.{i}.csv")
                    elif flag == 6:
                        df = pd.read_csv(f"Departments//EIE//EIE-{y}.{i}.csv")
                    elif flag == 7:
                        df = pd.read_csv(f"Departments//ECE//EC-{y}.{i}.csv")
                    elif flag == 8:
                        df = pd.read_csv(f"Departments//CIVIL//CE-{y}.{i}.csv")
                    elif flag == 9:
                        df = pd.read_csv(f"Departments//MECH//ME-{y}.{i}.csv")
                    elif flag == 10:
                        df = pd.read_csv(f"Departments//EEE//EEE-{y}.{i}.csv")
                except:
                    return render_template('Error.html')

                data =ma.loc[ma["File Name"] == f"{dep}-{y}.{i}.xlsx"]
                dat = data.values.tolist()[0]
                links.append(dat[1])
                re = df["Reg No"].tolist()
                if r in re:
                    x = df.loc[df["Reg No"] == r]
                    cols = x.columns.tolist()
                    marks = x.values.tolist()[0]
                    regd = marks[0].lower()
                    name = marks[1]
                    fname = marks[2]
                    rank_m = marks[4]
                    rank_s = marks[6]
                    sgpa = marks[5]
                    total1 = marks[3]
                    sems.append(i)
                    if len(cols) == 35:
                        # 7
                        subjects = cols[7:14]
                        sub_marks = marks[7:14]
                        cred = marks[14:21]
                        topper = df[df['total'] == df['total'].max()]
                        topper_m = topper.values.tolist()[0]
                        total2 = topper_m[2]
                        topper_m = topper_m[7:14]
                        subj = marks[-7:-1]
                        subj.append(marks[-1])
                        subj_rank = marks[-14:-7]
                        sub += 7
                        gt += total1
                        percent.append(int(total1/7))
                    elif len(cols) == 39:
                        subjects = cols[7:15]
                        # 8
                        sub_marks = marks[7:15]
                        cred = marks[15:24]
                        topper = df[df['total'] == df['total'].max()]
                        topper_m = topper.values.tolist()[0]
                        total2 = topper_m[2]
                        topper_m = topper_m[7:15]
                        subj = marks[-8:-1]
                        subj.append(marks[-1])
                        subj_rank = marks[-16:-8]
                        sub += 8
                        gt += total1
                        percent.append(int(total1/8))
                    elif len(cols) == 43:
                        # 9
                        subjects = cols[7:16]
                        sub_marks = marks[7:16]
                        cred = marks[16:25]
                        topper = df[df['total'] == df['total'].max()]
                        topper_m = topper.values.tolist()[0]
                        total2 = topper_m[2]
                        topper_m = topper_m[7:16]
                        subj = marks[-9:-1]
                        subj.append(marks[-1])
                        subj_rank = marks[-18:-9]
                        sub += 9
                        gt += total1
                        percent.append(int(total1/9))

                    p = pd.DataFrame({r: sub_marks, "1st ranker (Total Marks)": topper_m}, index=subjects)
                    ax = p.plot.bar()
                    plt.yticks(range(0, 160, 20))
                    plt.xticks(rotation=360)
                    plt.xlabel("Subjects",fontweight="bold")
                    plt.ylabel("Marks",fontweight="bold")
                    ax.set_facecolor("#e0e0e0")
                    for p in ax.patches:
                        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center',
                                    va='bottom', fontsize=10, color='black', xytext=(0, 5), textcoords='offset points')
                    plt.savefig(f"static/{r}_{i}.png")
                    plt.close()
                    img_list.append(f"static/{r}_{i}.png")
                    files.append(f"static/{r}_{i}.png")
                    grade=[]
                    ranks_t.append(total1)
                    total_m.append(total1)
                    ranks_t.append(rank_m)
                    ranks_t.append(sgpa)
                    total_s.append(sgpa)
                    ranks_t.append(rank_s)
                    for m in sub_marks:
                        if m>=90:
                            grade.append('10')
                        elif m<90 and m>=80:
                            grade.append('9')
                        elif m>=70 and m<80:
                            grade.append('8')
                        elif m>=60 and m<70:
                            grade.append('7')
                        elif m>=50 and m<60:
                            grade.append('6')
                        elif m>=40 and m<50:
                            grade.append('4')
                        else:
                            grade.append('0')

                    tabl = pd.DataFrame(list(zip(subj, sub_marks, subj_rank, grade, cred)),
                                        columns=['Subject Title & Code', 'Marks','Subject Rank', 'Grade','CR'])
                    html_table = tabl.to_html(index=False)
                    for t in range(len(grade)):
                        g.append(grade[t])
                        c.append(cred[t])
                    styles=f"<head><link href='styles.css?v={r}' rel='stylesheet'></head><center>"
                    with open(f"static/{r}_sem{i}.html","w+") as f:
                        f.write(styles)
                        f.write(html_table)
                        f.write("</center>")
                    cnt += 1
                    files.append(f"static/{r}_sem{i}.html")
                else:
                    continue
        except:
            return render_template('Error.html')

        index=[0,4,8,12,16,20,24]
        c_t=0.0
        gc_t=0.0
        for m in range(len(c)):
            gc_t+=float(g[m])*c[m]
            c_t+=c[m]
        plt.clf()
        x_ax = sems
        y_ax = percent
        plt1.xticks(x_ax)
        plt1.ylim((0, 100))
        plt1.plot(x_ax, y_ax, marker="o")
        ax=plt1.gca()
        ax.set_facecolor("#e0e0e0")
        for i, txt in enumerate(y_ax):
            plt1.annotate(txt, (x_ax[i], y_ax[i]), textcoords="offset points", xytext=(0,5), ha='center')
        plt1.xlabel("Semester",fontweight="bold")
        plt1.ylabel("Total Marks(%)",fontweight="bold")
        plt.title("Total Marks(%) Graph")
        plt1.savefig(f"static/marks_{r}.png")
        mar.append(f"static/marks_{r}.png")
        files.append(f"static/marks_{r}.png")
        plt1.clf()
        plt1.close()
        x_ax = sems
        y_ax = total_s
        plt1.xticks(x_ax)
        plt1.ylim((0, 10))
        plt1.plot(x_ax, y_ax, marker="o")
        ax=plt1.gca()
        ax.set_facecolor("#e0e0e0")
        for i, txt in enumerate(y_ax):
            plt1.annotate(txt, (x_ax[i], y_ax[i]), textcoords="offset points", xytext=(0, 5), ha='center')
        plt1.xlabel("Semester",fontweight="bold")
        plt1.ylabel("SGPA",fontweight="bold")
        plt1.title("SGPA Graph")
        plt1.savefig(f"static/sgpa_{r}.png")
        mar.append(f"static/sgpa_{r}.png")
        mar.append(f"static/sgpa_{r}.png")
        plt1.close()
        if cnt == 0:
            return render_template('Error.html')
        return render_template('result.html',r=r,R=r.upper(),n=name,lin=links,mar=mar,index=index,sem=sems,marks=ranks_t,gt=gt,perc=round(((gt/sub*100)/100),2),cgpa=round((gc_t/c_t),5),f=fname,l=len(img_list),img=img_list)
app.secreat_key='some secreat that you will never guss'

if __name__=="__main__":
    app.run(host="0.0.0.0",port=80,debug=True)



