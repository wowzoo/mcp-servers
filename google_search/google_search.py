#!/usr/bin/env python3
"""
Google Search MCP Server using FastMCP with Google Custom Search API
"""

import logging
import time
import os
import requests

from typing import Any, Dict, List
from bs4 import BeautifulSoup
from fastmcp import FastMCP


# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("google-search-mcp")

# FastMCP 앱 생성
app = FastMCP("google-search-mcp")

# Google Custom Search API 설정
API_KEY = os.environ.get("GOOGLE_CLOUD_API_KEY")
SEARCH_ENGINE_ID = os.environ.get("GOOGLE_CUSTOM_SEARCH_ENGINE_ID")

class GoogleSearcher:
    """Google Custom Search API를 사용한 검색 클래스"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get_webpage_content(self, url: str, max_chars: int = 2000) -> str:
        """
        웹페이지에서 텍스트 내용을 추출합니다.
        
        Args:
            url: 웹페이지 URL
            max_chars: 최대 문자 수 (기본값: 2000)
        
        Returns:
            추출된 텍스트 내용
        """
        try:
            response = self.session.get(url, timeout=10)
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
    
    def search(self, query: str, num_results: int = 5, fetch_content: bool = True) -> List[Dict[str, Any]]:
        """
        Google Custom Search API를 사용하여 검색합니다.
        
        Args:
            query: 검색 쿼리
            num_results: 반환할 결과 수 (기본값: 5, 최대: 10)
            fetch_content: 웹페이지 내용을 가져올지 여부 (기본값: True)
        
        Returns:
            검색 결과 리스트
        """
        try:
            # API 요청 URL
            url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&num={num_results}"
            
            # GET 요청 보내기
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # JSON 응답 파싱
            search_results = response.json()
            
            results = []
            
            if 'items' in search_results:
                for i, item in enumerate(search_results['items']):
                    result_data = {
                        'title': item.get('title', '제목 없음'),
                        'link': item.get('link', ''),
                        'snippet': item.get('snippet', '')
                    }
                    
                    # 웹페이지 내용 가져오기
                    if fetch_content and result_data['link']:
                        logger.info(f"웹페이지 내용 가져오는 중: {result_data['link']}")
                        result_data['content'] = self.get_webpage_content(result_data['link'])
                        
                        # 요청 간 딜레이 (서버 부하 방지)
                        if i < len(search_results['items']) - 1:
                            time.sleep(1)
                    
                    results.append(result_data)
            
            return results
            
        except Exception as e:
            logger.error(f"Google 검색 중 오류: {e}")
            raise Exception(f"검색 실패: {str(e)}")

# Google 검색 인스턴스
searcher = GoogleSearcher()

@app.tool()
def google_search(
    query: str,
    num_results: int = 5,
    fetch_content: bool = True
) -> str:
    """
    Google Custom Search API를 사용하여 검색하고 웹페이지 내용을 가져옵니다.
    
    Args:
        query: 검색할 쿼리
        num_results: 반환할 결과 수 (기본값: 5, 최대: 10)
        fetch_content: 웹페이지 내용을 가져올지 여부 (기본값: True)
    
    Returns:
        검색 결과 문자열 (웹페이지 내용 포함)
    """
    if not query:
        raise ValueError("검색 쿼리가 필요합니다.")
    
    # 결과 수 제한
    num_results = min(max(num_results, 1), 10)
    
    try:
        # Google 검색 수행
        results = searcher.search(query, num_results, fetch_content)
        
        if not results:
            return f"'{query}'에 대한 검색 결과를 찾을 수 없습니다."
        
        # 결과 포맷팅
        formatted_results = []
        formatted_results.append(f"Google 검색 결과 (쿼리: '{query}', {len(results)}개 결과):")
        formatted_results.append("=" * 80)
        
        for i, result in enumerate(results, 1):
            formatted_results.append(f"\n{i}. {result['title']}")
            formatted_results.append(f"링크: {result['link']}")
            
            if result['snippet']:
                formatted_results.append(f"스니펫: {result['snippet']}")
            
            if fetch_content and 'content' in result:
                formatted_results.append(f"\n웹페이지 내용:")
                formatted_results.append(result['content'])
            
            formatted_results.append("-" * 80)
        
        return "\n".join(formatted_results)
        
    except Exception as e:
        logger.error(f"검색 도구 실행 중 오류: {e}")
        return f"검색 중 오류가 발생했습니다: {str(e)}"


if __name__ == "__main__":
    # Initialize and run the server
    app.run(transport='stdio')
