import sys,time;
args=sys.argv;
def connect(url):
    print(f'Connecting to {url}, please wait...');
    time.sleep(3);
    print(f'Connected to {url} on port 8080.');
    action=input(f'{url}> ');
    print(f'{action}');
##end
def disconnect():
    print('disconnect called');
    print('Committing Changes, This may take a moment.');
    time.sleep(2);
    print('Changes Successfully deployed!');
##end
print(f'SCRIPT: {args[0]}');
if (len(args)>1):
    if (args[1].lower()=='> connect'):
        url=input('> ');
        connect(url);
    ##endif
else:
    print(f'Welcome to Serverlink v1.20.0\nWhat would you like to do?');
    action=input('> ');
    if (action=='connect'):
        url=input('connect > ');
        connect(url);
    ##endif
##endif
