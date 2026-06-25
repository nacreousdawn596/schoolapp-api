"""
HTTP Client with session and cookie management
"""
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import logging

from schoolapp_api.constants import DEFAULT_HEADERS

logger = logging.getLogger(__name__)

class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(
            req.full_url, code, msg, headers, fp
        )


class HTTPClient:
    """Base HTTP client for making authenticated requests"""
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.cookie_jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.cookie_jar)
        )
        self.headers = DEFAULT_HEADERS.copy()
    
    def get(self, url, params=None):
        """Perform GET request"""
        try:
            if params:
                query_string = urllib.parse.urlencode(params, doseq=True)
                separator = "&" if "?" in url else "?"
                url = f"{url}{separator}{query_string}"

            req = urllib.request.Request(url, headers=self.headers, method="GET")

            with self.opener.open(req, timeout=15) as response:
                code = response.getcode()
                response_url = response.geturl()
                content = response.read().decode("utf-8")
                return code, response_url, content

        except urllib.error.HTTPError as e:
            # Still get content from error page if possible (some portals return 401 with nice HTML)
            try:
                content = e.read().decode("utf-8")
            except:
                content = None
            logger.error(f"HTTP Error {e.code}: {e.reason}")
            return e.code, e.url, content
        except Exception as e:
            logger.error(f"GET Error: {e}")
            return None, None, None
    
    def post(self, url, data, referer=None):
        """Perform POST request"""
        try:
            encoded_data = urllib.parse.urlencode(data).encode('utf-8')
            req = urllib.request.Request(url, data=encoded_data, headers=self.headers)
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            req.add_header('Origin', self.base_url)
            if referer:
                req.add_header('Referer', referer)
            
            with self.opener.open(req, timeout=15) as response:
                code = response.getcode()
                response_url = response.geturl()
                content = response.read().decode('utf-8')
                return code, response_url, content
        except urllib.error.HTTPError as e:
            try:
                content = e.read().decode("utf-8")
            except:
                content = None
            logger.error(f"HTTP Error {e.code}: {e.reason}")
            return e.code, e.url, content
        except Exception as e:
            logger.error(f"POST Error: {e}")
            return None, None, None
