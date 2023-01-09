import json
import random
from flask import Flask,render_template,send_from_directory,request,redirect

app=Flask(__name__,template_folder='./templates',static_folder='./templates/css')

code_length=5	# 短链接code的长度
code_dic='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'	# code的值的来源
host='http://127.0.0.1:5000/'	# 服务器地址或域名, 用于返回短链
backup_pwd='123'	# 备份密码, 可使用上面的host+此密码获取全站数据(127.0.0.1:5000/123)

# 获取短链接的code
def get_new_code():
	return ''.join(random.sample(list(code_dic),code_length))

# 读取数据
def read_data():
	with open('data.json','r')as file:
		return json.loads(file.read())

# 判断是否已经存在了要缩短的链接
def if_in_data(url):
	if url in read_data()[1]:
		return True
	else:
		return False

# 前提是if_in_data通过, 从数据文件中根据code获取链接
def get_code_from_data(url):
	return read_data()[0][url]

# 根据code获取链接
def get_url_from_code(code):
	data_list=read_data()[0].items()
	for data_element in data_list:
		if data_element[1][0]==code:
			return data_element[1][1],data_element[0]
		else:
			pass

# 添加新数据到数据文件
def add_data(code,url,preview_word=''):
	data=read_data()
	data[0][url]=[code,preview_word]
	data[1].append(url)
	with open('data.json','w')as file:
		file.write(json.dumps(data,ensure_ascii=False))

@app.route('/',methods=['POST', 'GET'])
def index_page():
	if request.method=='POST':
		url=request.form.get('url')
		preview_word=request.form.get('preview_word')
		if url.startswith('https://') or url.startswith('http://'):
			if if_in_data(url):
				code=get_code_from_data(url)[0]
				used=True
			else:
				code=get_new_code()
				add_data(code,url,preview_word)
				used=False
			return json.dumps({'code':200,'used':used,'short_code':code,'short_url':host+code,'goal_url':url},ensure_ascii=False)
		else:
			return '请输入格式正确的链接!'
	return render_template('index.html')

@app.route('/<string:code>')
def send_me_to_page(code):
	if code=='about':
		pass
	else:
		try:
			description,url=get_url_from_code(code)
			return "<!DOCTYPE html><html><head><meta charset='utf-8'><meta name='description' content='%s'><title>%s</title></head><body><article>%s</article><meta http-equiv='refresh' content='0;url=%s'><</body></html>"%(description,description,description,url)
		except:
			return '错误!'

@app.route('/about')
def about_page():
	return '* 只需将要缩短的链接粘贴在第一个输入框, 随后回车即可(第二个输入框似乎是没用的...);<br>* 回车后会得到一组json数据, 若要直接使用短链只需复制short_url的值.'

@app.route('/%s'%backup_pwd)
def backup():
	return send_from_directory('./','data.json')