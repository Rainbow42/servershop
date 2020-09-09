from work_file import write_file


class Date:
    def get(self, filename, url, session, headers, params=None):
        """Метод для получение содержания со с старницы """
        request = session.get(url, headers=headers, params=params)
        try:
            request = session.get(url, headers=headers, params=params)
        except Exception as err:
            return 'Answer {} \nError url or Incorrect url!'.format(request.status_code) + str(err)
        else:
            if request.status_code == 200:
                print("Answer {}".format(request.status_code))
                write_file(filename, request)
                return request.text, request.status_code
            else:
                print('Answer {} \nSubmission link'.format(request.status_code))
                return request.text, request.status_code
