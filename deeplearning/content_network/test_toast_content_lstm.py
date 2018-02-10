from keras import models
from konlpy.tag import Twitter
import numpy as np
from gensim.models import KeyedVectors

# model = models.load_model('../../toast_lstm.h5')
model = models.load_model('../../toast_lstm_except_1word.h5')

trained_matrix = KeyedVectors.load_word2vec_format('../../data_noun_fasttext.vec', encoding='utf-8')
twiter = Twitter()
label = "1학기,2학기,3학기,4학기,5학기,6학기,7학기,8학기,경영,경제,공과,남자,문과,법과,사범,사회과학,생명공학,소프트웨어,스포츠과학,약학,여자,예술,유학,융합,의과,자연과학,재학생,정보통신,초과학기,휴학생,강연,교환학생,국내봉사,기자단,대외활동,대학원,마케터,여행,인턴,장학금,취업,학사일정,해외봉사,"
label = label.split(",")
data = """
2018학년도 1학기 삼성서울병원(일원동) 의료봉사활동 프로그램에 참여할

봉사자를 다음과 같이 모집하오니 관심 있는 학생들의 많은 신청 바랍니다.


1. 지원 자격 : 7학기 이하 학부생(휴학생 포함)

2. 봉사프로그램 내용

가. 의학정보센터 지원(이동문고, 잡지 배부, 오디오 북 서비스)
-병실 도서대출 및 반납
-도서대출 대장정리 및 통계작성
-잡지배부(외래, 병동), 잡지 대 정리, 병실 오디오 북 대출 및 반납

나. 검사실 지원 (영상의학과, 방사선 촬영, 심장초음파 안내)
-검사순서 및 갱의실 안내, 타 검사실 위치안내
-검사 진행안내

다. CS실 지원(고객 상담실, 음료서비스)
-고객의 소리 수거 및 입력
-외래 대기 환자 및 내원객을 위한 음료서비스

라. 교육실 지원(암교육센터, 영양교육실, 당뇨교육실)
-소식지 원고 교정 및 우편발송
-교육자료 준비, 파일 정리
-통합교육프로그램 등록 및 예약 등 진행 보조
-도서정리, 우편물 발송, 암교육센터 안내


3. 활동 기간 및 모집 인원

가. 활동 기간 : 2018년 3월 2일(금)~ 2018년 8월 31일(금)

나. 봉사자 사전 교육
- 일시: 2018년 2월 27일(화) 14:00 ~16:00
- 장소: 암병원 지하1층 암병원 강당
- 유의사항: 반명함판사진 1매 지참, 반드시 20분 전 (13:40) 도착 요망

다. 봉사활동 시간
- 오전 팀(09:00~12:30) - 봉사시간 10분전(8시 50분)까지 봉사실(지하3층) 10분전 도착
- 오후 팀(12:30~16:00) - 봉사시간 10분전(12시 20분)까지 봉사실(지하3층) 10분전 도착

※ 삼성서울병원 봉사자 점심식사 제공 → 오전 팀 봉사자는 봉사종료 후, 오후 팀 봉사자는 봉사시작 전 식사가능. 오후 팀 활동 종료 후 간식제공.

라. 모집 인원 : 월~금 오전 팀, 오후 팀으로 총 약 100명(금요일은 최대 10명만 가능)

* 신청현황에 따라 요일별로 조기 마감될 수 있습니다. *
신청 상황을 공지사항에 주기적으로 업데이트 할 예정이오니 신청 전 확인 부탁드립니다.
**접수 후 1지망으로 바로 배정됨. 1지망 시간대 마감으로 2지망으로 배정될 시에만 개인적으로 문자 공지함**


4. 모집기간 및 지원방법 2018. 2. 22 (목)까지 의료봉사신청서를 작성하여 studentaid@skku.edu로 송부

5. 문의: 학생지원팀 02-760-1004

# 필독
- 졸업예정자(8학기) 신청 불가
- 의료봉사활동은 2018년 3월 2일부터 시작되며, 시험기간, 방학기간 중에도 활동
- 활동기간 종료 전 봉사활동확인서 발급 불가(사회봉사론 수강자도 사전 발급 불가)
- 활동 종료 후 우수봉사자 선발 및 포상 증정
- 봉사활동은 교외봉사로 인정
- 중도포기자는 봉사시간 확인서 발급 불가 
"""
data = twiter.nouns(data)
input = np.zeros((1,100), dtype=np.float32)
for d in data:
    try:
        input = np.add(input, trained_matrix[d])
    except:
        pass
input = input.reshape(1,1,100)
predict = model.predict(input)
result = zip(label, predict[0])

real_result = sorted(result, key=lambda x: x[1], reverse=True)
for x, y in real_result:
    print("{} {}".format(x, y))