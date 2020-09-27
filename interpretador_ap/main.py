import automaton as atm
import functions as fnc

epsilon = "&"
verifi = "?"

arq = fnc.open_json()  # abre arquivo
pilha = atm.Pilha()  # criando pilha do automato
words_to_aprove = arq.get("aprovar")  # lote de palavras para aprovar
words_to_reject = arq.get("rejeitar")  # lote de palavras para rejeitar
init_state = arq.get("init_state")  # estado inicial
final_states = arq.get("final_states")  # estados finais
actual_state = atm.CurrentState(init_state)
mostrar_pilha = arq.get("mostrar_pilha")
evolucao_estados = arq.get("evolucao_estados")

all_states = []
for state_item in arq["all_states"]:
    transitions = []
    for transition_item in state_item.get("transitions"):
        transition = atm.Transition(transition_item.get("letter"), transition_item.get(
            "unstack"), transition_item.get("stack_up"), transition_item.get("goes_to"))
        transitions.append(transition)
    state = atm.State(state_item.get("state"), transitions)
    all_states.append(state)


if mostrar_pilha == "True" and evolucao_estados== "True":
    user_option = 0
elif mostrar_pilha == "True" and evolucao_estados == "False":
    user_option = 1
elif mostrar_pilha == "False" and evolucao_estados =="True":
    user_option = 2
elif mostrar_pilha == "False" and evolucao_estados == "False":
    user_option = 3

fnc.approving_words(all_states, final_states, actual_state,
                    words_to_aprove, pilha, user_option)

fnc.rejecting_words(all_states, final_states, actual_state,
                    words_to_reject, pilha, user_option)
