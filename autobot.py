import requests

import parse

CONFIG_PATH = 'autobotconfig.yaml'
API_ENDPOINT = 'http://127.0.0.1:8000/api/{action}'


class AutoBot:

    def __init__(self, config_path=CONFIG_PATH, api_endpoint=API_ENDPOINT):
        config_data = self.__parse_config(config_path)
        self.number_of_users = config_data['number_of_users']
        self.max_posts_per_user = config_data['max_posts_per_user']
        self.max_likes_per_user = config_data['max_likes_per_user']
        self.api_endpoint = api_endpoint

    def run(self):
        url = self.api_endpoint.format(action='user/register/')
        for i in range(self.number_of_users):
            data = {
                'username': f'AutoBot{i}',
                'password': 'autobotpasswordcommon',
                'email': '',
            }
            r = requests.post(url, data=data)
            print(r.status_code, r.json())

    #
    # End Public Methods
    #

    @staticmethod
    def __parse_config(config_path):
        return parse.parse_yaml('', config_path)


if __name__ == '__main__':
    bot = AutoBot()
    bot.run()

