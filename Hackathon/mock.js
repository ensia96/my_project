// 초대 링크로 접속 시 : 회원가입 필요
// 채팅방 설정을 단순하게 : 매칭 활성화 / 비활성화

// 목요일까지 사용자 관련 기능 마무리
// 호준 : 확인, 수정 부분, 우석 : 회원가입, 로그인 마무리

// 금요일부터 채팅 관련 조사 + 기능 구현

// 매칭 관련, 채팅 관련

// 설치 필요
// brew install redis
// redis-server
// pip install channels_redis

// 호스트 관련 문제 해결
// https://github.com/django/channels/issues/1422

// 소비자 라우팅 문제 해결
// https://github.com/django/channels/issues/1552

// 재접속 가능한 웹 소켓
// https://github.com/joewalnes/reconnecting-websocket

// 참고
// https://github.com/justdjango/justchat
// https://github.com/olivrg/chattr
// https://github.com/hishnash/djangochannelsrestframework

// sudo -u postgres -i && psql 포스트그리 접속
// \h 도움말 목록
// \l 데이터베이스 목록
// \c [database name] 데이터베이스 접속
// \du 사용자 목록
// \d  [table name] 테이블 정보 조회
// \q  포스트그리 접속 종료

const conditions = {
  // 필수 직군
  necessary_users: ["디자이너", "백엔드"],
  // 팀 구성 기본 조건
  minimal_condition: [
    "프론트엔드" || "안드로이드" || "아이폰",
    ...necessary_users,
  ],
  // 사용자 종류
  user: {
    match_user: "매칭을 돌린 사용자",
    room_maker: "방을 만든 사용자",
    usre_in_room: "방 안에 있는 사용자",
  },
  // 매칭 대기
  matching_pool: ["대기 중인 사용자들"],
  // 채팅방
  room: {
    users: ["사용자들"],
    chats: ["사용자가 남긴 채팅들"],
    matching_active: "매칭 기능 활성화 여부",
    setting: () => {
      if (matching_active === true) {
        ("URL 초대는 불가능하고, match_user 만 입장 가능");
      } else {
        ("URL 초대만 가능하고, match_user 는 입장 불가능");
      }
    },
    positions: {
      planner: "기획자" === "원하는 인원",
      designer: "디자이너" === "원하는 인원",
      frontend: "프론트엔드" === "원하는 인원",
      backend: "백엔드" === "원하는 인원",
      mldev: "머신러닝" === "원하는 인원", // 나중에 추가하기
      aosdev: "안드로이드" === "원하는 인원",
      iosdev: "아이폰" === "원하는 인원",
    },
  },
};

import { SERVER_HOST } from '../constants';
import axios from 'axios';

export default (method, endpoint, token, payload) => {
    const url = SERVER_HOST + endpoint,
    const config = {headers: {token}}

    method === 'get' ? axios.get(url, config) : (method === 'post' ? axios.post(url, payload, config) : (method === 'put' ? axios.put(url, payload, config) : {}))
};

const api_idea = {
  server: () => {
    // 웹 소켓
    if (new_room.created) {
      matching_pool.forEach((user) => {
        if (
          new_room.matching_active === true &&
          new_room.positions[user.position] === false
        ) {
          new_room.users.push(user);
        } else {
          ("사용자는 matching_pool 에서 대기");
        }
      });
    }

    if (user.request.matching) {
      matching_pool.push(user);

      if (matching_pool === minimal_condition) {
        const new_room = room;
        new_room.push(minimal_condition);
      }

      if (
        room &&
        room.matching_active === true &&
        room.positions[user.position] === false
      ) {
        room.push(user);
      }
    }
  },
};

// web socket creation
const webSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
);

// action per message event
webSocket.onmessage = (e) =>
  alert("원하는 함수를 집어넣으면 됨.(예: 화면 업데이트)");

// send message
const sendMessage = (message) =>
  webSocket.send(JSON.stringify({ message: message }));

// action when web socket closed
webSocket.onclose = (e) =>
  alert(
    "웹 소켓이 끝났을 때의 동작을 집어넣으면 됨.(예: 방이 폭파되었습니다 ㅎ)"
  );

// 해당 방 포지션 상태 : matching => filtering => count()

// 매칭, 채팅, 기본 API(방, 사용자 제공)

// Chatting(service)

// 모델링, 채팅, API

const matching = {
  // endpoint : /chat/matching/
  // view     : matching_view
  // method   : post
  request: { header: { token: "token" }, body: {} },
  response: {
    success: 1,
    data: "정해야함",
  },
};

const create_room = {
  // endpoint : /chat/room/create/
  // view     : create_room_view
  // method   : post
  request: {
    header: { token: "token" },
    body: {
      room_hash: "채팅방 주소 해시값",
      activate: "채팅방 랜덤 매칭 허용 여부",
      room_name: "채팅방 이름",
      max_planner: "기획자 정원",
      max_designer: "디자이너 정원",
      max_frontend: "프론트엔드 정원",
      max_backend: "백엔드 정원",
      max_aosdev: "안드로이드 정원",
      max_iosdev: "아이폰 정원",
    },
  },
  response: {
    success: 1,
    data: {
      room_hash: "채팅방 주소 해시값",
      activate: "채팅방 랜덤 매칭 허용 여부",
      room_name: "채팅방 이름",
    },
  },
};

const update_room = {
  // endpoint : /chat/room/update/
  // view     : update_room_view
  // method   : put
  request: {
    header: { token: "token" },
    body: {
      activate: "채팅방 랜덤 매칭 허용 여부",
      room_name: "채팅방 이름",
      max_planner: "기획자 정원",
      max_designer: "디자이너 정원",
      max_frontend: "프론트엔드 정원",
      max_backend: "백엔드 정원",
      max_aosdev: "안드로이드 정원",
      max_iosdev: "아이폰 정원",
    },
  },
  response: {
    success: 1,
    data: {
      activate: "채팅방 랜덤 매칭 허용 여부",
      room_name: "채팅방 이름",
      max_planner: "기획자 정원",
      max_designer: "디자이너 정원",
      max_frontend: "프론트엔드 정원",
      max_backend: "백엔드 정원",
      max_aosdev: "안드로이드 정원",
      max_iosdev: "아이폰 정원",
    },
  },
};

const get_room = {
  // endpoint : /chat/room/
  // view     : get_room_view
  // method   : get
  request: { header: { token: "token" }, body: {} },
  response: {
    success: 1,
    data: {
      room_hash: "채팅방 주소 해시값",
      users: [
        {
          email: "email@ema.il",
          nickname: "nickname",
          age: 20,
          phone: "010-1234-5678",
          position: "position",
          profile_image: "image_url",
        },
        {
          email: "email@ema.il",
          nickname: "nickname",
          age: 20,
          phone: "010-1234-5678",
          position: "position",
          profile_image: "image_url",
        },
      ],
    },
  },
};

const leave_room = {
  // endpoint : /chat/leave/
  // view     : leave_room_view
  // method   : post
  request: { header: { token: "token" }, body: {} },
  response: { success: 1 },
};

const get_messages = {
  // endpoint : /chat/messages/
  // view     : get_messages_view
  // method   : post
  request: {
    header: { token: "token" },
    body: {
      max_loading: "최대 페이지 인덱스",
      page_index: "현재 불러오기 페이지",
    },
  },
  response: {
    success: 1,
    data: {
      has_next: "추가적인 불러오기가 가능한지 여부",
      messages: [
        {
          nickname: "사용자 닉네임",
          content: "메시지 내용",
          created_at: "생성일",
          updated_at: "수정일",
        },

        {
          nickname: "사용자 닉네임",
          content: "메시지 내용",
          created_at: "생성일",
          updated_at: "수정일",
        },
      ],
    },
  },
};

// User

const sign_up = {
  // endpoint : /user/signup/
  // view     : signup_view
  // method   : post
  request: {
    header: {},
    body: {
      email: "email@ema.il",
      password: "password",
      nickname: "nickname",
      age: 20,
      phone: "010-1234-5678",
      position: "position",
      profile_image: "form_data(image_file)",
    },
  },
  response: {
    success: 1,
    data: {
      email: "email@ema.il",
      nickname: "nickname",
      age: 20,
      phone: "010-1234-5678",
      position: "position",
      profile_image: "image_url",
    },
  },
};

const login = {
  // endpoint : /user/login/
  // view     : login_view
  // method   : post
  request: {
    header: {},
    body: { email: "email@ema.il", password: "password" },
  },
  response: {
    success: 1,
    data: {
      token: "token",
      expire_time: "0000-00-00T00:00:00.000000",
      email: "email@ema.il",
      nickname: "nickname",
      position: "position",
      profile_image: "image_url",
    },
  },
};

const user_info = {
  // endpoint : /user/info/
  // view     : user_info_view
  // method   : get
  request: { header: { token: "token" }, body: {} },
  response: {
    success: 1,
    data: {
      email: "email@ema.il",
      age: 20,
      phone: "010-0000-0000",
    },
  },
};

const info_update = {
  // endpoint : /user/update/info/
  // view     : user_update_view
  // method   : put
  request: {
    header: { token: "token" },
    body: {
      email: "email@ema.il",
      password: "password",
      age: 20,
      phone: "010-0000-0000",
    },
  },
  response: { success: 1 },
};

const profile_update = {
  // endpoint : /user/update/profile/
  // view     : profile_update_view
  // method   : put
  request: {
    header: { token: "token" },
    body: {
      flag: 0, // 0 = 포지션만 변경
      position: "position",
    } || {
      flag: 1, // 1 = 프로필 변경(포지션 포함)
      nickname: "nickname",
      position: "position",
      profile_image: "form_data(image_file)",
    },
  },
  response: { success: 1 },
};
