
import argparse
import os
import server
import logging

class RobotServer:
    def __init__(self):
        self.parse_arguments()
        self.setup_logger()

    def parse_arguments(self):
        parser = argparse.ArgumentParser(prog='Robot Server', 
                            description='Robot Server', add_help=True)
        parser.add_argument('-p', '--port', type=int,
                            action='store',
                            help='port the server will run on. default=1337',default=1337)
        parser.add_argument('-l', '--log', type=str, action='store',
                            help="location for logs. default=./robotServer.log",
                            default="./robotServer.log")
        parser.add_argument('-r', '--ref', type=str, action='store',
                            help='IP of the ref. no default')
        parser.add_argument('-o', '--other-robot', type=str, action='store',
                            help='IP of the other robot. aka teammate')
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
        s = server.Server(self.args.port, self.args.ref, self.args.other_robot, self.logger)
        s.run()

if __name__ == "__main__":
    rs = RobotServer()
    rs.parse_arguments()
    try:
        rs.run()
    except KeyboardInterrupt:
        pass
