import requests
import random

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

        self.signup_url = self.api_endpoint.format(action='user/register/')
        self.auth_url = self.api_endpoint.format(action='user/token/')
        self.verify_url = self.api_endpoint.format(action='user/token-verify/')
        self.create_post_url = self.api_endpoint.format(action='post/create/')
        self.random_mark_post_url = self.api_endpoint.format(action='post/random/{mark}/')

    def run(self):

        for i in range(self.number_of_users):
            data = {
                'username': f'AutoBot{i}',
                'password': 'autobotpasswordcommon',
                'email': '',
            }
            r = requests.post(self.signup_url, data=data)
            r = requests.post(self.auth_url, data=data)
            access_token = r.json()['token']
            headers = {'Authorization': 'JWT {}'.format(access_token)}
            for j in range(random.randint(0, self.max_posts_per_user)):
                r = requests.post(
                    self.create_post_url,
                    data={"content": f'Content{j} via AutoBot{i}', "title": "Wow Test Post"},
                    headers=headers
                )
            for j in range(self.max_likes_per_user):
                r = requests.put(
                    self.random_mark_post_url.format(mark='like'),
                    headers=headers
                )

    #
    # End Public Methods
    #

    @staticmethod
    def __parse_config(config_path):
        return parse.parse_yaml('', config_path)


if __name__ == '__main__':
    bot = AutoBot()
    bot.run()
