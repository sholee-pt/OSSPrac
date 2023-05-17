from flask import Flask,render_template,request,redirect
from operator import itemgetter # 정렬 모듈

app=Flask(__name__)

rows = [] # 딕셔너리 데이터가 담긴 리스트

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/result',methods=['GET','POST'])
def result():
    global rows
    if request.method=='POST':
        result=dict()
        result['이름']=request.form.get('Name')
        result['학번']=request.form.get('StudentNumber')
        result['전공']=request.form.get('Major')
        result['이메일']=request.form.get('Email_id')+"@"+request.form.get('Email_addr')
        result['성별']=request.form.get("Gender")
        result['프로그래밍 언어']=",".join(request.form.getlist("PL_list"))
        rows.append(result)
        rows = sorted(rows, key = itemgetter('학번'))
        return render_template('result.html',rows=rows)
    else:
        if not rows:
            rows = [] 
        return render_template('result.html',rows=rows)

@app.route('/add', methods=['GET', 'POST'])
def add():
    action_btn = request.form.get('action_btn')
    global rows
    if request.method == 'POST':        
        if action_btn == 'delete_row':  # delete 기능
            selected_rows = request.form.getlist('row_checkbox')
            selected_rows = list(map(int, selected_rows))
            selected_rows.sort(reverse=True)
            for index in selected_rows:
                del rows[index]
            return redirect('/result')
        elif action_btn == 'home':  # Home 기능
            rows.clear()
            return redirect('/')
        else :
            return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=8000)