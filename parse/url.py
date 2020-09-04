import requests
import sys
from work_file import write_file

sys.path.append('../')


class Date:

    def get(self, filename, url, session):

        try:
            request = session.get(url)
        except:
            return 'Answer {} \nError url or Incorrect url!'.format(request)
        else:
            if '20' in str(request):
                print("Answer {}".format(request))
                write_file(filename, request)
            else:
                return 'Answer {} \nSubmission link'.format(request)
        return 'Answer {}'.format(request)
