import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_hello(self):
            url = f"{BASE_URL}"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.status, http.client.OK,f"hho"
            )

    def test_api_add(self):
            url = f"{BASE_URL}/calc/add/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.status, http.client.OK, f"Error en la petición API a {url}"
            )

    def test_api_add_bad(self):
            url = f"{BASE_URL}/calc/add/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.BAD_REQUEST
            )

    def test_api_add_not_found(self):
            url = f"{BASE_URL}/calc/add/2/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.NOT_FOUND
            )

    def test_api_add_sum(self):
            url = f"{BASE_URL}/calc/add/2/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.read().decode('utf-8'), "4"
            )

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/4/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract_bad(self):
            url = f"{BASE_URL}/calc/substract/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.BAD_REQUEST
            )

    def test_api_substract_not_found(self):
            url = f"{BASE_URL}/calc/substract/2/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.NOT_FOUND
            )

    def test_api_substract_result(self):
            url = f"{BASE_URL}/calc/substract/2/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.read().decode('utf-8'), "0"
            )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/4/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_bad(self):
            url = f"{BASE_URL}/calc/multiply/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.BAD_REQUEST
            )

    def test_api_multiply_not_found(self):
            url = f"{BASE_URL}/calc/multiply/2/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.NOT_FOUND
            )

    def test_api_divide(self):
            url = f"{BASE_URL}/calc/divide/4/0"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                   response.status, "400"
            )

    def test_api_divide_bad(self):
            url = f"{BASE_URL}/calc/divide/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.BAD_REQUEST
            )

    def test_api_divide_not_found(self):
            url = f"{BASE_URL}/calc/divide/2/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.NOT_FOUND
            )

    def test_api_power(self):
            url = f"{BASE_URL}/calc/power/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.status, http.client.OK, f"Error en la petición API a {url}"
            )

    def test_api_power_bad(self):
            url = f"{BASE_URL}/calc/power/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.BAD_REQUEST
            )

    def test_api_power_not_found(self):
            url = f"{BASE_URL}/calc/power/2/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.NOT_FOUND
            )
        
    def test_api_square(self):
            url = f"{BASE_URL}/calc/square/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.status, http.client.OK, f"Error en la petición API a {url}"
            )

    def test_api_square_bad(self):
            url = f"{BASE_URL}/calc/square/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.BAD_REQUEST
            )

    def test_api_square_not_found(self):
            url = f"{BASE_URL}/calc/square/2/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.NOT_FOUND
            )
    
    def test_api_log10(self):
            url = f"{BASE_URL}/calc/log10/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.status, http.client.OK, f"Error en la petición API a {url}"
            )

    def test_api_log10_bad(self):
            url = f"{BASE_URL}/calc/log10/4/4"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.BAD_REQUEST
            )

    def test_api_log10_not_found(self):
            url = f"{BASE_URL}/calc/log10/2/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.NOT_FOUND
            )