from Clases.Nodo import *

def getTmp():
    getTmp.var+=1
    return "t"+str(getTmp.var)
getTmp.var=0

def getEtq():
    getEtq.var+=1
    return "L"+str(getEtq.var)
getEtq.var=0

reservadas = {
    'nada' : 'Nada',
    'if' : 'If',
    'else' : 'Else',
    'true' : 'True',
    'false' : 'False'
}

tokens  = [
    'mas',
    'menos',
    'div',
    'por',
    'parA',
    'parC',
    'llavA',
    'llavC',
    'and',
    'or',
    'not',
    'igualdad',
    'diferente',
    'mayor',
    'menor',    
    'numero',
    'id'
] + list(reservadas.values())

# Tokens
t_mas = r'\+'
t_menos = r'-'
t_div = r'/'
t_por = r'\*'
t_parA = r'\('
t_parC = r'\)'
t_llavA = r'{'
t_llavC = r'}'
t_and = r'&&'
t_or = r'\|\|'
t_not = r'!'
t_igualdad = r'=='
t_diferente = r'<>'
t_mayor = r'>'
t_menor = r'<'
t_numero = r'[0-9]+'
# Caracteres ignorados
t_ignore = " \t"

def t_id(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'id')
     return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left','or'),
    ('left','and'),
    ('left','not'),
    ('left','igualdad','diferente'),
    ('left','mayor','menor'),
    ('left','mas','menos'),
    ('left','por','div'),        
    )

# Definición de la gramática

def p_incio(t):
    '''INI    : INSTRUCCIONES '''
    ls=t[1]
    for i in ls:
            print(i.getCodigo())

def p_lsInstrucciones(t):
    '''INSTRUCCIONES    : INSTRUCCIONES INSTRUCCION
                      | INSTRUCCION '''
    if len(t)==3:
        ls=t[1]
        ls.append(t[2])
        t[0]=ls
    else:         
        ls=[t[1]]
        t[0]=ls                                                 

def p_instrucciones(t):
    ''' INSTRUCCION : If parA S parC llavA INSTRUCCIONES llavC
                    | If parA S parC llavA INSTRUCCIONES llavC Else llavA INSTRUCCIONES llavC
                    | Nada '''
    if len(t)==8:
        nExp:Nodo=t[3]
        n=Nodo()
        n.cod+=nExp.getCodigo()
        n.cod+=nExp.getEtqV()+":\n"
        ls1=t[6]
        for i in ls1:
            n.cod+=i.getCodigo()
        n.cod+=nExp.getEtqF()+":"+"\n"
        t[0]=n
    elif len(t)==12:
        nExp:Nodo=t[3]
        etqS = getEtq()
        n=Nodo()
        n.cod+=nExp.getCodigo()
        n.cod+=nExp.getEtqV()+":\n"
        ls1=t[6]
        for i in ls1:
            n.cod+=i.getCodigo()
        n.cod+="goto "+etqS+"\n"
        n.cod+=nExp.getEtqF()+":"+"\n"
        ls2=t[10]
        for i in ls2:
            n.cod+=i.getCodigo()
        n.cod+=etqS+":"+"\n"
        t[0]=n
    else:
        n = Nodo()
        n.setCodigo("<Sentencias>\n")
        t[0]=n

def p_s(t):
    ' S : L '
    t[0]=t[1]

def p_l(t):
    'L : L or M'
    l:Nodo=t[1]
    m:Nodo=t[3]
    n=Nodo()
    n.setEtqV(l.getEtqV())
    n.setEtqV(m.getEtqV())
    n.setEtqF(m.getEtqF())
    n.cod+=l.getCodigo()
    n.cod+=l.getEtqF()+":\n"
    n.cod+=m.getCodigo()
    t[0]=n
def p_l2(t):
    'L : M'
    t[0]=t[1]

def p_M(t):
    'M : M and NEG'
    m:Nodo=t[1]
    r:Nodo=t[3]
    n=Nodo()
    n.setEtqV(r.getEtqV())
    n.setEtqF(m.getEtqF())
    n.setEtqF(r.getEtqF())
    n.cod+=m.getCodigo()
    n.cod+=m.getEtqV()+":\n"
    n.cod+=r.getCodigo()
    t[0]=n
def p_M2(t):
    'M : NEG'
    t[0]=t[1]

def p_Not(t):
    '''NEG : not S
           | R'''
    
    if len(t)==3:
        r:Nodo = t[2]
        n=Nodo()
        n.etqV=r.etqF
        n.etqF=r.etqV
        n.cod=r.cod
        t[0]=n
    else:
        t[0]=t[1]

def p_R1(t):
    'R : E mayor E'
    e1:Nodo = t[1]
    e2:Nodo = t[3]
    n=Nodo()
    ev = getEtq()
    ef = getEtq()
    n.setEtqV(ev)
    n.setEtqF(ef)
    n.cod+=e1.getCodigo()
    n.cod+=e2.getCodigo()
    n.cod+="if "+e1.getTmp()+" > "+e2.getTmp()+" goto "+ev+"\n"
    n.cod+="goto "+ef+"\n"
    t[0]=n

def p_R2(t):
    'R : E menor E'
    e1:Nodo = t[1]
    e2:Nodo = t[3]
    n=Nodo()
    ev = getEtq()
    ef = getEtq()
    n.setEtqV(ev)
    n.setEtqF(ef)
    n.cod+=e1.getCodigo()
    n.cod+=e2.getCodigo()
    n.cod+="if "+e1.getTmp()+" < "+e2.getTmp()+" goto "+ev+"\n"
    n.cod+="goto "+ef+"\n"
    t[0]=n

def p_R3(t):
    'R : E igualdad E'
    e1:Nodo = t[1]
    e2:Nodo = t[3]
    n=Nodo()
    ev = getEtq()
    ef = getEtq()
    n.setEtqV(ev)
    n.setEtqF(ef)
    n.cod+=e1.getCodigo()
    n.cod+=e2.getCodigo()
    n.cod+="if "+e1.getTmp()+" == "+e2.getTmp()+" goto "+ev+"\n"
    n.cod+="goto "+ef+"\n"
    t[0]=n

def p_R4(t):
    'R : E diferente E'
    e1:Nodo = t[1]
    e2:Nodo = t[3]
    n=Nodo()
    ev = getEtq()
    ef = getEtq()
    n.setEtqV(ev)
    n.setEtqF(ef)
    n.cod+=e1.getCodigo()
    n.cod+=e2.getCodigo()
    n.cod+="if "+e1.getTmp()+" <> "+e2.getTmp()+" goto "+ev+"\n"
    n.cod+="goto "+ef+"\n"
    t[0]=n

def p_R5(t):
    'R : parA S parC'
    t[0]=t[2]

def p_R6(t):
    'R : True'
    n=Nodo()
    ev = getEtq()
    ef = getEtq()
    n.setEtqV(ev)
    n.setEtqF(ef)
    n.cod+="if 1==1 goto "+ev+"\n"
    n.cod+="goto "+ef+"\n"
    t[0]=n

def p_R7(t):
    'R : False'
    n=Nodo()
    ev = getEtq()
    ef = getEtq()
    n.setEtqV(ev)
    n.setEtqF(ef)
    n.cod+="if 1==0 goto "+ev+"\n"
    n.cod+="goto "+ef+"\n"
    t[0]=n


def p_E(t):
    '''E : E mas T
         | E menos T
         | T'''
    if(len(t)==4):
        e1:Nodo = t[1]
        t1:Nodo = t[3]
        n=Nodo()
        tmp=getTmp()
        n.setTemporal(tmp)
        n.cod+=e1.getCodigo()
        n.cod+=t1.getCodigo()
        n.cod+=tmp+" = "+e1.getTmp()+" "+t[2]+" "+t1.getTmp()+"\n"
        t[0]=n
    else:
        t[0]=t[1]

def p_T(t):
    '''T : T por F
         | T div F
         | F '''
    if len(t)==4:
        e1:Nodo = t[1]
        t1:Nodo = t[3]
        n=Nodo()
        tmp=getTmp()
        n.setTemporal(tmp)
        n.cod+=e1.getCodigo()
        n.cod+=t1.getCodigo()        
        n.cod+=tmp+" = "+e1.getTmp()+" "+t[2]+" "+t1.getTmp()+"\n"
        t[0]=n
    else:
        t[0]=t[1]

def p_F(t):
    '''F : parA E parC
        | numero 
        | id'''
    if len(t)==4:
        t[0]=t[2]
    else:
        n = Nodo()
        n.setTemporal(t[1])
        t[0]=n

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)