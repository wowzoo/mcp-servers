# MCP Servers

Model Context Protocol(MCP) 서버 모음입니다. 이 저장소는 Claude와 같은 AI 어시스턴트가 사용할 수 있는 다양한 MCP 서버를 포함하고 있습니다.

## 포함된 서버

### 날씨 정보 서버 (weather)

[공공데이터포털의 기상청 초단기예보 API](https://www.data.go.kr/data/15043492/fileData.do?recommendDataYn=Y)를 활용하여 대한민국의 실시간 날씨 정보를 제공합니다.

- 위도와 경도를 기반으로 한 현재 날씨 정보 제공
- 기온, 하늘상태, 강수형태, 습도, 1시간 강수량 등 상세 정보 제공

[자세한 정보](./weather/README.md)

## 설치 및 사용 방법

각 서버 디렉토리에 있는 README.md 파일을 참조하세요.

## 요구 사항

- Python 3.13 이상
- [uv 패키지 매니저](https://docs.astral.sh/uv/getting-started/installation/)

## 라이선스

[MIT 라이선스](./LICENSE)에 따라 배포됩니다.

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새로운 브랜치를 생성합니다.
3. 변경사항을 커밋합니다.
4. 브랜치를 푸시합니다.
5. Pull Request를 생성합니다.