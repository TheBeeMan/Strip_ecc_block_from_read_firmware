import os
import fcntl

ifile = 'big.firmware'
ofile = 'small.firmware'
fakePageSize = 2112
realPageSize = 2048

def readBlock(fd, size):
    while True:
        try:
            data = fd.read(size)
            if data:
                yield data
            else:
                print('read finished')
                break
        except Exception as e:
            print('read() received exception: ', e)
            break

def process(fd, data):
    try:
        fd.write(data[:realPageSize])
    except Exception as e:
        print('write error with ', e)

def main():
    ofd = open(ofile, 'wb')
    ifd = open(ifile, 'rb')
    #flag = fcntl.fcntl(f.fileno(), fcntl.F_GETFL)
    #fcntl.fcntl(f.fileno(), fcntl.F_SETFL, flag | os.O_NONBLOCK)
    while True:
        try:
            idata = readBlock(ifd, fakePageSize).next()
            process(ofd, idata)
        except (GeneratorExit, StopIteration) as e:
            print('write finished until ', e)
            break

if __name__ == '__main__':
    main()
