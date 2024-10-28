from locust import task, SequentialTaskSet, HttpUser, constant_pacing, constant_throughput, events
from config.config import cfg, logger


class PurchaseFlightTicket(SequentialTaskSet): # класс с задачами (содержит основной сценарий)
    @task
    def uc_00_getHomePage(self) -> None:

        r00_01_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7',
            'Cache-Control':'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'localhost:1080',
            'If-Modified-Since':'Mon, 27 May 2013 11:20:22 GMT',
            'If-None-Match': '"30000000ac7b8-16e-4ddb1559ac980"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows"
        }

        r00_01_response = self.client.get(
            '/WebTours/',
            name="REQ_00_0_getHtml",
            # headers=r00_01_headers,
            allow_redirects=False
        )

        print(r00_01_response.status_code)
        print(r00_01_response.request.url)
        print(r00_01_response.text)


class WebToursBaseUserClass(HttpUser): # юзер-класс, принимающий в себя основные параметры теста
    wait_time = constant_pacing(cfg.pacing)

    host = cfg.url

    logger.info(f'WebToursBaseUserClass started. Host: {host}')

    tasks = [PurchaseFlightTicket]