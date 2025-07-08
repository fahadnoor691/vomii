from tavily import TavilyClient
from dextop_agent import DextopAgent
from config import TAVILY_API_KEY
from datetime import datetime

import webbrowser

dextop_agent = DextopAgent()
tavily_client = TavilyClient(TAVILY_API_KEY)

def open_application(app_name):
    return dextop_agent.open_application(app_name)

def take_screenshot(filename=None):
    return dextop_agent.take_screenshot(filename)

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
    
    # Get top 2 results
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

def lock_computer():
    return dextop_agent.lock_computer()

def get_system_info():
    return dextop_agent.get_system_info()

def get_running_apps():
    return dextop_agent.get_running_apps()

def get_system_battery():
    return dextop_agent.get_system_battery()

def get_ip_address():
    return dextop_agent.get_ip_address()

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "open_application",
            "description": "Use this to open an application",
            "parameters": {
                "type": "object",
                "properties": {"app_name": {"type": "string"}},
                "required": ["app_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "take_screenshot",
            "description": "Use this to take a screenshot",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Optional filename of the screenshot"}
                },
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "crawl_website",
            "description": "Use this to crawl a website. Accepts URLs in various formats including 'url.com', 'url dot com', or full URLs like 'https://url.com'",
            "parameters": {
                "type": "object",
                "properties": {"url": {"type": "string"}},
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_internet",
            "description": "Fetch real-time web data on [topic/question], focusing on recent developments (especially from today, this week, or post-2020)",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string", "description": "The search query or question to search the web for"}},
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "open_any_website",
            "description": "Opens any URL in the browser",
            "parameters": {
                "type": "object",
                "properties": {"url": {"type": "string", "description": "The URL of the website to open"}},
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current time",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "minimize_window",
            "description": "Minimize the windows",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "close_window",
            "description": "Close the windows",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "restore_windows",
            "description": "Restore the windows",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "lock_computer",
            "description": "Lock the computer",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_system_info",
            "description": "Get the system information",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_running_apps",
            "description": "Get the running applications",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_system_battery",
            "description": "Get the system battery",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ip_address",
            "description": "Get the IP address",
            "parameters": {}
        }
    }
]


TOOLS_MAP = {
    "open_any_website": open_any_website,
    "open_application": open_application,
    "take_screenshot": take_screenshot,
    "crawl_website": crawl_website,
    "search_internet": search_internet,
    "get_current_time": get_current_time,
    "minimize_window": minimize_window,
    "close_window": close_windows,
    "restore_windows": restore_windows,
    "lock_computer": lock_computer,
    "get_system_info": get_system_info,
    "get_running_apps": get_running_apps,
    "get_system_battery": get_system_battery,
    "get_ip_address": get_ip_address
}
