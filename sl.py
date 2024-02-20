import socket,sys,time;
args=sys.argv;
def connect(host=None,options=None):
    global magicExitCode;
    magicExitCode=False;
    def doCLI(host):
        global magicExitCode;
        while (not magicExitCode):
            action=input(f'https://{host} >');
            if (action=='exit' or action=='quit' or action=='disconnect'):
                magicExitCode=True;
            ##endif
        ##end
    ##end
    print(f'Connecting to https://{host}, please wait...');
    time.sleep(3);
    try:
        global magicExitCode;
        if (socket.gethostfromname(host)):
            addr=socket.gethostfromname(host);
            print(f'Connected to https://{addr} on port 8080.');
            magicExitCode=False;
            doCLI(host);
        ##endif
    except socket.gaierror as err:
        print('Unable to get address info.. Host doesn\'t exist or is not resolved.')
    ##endtry
##end
def mount(host):
    pass;
##end
def disconnect():
    print('disconnect called');
    print('Committing Changes, This may take a moment.');
    time.sleep(2);
    print('Changes Successfully deployed!');
##end
print(f'SCRIPT: {args[0]}');
if (len(args)>1):
    if (args[1].lower()=='>connect'):
        url=input('> ');
        connect(url);
    ##endif
else:
    print(f'Welcome to Serverlink v1.20.0\nWhat would you like to do?');
    action=input('> ');
    if (action=='connect'):
        def getInput():
            host=input('connect > ');
            if (host!=None and host!=""):
                connect(host);
            else:
                getInput();
            ##endif
        ##end
    ##endif
##endif
