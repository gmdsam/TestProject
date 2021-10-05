from abc import ABC, abstractstaticmethod

class IReader(ABC):
    @abstractstaticmethod
    def read(filename):
        raise NotImplementedError()


class JsonReader(IReader):
    def read(self, filename) -> dict:
        pass


class XmlReader(IReader):
    def read(self, filename) -> dict:
        pass


class ReaderFactory:
    @staticmethod
    def get_reader(filename):
        if filename.endswith('.json'):
            return JsonReader()
        if filename.endswith('.xml'):
            return XmlReader()


class IWriter(ABC):
    @abstractstaticmethod
    def write(filename, content: dict):
        pass

class JsonWriter(IWriter):
    def write(self, filename, content: dict):
        pass

class TextWriter(IWriter):
    def write(self, filename, content: dict):
        pass


class WriterFactory:
    @staticmethod
    def get_writer(filename):
        if filename.endswith('.json'):
            return JsonWriter()
        if filename.endswith('.txt'):
            return TextWriter()


class MongoDatabaseConfig:
    hostname: str
    port: int
    username: str
    password: str

    def __init__(
            self,
            hostname: str,
            port: int,
            username: str,
            password: str
        ):
    self.hostname = hostname
    self.port = port
    self.username = username
    self.password = password

    @staticmethod
    def from_dict(data: dict):
        return MongoDatabaseConfig(
            hostname=data.get('hostname'),
            port=data.get('port'),
            username=data.get('username'),
            password=data.get('password')
        )
    
    @staticmethod
    def to_dict(data):
        return {}


class DatabaseConfig:
    filename: str
    cache_database_config: MongoDatabaseConfig
    predictions_database_config: MongoDatabaseConfig

    def to_dict(self):
        return {
            'cache_database_config': self.cache_database_config.to_dict()
            'predictions_database_config': self.predictions_database_config.to_dict()
        }

    @staticmethod
    def set_config(data):
        DatabaseConfig.cache_database_config = MongoDatabaseConfig.from_dict(data.get('cache_database_config'))
        DatabaseConfig.predictions_database_config = MongoDatabaseConfig.from_dict(data.get('predictions_database_config'))
    
    def read(self):
        reader = ReaderFactory.get_reader(self.filename)
        data = reader.read(self.filename)
        DatabaseConfig.set_config(data)
    
    def write(self):
        writer = WriterFactory.get_writer(self.filename)
        writer.write(self.filename, self.to_dict())
