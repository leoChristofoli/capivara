from __bin.send_to_s3 import send
import subprocess


def deployit():
    send()

def build():
    print('start to build')
    try:
        res = subprocess.check_output(['jekyll', 'build'], shell=True)
        print(res)
        return True
    except subprocess.SubprocessError as err:
        print(err)
    return False

def worker():
    builded = build()
    if builded:
        deployit()

if __name__ == '__main__':
    worker()