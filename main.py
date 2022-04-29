import os


# os.getcwd() = get current working directory

def file_size(cartella=os.getcwd()):
    totale = 0
    for file in os.listdir(cartella):
        totale += os.path.getsize(os.path.join(cartella, file))
        print("La dimensione è "+str(totale/1e6)+" MB")

file_size()