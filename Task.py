class Task:

    def __init__(self: object, name: str, url):
        self.__name = name
        self.__url = url

    def name(self: object):
        return self.__name

    def url(self: object):
        return self.__url
