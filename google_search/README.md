# Google Search MCP Server

Google Custom Search API를 사용하여 검색 기능과 웹페이지 내용 추출을 제공하는 MCP (Model Context Protocol) 서버입니다.

## 기능

Google Custom Search API를 사용하여 검색하고 각 결과의 웹페이지 내용까지 추출합니다.

## 사전 준비

### Google Custom Search API 설정

1. **Google Cloud Console에서 API 키 생성**
   - [Google Cloud Console](https://console.cloud.google.com/)에 접속
   - 새 프로젝트 생성 또는 기존 프로젝트 선택
   - "API 및 서비스" > "라이브러리"로 이동
   - "Custom Search API" 검색 후 활성화
   - "API 및 서비스" > "사용자 인증 정보"로 이동
   - "사용자 인증 정보 만들기" > "API 키" 선택
   - 생성된 API 키 복사

2. **Custom Search Engine 생성**
   - [Google Custom Search Engine](https://cse.google.com/cse/)에 접속
   - "추가" 클릭
   - 검색엔진 이름 입력, 검색할 내용에서 "전체 웹 검색" 선택 후 "만들기" 클릭
   - 만든 검색엔지 개요의 기본에서 "검색엔진 ID" 복사

3. **코드에 API 정보 설정**
   ```python
   # google_search.py 파일에서 다음 부분 수정
   API_KEY = "YOUR_API_KEY_HERE"
   SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID_HERE"
   ```

## 설치

### uv 설치 (필요시)
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 프로젝트 설정
```bash
# 프로젝트 디렉토리로 이동
cd google_search

# 가상환경 생성 및 의존성 설치
uv sync
```

## q CLI에서 MCP 서버 등록

**mcp.json 설정**
```json
{
    "mcpServers": {
        "google-search": {
        "command": "uv 절대 경로",
        "args": [
            "--directory",
            "google_search.py 가 위치한 디렉토리의 절대경로 입력",
            "run",
            "google_search.py"
        ],
        "disabled": false
    }
    }
}
```


## 도구 설명

### google_search
- **설명**: Google Custom Search API를 사용하여 검색하고 웹페이지 내용을 추출합니다.
- **매개변수**:
  - `query` (필수): 검색할 쿼리
  - `num_results` (선택, 기본값: 5): 반환할 결과 수 (최대 10)
  - `fetch_content` (선택, 기본값: True): 웹페이지 내용을 가져올지 여부


## 설정

### API 제한사항
- Google Custom Search API는 하루 100회 무료 쿼리 제공
- 추가 쿼리는 유료 ($5/1000 쿼리)
- 자세한 내용은 [Google Custom Search API 가격 정책](https://developers.google.com/custom-search/v1/overview#pricing) 참조

### 성능 최적화
- 웹페이지 내용 추출 시 요청 간 1초 딜레이 적용
- 각 웹페이지 내용은 2000자로 제한
- 타임아웃 10초 설정

## 문제 해결

### 일반적인 오류
1. **API 키 오류**: API 키가 올바르게 설정되었는지 확인
2. **검색엔진 ID 오류**: Custom Search Engine ID가 올바른지 확인
3. **할당량 초과**: API 사용량이 일일 한도를 초과했는지 확인

## 라이선스

MIT License