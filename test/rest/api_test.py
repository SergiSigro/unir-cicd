import http.client
import os
import unittest
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

import pytest

BASE_URL = os.environ.get("BASE_URL", "http://localhost:5000")
DEFAULT_TIMEOUT = 2  # in secs
INVALID_PARAMS = ["abc", "", None]

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add_success(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.read().decode(), "4")

    def test_api_add_failure(self):
        for invalid_param in INVALID_PARAMS:
            url = f"{BASE_URL}/calc/add/2/{invalid_param}"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

            url = f"{BASE_URL}/calc/add/{invalid_param}/2"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

    def test_api_subtract_success(self):
        url = f"{BASE_URL}/calc/subtract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.read().decode(), "2")

    def test_api_subtract_failure(self):
        for invalid_param in INVALID_PARAMS:
            url = f"{BASE_URL}/calc/subtract/5/{invalid_param}"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

            url = f"{BASE_URL}/calc/subtract/{invalid_param}/3"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

    def test_api_multiply_success(self):
        url = f"{BASE_URL}/calc/multiply/3/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.read().decode(), "9")

    def test_api_multiply_failure(self):
        for invalid_param in INVALID_PARAMS:
            url = f"{BASE_URL}/calc/multiply/3/{invalid_param}"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

            url = f"{BASE_URL}/calc/multiply/{invalid_param}/3"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

    def test_api_divide_success(self):
        url = f"{BASE_URL}/calc/divide/6/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.read().decode(), "3.0")

    def test_api_divide_failure(self):
        url = f"{BASE_URL}/calc/divide/1/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
        except URLError as e:
            self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
        else:
            self.fail(f"Expected HTTPError for URL {url}, but got success")

        for invalid_param in INVALID_PARAMS:
            url = f"{BASE_URL}/calc/divide/6/{invalid_param}"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

            url = f"{BASE_URL}/calc/divide/{invalid_param}/2"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

    def test_api_power_success(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.read().decode(), "8")

    def test_api_power_failure(self):
        for invalid_param in INVALID_PARAMS:
            url = f"{BASE_URL}/calc/power/2/{invalid_param}"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

            url = f"{BASE_URL}/calc/power/{invalid_param}/3"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

    def test_api_sqrt_success(self):
        url = f"{BASE_URL}/calc/sqrt/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.read().decode(), "3.0")

    def test_api_sqrt_failure(self):
        url = f"{BASE_URL}/calc/sqrt/-9"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
        except URLError as e:
            self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
        else:
            self.fail(f"Expected HTTPError for URL {url}, but got success")

        for invalid_param in INVALID_PARAMS:
            url = f"{BASE_URL}/calc/sqrt/{invalid_param}"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

    def test_api_log10_success(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.read().decode(), "2.0")

    def test_api_log10_failure(self):
        url = f"{BASE_URL}/calc/log10/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
        except URLError as e:
            self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
        else:
            self.fail(f"Expected HTTPError for URL {url}, but got success")

        for invalid_param in INVALID_PARAMS:
            url = f"{BASE_URL}/calc/log10/{invalid_param}"
            try:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            except HTTPError as e:
                self.assertIn(e.code, [http.client.BAD_REQUEST, http.client.NOT_FOUND], f"Error en la petición API a {url} con código {e.code}")
            except URLError as e:
                self.fail(f"Unexpected URLError for URL {url}: {e.reason}")
            else:
                self.fail(f"Expected HTTPError for URL {url}, but got success")

if __name__ == "__main__":
    unittest.main()
