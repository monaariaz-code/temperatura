{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red111\green14\blue195;\red236\green241\blue247;\red98\green98\blue98;
\red0\green0\blue0;\red24\green112\blue43;\red77\green80\blue85;\red164\green69\blue11;}
{\*\expandedcolortbl;;\cssrgb\c51765\c18824\c80784;\cssrgb\c94118\c95686\c97647;\cssrgb\c45882\c45882\c45882;
\cssrgb\c0\c0\c0;\cssrgb\c9412\c50196\c21961;\cssrgb\c37255\c38824\c40784;\cssrgb\c70980\c34902\c3137;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  streamlit \cf2 \strokec2 as\cf4 \strokec4  st\cb1 \
\
\cf2 \cb3 \strokec2 def\cf4 \strokec4  convertir_temperatura\strokec5 (\strokec4 valor\strokec5 ,\strokec4  de_unidad\strokec5 ,\strokec4  a_unidad\strokec5 ):\cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 \strokec6 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6     Funci\'f3n para convertir la temperatura entre Celsius, Fahrenheit y Kelvin.\cf4 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 # Si las unidades son iguales, retornamos el mismo valor\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  de_unidad == a_unidad\strokec5 :\cb1 \strokec4 \
\cb3         \cf2 \strokec2 return\cf4 \strokec4  valor\cb1 \
\cb3     \cb1 \
\cb3     \cf7 \strokec7 # Primero convertimos el valor de entrada a Celsius como punto intermedio\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  de_unidad == \cf6 \strokec6 "Fahrenheit"\cf4 \strokec5 :\cb1 \strokec4 \
\cb3         celsius = \strokec5 (\strokec4 valor - \cf8 \strokec8 32\cf4 \strokec5 )\strokec4  * \cf8 \strokec8 5.0\cf4 \strokec4  / \cf8 \strokec8 9.0\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 elif\cf4 \strokec4  de_unidad == \cf6 \strokec6 "Kelvin"\cf4 \strokec5 :\cb1 \strokec4 \
\cb3         celsius = valor - \cf8 \strokec8 273.15\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 else\cf4 \strokec5 :\cb1 \strokec4 \
\cb3         celsius = valor\cb1 \
\cb3         \cb1 \
\cb3     \cf7 \strokec7 # Luego convertimos de Celsius a la unidad de destino\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  a_unidad == \cf6 \strokec6 "Fahrenheit"\cf4 \strokec5 :\cb1 \strokec4 \
\cb3         \cf2 \strokec2 return\cf4 \strokec4  \strokec5 (\strokec4 celsius * \cf8 \strokec8 9.0\cf4 \strokec4  / \cf8 \strokec8 5.0\cf4 \strokec5 )\strokec4  + \cf8 \strokec8 32\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 elif\cf4 \strokec4  a_unidad == \cf6 \strokec6 "Kelvin"\cf4 \strokec5 :\cb1 \strokec4 \
\cb3         \cf2 \strokec2 return\cf4 \strokec4  celsius + \cf8 \strokec8 273.15\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 else\cf4 \strokec5 :\cb1 \strokec4 \
\cb3         \cf2 \strokec2 return\cf4 \strokec4  celsius\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # Configuraci\'f3n b\'e1sica de la p\'e1gina para darle un mejor aspecto\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 st.set_page_config\strokec5 (\strokec4 page_title=\cf6 \strokec6 "Conversor de Temperatura"\cf4 \strokec5 ,\strokec4  page_icon=\cf6 \strokec6 "\uc0\u55356 \u57121 \u65039 "\cf4 \strokec5 ,\strokec4  layout=\cf6 \strokec6 "centered"\cf4 \strokec5 )\cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # T\'edtulo y descripci\'f3n\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 st.title\strokec5 (\cf6 \strokec6 "\uc0\u55356 \u57121 \u65039  Conversor de Temperatura"\cf4 \strokec5 )\cb1 \strokec4 \
\cb3 st.markdown\strokec5 (\cf6 \strokec6 "Una herramienta sencilla y r\'e1pida para convertir entre **Celsius, Fahrenheit y Kelvin**."\cf4 \strokec5 )\cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # Usamos columnas para darle un dise\'f1o m\'e1s estructurado a la interfaz\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 col1\strokec5 ,\strokec4  col2 = st.columns\strokec5 (\cf8 \strokec8 2\cf4 \strokec5 )\cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf4 \strokec4  col1\strokec5 :\cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     st.subheader\strokec5 (\cf6 \strokec6 "Entrada"\cf4 \strokec5 )\cb1 \strokec4 \
\cb3     \cf7 \strokec7 # Campo para ingresar el valor num\'e9rico\cf4 \cb1 \strokec4 \
\cb3     valor_entrada = st.number_input\strokec5 (\cf6 \strokec6 "Ingresa el valor:"\cf4 \strokec5 ,\strokec4  value=\cf8 \strokec8 0.0\cf4 \strokec5 ,\strokec4  step=\cf8 \strokec8 1.0\cf4 \strokec5 )\cb1 \strokec4 \
\cb3     \cf7 \strokec7 # Selector de la unidad de origen\cf4 \cb1 \strokec4 \
\cb3     unidad_origen = st.selectbox\strokec5 (\cf6 \strokec6 "Convertir de:"\cf4 \strokec5 ,\strokec4  \strokec5 [\cf6 \strokec6 "Celsius"\cf4 \strokec5 ,\strokec4  \cf6 \strokec6 "Fahrenheit"\cf4 \strokec5 ,\strokec4  \cf6 \strokec6 "Kelvin"\cf4 \strokec5 ])\cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf4 \strokec4  col2\strokec5 :\cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     st.subheader\strokec5 (\cf6 \strokec6 "Salida"\cf4 \strokec5 )\cb1 \strokec4 \
\cb3     \cf7 \strokec7 # Selector de la unidad de destino\cf4 \cb1 \strokec4 \
\cb3     unidad_destino = st.selectbox\strokec5 (\cf6 \strokec6 "Convertir a:"\cf4 \strokec5 ,\strokec4  \strokec5 [\cf6 \strokec6 "Celsius"\cf4 \strokec5 ,\strokec4  \cf6 \strokec6 "Fahrenheit"\cf4 \strokec5 ,\strokec4  \cf6 \strokec6 "Kelvin"\cf4 \strokec5 ])\cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf7 \strokec7 # Realizamos el c\'e1lculo en tiempo real\cf4 \cb1 \strokec4 \
\cb3     resultado = convertir_temperatura\strokec5 (\strokec4 valor_entrada\strokec5 ,\strokec4  unidad_origen\strokec5 ,\strokec4  unidad_destino\strokec5 )\cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf7 \strokec7 # Mostramos el resultado destacado\cf4 \cb1 \strokec4 \
\cb3     st.markdown\strokec5 (\cf6 \strokec6 "### Resultado:"\cf4 \strokec5 )\cb1 \strokec4 \
\cb3     st.success\strokec5 (\cf6 \strokec6 f"\cf4 \strokec4 \{valor_entrada\cf6 \strokec6 :.2f\cf4 \strokec4 \}\cf6 \strokec6  \cf4 \strokec4 \{unidad_origen\}\cf6 \strokec6  equivale a **\cf4 \strokec4 \{resultado\cf6 \strokec6 :.2f\cf4 \strokec4 \}\cf6 \strokec6  \cf4 \strokec4 \{unidad_destino\}\cf6 \strokec6 **"\cf4 \strokec5 )\cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # Un peque\'f1o pie de p\'e1gina\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 st.divider\strokec5 ()\cb1 \strokec4 \
\cb3 st.caption\strokec5 (\cf6 \strokec6 "Aplicaci\'f3n creada con Streamlit \uc0\u55356 \u57224 "\cf4 \strokec5 )\cb1 \strokec4 \
}