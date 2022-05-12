from bottle import route, run

@route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
    <body>
    <p>Hello World!</p>
    </body>
</html>
'''

run(host='10.82.27.199', port 8080)