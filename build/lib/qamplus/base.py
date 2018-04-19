from base64 import b64encode
import requests

from qamplus.voice import VoiceClient
from qamplus.sms import SmsClient
from qamplus.email import EmailClient
from qamplus.api import ApiClient


QAMPLUS_BASE_URL = "http://api.qamplus.com"
QAMPLUS_VERSION = "v1"
#

class Response(object):
    """
    A simple HTTP Response object to abstract the underlying Requests library response.
    :param requests_response: A Requests response object.
    """

    def __init__(self, requests_response):
        self.status_code = requests_response.status_code
        self.headers = requests_response.headers
        self.body = requests_response.text
        self.ok = requests_response.ok

        try:
            self.json = requests_response.json()
        except (Exception, ValueError):
            self.json = None


class QamPlusClient(requests.models.RequestEncodingMixin):

    def __init__(self, customer_id,
                 password,
                 base_url=QAMPLUS_BASE_URL,
                 proxies=None,
                 timeout=10):
        """
        QAMplus RestClient useful for making generic RESTful requests against our API.
        :param customer_id: Your customer_id string associated with your account.
        :param password: Your api_key string associated with your account.
        :param base_url: (optional) Override the default rest_endpoint to target another endpoint string.
        :param proxies: (optional) Dictionary mapping protocol or protocol and hostname to the URL of the proxy.
        :param timeout: (optional) How long to wait for the server to send data before giving up, as a float,
                        or as a (connect timeout, read timeout) tuple
        """
        self.customer_id = customer_id
        self.session = requests.Session()
        self.session.proxies = proxies if proxies else {}

        self.timeout = timeout
        self.base_url = base_url
        self.password = password
        self.auth_header = QamPlusClient.generate_auth_header(customer_id, password)

        self.voice = VoiceClient(self)
        # self.sms = SmsClient()
        # self.api = ApiClient()
        # self.email = EmailClient()

    @staticmethod
    def generate_auth_header(customer_id, password):
        userpass_concat = "{}:{}".format(customer_id, password)
        userAndPass = b64encode(userpass_concat.encode()).decode("ascii")
        header = {'Authorization': 'Basic %s' % userAndPass}
        return header

    def post(self, api_resource, **params):
        return self._send(api_resource, self.session.post, **params)

    def put(self, api_resource, **params):
        return self._send(api_resource, self.session.put, **params)


    def get(self, api_resource, **params):
        return self._send(api_resource, self.session.get, **params)


    def delete(self, api_resource, **params):
        return self._send(api_resource, self.session.delete, **params)

    def _send(self, api_resource, method_function, **params):
        """
        Generic REST API request handler.
        :param api_resource: The partial resource URI to perform the request against, as a string.
        :param method_function: The Requests HTTP request function to perform the request.
        :param params: Body params to perform the HTTP request with, as a dictionary.
        :return: The RestClient Response object.
        """
        resource_uri = "{api_host}{resource}".format(api_host=self.base_url, resource=api_resource)


        headers = {
            "Content-Type": "application/json",
        }
        headers.update(self.auth_header)

        response = Response(method_function(resource_uri,
                                            json=params,
                                                 headers=headers,
                                                 timeout=self.timeout
                                                 ))

        return response



