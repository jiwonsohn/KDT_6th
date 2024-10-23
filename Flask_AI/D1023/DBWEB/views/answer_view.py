
from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from DBWEB import DB
from DBWEB.models.models import Question, Answer

AnswerBP = Blueprint('answer', __name__, url_prefix='/answer', template_folder='templates')


# 라우팅
@AnswerBP.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    q = Question.query.get_or_404(question_id)
    content = request.form['content']   # POST 폼 방식으로 전송된 데이터 항목 중 content 값

    answer = Answer(content=content, create_date=datetime.now())
    q.answer_set.append(answer)         # Question 테이블에 answer 인스턴스 연결
                                        # 질문에 달린    답변 개념

    DB.session.commit()

    return redirect(url_for('MAIN.questionItem', question_id=question_id))



