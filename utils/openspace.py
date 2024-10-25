from utils.table import Table
import random
import pandas as pd


class Openspace:

    def __init__(self, number_of_tables):
        numberofseatspertable = 4 # Aqui se asigna la capacidad de todas las mesas
        self.tables = []
        self.number_of_tables = number_of_tables
        for i in range(number_of_tables):
            self.tables.append(Table(numberofseatspertable))# se crea una lista dinamica de objetos mesas

    def organize(self, names):
        random_number_of_table = random.randint(0, self.number_of_tables-1)

        for tempname in names: #se recorre la lista de nombres names que viene de main.py
            fulltablecounter = 0
            while fulltablecounter < self.number_of_tables:# While que se ejecuta hasta que las capacidades se acaben
                if self.tables[random_number_of_table].has_free_spot() is True:
                    self.tables[random_number_of_table].assign_seat(tempname)
                    random_number_of_table = random.randint(0, self.number_of_tables-1)
                    fulltablecounter = self.number_of_tables #Si un nombre encuentra un espacio libre se fuerza la terminacion del while
                else:
                    random_number_of_table = random.randint(0, self.number_of_tables-1)
                    fulltablecounter+=1# incrementar cada vez que encuentre una mesa llena
    def display(self):

        for i in range(self.number_of_tables):# se recorre un loop tantas veces como mesas se creen
            print(f"Table: {i+1}\t")#Iterador para imprimir el numero de la tabla
            self.tables[i].print_everything()#imprime los nombres sentados en esa mesa

    def store(self):
     row = []
     rows =[]

     for j in range(self.number_of_tables):
        row.append(f"Table: {j+1}")
        for i in range(self.tables[1].capacity):# se pone el iterador fijo porque todas las mesas tienen la misma cantidad de asientos
            row.append(self.tables[j].seats[i].occupant)
        rows.append(row)# se guarda la lista en la lista de listas
        row=[]#Vuelve la lista row que se usa para cada fila una lista vacia
     print(rows)
     df1 = pd.DataFrame(rows)# se convierte la lista de listas en Dataframe
     df1.to_excel('TablesDistribution.xlsx',index=False)

