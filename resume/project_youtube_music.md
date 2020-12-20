프로젝트 명
Youtube Music 서비스 클론 프로젝트
시작일
2020-05-11
종료일
2020-05-22
프로젝트 유형
기타
소속회사명
WeCode
주사용기술
프론트엔드 ( React ), 백엔드 ( Django, MySQL ), 인프라 ( AWS, Docker )

프로젝트에 대한 소개와 본인이 수행한 역할을 상세히 작성해주세요.
-----------------------------------------------------------------------------------------------------------------------

코딩 부트캠프 위코드에서 진행한 2차 팀 프로젝트입니다.

참가 인원
프론트엔드 : 3명
백엔드 : 2명 ( 본인 포함 )

구성 기술
- 서버 : AWS EC2 ( Django )
- 데이터베이스 : AWS RDS ( MySQL )
- 정보 수집 : Selenium ( Python )
- 배포 : Docker
- 클라이언트 : React

담당 업무
- 정보 수집 ( 추천 테마, 음원 정보 등 )
- 로컬 데이터베이스 구성
- 작업 명세 작성 및 업무 분배
- 서버 기능요소 구현 ( + Streaming 기능 구현 방법 파악 )
- 기능 동작 점검 ( PostMan )
- 유닛 테스트 코드 작성
- API 문서 작성
- RDS 마이그레이션 ( Dump )
- AWS EC2 배포 => Docker 기반 배포
- 발표자료 제작 및 발표

관련 자료
GitHub 저장소 ( https://github.com/wecode-bootcamp-korea/YoutubeMuzic-backend )
Trello ( https://trello.com/b/Gwa08tmi )
Aquery ( https://aquerytool.com/aquerymain/index/?rurl=7a682ed1-5f50-4743-82c3-438992121a5f | 비밀번호 : h2awcy )
발표 자료 ( https://docs.google.com/presentation/d/1gDzJ6t_EijS7fAEzGdNLfVy-cs6K9yk1_LCBMW2OiJ0/edit?usp=sharing )

배운 것
- Python 의 Dictionary 와 JSON 은 코드 상으로는 같은 형태를 띄지만, 종류가 다르다.
- Django 의 get_or_create 메소드는 정보 객체와 생성 여부를 반환한다.
- Django 의 get_object_or_404 메소드는 객체가 없을 경우 HTTP 404 Error 를 throw 한다.
- Django 의 Q 객체는 SQL 의 OR 구문처럼 활용할 수 있다.
- Django 의 Annotate 메소드는 SQL 의 AS 구문처럼 활용할 수 있다.
- Streaming 은 FileLike, OctetStream 과 같은 패킷을 반복 응답하는 기술이다.
- Django DataBase 설정의 Test 항목을 'Mirror' 로 지정하면, 실제 데이터베이스 내용을 기준으로 테스트할 수 있다.
- OAuth 로 제공받는 토큰에는 거의 모든 사용자 정보가 담겨있다.

깨달은 점
- 소스 코드에서 상당히 많은 것을 배울 수 있다.
- 협업은 잘맞는 것보다, 잘 맞추는 것이 중요하다.
- 모델링할 때 고통받은 만큼, 기능 구현 작업이 수월해진다.
- 기능의 본질을 잘 파악할수록, 테스트 코드 작성이 쉬워진다.
- 프로그래밍으로 해결 가능한 단순 작업은 생각보다 많다.
- 최소한의 여유는 유지해야, 많은 상황에 대비할 수 있다.
- Docker 로 배포하는 것은 신세계다.
- 발표자료에 유머를 넣는 것은 쉽지 않다.
- 유머를 발표에 녹여내는 것 역시 쉽지 않다.

-----------------------------------------------------------------------------------------------------------------------
