## 测试表单提交
from flask import Flask
from flask import render_template, request
from wtforms import Form
# 导入数据范围 类
from wtforms import validators
from wtforms import widgets
# 导入注册数据 类
from wtforms.fields import simple

app = Flask(__name__, template_folder="views")
app.debug = True


# 注册表单类
class SubmitForm(Form):
    name = simple.StringField(
        label="用户名",
        validators=[
            validators.Length(min=5, max=10, message="用户名必须大于5位，小于10位"),
            validators.DataRequired(message="用户名不能为空")
        ],
        widget=widgets.TextInput(),

    )
    pwd = simple.StringField(
        label="密码",
        validators=[
            validators.DataRequired("密码不能为空"),
            validators.Length(min=6, message="密码不能小于6位"),
            validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{6,}",
                              message="密码至少6个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符")

        ],
        widget=widgets.PasswordInput()
    )


@app.route('/')
def hello_world():
    return login()


@app.route('/login', methods=['GET', 'POST'])
def login():
    lod = SubmitForm()
    # 提交方式验证 数据验证
    if request.method == 'POST' and lod.validate():
        # 返回的 getf 为一个  wtform 对象
        lod = SubmitForm(formdata=request.form)

        return render_template("login.html", cntent="hello",getf=lod )
    else:
        return render_template("login.html", cntent="hello",getf=lod)


if __name__ == '__main__':
    app.run()
