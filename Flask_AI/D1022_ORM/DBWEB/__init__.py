
# -------------------------------------------------------------
# Flask Framework에서 WebServer 구동 파일
#  - 파일명: app.py
# -------------------------------------------------------------

# 모듈 로딩
from flask import Flask


# DB관련 설정
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB = SQLAlchemy()           #
MIGRATE = Migrate()



# -------------------------------------------------------------
# Application 생성 함수
#  - 함수명: create_app
# -------------------------------------------------------------


def create_app():

    # flask web server 인스턴스 생성
    APP = Flask(__name__)


    ## 점프 투 플라스트 p.51--------------------
    # DB 관련 초기화 설정
    APP.config.from_object(config)

    # DB 초기화 및 앱 연동
    DB.init_app(APP)
    MIGRATE.init_app(APP, DB)

    # DB 클래스 정의 모듈 로딩
    from .models import models


    # URL 처리 모듈
    from .views import main_view
    APP.register_blueprint(main_view.mainBP)



    return APP
    '''
    # URL 즉, 클라이언트 요청 페이지 주소를 보여줄 기능 함수
    def printPage():
        return "<h1>Hello~~~^A^</h1>"


    # URL 처리 함수 연결
    APP.add_url_rule('/', view_func=printPage, endpoint='INDEX')
     
    [flask routes 결과]
            Endpoint  Methods  Rule
        --------  -------  -----------------------
        INDEX     GET      /
        static    GET      /static/<path:filename>

    ## 라우팅!!!!-------------------------------------------------
    # 아래와 같은 결과
    # APP.add_url_rule('/', view_func=printPage, endpoint='INDEX')
    @APP.route('/', endpoint='INDEX')
    def printPage():
        return "<h1>Hello~~~^A^</h1>"
    
    '''





