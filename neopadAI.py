__user__ = ''
__ai__ = ''
def runAI(__user__):
    def ai_output(__user__):
        with open('file.data', 'r') as file:
            for line in file:
                if line.startswith(__user__):
                    _, return_ = line.split(':', 1)
                    return return_.strip()
        __Ai__ = input('Enter your answer: ')
        __text__ = __user__ + ':' + __Ai__
        with open('file.data', 'a+', encoding='utf-8') as file:
            file.write('\n' + __text__)
        return "Error: " + __user__ + '??'

    __ai__ = ai_output(__user__)
    return __ai__

def par(__nameai__, __username__, __text__, __special__):
    if(__special__ == 'username'):
        return 'username: ' + __username__
    
    elif(__special__ == 'name ai'):
        return 'name ai: ' + __nameai__
    
    elif(__special__ == 'add'):
        with open('file.data', 'a+', encoding='utf-8') as file:
            file.write('\n' + __text__)
        return 'add: ' + __text__
    
    else:
        return "err: ' --" + __special__ + "-- '??"