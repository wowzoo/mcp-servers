import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

# 발급받은 API 키와 검색 엔진 ID로 교체해야 합니다.
API_KEY = "YOUR_API_KEY_HERE"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID_HERE"

def get_webpage_content(url, max_chars=2000):
    """
    웹페이지에서 텍스트 내용을 추출합니다.
    
    Args:
        url: 웹페이지 URL
        max_chars: 최대 문자 수 (기본값: 2000)
    
    Returns:
        추출된 텍스트 내용
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 불필요한 태그 제거
        for script in soup(["script", "style", "nav", "header", "footer", "aside"]):
            script.decompose()
        
        # 텍스트 추출
        text = soup.get_text()
        
        # 공백 정리
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        # 최대 문자 수 제한
        if len(text) > max_chars:
            text = text[:max_chars] + "..."
        
        return text
        
    except Exception as e:
        return f"웹페이지 내용을 가져올 수 없습니다: {str(e)}"

def search(query, fetch_content=True, max_results=5):
    """
    Google Custom Search API를 사용하여 검색하고 웹페이지 내용을 가져옵니다.
    
    Args:
        query: 검색 쿼리
        fetch_content: 웹페이지 내용을 가져올지 여부 (기본값: True)
        max_results: 최대 결과 수 (기본값: 5)
    """
    # API 요청 URL
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&num={max_results}"

    # GET 요청 보내기
    response = requests.get(url)

    # 응답 상태 코드 확인
    if response.status_code == 200:
        # JSON 응답 파싱
        search_results = response.json()

        # 검색 결과 아이템 출력
        if 'items' in search_results:
            print(f"'{query}'에 대한 검색 결과 (총 {len(search_results['items'])}개):")
            print("=" * 80)
            
            for i, item in enumerate(search_results['items'], 1):
                print(f"\n{i}. {item['title']}")
                print(f"링크: {item['link']}")
                
                if 'snippet' in item:
                    print(f"스니펫: {item['snippet']}")
                
                if fetch_content:
                    print("\n웹페이지 내용:")
                    content = get_webpage_content(item['link'])
                    print(content)
                    
                    # 요청 간 딜레이 (서버 부하 방지)
                    if i < len(search_results['items']):
                        time.sleep(1)
                
                print("-" * 80)
        else:
            print("검색 결과가 없습니다.")

    else:
        print(f"Error: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    # 검색할 키워드
    query = "aws graviton 3 한국 출시 정보"
    
    # 웹페이지 내용까지 가져오기
    search(query, fetch_content=True, max_results=3)
    
    # print("\n" + "="*80)
    # print("스니펫만 보기:")
    # print("="*80)
    
    # # 스니펫만 보기
    # search(query, fetch_content=False, max_results=3)
