# coding: utf-8


import time
import paramiko
import log
import os
import logging


def sftp_transfer(host, src_path, dst_path, username, password):
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(host, 22, username, password)

    sftp = s.open_sftp()
    file_list = os.listdir(src_path)
    for file_name in file_list:
        src_file = os.path.join(src_path, file_name)
        dst_file = os.path.join(dst_path, file_name)
        try:
            sftp.put(src_file, dst_file)
        except IOError as e:
            sftp.mkdir(dst_path)
            sftp.put(src_file, dst_file)
        except Exception as e:
            logging.exception(str(e))
    s.close()
    pass


def upgrade(hostname,
            port,
            username,
            password,
            src_file,
            dst_file,
            cmd_list):
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, port, username, password)
    sftp = s.open_sftp()
    sftp.put(src_file, dst_file)
    for cmd in cmd_list:
        stdin, stdout, stderr = s.exec_command(cmd)
        out = stdout.read()
        if len(out) != 0:
            log.record("out: %s - %s" % (hostname, out))
        err = stderr.read()
        if len(err) != 0:
            log.record("err: %s - %s" % (hostname, err))
        time.sleep(1)
    s.close()
    pass


if __name__ == "__main__":
    pass
