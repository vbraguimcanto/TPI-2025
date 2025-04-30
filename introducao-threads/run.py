import threading
import time

def tarefa_1(nome, tempo):
    print(f"[{nome}] Iniciando Tarefa...")
    time.sleep(tempo)
    print(f"[{nome}] Finalizado após {tempo} segundos.")

def tarefa_2(nome, tempo):
    print(f"[{nome}] Iniciando Tarefa...")
    time.sleep(tempo)
    print(f"[{nome}] Finalizado após {tempo} segundos.")

thread1 = threading.Thread(target=tarefa_1, args=("Thread-1", 5))
thread2 = threading.Thread(target=tarefa_2, args=("Thread-2", 50))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Todas as threads foram finalizadas.")