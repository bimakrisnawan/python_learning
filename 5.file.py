# # create a file.
# # If file is existing, it erases and creates a new one
# f1 = open('1.coba.txt', 'w')

# # create a file.
# # If file is existing, it appends. Otherwise, it creates
# f2 = open('2.coba.txt', 'a')

# # binary files
# bf1 = open('3.coba.txt', 'wb')
# bf2 = open('4.coba.txt', 'ab')


# #####################################
# # writing data
# print('writing data into files…')
# for index in range(1, 12):
#     data = ''
#     name = 'user ' + str(index-1)
#     email = 'user' + str(index-1) + '@email.com'
#     if index == 1:
#         data = '{0:3s} {1:10s} {2:15s}\n'.format('No', 'Name', 'Email')
#     else:
#         data = '{0:3s} {1:10s} {2:15s}\n'.format(str(index-1), name, email)
        
# f1.write(data)
# f2.write(data)

# # error bcs binary
# # bf1.write(data)
# # bf2.write(data)

# #####################################
# # close all
# print('close files…')
# f1.close()
# f2.close()
# bf1.close()
# bf2.close()

# reading
import sys
#####################################
print('opening files…')
f1 = open('1.coba.txt', 'r')
f2 = open('2.coba.txt', 'r')
bf1 = open('3.coba.txt', 'rb')
bf2 = open('4.coba.txt', 'rb')
#####################################
# reading data
def reading_data(f):
    while True:
        data = f.readline()
        if (data == '') or (data == None):
            break

        sys.stdout.write(data)

print('for mydoc1>>>>>')
reading_data(f1)
print('>>>>>>>>>>>>>>>')
print('for mydoc2>>>>>')
reading_data(f2)
print('>>>>>>>>>>>>>>>')
print('for mydoc3>>>>>')
reading_data(bf1)
print('>>>>>>>>>>>>>>>')
print('for mydoc4>>>>>')
reading_data(bf1)
print('>>>>>>>>>>>>>>>')

#####################################
# close all

print('close files…')
f1.close()
f2.close()
bf1.close()
bf2.close()