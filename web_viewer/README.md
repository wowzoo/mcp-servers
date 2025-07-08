# Web Viewer MCP Server

웹페이지의 내용을 가져와서 깔끔한 텍스트로 변환하는 MCP (Model Context Protocol) 서버입니다. HTML을 파싱하여 불필요한 요소들을 제거하고 읽기 쉬운 텍스트 형태로 반환합니다.

## 기능

- 웹페이지 내용 추출 및 텍스트 변환
- HTML 태그 제거 및 텍스트 정리
- 스크립트, 스타일, 네비게이션 등 불필요한 요소 자동 제거
- 타임아웃 설정으로 안정적인 요청 처리

## 사용법

### q CLI에서 MCP 서버로 사용

**mcp.json 설정**
```json
{
    "mcpServers": {
        "google-search": {
            "command": "uv 절대 경로",
            "args": [
                "--directory",
                "web_viewer.py 가 위치한 디렉토리의 절대경로 입력",
                "run",
                "web_viewer.py"
            ],
            "disabled": false
        }
    }
}
```

## 도구

### fetch_url

웹페이지의 내용을 가져와서 텍스트로 변환합니다.

**매개변수:**
- `url` (string, 필수): 가져올 웹페이지의 URL

**반환값:**
- 웹페이지의 텍스트 내용 (HTML 태그 제거됨)
- 오류 발생 시 오류 메시지

**예시:**

```json
{
  "name": "fetch_url",
  "arguments": {
    "url": "https://example.com"
  }
}
```

## 라이선스

MIT License