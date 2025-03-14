import streamlit as st

st.title ('Calculadora simples')

op1=st. number_input ('Operador 1:', value=0.0)
op2=st. number_input ('Operador 2:', value=0.0)

def calcular (op, op1, op2):
    if op== '+':
        return op1+op2
    if op== '-':
        return op1-op2 
    if op=='*':
        return op1*op2
    if op== '/':
        return op1/op2
col1,col2,col3,col4 = st.columns(4)
with col1:
    if st.button('\+'):
        resultado= calcular ('+' , op1, op2)
        st.success (f'resultado: { resultado}')
with col2:
           if st.button('\-'):
                resultado= calcular ('-' , op1, op2)
                st.success (f"resultado { resultado}")
with col3:
                if st.button ('\*'):
                        resultado= calcular ('*' , op1, op2)
                        st.success (f"resultado { resultado}")

with col4:
     if st.button ('/'):
          if op2==0:
               st.error('erro: de divisão por 0')
          else:
               resultado= calcular ('/' , op1, op2)
               st.success  (f'resultado: { resultado}')
               