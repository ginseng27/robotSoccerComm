import argparse

from client import Client

class Main:
    def __init__(self):
        self.parse_arguments()
        self.setup_logger()

    def parse_arguments(self):
        parser = argparse.ArgumentParser(prog='robot client',
                                         description='client program to attach to any server',
                                         add_help=True)
        parser.add_argument('-s', '--server', type=str,
                            action='store',
                            help='IP of the server to connect to. default=localhost',
                            default='localhost')
        parser.add_argument('-p', '--port', type=int, action='store',
                            help='port the server is running on. default=1337',
                            default=1337)
        self.args = parser.parse_args()


    def setup_logger(self):
        self.logger = logging.getLogger('RobotServer')
        self.logger.setLevel(logging.DEBUG)
        self.log_location = os.path.abspath(self.args.log)
        fh = logging.FileHandler(self.log_location)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def run(self):
        c = Client(self.args.server,self.args.port)
        c.run()

if __name__ == "__main__":
    m = Main()
    m.parse_arguments()
    m.run()
