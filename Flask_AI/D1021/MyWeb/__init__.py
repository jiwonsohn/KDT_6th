
# -------------------------------------------------------------
# Flask Framework에서 WebServer 구동 파일
#  - 파일명: app.py
# -------------------------------------------------------------

# 모듈 로딩
from flask import Flask, render_template

# 사용자 정의 함수-----------------------------------------------
def create_app():

    # 전역변수-------------------------------------------------------------------------
    # Flask Web Server 인스턴스 생성----------------------------------------------------
    #   => 서버 생성된 상황!
    APP = Flask(__name__)




    # 라우팅 기능 함수들-----------------------------------------------------------------
    #   => url 페이지 보여주는 기능
    #   ===사용법===
    #   @Flask Web Server 인스턴스변수명.route("URL")


    #   http://127.0.0.1:5000/
    #   "/" -> 루트 root: SW 시작 폴더, Linux/Mac 저장소 시작점
    @APP.route("/")
    def index():
        # return """ <body style='background-color:yellow; text-align:center'>
        #         <h1>Hello</h1>s
        #         </body>"""
        return render_template("index.html")



    @APP.route("/info")             #   http://127.0.0.1:5000/info
    @APP.route("/info/")             #   http://127.0.0.1:5000/info/
    def info():
        return """ <body style='background-color:skyblue; text-align:center'>
                <h1>INFORMATION</h1>
                </body>"""


    # http://127.0.0.1:5000/info/문자열변수
    # name에 문자열 변수 저장 , name=문자열변수
    @APP.route('/info/<name>')
    def printInfo(name):
        # return f"""
        #     <body style='background-color:bisque; text-align:center;'>
        #     <h1>{name}'s Information</h1>
        #     마침표 안했네...
        #     </body>
        # """
        return render_template("info.html", name=name)

    # http://127.0.0.1:5000/info/정수
    # age에 정수 저장
    @APP.route('/info/<int:age>')
    def checkAge(age):
        return f"""
            <body style='background-color:bisque; text-align:center;'>
            나이: {age}
            </body>
        """

    # http://127.0.0.1:5000/go
    #                   -> 여기서는 http://127.0.0.1:5000/로 이동하도록
    @APP.route("/go")
    def goHome():
        return APP.redirect("/")
    
    
    return APP

# 조건부 실행--------------------------------------------------------------
#   => 
if __name__ == '__main__':

    # Flask Web Server 구동
    app = create_app()
    app.run()


