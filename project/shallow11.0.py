password = 'tinutimmy'


def here():
    print('Here you go, sir!')
command = ''
password_a = input('what is the password ? ')
while password == password_a:
    help = input('how can i help you ? ')
    while help != 'thanks':
        if help == 'open google':
            print(f'''
{here()}
www.google.com
            ''')

        elif help == 'open gmail':
            print(f'''
{here()}
https://mail.google.com/
''')

        elif help == 'open youtube':
            print(f'''
{here()}
https://www.youtube.com/
''')

        elif help == 'open insta':
            print(f'''
{here()}
https://www.instagram.com/
''')

        elif help == 'open nasa':
            print(f'''
{here()}
https://www.nasa.gov/
''')

        elif help == 'open amazon':
            print(f'''
{here()}
https://www.amazon.in/
''')

        elif help == 'learn code':
            print(f'''
{here()}
https://www.freecodecamp.org/
''')

        elif help == 'test net speed':
            print(f''''
{here()}
https://www.speedtest.net/
''')

        elif help == 'what is the weather':
            print(f'''
{here()}
https://www.accuweather.com/
''')

        elif help == 'add':
            number = input('what you want to add ')
            num = input('by which number ? ')
            real_number = int(number) + int(num)
            print(real_number)


        elif help == 'subtract':
            number = input('what you want to subtract ? ')
            num = input('by which number ? ')
            real_number = int(number) - int(num)
            print(real_number)


        elif help == 'multiply':
            number = input('what you want to multiply ? ')
            num = input('by which number ? ')
            real_number = int(number) * int(num)
            print(real_number)


        elif help == 'divide':
            number = input('what you want to divide ? ')
            num = input('by which number ? ')
            real_number = int(number) / int(num)
            print(real_number)

        elif help == 'how this program work':
            print(f'''
to open gmail type 
    #open gmail
to open google type 
    #open google
to open YouTube type
    #open youtube 
to open Instagram type
    #open insta
to open amazon type
    #open amazon
to test network type 
    #test net speed
to know weather type
    #what is the weather 

''')

        elif help == 'thanks':
            print('your welcome')
            break

        else:
            print("i don't understand, try again.")

else:
    print("wrong password")
