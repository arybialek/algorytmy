
# Funkcje pomocnicze

import numpy as np
import os

def load_reference_set_from_file(filename):
    with open(filename, "r") as file:
        data = file.read()
        data = data.replace("\n","").split(" ")
        data = list(map(int, data))
        
    return data

def load_data_from_user():
    data = input("Prosze podac ciag odniesien (oddzielonych spacja): ")
    data = data.replace("\n", "").split(" ")
    data = list(map(int, data))
    
    num_frames = input("Prosze podac liczbe ramek: ")
    num_frames = num_frames.replace("\n", "")
    num_frames = int(num_frames)
    
    return data, num_frames

def save_to_file(output, filename):
    with open(filename, "w") as file:
        file.write(output) 
    
def generate_reference_set(set_size):
    return np.random.randint(0,10,size=set_size).tolist()



class Process():
    def __init__(self, number, priority, enter, duration):
        self.number = number
        self.priority = priority
        self.enter = enter
        self.duration = duration
        
        self.remaining_time = duration        
        self.being_executed = False
        
    def execute(self):
        self.remaining_time -= 1
        
        
def convert_to_objects(data_from_file):
    tasks = []
    
    for process in data_from_file:
        task = Process(process[0], process[1], process[2], process[3])
        tasks.append(task)
        
    return tasks

def load_tasks_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        del lines[-1]
        
        data = []
        for idx, line in enumerate(lines):
            lines[idx] = line.replace("\n", "")
            data.append(list(map(int, lines[idx].split(" "))))
            
    tasks = convert_to_objects(data)
    return tasks


# Program główny

import time

def application():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Algorytmy zastępowania stron.")
        print("2. Algorytmy szeregowania zadań.")
        print("3. Zakończ program.")
        program = int(input("> Wybierz jedną z opcji: "))
        
        if program is 1:
            print("Wybrano opcję nr 1.")
            time.sleep(1)
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("0. Wczytaj plik z danymi.")
                print("1. Algorytm FIFO.")
                print("2. Algorytm OPT.")
                print("3. Algorytm LRU.")
                print("4. Algorytm drugiej szansy (SCA).")
                print("5. Wróć.")
                choose = int(input("> Wybierz jedną z opcji: "))
                
                if choose is 0:
                    path = input("> Podaj ścieżkę do pliku: ")
                    data = load_reference_set_from_file(path)
                    _ = input("Wczytano dane z pliku. Naciśnij Enter, aby przejść do wyboru algorytmu.")
                elif choose is 1:
                    num_frames = int(input("Podaj liczbę ramek pamięci: "))
                    print("Efekt działania algorytmu FIFO: ")
                    output = FIFO(data, num_frames)
                    print(output)
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 2:
                    num_frames = int(input("Podaj liczbę ramek pamięci: "))
                    print("Efekt działania algorytmu OPT: ")
                    output = OPT(data, num_frames)
                    print(output)
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 3:
                    num_frames = int(input("Podaj liczbę ramek pamięci: "))
                    print("Efekt działania algorytmu LRU: ")
                    output = LRU(data, num_frames)
                    print(output)
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)                   
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 4:
                    num_frames = int(input("Podaj liczbę ramek pamięci: "))
                    print("Efekt działania algorytmu SCA: ")
                    output = SCA(data, num_frames)
                    print(output)
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 5:
                    break
                else:
                    print("Wybrano niepoprawną opcję. Proszę spróbować ponownie.")
            
        elif program is 2:
            print("Wybrano opcję nr 2.")
            time.sleep(1)
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("1. Algorytm FCFS z otwartą pulą zadań.")
                print("2. Algorytm SJF bez wywłaszczania z otwartą pulą zadań.")
                print("3. Algorytm SJF z wywłaszczaniem z otwartą pulą zadań.")
                print("4. Algorytm priorytetowy z postarzaniem procesów z otwartą pulą zadań.")
                print("5. Algorytm FCFS z zamkniętą pulą zadań.")
                print("6. Algorytm SJF bez wywłaszczania z zamkniętą pulą zadań.")
                print("7. Algorytm SJF z wywłaszczaniem z zamkniętą pulą zadań.")
                print("8. Algorytm priorytetowy z postarzaniem procesów z zamkniętą pulą zadań.")
                print("9. Wróć.")
                choose = int(input("> Wybierz algorytm, których chcesz przestestować: "))
                
                if choose is 1:
                    print("Efekt działania algorytmu FCFS: ")
                    output = FCFS_open()
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 2:
                    print("Efekt działania algorytmu SJF bez wywłaszczania: ")
                    output = SJF_nonpreemptive_open()
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 3:
                    print("Efekt działania algorytmu SJF z wywłaszczaniem: ")
                    output = SJF_preemptive_open()
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)                   
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 4:
                    print("Efekt działania algorytmu priorytetowego: ")
                    output = PRIORITY_preemptive_open()
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 5:
                    filename = input("> Podaj nazwę pliku z danymi wejściowymi: ")
                    tasks = load_tasks_from_file(filename)
                    print("Efekt działania algorytmu FCFS: ")
                    output = FCFS_closed(tasks)
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 6:
                    filename = input("> Podaj nazwę pliku z danymi wejściowymi: ")
                    tasks = load_tasks_from_file(filename)
                    print("Efekt działania algorytmu SJF bez wywłaszczania: ")
                    output = SJF_nonpreemptive_closed(tasks)
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 7:
                    filename = input("> Podaj nazwę pliku z danymi wejściowymi: ")
                    tasks = load_tasks_from_file(filename)
                    print("Efekt działania algorytmu SJF z wywłaszczaniem: ")
                    output = SJF_preemptive_closed(tasks)
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)                   
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 8:
                    filename = input("> Podaj nazwę pliku z danymi wejściowymi: ")
                    tasks = load_tasks_from_file(filename)
                    print("Efekt działania algorytmu priorytetowego: ")
                    output = PRIORITY_preemptive_closed(tasks)
                    output_file = input("> Podaj nazwę pliku wyjściowego z rezultatem działania: ")
                    save_to_file(output, output_file)
                    # podkreślnik oznacza zmienną, która nigdzie nie będzie zapamiętana (bo input() coś zwraca, a nas to nie interesuje)
                    _ = input("Naciśnij Enter, by wrócić do menu algorytmów zastępowania stron.")
                elif choose is 9:
                    break
                else:
                    print("Wybrano niepoprawną opcję. Proszę spróbować ponownie.")
            
        elif program is 3:
            break
        else:
            print("Wybrano niepoprawną opcję. Proszę spróbować ponownie.")


# Algorytmy stronicowania

def FIFO(input_set, num_frames): #input_set - lista
    output_string = ""
    frames = num_frames * [None]
    frames_changes = 0
    
    for element in input_set:
        
        if element in frames:
            output_string += "---\n"
            continue
        
        #poniższa pętla szuka wolnego miejsca w ramkach
        if None in frames:
            for idx, frame in enumerate(frames): #zwraca element frame i indeks(do modyfikacji ramek)
                if frame is None:
                    frames[idx] = element
                    frames_changes += 1
                    break
        
        else:
            del frames[0]
            frames.append(element)
            frames_changes += 1
        output_string += str(frames) + "\n"
        
    output_string += "Ilość zastąpień stron: " + str(frames_changes) + "\n"
    return output_string


def OPT(input_set, num_frames):
    output_string = ""
    frames = num_frames * [None]
    frames_changes = 0
    
    for el_idx, element in enumerate(input_set):
        
        if element in frames:
            output_string += "---\n"
            continue
            
        if None in frames:
            for idx, frame in enumerate(frames):
                if frame is None:
                    frames[idx] = element
                    frames_changes += 1
                    break
                    
        else:
            subset_to_check = input_set[el_idx+1:]
            
            oldest_idx = -1
            oldest_value = -1
            for frame in frames:
                if frame is not None:
                    try:
                        current_idx = subset_to_check.index(frame) #najwczesniejszy indeks sprawdzanej wartosci z ramki
                    except ValueError:
                        oldest_value = frame #sprawdzana wartoć nie istnieje w zbiorze sprawdzanych wartości, dlatego f-cja subset.. wyrzuca exception
                        break
                    else: #jeżeli jest wartość w zbiorze sprawdzanych wartości
                        if oldest_idx < current_idx:
                            oldest_idx = current_idx
                            oldest_value = subset_to_check[oldest_idx]
            
            frames[frames.index(oldest_value)] = element #sprawdzany jest idx wartości, która ma być nadpisana przez nowy proces
            frames_changes += 1
        
        output_string += str(frames) + "\n"
    
    output_string += "Ilość zastąpień stron: " + str(frames_changes) + "\n"
    return output_string

# Implementacja LRU za pomocą stosu
def LRU(input_set, num_frames):
    output_string = ""
    frames = num_frames * [None]
    frames_changes = 0
    
    # Pętla iterująca po kolejnych zadaniach umieszczanych w stronach pamięci
    for el_idx, element in enumerate(input_set):
        # Jeżeli proces jest już w pamięci, zostaw go tam i przejdź do następnego elementu
        if element in frames:
            # Usuń istniejące zadanie z ramek pamięci
            del frames[frames.index(element)] 
            
            # Umieść nowe zadanie na szczycie stosu (pierwsza ramka pamięci)
            frames = [element] + frames
            
            output_string += str(frames) + "\n"
            continue
            
        # Jeżeli są jeszcze puste ramki, wypełniaj je zadaniami (None są na górze stosu)
        if None in frames:
            for idx, frame in reversed(list(enumerate(frames))):
                if frame is None:
                    frames[idx] = element
                    frames_changes += 1
                    break
        else:
            # Przyszło nowe zadanie i nie ma już pustych ramek do wypełnienia
            
            # Usuń najdawniej używane zadanie (umieszczone na dnie stosu, stąd ostatni element z ramek usuwamy)
            del frames[-1]
            
            # Nowe zadanie na górze stosu
            frames = [element] + frames
            frames_changes += 1
            
        output_string += str(frames) + "\n"
    
    output_string += "Ilość zastąpień stron: " + str(frames_changes) + "\n"
    return output_string

def SCA(input_set, num_frames):
    output_string = ""
    frames = num_frames * [None]
    all_second_chance = False
    frames_changes = 0
    
    # Lista bitów odniesienia
    give_second_chance = [False] * num_frames
    
    print("[zawartość ramek pamięci] || [bit odniesienia]\n\n")
    for el_idx, element in enumerate(input_set):
         
        # Jeżeli element jest już w ramkach, to daj mu drugą szansę (ustawiając bit drugiej szansy na True)
        if element in frames:
            give_second_chance[frames.index(element)] = True            
            output_string += str(frames) + " || " + str(list(map(int, give_second_chance))) + "\n"       
            continue
            
        # Jeżeli są jeszcze puste ramki, wypełniaj je zadaniami (None są na górze stosu)
        if None in frames:
            for idx, frame in reversed(list(enumerate(frames))):
                if frame is None:
                    frames[idx] = element
                    frames_changes += 1
                    break
        else:
            # Jeżeli najstarsza ramka (dolna) jest False (nie ma danej drugiej szansy), to usuń ją i na szczycie FIFO daj nowe zadanie
            if give_second_chance[-1] is False:
                del frames[-1]
                frames = [element] + frames
                frames_changes += 1
            else:
                # Jeżeli najstarsza wg FIFO ramka ma drugą szansę, to usuń jej drugą szansę i szukaj dalej wolnego miejsca do zamiany
                give_second_chance[-1] = False
                
                # Sprawdzimy kolejne elementy (od najstarszego wg FIFO) - lecimy od tyłu listy, stąd ujemne indeksy
                idx_el_to_change = -2
                
                while True:
                    
                    # Ta sytuacja wystąpi tylko wtedy, gdy wszystkie zadania w ramkach mają drugą szansę. Wtedy przerywamy pętlę i wykona się
                    # kod od razu poza nią (# 2nd Chance)
                    if np.abs(idx_el_to_change) > num_frames:
                        all_second_chance = True
                        break
                        
                    if give_second_chance[idx_el_to_change] is False:
                        del frames[idx_el_to_change]
                        frames = [element] + frames
                        frames_changes += 1
                        break
                    else:
                        give_second_chance[idx_el_to_change] = False
                        idx_el_to_change -= 1
                
                # 2nd Chance
                if all_second_chance is True:
                    del frames[-1]
                    frames = [element] + frames
                    frames_changes += 1
                    
        output_string += str(frames) + " || " + str(list(map(int, give_second_chance))) + "\n"       
    
    output_string += "Ilość zastąpień stron: " + str(frames_changes) + "\n"
    return output_string


# Algorytmy szeregowania procesów z otwartą pulą zadań

import threading
import time as tm

def FCFS_open():
    num_processes = 0
    list_of_processes = []
    output = ""
    
    print("> Podaj bazową pulę procesów, która następnie może być poszerzana o procesy z otwartej puli zadań (po zakończeniu " + 
          "wprowadzania danych danego procesu wciśnij Enter, by zacząć wprowadzanie kolejnego procesu. q zakończy wprowadzanie procesów i uruchomi " +
          "algorytm) [priorytet][czas trwania]: ")
    
    while True:
        data = input()
        if data is "q":
            break
        else:
            num_processes += 1
            data = data.replace("\n", "").split(" ")
            data = list(map(int, data))
            process = Process(num_processes, data[0], 0, data[1])
            list_of_processes.append(process)
            
    user_input = [None]

    # Utwórz nowy wątek czekający na wejście użytkownika
    def get_user_input(user_input_ref):
        user_input_ref[0] = input("> Naciśnij p, aby spauzować działanie algorytmu i podać nowy proces.\n")

    mythread = threading.Thread(target=get_user_input, args=(user_input,))
    mythread.daemon = True
    mythread.start()
    
    time = 0
    
    # Ustaw procesy w kolejności wykonywania (wg czasu przyjścia)
    tasks = sorted(list_of_processes, key=lambda x: x.enter)    
    wait_time = [0] * len(tasks)
    
    print("[przedział czasu] || [nr procesu]\n")
    output += "[przedział czasu] || [nr procesu]\n"
    while len(tasks) > 0:
        
        if user_input[0] is "p":
            usr_input = input("> Podaj priorytet i czas trwania procesu: ")
            usr_input = usr_input.split(" ")
            usr_input = list(map(int, usr_input))
            num_processes += 1
            tasks.append(Process(num_processes, usr_input[0], time, usr_input[1]))
            wait_time.append(0)
            tasks = sorted(list_of_processes, key=lambda x: x.enter)
            user_input[0] = ""
                
        tasks[0].being_executed = True
        while tasks[0].remaining_time > 0:
            
            if user_input[0] is "p":
                usr_input = input("> Podaj priorytet i czas trwania procesu: ")
                usr_input = usr_input.split(" ")
                usr_input = list(map(int, usr_input))
                num_processes += 1
                tasks.append(Process(num_processes, usr_input[0], time, usr_input[1]))
                wait_time.append(0)
                user_input[0] = ""
            
            tasks[0].execute()
            time += 1
            print("[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[0].number) + "\n")
            output += "[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[0].number) + "\n"
            
            for task in tasks:
                if not task.being_executed and task.enter < time:
                    wait_time[task.number - 1] += 1  

            tm.sleep(1)
        
        del tasks[0]
        
    output += "Czas oczekiwania poszczególnych procesów: " + str(list(map(int, wait_time))) + "\n"
    output += "Średni czas oczekiwania: " + str(float(sum(wait_time) / num_processes)) + "\n"

    print("Naciśnij Enter, by zakończyć działanie programu...")
    mythread.join()
    
    return output

# SJF bez wywłaszczenia
def SJF_nonpreemptive_open():
    
    num_processes = 0
    list_of_processes = []
    output = ""
    
    print("> Podaj bazową pulę procesów, która następnie może być poszerzana o procesy z otwartej puli zadań (po zakończeniu " + 
          "wprowadzania danych danego procesu wciśnij Enter, by zacząć wprowadzanie kolejnego procesu. q zakończy wprowadzanie procesów i uruchomi " +
          "algorytm) [priorytet][czas trwania]: ")
    
    while True:
        data = input()
        if data is "q":
            break
        else:
            num_processes += 1
            data = data.replace("\n", "").split(" ")
            data = list(map(int, data))
            process = Process(num_processes, data[0], 0, data[1])
            list_of_processes.append(process)
            
    user_input = [None]

    # Utwórz nowy wątek czekający na wejście użytkownika
    def get_user_input(user_input_ref):
        user_input_ref[0] = input("> Naciśnij p, aby spauzować działanie algorytmu i podać nowy proces.\n")

    mythread = threading.Thread(target=get_user_input, args=(user_input,))
    mythread.daemon = True
    mythread.start()
    
    time = 0
    
    # Ustaw procesy wg czasu przyjścia
    tasks = sorted(list_of_processes, key=lambda x: x.enter)
    wait_time = [0] * len(tasks)
    
    print("[przedział czasu] || [nr procesu]\n")
    output += "[przedział czasu] || [nr procesu]\n"
    while len(tasks) > 0:
        
        if user_input[0] is "p":
            usr_input = input("> Podaj priorytet i czas trwania procesu: ")
            usr_input = usr_input.split(" ")
            usr_input = list(map(int, usr_input))
            num_processes += 1
            tasks.append(Process(num_processes, usr_input[0], time, usr_input[1]))
            wait_time.append(0)
            user_input[0] = ""
        
        ready_to_be_executed = []
        # Stwórz listę zadań, które mogą być już wykonywane (przyleciały)
        for task in tasks:
            if task.enter <= time and task.remaining_time > 0:
                ready_to_be_executed.append(task)
                
        # Posortuj 
        num_task_to_exec = sorted(ready_to_be_executed, key=lambda x: (x.duration, x.enter))[0].number
        idx = None
        
        for task_idx, task in enumerate(tasks):
            if task.number == num_task_to_exec:
                tasks[task_idx].being_executed = True
                idx = task_idx
                
        while tasks[idx].remaining_time > 0:
            if user_input[0] is "p":
                usr_input = input("> Podaj priorytet i czas trwania procesu: ")
                usr_input = usr_input.split(" ")
                usr_input = list(map(int, usr_input))
                num_processes += 1
                tasks.append(Process(num_processes, usr_input[0], time, usr_input[1]))
                wait_time.append(0)
                user_input[0] = ""
                
            tasks[idx].execute()
            time += 1
            print("[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n")
            output += "[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n"
            
            # Inkrementuj liczniki czekania zadań
            for task in tasks:
                if not task.being_executed and task.enter < time:
                    wait_time[task.number - 1] += 1
                    
            tm.sleep(1)
        
        del tasks[idx]
        
    output += "Czas oczekiwania poszczególnych procesów: " + str(list(map(int, wait_time))) + "\n"
    output += "Średni czas oczekiwania: " + str(float(sum(wait_time) / num_processes)) + "\n"

    print("Naciśnij Enter, by zakończyć działanie programu...")
    mythread.join()
    
    return output

# SJF z wywłaszczeniem
def SJF_preemptive_open():
    
    num_processes = 0
    list_of_processes = []
    alg_output = ""
    
    print("> Podaj bazową pulę procesów, która następnie może być poszerzana o procesy z otwartej puli zadań (po zakończeniu " + 
          "wprowadzania danych danego procesu wciśnij Enter, by zacząć wprowadzanie kolejnego procesu. q zakończy wprowadzanie procesów i uruchomi " +
          "algorytm) [priorytet][czas trwania]: ")
    
    while True:
        data = input()
        if data is "q":
            break
        else:
            num_processes += 1
            data = data.replace("\n", "").split(" ")
            data = list(map(int, data))
            process = Process(num_processes, data[0], 0, data[1])
            list_of_processes.append(process)
            
    user_input = [None]

    # Utwórz nowy wątek czekający na wejście użytkownika
    def get_user_input(user_input_ref):
        user_input_ref[0] = input("> Naciśnij p, aby spauzować działanie algorytmu i podać nowy proces.\n")

    mythread = threading.Thread(target=get_user_input, args=(user_input,))
    mythread.daemon = True
    mythread.start()
    
    time = 0
    
    # Ustaw procesy wg czasu przyjścia
    tasks = sorted(list_of_processes, key=lambda x: x.enter)
    wait_time = [0] * len(tasks)
    
    # Wykonuj pętlę, dopóki są zadania do wykonania
    print("[przedział czasu] || [nr procesu]\n")
    alg_output += "[przedział czasu] || [nr procesu]\n"
    while len(tasks) > 0:
        ready_to_be_executed = []
        
        if user_input[0] is "p":
            usr_input = input("> Podaj priorytet i czas trwania procesu: ")
            usr_input = usr_input.split(" ")
            usr_input = list(map(int, usr_input))
            num_processes += 1
            tasks.append(Process(num_processes, usr_input[0], time, usr_input[1]))
            wait_time.append(0)
            user_input[0] = ""

        # Stwórz listę zadań, które mogą być już wykonywane (przyleciały)
        for task in tasks:
            if task.enter <= time and task.remaining_time > 0:
                ready_to_be_executed.append(task)
                
        # Posortuj 
        sorted_tasks = sorted(ready_to_be_executed, key=lambda x: (x.duration, x.enter))
        num_task_to_exec = sorted_tasks[0].number
        idx = None
        output = ""
        for task in sorted_tasks:
            output += str(task.number) + " "
            
        print("Kolejka pozostałych procesów: " + output)
        alg_output += "Kolejka pozostałych procesów: " + output + "\n"
        
        if len(sorted_tasks) > 1:
            for task in sorted_tasks[1:]:
                wait_time[task.number - 1] += 1
        
        # Znajdź w liście tasks i oznacz aktualnie wykonywane zadanie jako being_executed, reszta jest False
        for task_idx, task in enumerate(tasks):
            tasks[task_idx].being_executed = False
            
            if task.number == num_task_to_exec:
                tasks[task_idx].being_executed = True
                idx = task_idx

        tasks[idx].execute()
        time += 1
        print("[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n")
        alg_output += "[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n"

        # Inkrementuj liczniki czekania zadań i usuń wykonane zadania
        for task_idx, task in enumerate(tasks):
            if task.remaining_time == 0:
                del tasks[task_idx]
                
        tm.sleep(1)
    
    alg_output += "Czas oczekiwania poszczególnych procesów: " + str(list(map(int, wait_time))) + "\n"
    alg_output += "Średni czas oczekiwania: " + str(float(sum(wait_time) / num_processes)) + "\n"

    print("Naciśnij Enter, by zakończyć działanie programu...")
    mythread.join()
    
    return alg_output

# priorytetowy z wywłaszczaniem
def PRIORITY_preemptive_open():
    
    num_processes = 0
    list_of_processes = []
    alg_output = ""
    
    print("> Podaj bazową pulę procesów, która następnie może być poszerzana o procesy z otwartej puli zadań (po zakończeniu " + 
          "wprowadzania danych danego procesu wciśnij Enter, by zacząć wprowadzanie kolejnego procesu. q zakończy wprowadzanie procesów i uruchomi " +
          "algorytm) [priorytet][czas trwania]: ")
    
    while True:
        data = input()
        if data is "q":
            break
        else:
            num_processes += 1
            data = data.replace("\n", "").split(" ")
            data = list(map(int, data))
            process = Process(num_processes, data[0], 0, data[1])
            list_of_processes.append(process)
            
    user_input = [None]

    # Utwórz nowy wątek czekający na wejście użytkownika
    def get_user_input(user_input_ref):
        user_input_ref[0] = input("> Naciśnij p, aby spauzować działanie algorytmu i podać nowy proces.\n")

    mythread = threading.Thread(target=get_user_input, args=(user_input,))
    mythread.daemon = True
    mythread.start()
    
    time = 0
    
    # Ustaw procesy wg czasu przyjścia
    tasks = sorted(list_of_processes, key=lambda x: x.enter)
    wait_time = [0] * len(tasks)
    finished = [False] * len(tasks)
    
    # Wykonuj pętlę, dopóki są zadania do wykonania
    loop = 1
    print("[kolejka procesów] # [priorytety]")
    print("[przedział czasu] || [nr procesu]\n")
    alg_output += "[kolejka procesów] # [priorytety]\n"
    alg_output += "[przedział czasu] || [nr procesu]\n"
          
    while len(tasks) > 0:
        ready_to_be_executed = []
        if user_input[0] is "p":
            usr_input = input("> Podaj priorytet i czas trwania procesu: ")
            usr_input = usr_input.split(" ")
            usr_input = list(map(int, usr_input))
            num_processes += 1
            tasks.append(Process(num_processes, usr_input[0], time, usr_input[1]))
            wait_time.append(0)
            finished.append(False)
            user_input[0] = ""

        # Stwórz listę zadań, które mogą być już wykonywane (przyleciały)
        for task in tasks:
            if task.enter <= time and task.remaining_time > 0:
                ready_to_be_executed.append(task)
                
        # Postarzenie procesu długo oczekującego
        if loop % 5 is 0:
            for task in ready_to_be_executed:
                if not finished[task.number - 1]:
                    if not task.priority is 1:
                        task.priority -= 1
                
        # Posortuj 
        sorted_tasks = sorted(ready_to_be_executed, key=lambda x: (x.priority, x.enter))
        num_task_to_exec = sorted_tasks[0].number
        idx = None
        output = ""
        priorities = ""
        for task in sorted_tasks:
            output += str(task.number) + " "
            priorities += str(task.priority) + " "
            
        print(output + " # " + priorities)
        
        if len(sorted_tasks) > 1:
            for task in sorted_tasks[1:]:
                wait_time[task.number - 1] += 1
        
        # Znajdź w liście tasks i oznacz aktualnie wykonywane zadanie jako being_executed, reszta jest False
        for task_idx, task in enumerate(tasks):
            tasks[task_idx].being_executed = False
            
            if task.number == num_task_to_exec:
                tasks[task_idx].being_executed = True
                idx = task_idx

        tasks[idx].execute()
        time += 1
        print("[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n")
        alg_output += "[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n"
                       
        # Inkrementuj liczniki czekania zadań i usuń wykonane zadania
        for task_idx, task in enumerate(tasks):
            if task.remaining_time == 0:
                finished[task.number - 1] = True
                del tasks[task_idx]
                
        tm.sleep(1)
        loop += 1
    
    alg_output += "Czas oczekiwania poszczególnych procesów: " + str(list(map(int, wait_time))) + "\n"
    alg_output += "Średni czas oczekiwania: " + str(float(sum(wait_time) / num_processes)) + "\n"

    print("Naciśnij Enter, by zakończyć działanie programu...")
    mythread.join()
    
    return alg_output


# Algorytmy szeregowania dla zamkniętej puli zadań

def FCFS_closed(list_of_processes):
    
    time = 0
    output = ""
    num_processes = len(list_of_processes)
    
    # Ustaw procesy w kolejności wykonywania (wg czasu przyjścia)
    tasks = sorted(list_of_processes, key=lambda x: x.enter)    
    wait_time = [0] * len(tasks)
    
    print("[przedział czasu] || [nr procesu]\n")
    output += "[przedział czasu] || [nr procesu]\n"
    while len(tasks) > 0:
                
        tasks[0].being_executed = True
        while tasks[0].remaining_time > 0:
            print(str(time + 1) + " | " + str(tasks[0].number))

            tasks[0].execute()
            time += 1
            print("[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[0].number) + "\n")
            output += "[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[0].number) + "\n"
            
            for task in tasks:
                if not task.being_executed and task.enter < time:
                    wait_time[task.number - 1] += 1  
        
        del tasks[0]
        
    output += "Czas oczekiwania poszczególnych procesów: " + str(list(map(int, wait_time))) + "\n"
    output += "Średni czas oczekiwania: " + str(float(sum(wait_time) / num_processes)) + "\n"
    
    return output
        
# SJF bez wywłaszczenia
def SJF_nonpreemptive_closed(list_of_processes):
    
    time = 0
    output = ""
    num_processes = len(list_of_processes)
    
    # Ustaw procesy wg czasu przyjścia
    tasks = sorted(list_of_processes, key=lambda x: x.enter)
    wait_time = [0] * len(tasks)
    
    print("[przedział czasu] || [nr procesu]\n")
    output += "[przedział czasu] || [nr procesu]\n"
    while len(tasks) > 0:
        

        ready_to_be_executed = []
        # Stwórz listę zadań, które mogą być już wykonywane (przyleciały)
        for task in tasks:
            if task.enter <= time and task.remaining_time > 0:
                ready_to_be_executed.append(task)
                
        # Posortuj 
        num_task_to_exec = sorted(ready_to_be_executed, key=lambda x: (x.duration, x.enter))[0].number
        idx = None
        
        for task_idx, task in enumerate(tasks):
            if task.number == num_task_to_exec:
                tasks[task_idx].being_executed = True
                idx = task_idx
                
        while tasks[idx].remaining_time > 0:
            print(str(time) + " | " + str(tasks[idx].number))

            tasks[idx].execute()
            time += 1
            print("[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n")
            output += "[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n"

            # Inkrementuj liczniki czekania zadań
            for task in tasks:
                if not task.being_executed and task.enter < time:
                    wait_time[task.number - 1] += 1
        
        del tasks[idx]
        
    output += "Czas oczekiwania poszczególnych procesów: " + str(list(map(int, wait_time))) + "\n"
    output += "Średni czas oczekiwania: " + str(float(sum(wait_time) / num_processes)) + "\n"
    
    return output

# SJF z wywłaszczeniem
def SJF_preemptive_closed(list_of_processes):
    
    time = 0
    alg_output = ""
    num_processes = len(list_of_processes)
    
    # Ustaw procesy wg czasu przyjścia
    tasks = sorted(list_of_processes, key=lambda x: x.enter)
    wait_time = [0] * len(tasks)
    
    # Wykonuj pętlę, dopóki są zadania do wykonania
    print("[przedział czasu] || [nr procesu]\n")
    alg_output += "[przedział czasu] || [nr procesu]\n"
    while len(tasks) > 0:
        ready_to_be_executed = []

        # Stwórz listę zadań, które mogą być już wykonywane (przyleciały)
        for task in tasks:
            if task.enter <= time and task.remaining_time > 0:
                ready_to_be_executed.append(task)
                
        # Posortuj 
        sorted_tasks = sorted(ready_to_be_executed, key=lambda x: (x.duration, x.enter))
        num_task_to_exec = sorted_tasks[0].number
        idx = None
        output = ""
        for task in sorted_tasks:
            output += str(task.number) + " "
            
        print("Kolejka pozostałych procesów: " + output)
        alg_output += "Kolejka pozostałych procesów: " + output + "\n"
        
        if len(sorted_tasks) > 1:
            for task in sorted_tasks[1:]:
                wait_time[task.number - 1] += 1
        
        # Znajdź w liście tasks i oznacz aktualnie wykonywane zadanie jako being_executed, reszta jest False
        for task_idx, task in enumerate(tasks):
            tasks[task_idx].being_executed = False
            
            if task.number == num_task_to_exec:
                tasks[task_idx].being_executed = True
                idx = task_idx

        tasks[idx].execute()
        time += 1
        print("[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n")
        alg_output += "[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n"

        # Inkrementuj liczniki czekania zadań i usuń wykonane zadania
        for task_idx, task in enumerate(tasks):
            if task.remaining_time == 0:
                del tasks[task_idx]
    
    alg_output += "Czas oczekiwania poszczególnych procesów: " + str(list(map(int, wait_time))) + "\n"
    alg_output += "Średni czas oczekiwania: " + str(float(sum(wait_time) / num_processes)) + "\n"
    
    return alg_output

# priorytetowy z wywłaszczaniem
def PRIORITY_preemptive_closed(list_of_processes):
    
    time = 0
    alg_output = ""
    num_processes = len(list_of_processes)
    
    # Ustaw procesy wg czasu przyjścia
    tasks = sorted(list_of_processes, key=lambda x: x.enter)
    wait_time = [0] * len(tasks)
    finished = [False] * len(tasks)
    
    # Wykonuj pętlę, dopóki są zadania do wykonania
    loop = 1
    print("[kolejka procesów] # [priorytety]")
    print("[przedział czasu] || [nr procesu]\n")
    alg_output += "[kolejka procesów] # [priorytety]\n"
    alg_output += "[przedział czasu] || [nr procesu]\n"
    while len(tasks) > 0:
        ready_to_be_executed = []

        # Stwórz listę zadań, które mogą być już wykonywane (przyleciały)
        for task in tasks:
            if task.enter <= time and task.remaining_time > 0:
                ready_to_be_executed.append(task)
                
        # Postarzenie procesu długo oczekującego
        if loop % 5 is 0:
            for task in ready_to_be_executed:
                if not finished[task.number - 1]:
                    if not task.priority is 1:
                        task.priority -= 1
                
        # Posortuj 
        sorted_tasks = sorted(ready_to_be_executed, key=lambda x: (x.priority, x.enter))
        num_task_to_exec = sorted_tasks[0].number
        idx = None
        output = ""
        priorities = ""
        for task in sorted_tasks:
            output += str(task.number) + " "
            priorities += str(task.priority) + " "
            
        print(output + " # " + priorities)
        
        if len(sorted_tasks) > 1:
            for task in sorted_tasks[1:]:
                wait_time[task.number - 1] += 1
        
        # Znajdź w liście tasks i oznacz aktualnie wykonywane zadanie jako being_executed, reszta jest False
        for task_idx, task in enumerate(tasks):
            tasks[task_idx].being_executed = False
            
            if task.number == num_task_to_exec:
                tasks[task_idx].being_executed = True
                idx = task_idx

        tasks[idx].execute()
        time += 1
        print("[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n")
        alg_output += "[" + str(time - 1) + "-" + str(time) + "]" + " || " + str(tasks[idx].number) + "\n"

        # Inkrementuj liczniki czekania zadań i usuń wykonane zadania
        for task_idx, task in enumerate(tasks):
            if task.remaining_time == 0:
                finished[task.number - 1] = True
                del tasks[task_idx]
                
        loop += 1
    
    alg_output += "Czas oczekiwania poszczególnych procesów: " + str(list(map(int, wait_time))) + "\n"
    alg_output += "Średni czas oczekiwania: " + str(float(sum(wait_time) / num_processes)) + "\n"
    
    return alg_output


application()
