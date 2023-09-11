# cargar el archivo fasta de "Bacilus halodurans" para su lectura

with open("Bacillus_halodurans.fasta", "r") as file:

    B_halodurans_gene_names_list = list()  # Inicializar una lista vacía para almacenar los nombres de los genes
    B_halodurans_gene_names_set = set()  # Inicializar un set  vacio para almacenar los nombres de los genes

    for line in file:
        if line.startswith(">"):  # Caturar solo línea cabecera de secuencia que inicia >
            temp = line.split()  # Dividir la línea de cabecera por espacios en blanco
            gene_name = temp[1]  # Seleccionar la posicion donde estan los genes
            gene_name = gene_name.replace("[gene=", "").rstrip("]")  # Seleccionar solo los nombres de los genes
            B_halodurans_gene_names_set.add(gene_name)  # Añadir los genes a un set
            B_halodurans_gene_names_list.append(gene_name)  # Añadir los genes a una lista
            print(B_halodurans_gene_names_set)  # imprimir los genes del set
            print(B_halodurans_gene_names_list)  # imprimir los genes de la lista
    pass

###################

# cargar el archivo fasta de "Bacilus subtilis" para su lectura

with open("Bacillus_subtilis.fasta", "r") as file:

    B_subtilis_gene_names_list = list()  # Inicializar una lista vacía para almacenar los nombres de los genes
    B_subtilis_gene_names_set = set()  # Inicializar un set  vacio para almacenar los nombres de los genes

    for line in file:
        if line.startswith(">"):  # Caturar solo línea cabecera de secuencia que inicia >
            temp = line.split()  # Dividir la línea de cabecera por espacios en blanco
            gene_name = temp[1]  # Seleccionar la posicion donde estan los genes
            gene_name = gene_name.replace("[gene=", "").rstrip("]")  # Seleccionar solo los nombres de los genes
            B_subtilis_gene_names_set.add(gene_name)  # Añadir los genes a un set
            B_subtilis_gene_names_list.append(gene_name)  # Añadir los genes a una lista
            print(B_subtilis_gene_names_set)  # imprimir los genes del set
            print(B_subtilis_gene_names_list)  # imprimir los genes de la list
    pass


######################################################################################################

# Para calcular la diferencia de genes

# genes presentes solo en Bacillus halodurans
genes_diferent_halodurans_set = set()
genes_diferent_halodurans_list = []

for element in B_halodurans_gene_names_set:
    if element not in B_subtilis_gene_names_set:
        genes_diferent_halodurans_set.add(element)
        genes_diferent_halodurans_list.append(element)
print("Genes presentes solo  B. halodurans:", genes_diferent_halodurans_set)
pass

######################################################################################################

# genes presentes solo en Bacillus subtilis
genes_diferent_subtilis_set = set()
genes_diferent_subtilis_list = []

for element in B_subtilis_gene_names_set:
    if element not in B_halodurans_gene_names_set:
        genes_diferent_subtilis_set.add(element)
        genes_diferent_subtilis_list.append(element)
print("Genes presentes solo  B. subtilis:", genes_diferent_subtilis_set)
pass


######################################################################################################

# Para encontrar los genes en comun que comparten Bacillus halodurans y  Bacillus thuringiensis

gene_equals_halodurans_subtilis_list = []  # Inicializar una lista vacía
gene_equals_halodurans_subtilis_set = set()  # Inicializar un set vacío

for genes in B_halodurans_gene_names_set:  # indica los genes que comparten B_halodurans y B_subtilis
    if genes in B_subtilis_gene_names_set:
        gene_equals_halodurans_subtilis_list.append(genes)  # crear la lista de genes que comparten
        gene_equals_halodurans_subtilis_set.add(genes)  # crear set de genes que comparten
print("Genes que comparten B. halodurans y B. subtilis :", gene_equals_halodurans_subtilis_set)
pass

# genes_en_comun = set(B_halodurans_gene_names_set).intersection(set(B_subtilis_gene_names_set))
# print(list(genes_en_comun))


#######################################################################################################

# para ver si  el codigo funciona,
# se comprovo mediante genes que comparten en comun y genes que no comparten,
# reportados en la literatura, Articulo https://doi.org/10.1093/nar/28.21.4317

# genes de esporulacion presentes solo en B_sutilis: rapA, rapK, phrA, phrC, phrE, phrG, phrI y phrK
# genes relacionados con la biosíntesis de peptidoglicanos que comparten ambas bactarias:  mraY, murC, murG, cwlA, ddlA y glnA


gene_coresponde = "rapA"  # para buscar el gen, para ver si lo comparten o no.

if gene_coresponde in B_halodurans_gene_names_set:
    print(f"{gene_coresponde}, corresponde a B_halodurans")
else:
    print(f"{gene_coresponde}, no corresponde a B_halodurans")

if gene_coresponde in B_subtilis_gene_names_set:
    print(f"{gene_coresponde}, corresponde a B_subtilis")
else:
    print(f"{gene_coresponde}, no corresponde a B_subtilis")


