class App:
    def __init__(self, env):
        self.__env = env

    def read_config(self):
        DatabaseConfig.filename = os.path.join(self.__env, 'database.json')
    
    def configure_services(self):
        services = [
            OCRService(),
            ClassificationService(),
            FeedbackService()
        ]
        for service in services:
            service.run()

    def run():
        pass

if __name__ == '__main__':
    app = App(os.getenviron('dev'))
    app.read_config()
    app.run()
