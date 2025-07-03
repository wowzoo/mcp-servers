# Geocoder MCP Server

한국 주소를 위도/경도로 변환하는 MCP (Model Context Protocol) 서버입니다.

## 기능

- 한국 주소를 Google Maps API를 통해 위도/경도로 변환

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

2. **환경변수로 API 정보 설정**
   ```bash
   # 환경변수 설정 (터미널에서) 또는 쉘 설정 파일 (.zshrc, .bashrc 등) 
   export GOOGLE_CLOUD_API_KEY="your_api_key_here"
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
cd geocoder

# 가상환경 생성 및 의존성 설치
uv sync
```


## 사용법

### 환경변수 설정
사용하기 전에 반드시 환경변수를 설정해야 합니다:

```bash
# 방법 1: 터미널에서 직접 설정
export GOOGLE_CLOUD_API_KEY="your_api_key_here"

# 방법 2: ~/.zshrc 또는 ~/.bashrc에 추가 (영구 설정)
echo 'export GOOGLE_CLOUD_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

### q CLI에서 MCP 서버로 사용

**mcp.json 설정**
```json
{
    "mcpServers": {
        "google-search": {
            "command": "uv 절대 경로",
            "args": [
                "--directory",
                "geocoder.py 가 위치한 디렉토리의 절대경로 입력",
                "run",
                "geocoder.py"
            ],
            "disabled": false
        }
    }
}
```

