from json import load
from fita import Word

def open_json():
    with open('entrada.json', 'r') as json_file:
        data = load(json_file)
    return data


def calculate(all_states, final_states, actual_state, obj_word, pilha):
    """Calcula as devidas transições"""
    epsilon = "&"
    verifi = "?"

    actual_letter = None
    if len(obj_word.word)> 1:
        actual_letter = obj_word.word[0]
        obj_word.word = obj_word.word[1:]
    elif len(obj_word) == 1:
        actual_letter = obj_word.word[0]
        obj_word.word = ""

    estado_atual = [
        state for state in all_states if state.state == actual_state.state][0]
           

    if actual_letter == None:
        for transition in estado_atual.transitions:
            if transition.letter == verifi:
                if transition.unstack == verifi:
                    if len(pilha.stack) == 0:
                        if transition.goes_to in final_states:
                            actual_state.state = transition.goes_to
                            return True
                elif pilha.stack[-1] == transition.unstack:
                    pilha.stack.pop()
                    if transition.stack_up != epsilon:
                        pilha.stack.extend([item for item in transition.stack_up])
                    actual_state.state = transition.goes_to
                    return True
        return False

    for transition in estado_atual.transitions:
        if transition.letter == actual_letter:
            if epsilon == transition.unstack:
                if transition.stack_up != epsilon:
                    pilha.stack.extend([item for item in transition.stack_up])
                actual_state.state = transition.goes_to
                return True
            elif (len(pilha.stack) > 0) and (pilha.stack[-1] == transition.unstack):
                pilha.stack.pop()
                if transition.stack_up != epsilon:
                    pilha.stack.extend([item for item in transition.stack_up])
                actual_state.state = transition.goes_to
                return True
            elif transition.unstack == verifi and len(pilha.stack) == 0:
                if transition.stack_up != epsilon:
                    pilha.stack.extend([item for item in transition.stack_up])
                    actual_state.state = transition.goes_to
                    return True
    return False


def confirmating(all_states):
    """Confirmando autômato inserido"""
    print("Estados e suas transições")
    print("--------------------------------------")
    for state in all_states:
        if(len(state.transitions) == 0):
            print("Estado("+str(state.state).upper()+")")
            print("Este estado não possui nenhuma transição")
            print("--------------------------------------")
        else:
            print("Estado("+str(state.state).upper()+")")
            print("Transições:"+str(state.transitions) + ".")
            print("--------------------------------------")

def approving_words(all_states, final_states, actual_state, words_to_aprove, pilha, user_option):
    """Função dedicada á aprovação das palavras"""
    initial_state = actual_state.state
    print("-------------FITAS Á APROVAR-------------")
    for word in words_to_aprove:
        obj_word = Word(word)
        bck_word = word
        flag = True
        print(bck_word+": ")
        while flag:
            flag = calculate(all_states, final_states, actual_state, obj_word, pilha)
            printer(user_option, actual_state, pilha)

            
        if len(obj_word.word)==0 and len(pilha.stack) == 0 and actual_state.state in final_states:
            print(bck_word +" => FOI APROVADA !\n\n")
            actual_state.state = initial_state
            pilha.stack.clear()
        else:
            print(bck_word + " => ERROR::FITA NÃO APROVADA\n\n")
            actual_state.state = initial_state
            pilha.stack.clear()


def rejecting_words(all_states, final_states, actual_state, words_to_reject, pilha, user_option):
    """Função dedicada á reprovação das palavras"""
    initial_state = actual_state.state
    print("-------------FITAS Á REPROVAR-------------")
    for word in words_to_reject:
        obj = Word(word)
        backup = word
        flag = True
        print(backup+": ")
        while flag:
            flag =  calculate(all_states, final_states, actual_state, obj, pilha)
            printer(user_option, actual_state, pilha)
            
        
        if len(pilha.stack)!= 0 or len(obj.word)!=0 or not actual_state.state in final_states:
            print(backup +" => FOI REPROVADA!\n\n")
            actual_state.state = initial_state
            pilha.stack.clear()
        else:
            print(backup +" => ERROR::FITA NÃO REPROVADA\n\n")
            actual_state.state = initial_state
            pilha.stack.clear()

def printer(user_option, actual_state, pilha):
    """Printa as evoluções do automato"""
    if user_option == 0:
        print("Estado atual: "+ str(actual_state.state)+"; Situação da pilha: "+ str(pilha.stack))
    elif user_option == 1:
        print("Situação da pilha: "+str(pilha.stack))
    elif user_option == 2:
        print("Estado atual: "+ str(actual_state.state))
    
