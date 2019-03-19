#par false para impar,true para par
def calcular_hamming(binario,par):
    index = 0
    binario_ham = []
    binario_ham.append("0")
    binario_ham.append("0")
    while index!=12:
        if(index==1or index==4 or index==11):
            binario_ham.append("0")
        binario_ham.append(binario[index])
        index+=1
    return calculo_hamming(binario_ham,par)
def calculo_hamming(binario,par):
    binario[0] = calcular_p1(binario,par)
    binario[1] = calcular_p2(binario,par)
    binario[3] = calcular_p3(binario,par)
    binario[7] = calcular_p4(binario,par)
    binario[15]=calcular_p5(binario,par)
    return binario
def calcular_p1(binario,par):
    index =0
    valor = 0
    while(index<len(binario)):
        valor = valor+int(binario[index])
        index+=2
    if (valor % 2 == 0):
        if (par):
            return "0"
        else:
            return "1"
    else:
        if (par):
            return "1"
        else:
            return "0"
def calcular_p2(binario,par):
    index = 1
    valor = 0
    while index< len(binario):
        valor = valor + int(binario[index]) +int(binario[index+1])
        index+=4
    if (valor % 2 == 0):
        if (par):
            return "0"
        else:
            return "1"
    else:
        if (par):

            return "1"
        else:
            return "0"
def calcular_p3(binario,par):
    valor =  int(binario[3]) +int(binario[4])+int(binario[5])+ int(binario[6])+int(binario[9])+int(binario[11]) +int(binario[12])+int(binario[13])+int(binario[14])
    if (valor % 2 == 0):
        if (par):
            return "0"
        else:
            return "1"
    else:
        if (par):
            return "1"
        else:
            return "0"

def calcular_p4(binario, par):
    valor =  int(binario[7]) +int(binario[8])+int(binario[9]) +int(binario[10])+int(binario[11])+int(binario[12])+int(binario[13])+int(binario[14])
    if (valor % 2 == 0):
        if (par):
            return "0"
        else:
            return "1"
    else:
        if (par):
            return "1"
        else:
            return "0"
def calcular_p5(binario,par):
    valor = int(binario[len(binario)-1])
    if (valor % 2 == 0):
        if (par):
            return "0"
        else:
            return "1"
    else:
        if (par):
            return "1"
        else:
            return "0"
calcular_hamming("100110110110",True)
#calcular_hamming("100110110110",False)
def arreglar_hamming(binario,par):
    if(par):
        return arreglar_hamming_par(binario)
    else:
       return arreglar_hamming_impar(binario)

def arreglar_hamming_par(binario):
    conteo_error = 0
    lista_errores = []
    indice = 0
    binario_ham = []
    while indice<17:
        if (indice==0 or indice==1 or indice == 3 or indice == 7 or indice == 15):
            binario_ham.append("0")
        else:
            binario_ham.append(binario[indice])
        indice += 1
    p1=binario[0] != calcular_p1(binario_ham, True)
    p2=binario[1] != calcular_p2(binario_ham, True)
    p3=binario[3] != calcular_p3(binario_ham, True)
    p4=binario[7] !=calcular_p4(binario_ham, True)
    p5 = binario[15]!=calcular_p5(binario_ham,True)
    if(p1):
        lista_errores.append(1)
        conteo_error= conteo_error+1
    if (p2):
        lista_errores.append(2)
        conteo_error = conteo_error + 2
    if(p3):
        lista_errores.append(3)
        conteo_error = conteo_error + 4
    if(p4):
        lista_errores.append(4)
        conteo_error = conteo_error + 8
    if(p5):
        lista_errores.append(5)
        conteo_error = conteo_error + 16
    if(not p1 and not p2 and not p3 and not p4 and not p5):
        return(binario,"No hubo error alguno")
    if (p1 or p2 or p3 or p4 or p5):
        x=binario[conteo_error-1]
        if(binario[conteo_error-1]=="1"):
            binario[conteo_error-1]="0"
            return [binario, "Hubo un error en el bit", conteo_error,lista_errores]
        else:
            binario[conteo_error-1]="1"
            return [binario, "Hubo un error en el bit", conteo_error,lista_errores]

def arreglar_hamming_impar(binario):
    print("NOPAR")
    conteo_error = 0
    lista_errores = []
    indice = 0
    binario_ham = []
    while indice < 17:
        if (indice == 0 or indice == 1 or indice == 3 or indice == 7 or indice == 15):
            binario_ham.append("0")
        else:
            binario_ham.append(binario[indice])
        indice += 1
    p1 = binario[0] != calcular_p1(binario_ham, False)
    p2 = binario[1] != calcular_p2(binario_ham, False)
    p3 = binario[3] != calcular_p3(binario_ham, False)
    p4 = binario[7] != calcular_p4(binario_ham, False)
    p5 = binario[15] != calcular_p5(binario_ham, False)
    print([p1, p2, p3, p4, p5])
    if (p1):
        conteo_error = conteo_error + 1
        lista_errores.append(1)
    if (p2):
        conteo_error = conteo_error + 2
        lista_errores.append(2)
    if (p3):
        conteo_error = conteo_error + 4
        lista_errores.append(3)
    if (p4):
        conteo_error = conteo_error + 8
        lista_errores.append(4)
    if (p5):
        lista_errores.append(5)
        conteo_error = conteo_error + 16
    if (not p1 and not p2 and not p3 and not p4 and not p5):
        return (binario, "Nu hubo error alguno")
    if (p1 or p2 or p3 or p4 or p5):
        x = binario[conteo_error - 1]
        if (binario[conteo_error - 1] == "1"):
            binario[conteo_error - 1] = "0"
            return [binario, "Hubo un error en el bit", conteo_error,lista_errores]
        else:
            binario[conteo_error - 1] = "1"
            return [binario, "Hubo un error en el bit", conteo_error,lista_errores]


