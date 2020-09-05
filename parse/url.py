import requests

from work_file import write_file


class Date:

    def get(self, filename, url, session):
        request = 'Error link'
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
