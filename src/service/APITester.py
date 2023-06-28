import os
from dotenv import load_dotenv
import requests
from zeep import Client
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Carga las variables de entorno del archivo .env
load_dotenv()

class APIRestTester:

    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")

    def test_endpoint(self, endpoint, method, input_object, output_object):
        url = self.base_url + endpoint

        if method.lower() == "get":
            response = requests.get(url, params=input_object)
        elif method.lower() == "post":
            response = requests.post(url, json=input_object)
        elif method.lower() == "put":
            response = requests.put(url, json=input_object)
        elif method.lower() == "delete":
            response = requests.delete(url, json=input_object)
        else:
            raise ValueError(f"Invalid method: {method}")

        assert response.json() == output_object, f"Expected {output_object}, got {response.json()}"
        
class SoapAPITester:

    def __init__(self):
        self.wsdl_url = os.getenv("SOAP_WSDL_URL")
        self.client = Client(self.wsdl_url)

    def test_operation(self, operation_name, input_object, expected_output_object):
        service = self.client.service
        operation = getattr(service, operation_name)
        response = operation(**input_object)

        assert response == expected_output_object, f"Expected {expected_output_object}, got {response}"



class GraphQLAPITester:

    def __init__(self):
        self.base_url = os.getenv("GRAPHQL_API_URL")
        self.transport = RequestsHTTPTransport(url=self.base_url)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def test_query(self, query, variables, expected_result):
        prepared_query = gql(query)
        response = self.client.execute(prepared_query, variable_values=variables)

        assert response == expected_result, f"Expected {expected_result}, got {response}"
