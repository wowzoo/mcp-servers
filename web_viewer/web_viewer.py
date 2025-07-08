import requests
from bs4 import BeautifulSoup
from fastmcp import FastMCP

mcp = FastMCP("web-viewer")

@mcp.tool()
def fetch_url(url: str) -> str:
    """Fetch and return the content of a given URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove unwanted tags
        for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'noscript']):
            tag.decompose()
        
        # Extract clean text
        text_content = soup.get_text(strip=True, separator='\n')
        
        # Clean up extra whitespace
        lines = [line.strip() for line in text_content.split('\n') if line.strip()]
        return '\n'.join(lines)
        
    except Exception as e:
        return f"Error fetching URL: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")