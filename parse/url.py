import requests
import sys
sys.path.append('../')

def write_file(filename, request):
    with open(filename, 'w') as output_file:
        output_file.write(str(request.text))



class Date:
    def get(self, filename, url, session):

        try:
            request = session.get(url)
        except:
            request = 'error'
            print('Incorrect url!')
        else:
            print("Answer {}".format(request))
            write_file(filename, request)
        return request
