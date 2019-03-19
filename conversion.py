
def binarioDeci(num):
    n=len(str(num))-1
    i=0
    tot=0
    while i<=len(str(num))-1:
        result=int(str(num)[i])*(2**n)
        n=n-1
        i=i+1
        tot=tot+result
    return tot

def deciBCD (decimal):
    BCDtot=''
    i=0
    while i<len(str(decimal)):
        numero=int(str(decimal)[i])
        BCDinv=''
        BCD=''
        flag=True
        if numero==1: #si es un 1 lo agrega directamente a la variable inversa
            BCDinv=BCDinv+str(numero)
        else:
            while flag:  #realiza las divisiones hasta que el resultado sea 1 y agrega los residuos a la variable
                binari=str(numero%2)
                numero=numero//2
                BCDinv=BCDinv+binari
                if numero==1 or numero == 0:
                    BCDinv=BCDinv+str(numero)
                    flag=False
        if len(BCDinv)<4: #si se guardan menos de 4 números, rellena con ceros
            while len(BCDinv)<4:
                BCDinv=BCDinv+'0'
        n=len(BCDinv)-1
        while n>=0: # invierte la variable 
            BCD=BCD+BCDinv[n]
            n=n-1
        BCDtot=BCDtot+BCD
        i+=1
    return BCDtot
              
def binahexa(binario):
    strnumero=''
    hexatot=''
    i=0
    while i<len(str(binario)):
        strnumero=strnumero+str(binario)[i] 
        if (i+1)%4==0: #se agregan número hasta que hayan 4 bits en la variable
            numero=int(strnumero)
            deci=binarioDeci(numero) #se convierte ese número binario a decimal
            if deci<=9:
                hexatot=hexatot+str(deci)
            else:
                if deci==10:
                    hexatot=hexatot+'A'
                elif deci==11:
                    hexatot=hexatot+'B'
                elif deci==12:
                    hexatot=hexatot+'C'
                elif deci==13:
                    hexatot=hexatot+'D'
                elif deci==14:
                    hexatot=hexatot+'E'
                elif deci==15:
                    hexatot=hexatot+'F'                  
            strnumero=''                  
        i+=1      
    return hexatot