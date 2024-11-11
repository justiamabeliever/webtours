from locust import LoadTestShape
from config.config import cfg


class MyCustomLoadShape(LoadTestShape):
    match cfg.loadshape_type:
        case "baseline":
            stages = [
                {"duration": 60, "users": 1, "spawn_rate": 1}
            ]
            
        case "fixedload":
            stages = [
                {"duration": 300, "users": 20, "spawn_rate": 0.3}
            ]

        case "stages":
            stages = [
                {"duration": 60, "users": 5, "spawn_rate": 0.3}, #0.3 пользователя в секунду, то есть один юзер в ~ 3секунды / все 10 за 30 секунд
                {"duration": 120, "users": 10, "spawn_rate": 0.3},
                {"duration": 180, "users": 15, "spawn_rate": 0.3},
                {"duration": 240, "users": 20, "spawn_rate": 0.3},
                {"duration": 300, "users": 25, "spawn_rate": 0.3}
            ]

    def tick(self): # стандартная функция локаста, взятая из документации, для работы с кастомными "Лоад-Шейпами"
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None