# cargar el archivo fasta de "Bacillus halodurans" para su lectura

B_halodurans_gene_set = set()  # definir el set
B_halodurans_gene_list = list()  # definir la lista otra manera mas profecional = []


with open("Bacillus_halodurans.gb") as file:
    for lines in file:
        if "/gene=" in lines:  # catura las filas que contengan /gene=
            line = lines.strip()  # junta los genes, sin espacio entre lineas
            gene_name = line[7:-1]  # catura solo los nombres de los genes
            #print(lines)
            #print(line)
            #print(gene_name)
            B_halodurans_gene_set.add(gene_name)  # guarda los genes en el set
            B_halodurans_gene_list.append(gene_name)  # guarda los genes en la lista
    pass



# cargar el archivo fasta de "Bacillus halodurans" para su lectura

B_subtilis_gene_set = set()  # definir el set
B_subtilis_gene_list = list()  # definir la lista otra manera mas profecional = []

with open("Bacillus_subtilis.gb") as file:
    for lines in file:
        if "/gene=" in lines:  # catura las filas que contengan /gene=
            line = lines.strip()  # junta los genes, sin espacio entre lineas
            gene_name = line[7:-1]  # catura solo los nombres de los genes
            #print(lines)
            #print(line)
            #print(gene_name)
            B_subtilis_gene_set.add(gene_name)  # guarda los genes en el set
            B_subtilis_gene_list.append(gene_name)  # guarda los genes en la lista
    pass




# Para calcular la diferencia de genes existentes entre Bacillus halodurans y  Bacillus thuringiensis

gene_diferent_halodurans_subtilis = []
for element in B_halodurans_gene_set:
    if element not in B_subtilis_gene_set:
        gene_diferent_halodurans_subtilis.append(element)
print("Genes presentes en B. halodurans y no en B. subtilis :", gene_diferent_halodurans_subtilis)
pass



# Para encontrar los genes en comun que comparten Bacillus halodurans y  Bacillus thuringiensis

gene_equals_halodurans_subtilis_list = []  # Inicializar una lista vacía
gene_equals_halodurans_subtilis_set = set()  # Inicializar un set vacío

for genes in B_halodurans_gene_set:  # indica los genes que comparten B_halodurans y B_subtilis
    if genes in B_subtilis_gene_set:
        gene_equals_halodurans_subtilis_list.append(genes)  # crear la lista de genes que comparten
        gene_equals_halodurans_subtilis_set.add(genes)  # crear set de genes que comparten
print("Genes que comparten B. halodurans y B. subtilis :", gene_equals_halodurans_subtilis_set)
pass




# para ver si  el codigo funciona,
# se comprovo mediante genes que comparten en comun y genes que no comparten,
# reportados en la literatura, Articulo https://doi.org/10.1093/nar/28.21.4317

# genes de esporulacion presentes solo en B_sutilis: rapA, rapK, phrA, phrC, phrE, phrG, phrI y phrK
# genes relacionados con la biosíntesis de peptidoglicanos que comparten ambas bactarias:  mraY, murC, murG, cwlA, ddlA y glnA

gene_coresponde = "rapA"  # para buscar el gen, para ver si lo comparten o no.

if gene_coresponde in B_halodurans_gene_set:
    print(f"{gene_coresponde}, corresponde a B_halodurans")
else:
    print(f"{gene_coresponde}, no corresponde a B_halodurans")

if gene_coresponde in B_subtilis_gene_set:
    print(f"{gene_coresponde}, corresponde a B_subtilis")
else:
    print(f"{gene_coresponde}, no corresponde a B_subtilis")










