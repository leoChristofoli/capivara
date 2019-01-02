import subprocess

def send():
    try:
        res = subprocess.check_output(r'aws s3 cp .\_site\ s3://leochp --recursive')
        print('success')
    except subprocess.SubprocessError as err:
        print(err)
    input('pause')


if __name__ == '__main__':
    send()