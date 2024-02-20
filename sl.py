import socket,sys,time;
#Private Functions
def host_resolves(host):
    try:
        ip=socket.gethostbyname(host);
        return True;
    except socket.error:
        return False;
    ##endtry
##end
#ARGUMENT PARSER
def parseArguments(args=None,parseOptions=None):
    if (args!=None):
        arguments=[];
        kwarguments={};
        flags=[];
    ##endif
##end
def parseInput(val):
    global command,args;
    table=val.split(' ');
    command=table[0];
    args=[];
    if (len(table)>1):
        for i in range(1,len(table)-1):
            args.append(table[i]);
        ##end
    ##endif
    return command,args;
##end
def ynPrompt(prompt,ony=None,onn=None):
    yn=input(prompt);
    if (yn.lower()=='y' or yn.lower()=='yes'):
        if ony:ony();
        else:return True;
        ##endif
    elif (yn.lower()=='n' or yn.lower()=='no'):
        if onn:onn();
        else:return False;
        ##endif
    else:
        print('Invalid Input! Type either y/n or yes/no');
        return ynPrompt(prompt,ony,onn);
    ##endif
##end
def validateInput(prompt=None,onEnter=None):
    global val;
    val=input(prompt);
    if (onEnter(val)!=True):
        validateInput(prompt,onEnter);
    else:
        return val;
    ##endif
##end
def strToBool(string):
    if (string=='true' or string=='t'):
        return True;
    else:
        return False;
    ##endif
##end
#CLI FUNCTIONS
def handleViewAsPage(url):
    print(f'Viewing {url} as Page with Microsoft Edge WebView');
##end
def handleViewAsText(url):
    print(f'Viewing {url} as Text with tkinter');
##end
def connect(host=None,port=None):
    global magicExitCode;
    magicExitCode=False;
    def doCLI(dir):
        global magicExitCode;
        while (not magicExitCode):
            command=input(f'https://{dir} >');
            action,args=parseInput(command);
            if (action.lower()=='exit' or action.lower()=='quit' or action.lower()=='disconnect'):
                magicExitCode=True;
            elif (action.lower()=='mount' or action.lower()=='mt'):
                print('Mounting to VirtualDrive.');
                if (args!=[]):
                    path=args[0];
                    if (path=='' or path=='/'):
                        print('Mounting to Root Directory of VirtualDrive. To mount another, unmount this one.');
                    ##endif
                ##endif
            elif (action.lower()=='unmount' or action.lower()=='unmt'):
                print('Unmounting from VirtualDrive');
                if (args!=[]):
                    path=args[0];
                    unmountGranted=ynPrompt('Are you sure you want to unmount? You will lose any unsaved progress.(y/n)\n> ');
                    if (unmountGranted):
                        if (path=='' or path=='/'):
                            print('Unmounting from Root Directory of VirtualDrive.');
                        ##endif
                    else:
                        print('Unmounting cancelled');
                    ##endif
                ##endif
            ##endif
        ##end
    ##end
    print(f'Connecting to https://{host}, please wait...');
    time.sleep(3);
    if (host_resolves(host)):
        print(f'Connected to https://{host} on port {port}.');
        magicExitCode=False;
        doCLI(host);
        yn=input('Connection halted. Would you like to reconnect (y/n)?\n> ');
        if (yn):
            connect(host,port);
        else:
            print('Reconnect declined, disconnecting...');
            disconnect();
        ##endif
    else:
        print('Unable to get address info.. Host doesn\'t exist or is not resolved.');
    ##endif
##end
def mount(host,port):
    pass;
##end
def disconnect():
    print('disconnect called');
    print('Committing Changes, This may take a moment.');
    time.sleep(2);
    print('Changes Successfully deployed!');
##end
def main():
    args=sys.argv;
    print(f'SCRIPT: {args[0]}');
    if (len(args)>1):
        if (args[1].lower()=='>connect'):
            if (len(args)>2):
                def getInputArg(bool):
                    global host,port;
                    host=args[2].lower();
                    if (len(args)>3):
                        port=int(args[3]);
                    else:
                        port=8080;
                    ##endif
                    if (host!=None and host!=""):
                        connect(host,port);
                    ##endif
                ##end
            elif (len(args)==2):
                def getInput():
                    host=input('> ');
                    if (host!=None and host!=""):
                        connect(host);
                    else:
                        getInput();
                    ##endif
                ##end
                getInput();
            ##endif
        ##endif
    else:
        print(f'Welcome to Serverlink v1.20.0\nWhat would you like to do?');
        global exitCode;
        exitCode=False;
        while (not exitCode):
            cmdstr=input('> ');
            action,cmdargs=parseInput(cmdstr);
            if (action=='quit' or action=='exit'):
                exitCode=True;
            elif (action=='connect'):
                def getInput():
                    global host,port;
                    argstr=input('connect> ');
                    arg=argstr.split(' ');
                    host=arg[0];
                    if (len(arg)>1):
                        port=int(arg[1]);
                    else:
                        port=8080;
                    ##endif
                    if (host!=None and host!=""):
                        connect(host,port);
                    else:
                        getInput();
                    ##endif
                ##end
                getInput();
            elif (action=='webview'):
                if (cmdargs!=[]):
                    url=cmdargs[0];
                    if (len(cmdargs)>1):
                        asText=strToBool(cmdargs[1]);
                        if (asText==True):
                            handleViewAsText(url);
                        else:
                            handleViewAsPage(url);
                        ##endif
                    ##endif
                ##endif
            else:
                print(f"SYNTAX ERROR: Unknown command '{action}'.");
            ##endif
        ##end
    ##endif
##end
main();
