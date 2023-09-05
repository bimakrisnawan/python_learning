# try:
#     a = 18
#     b = 0
#     c = a / b
#     print('result:', str(c))
# except Exception  as e:
#     # ZeroDivisionError
#     # print('Error: division by zero')
#     print(e)

# finally:
#     print('Done')
    
# print('exit from program')


# raise = highlight error dmn
# try:
#     a = 18
#     b = 0
#     c = a / b
#     print('result:', str(c))
# except Exception as e:
#     raise
# finally:
#     print('Done')
# this code is never called

class MySimpleError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
    def __str__(self):
        return repr(str(self.code) + ":" + self.message)
    def save_to_database(self):
        print('save this error into database..')
# how to use custom error
try:
    print('demo custom error')
    print('raise error now')
    raise MySimpleError(100,'This is custom error')
except MySimpleError as e:
    print(e)
    e.save_to_database()
