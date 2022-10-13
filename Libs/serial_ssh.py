from netmiko import ConnectHandler
import time
import paramiko
from paramiko.client import AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException


def ssh_connect(self, USERNAME="admin", password="", host=None):
    # global session
    try:
        self.client = paramiko.SSHClient()
        # self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.connect(hostname=host,
                            username=USERNAME,
                            password=password,
                            look_for_keys=False,
                            allow_agent=False)
        self.client.invoke_shell()
        print("Interactive SSH session established ", host)
        time.sleep(2)
    except AuthenticationException as error:
        print('Authentication Failed: Please check your network/ssh key')
    finally:
        return self.client


def disconnect(self):
    self.client.close()


def execute_cmd(self, command, host=None):
    output_file = 't.txt'
    max_bytes = 65535
    short_pause = 2
    long_pause = 5

    # if self.client is None:
    #    var = self.client == self.ssh_connect()

    print('started...')
    ssh = self.ssh_connect(host=host)  # .invoke_shell()
    deffi = ssh.invoke_shell()
    conf_t = "conf t"
    deffi.sendall(conf_t + "\n")
    time.sleep(5)
    deffi.sendall(command + "\n")
    time.sleep(5)
    output = deffi.recv(4096).decode("utf-8")
    print('Command %s on %s' % (command, host))
    # print(output)

    print("ssh successful. Closing connection")
    self.client.close()
    print('Connection closed')

    return output


def load_config(self):
    pass


def connector(connection_master_comport):
    device = {
        "device_type": "cisco_ios_serial",
        "username": "admin",
        "password": "",
        "serial_settings": {"port": connection_master_comport,
                            "baudrate": 115200}
    }
    console = ConnectHandler(**device)

    # console.enable()
    # print(console.find_prompt())
    return console


def send_command(connection_master_comport, command_set):
    # console_cmd = connector().send_command(command, expect_string=r"#",
    #                                       read_timeout=20.0)
    console_cmd = connector(connection_master_comport).send_config_set(command_set, read_timeout=90.0)
    # print(console_cmd)
    return console_cmd
