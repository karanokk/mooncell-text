import requests


class MediaWikiEndpoints:
    def __init__(self, domain: str):
        self.domain = domain
        session = requests.Session()
        session.headers['Accept-Encoding'] = 'gzip'
        session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4090.0 Safari/537.36 Edg/83.0.467.0'
        self.session = session

    def raw(self, params: dict):
        params = self._format_list_value(params)
        params['format'] = 'json'
        params["formatversion"] = 2
        return self.session.get(self.domain, params=params).json()

    def query(self, params: dict):
        params['action'] = 'query'
        return self.raw(params)['query']

    def parse(self, params: dict):
        params['action'] = 'parse'
        return self.raw(params)['parse']

    def _format_list_value(self, params: dict) -> dict:
        for k, v in params.items():
            if isinstance(v, tuple) or isinstance(v, list):
                assert (len(v) <= 50)
                params[k] = '|'.join(v)
        return params
