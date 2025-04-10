import streamlit as st  # Importa a biblioteca Streamlit para criar interfaces web interativas

st.title('Calculadora simples')  # Define o título da aplicação

# Cria dois campos numéricos para entrada dos operadores
op1 = st.number_input('Operador 1:', value=0.0)  
op2 = st.number_input('Operador 2:', value=0.0)

# Função que realiza o cálculo com base na operação escolhida
def calcular(op, op1, op2):
    if op == '+':  # Soma
        return op1 + op2
    if op == '-':  # Subtração
        return op1 - op2 
    if op == '*':  # Multiplicação
        return op1 * op2
    if op == '/':  # Divisão
        return op1 / op2

# Divide a interface em 4 colunas para os botões das operações
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button('\+'):  # Botão de soma
        resultado = calcular('+', op1, op2)
        st.success(f'resultado: {resultado}')  # Exibe o resultado em verde

with col2:
    if st.button('\-'):  # Botão de subtração
        resultado = calcular('-', op1, op2)
        st.success(f"resultado {resultado}")  # Exibe o resultado em verde

with col3:
    if st.button('\*'):  # Botão de multiplicação
        resultado = calcular('*', op1, op2)
        st.success(f"resultado {resultado}")  # Exibe o resultado em verde

with col4:
    if st.button('/'):  # Botão de divisão
        if op2 == 0:  # Verifica divisão por zero
            st.error('erro: de divisão por 0')  # Exibe mensagem de erro em vermelho
        else:
            resultado = calcular('/', op1, op2)
            st.success(f'resultado: {resultado}')  # Exibe o resultado em verde

               
