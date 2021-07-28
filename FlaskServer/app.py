from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import os

from waitress import serve


app = Flask(__name__,template_folder='templates')

app.config['JSON_ASCII']=False


@app.route("/")
def index():
    return "<h2>Hello, World!</h2>"

@app.route('/method',methods=['GET','POST'])
def method():
    if request.method == 'GET':
        return "<h2>GET방식 요청</h2>"
    return "<h2>POST방식 요청</h2>"

@app.route('/querystring')
def query():
    name = request.args.get('name')
    id = request.args.get('id')
    pwd = request.args.get('pwd')
    return '''        
        <ul>
            <li>아이디 : {}</li>
            <li>비번 : {}</li>
            <li>이름 : {}</li>
        </ul>
    '''.format(id,pwd,name)

@app.route('/parameter/<name>')
def parameter(name):
    return '<h2>파라미터:{}</h2>'.format(name)

#템플릿파일 사용하기
#app.py와 같은 위치에 반드시 templates 라는 폴더 생성
#단 app = Flask(__name__,template_folder='임의의 폴더명')
#코드로 templates 폴더명 변경 가능
#템플릿 파일인 .html파일을 templates 폴더에 저장
#사용자에게 입력폼 서비스하기

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/formok',methods=['POST'])
def formok():
    name = request.form['name']
    id = request.form['id']
    pwd = request.form['pwd']
    return '''
            <ul>
                <li>아이디 : {}</li>
                <li>비번 : {}</li>
                <li>이름 : {}</li>
            </ul>
        '''.format(id, pwd, name)

@app.route('/template')
def template():
    return render_template('index.html')

@app.route('/ajax',methods=['POST'])
def ajax():
    print('request.content_type',request.content_type)
    print('request.is_json',request.is_json)
    data=request.get_json(force=True)
    print('value:{},type:{}'.format(data,type(data)))
    return jsonify({'users':data})


#jinja2 템플릿엔진 사용하기
'''
템플릿 파일인 .html에서 파이썬 코드 사용하기
{{변수}} 는 출력문  
{% 파이썬 코드 %}   
{#   주석   #}  
for문이나 if문은 반드시 블락을 닫아야 한다
{% for i in range(10) %}

{% endfor %}
{% if True %}

{% endif %} 식으로
'''
@app.route('/jinja2')
def jinja2():
    title='jinja2 템플릿 엔진'
    return render_template('jinja2/jinja2.html',title=title,header='JINJA2사용하기')

@app.route('/jinja2/extends')
def jinja2_extends():
    return render_template('jinja2/jinja2_1.html',title='템플릿 파일 상속받기',header='JINJA2의 템플릿 상속',number=2021)

@app.route('/upload')
def upload_form():
    return render_template('upload.html')

@app.route('/upload',methods=["POST"])
def upload():
    try:
        f=request.files['upload']
        print('value:{},type:{}'.format(f,type(f)))
        filename=f.filename[0:-1] if f.filename[-1]=='"' else f.filename
        print('filename:',filename)
        f.save('upload{}{}'.format(os.path.sep,filename))
    except Exception as e:
        return jsonify({'error':e})
    return jsonify({'success':filename})

if __name__== '__main__':

    #app.run(host='0.0.0.0',port=8282)
    serve(app,host='0.0.0.0',port=8282)

