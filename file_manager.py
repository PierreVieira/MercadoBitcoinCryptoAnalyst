class FileManager:
    @staticmethod
    def get_tap_user_info() -> dict:
        with open('tapi.txt') as arq:
            content = tuple(map(lambda string: string.replace('\n', ''), arq.readlines()))
        return {
            'tapi_id': content[0],
            'tapi_secret': content[1]
        }