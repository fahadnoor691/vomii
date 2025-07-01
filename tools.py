from tavily import TavilyClient
from dextop_agent import DextopAgent
from config import TAVILY_API_KEY
from datetime import datetime

import webbrowser

dextop_agent = DextopAgent()
tavily_client = TavilyClient(TAVILY_API_KEY)

def open_application(app_name):
    return dextop_agent.open_application(app_name)

def take_screenshot():
    return dextop_agent.take_screenshot()

def crawl_website(url):
    crawl_result = tavily_client.crawl(
        url=url
    )
    
    raw_contents = []
    for result in crawl_result['results']:
        if hasattr(result, 'raw_content'):
            raw_contents.append(result.raw_content)
        elif isinstance(result, dict) and 'raw_content' in result:
            raw_contents.append(result['raw_content'])
    
    return raw_contents

def search_internet(query):
    search_result = tavily_client.search(
        query=query
    )
    content = []
    for result in search_result['results'][:2]:
        content.append(result['content'])
    return content

def open_any_website(url):
    try:
        webbrowser.open(url)
        return "Opening: " + url
    except Exception as e:
        return "Error opening website: " + str(e)

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def minimize_window():
    return dextop_agent.minimize_windows()

def close_windows():
    return dextop_agent.close_windows()

def restore_windows():
    return dextop_agent.restore_windows()



FUNCTIONS = [
    {
        "name": "open_application",
        "description": "Use this to open an application",
        "parameters": {
            "type": "object",
            "properties": {"app_name": {"type": "string"}},
            "required": ["app_name"]
        }
    },
    {
        "name": "take_screenshot",
        "description": "Use this to take a screenshot",
        "parameters": {}
    },
    {
        "name": "crawl_website",
        "description": "Use this to crawl a website. Accepts URLs in various formats including 'url.com', 'url dot com', or full URLs like 'https://url.com'",
        "parameters": {
            "type": "object",
            "properties": {"url": {"type": "string"}},
            "required": ["url"]
        }
    },
    {
        "name": "search_internet",
        "description": "Fetch real-time web data on [topic/question], focusing on recent developments (especially from today, this week, or post-2020)",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "The search query or question to search the web for"}},
            "required": ["query"]
        }
    },
    {
        "name": "open_any_url",
        "description": "Opens any URL in the browser",
        "parameters": {
            "type": "object",
            "properties": {"url": {"type": "string", "description": "The URL of the website to open"}},
            "required": ["url"]
        }
    },
    {
        "name": "get_current_time",
        "description": "Get the current time",
        "parameters": {}
    },
    {
        "name": "minimize_window",
        "description": "Minimize the current window",
        "parameters": {}
    },
    {
        "name": "close_window",
        "description": "Close the current window",
        "parameters": {}
    }
]


FUNCTIONS_MAP = {
    "open_any_website": open_any_website,
    "open_application": open_application,
    "take_screenshot": take_screenshot,
    "crawl_website": crawl_website,
    "search_internet": search_internet,
    "get_current_time": get_current_time,
    "minimize_window": minimize_window,
    "close_window": close_windows,
    "restore_windows": restore_windows
}
