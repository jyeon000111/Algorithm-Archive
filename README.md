# 🏃‍♂️ Algorithm Archive
알고리즘 학습 기록 저장소입니다.  
**BaekjoonHub**를 통한 자동 연동과, 직접 정리한 문제 풀이를 함께 관리합니다.


<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Baekjoon-0078D7?style=flat-square&logo=Baekjoon&logoColor=white"/> <img src="https://img.shields.io/badge/SWEA-D71920?style=flat-square&logo=Samsung&logoColor=white"/> <img src="https://img.shields.io/badge/Programmers-292e49?style=flat-square&logo=programmers&logoColor=white"/> <img src="https://img.shields.io/badge/BaekjoonHub-Auto_Sync-222222?style=flat-square&logo=github"/>

## 📊 Profile
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=2sweetpotato22)](https://solved.ac/2sweetpotato22/)

## 📖 Retrospective Pattern
`Manual Archive`의 문제는 아래 5단계 프로세스를 거쳐 회고를 작성하고 있습니다.

| Step | Section | Description |
|:---:|:--- |:--- |
| **1** | **문제 정보** <br> *(Problem)* | 문제의 핵심 요구사항과 난이도를 파악합니다. |
| **2** | **핵심 아이디어** <br> *(Core Logic)* | 문제를 해결하는 결정적 알고리즘과 논리 흐름을 도출합니다. |
| **3** | **어려웠던 점** <br> *(Difficulties)* | 접근 과정에서의 시행착오와 디버깅 과정을 기록합니다. |
| **4** | **배운 점** <br> *(What I Learned)* | 새롭게 알게 된 라이브러리, 문법, 자료구조 활용법을 정리합니다. |
| **5** | **코드 개선** <br> *(Refactoring)* | 메모리/시간 복잡도를 줄이거나 가독성을 높이는 방향으로 코드를 개선합니다. |

## 📌 Selected Problems

| Topic | Difficulty | Problem | Key Learning | Link |
|:---:|:---:|:--- |:--- |:---:|
| **Data Structure** | ![Silver 2](https://img.shields.io/badge/Silver%202-465E69?style=flat-square&logo=solved.ac&logoColor=white) | **[BOJ] 키로거** | 중간 삽입/삭제의 비효율성을 개선한 Two-Deque 구조 | [바로가기 🔗](./boj/kkr_workbook/04_stack_queue/cleared/5397_key_logger/) |
| **Union-Find** | ![Gold 4](https://img.shields.io/badge/Gold%204-EC9A00?style=flat-square&logo=solved.ac&logoColor=white) | **[BOJ] 여행 가자** | 그래프 연결성 판별을 위한 집합 관리와 중복 탐색 최적화 | [바로가기 🔗](./boj/step_by_step/34_union_find_1/completed/1976_lets_travel/) |
| **Parametric Search** | ![Gold 4](https://img.shields.io/badge/Gold%204-EC9A00?style=flat-square&logo=solved.ac&logoColor=white) | **[BOJ] 공유기 설치** | 결정 문제 변환 및 탐색 범위(Search Space) 최적화 | [바로가기 🔗](./boj/step_by_step/25_binary_search/completed/2110_install_router/) |



## 📂 Directory Structure
백준허브의 자동 업로드 폴더와 수동으로 관리하는 폴더가 공존하는 구조입니다.

특히 **Manual Archive**에는 문제별 **회고(README)** 가 포함되어 있습니다.
```text
Algorithm-Archive
├── 🤖 Auto-Sync (by BaekjoonHub)
│   ├── 📁 백준             # 백준허브 자동 연동
│   └── 📁 프로그래머스      # 백준허브 자동 연동
│
└── 👤 My Study Logs (Manual Archive)
    ├── 📂 boj              # 백준 개인 풀이 (직접 분류)
    │   ├── 📁 kkr_workbook       # SSAFY 강사님 추천 문제집
    │   ├── 📁 step_by_step       # 유형별/단계별 학습
    │   │   ├── 📁 문제번호_문제이름
    │   │   │   ├── 🐍 solution.py    # 풀이 코드
    │   │   │   └── 📝 README.md      # 문제 분석 & 회고 (Key Logic, Review)
    │   │   └── ...
    │   │
    │   └── 📁 samsung_a          # 삼성 A형 기출
    │
    ├── 📂 swea             # SWEA 개인 풀이
    └── 📂 template         # 알고리즘 풀이용 템플릿
```

## 📝 Commit Convention

#### Auto-Sync (BaekjoonHub)

> 백준허브 확장에 의해 자동으로 생성된 커밋 메시지를 따릅니다.

#### Manual Commit

> 개인적인 코드 수정 및 파일 이동 시 아래 규칙을 따릅니다.
  - `[사이트] 문제이름 / 난이도`
  - `[BOJ] 25330 거리 문자열 / 골드5`
  - `[SWEA] 1244 최대 상금 / D3`


## 💡 Study Log

  - **System:** BaekjoonHub Extension + Manual Upload
  - **Period:** 2025.07.17 \~ Present
  - **Focus:** Python 기반의 자료구조/알고리즘 역량 강화




