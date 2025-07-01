# MCP Servers

Model Context Protocol(MCP) 서버 모음입니다. 이 저장소는 Claude와 같은 AI 어시스턴트가 사용할 수 있는 다양한 MCP 서버를 포함하고 있습니다.

## 포함된 서버

### Google 검색 서버 (google_search)

Google 검색 기능을 제공하는 MCP 서버입니다. 웹 스크래핑을 통해 Google 검색 결과를 가져와 AI 어시스턴트가 실시간 정보에 접근할 수 있도록 합니다.

- Google 검색 결과 제공 (제목, URL, 요약)
- 검색 결과 수 조절 가능 (최대 20개)
- 다국어 검색 지원 (한국어, 영어 등)
- CLI 도구로 간편한 사용

[자세한 정보](./google_search/README.md)

### 날씨 정보 서버 (weather)

[공공데이터포털의 기상청 초단기예보 API](https://www.data.go.kr/data/15043492/fileData.do?recommendDataYn=Y)를 활용하여 대한민국의 실시간 날씨 정보를 제공합니다.

- 위도와 경도를 기반으로 한 현재 날씨 정보 제공
- 기온, 하늘상태, 강수형태, 습도, 1시간 강수량 등 상세 정보 제공

[자세한 정보](./weather/README.md)