import datetime

def verificar_data(data):
    try:
        #para converter a string em datetime
        data_formatada = datetime.strptime(data, "%d/%m/%Y")
        print("A data é válida:", data_formatada.strftime("%d/%m/%Y"))
    except ValueError:
        print("Data inválida. Verifique se o formato é dd/mm/yyyy e se a data existe.")

#solicita que insira uma data
data = input("Digite uma data no formato dd/mm/yyyy: ")

#verificar se a data é válida
verificar_data(data)



    