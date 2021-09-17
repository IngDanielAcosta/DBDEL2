#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 11:52:29 2021

@author: laurayarce
"""

# Importar paquetes
import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go
import base64
import numpy as np

# Utilizar la página completa en lugar de una columna central estrecha
st.set_page_config(layout="wide")

# Título principal, h1 denota el estilo del título 1
st.markdown("<h1 style='text-align: center; color: #3C9AD0;'>Delictividad en Colombia</h1>", unsafe_allow_html=True)

# Generar espacio entre el título y los indicadores
st.markdown("<h3 </h3>", unsafe_allow_html=True)

# Función para importar datos
@st.cache(persist=True) # Código para que quede almacenada la información en el cache
def load_data(url):
    df = pd.read_csv(url) # leer datos
    return df

# función para obtener link de descarga
#def get_table_download_link(df):
#    csv = df.to_csv(index=False)
#    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
#    href = f'<a href="data:file/csv;base64,{b64}" download="datos.csv">Descargar archivo csv</a>'
#    return href

# Aplicar función


adu_capturados=pd.read_csv('Bases/adu_capturados.csv')
adu_policia = pd.read_csv("https://drive.google.com/file/d/1HXQ6z4nAeIhQnLm22EmDy-JYWF0NbBYB/view?usp=sharing")
adu_indiciados = pd.read_csv("https://drive.google.com/file/d/1Ge8uiZ1Xs-qb2vgiD11GxYb65REuAJSO/view?usp=sharing")
adu_indicadores = pd.read_csv("Bases/adu_indicadores.csv")
adu_indicadores['FECHA']= adu_indicadores['AÑO'].apply(lambda x: "01-01-"+str(x))
adu_indicadores['FECHA'] = pd.to_datetime(adu_indicadores['FECHA'])
adu_educacion = pd.read_csv("Bases/adu_educacion.csv")
#---------------------------------------------------------------------


# Dividir el layout en cinco partes
#########################################################################
#########################################################################
######################################################################### LY1
#########################################################################
#########################################################################
c1, c2, c3 = st.beta_columns((1,1,1))

# Primer markdown
c1.markdown("<h3 style='text-align: left; color: Gray;'> Grupo edad capturados </h3>", unsafe_allow_html=True)

# Organizar data

# pie_Grupo_Edad_Capturado:
################################################################################
base = pd.DataFrame(adu_capturados['GRUPO_EDAD_CAPTURADO'].value_counts()).reset_index().rename(columns={'index':'GRUPO_EDAD','GRUPO_EDAD_CAPTURADO':'CANTIDAD'})
fig = px.pie(base, values = 'CANTIDAD', names ='GRUPO_EDAD',
             #title= '<b>Capturados y grupo etario<b>',
             color_discrete_sequence=px.colors.qualitative.G10,
             width=340,  height=240)

# agregar detalles a la gráfica:
fig.update_layout(
    #xaxis_title = 'Año',
    #yaxis_title = 'Precio de venta',
    template = 'simple_white',
    #title_x = 0.5
    )

c1.plotly_chart(fig)
############################################################################### 

# Segundo markdown
c2.markdown("<h3 style='text-align: left; color: Gray;'> Grupo edad víctimas </h3>", unsafe_allow_html=True)


# pie_Grupo_Edad_Victima:
base = pd.DataFrame(adu_policia['EDAD_VICTIMA'].value_counts()).reset_index().rename(columns={'index':'GRUPO_EDAD_VICTIMA','EDAD_VICTIMA':'CANTIDAD'})
fig = px.pie(base, values = 'CANTIDAD', names ='GRUPO_EDAD_VICTIMA',
             #title= '<b>Víctimas y grupo etario<b>',
             color_discrete_sequence=px.colors.qualitative.G10,
             width=340,  height=240)

# agregar detalles a la gráfica:
fig.update_layout(
    #xaxis_title = 'Año',
    #yaxis_title = 'Precio de venta',
    template = 'simple_white',
    #title_x = 0.5
    )

c2.plotly_chart(fig)
###############################################################################  

# tercer markdown
c3.markdown("<h3 style='text-align: left; color: Gray;'> Grupo edad indiciados </h3>", unsafe_allow_html=True)


# pie_Grupo_Edad_Victima:
base = pd.DataFrame(adu_indiciados['GRUPO_EDAD_INDICIADO'].value_counts()).reset_index().rename(columns={'index':'GRUPO_EDAD','GRUPO_EDAD_INDICIADO':'CANTIDAD'})
fig = px.pie(base, values = 'CANTIDAD', names ='GRUPO_EDAD',
             color_discrete_sequence=px.colors.qualitative.G10,
             width=340,  height=240)

# agregar detalles a la gráfica:
fig.update_layout(
    #xaxis_title = 'Año',
    #yaxis_title = 'Precio de venta',
    template = 'simple_white',
    #title_x = 0.5
    )

c3.plotly_chart(fig)


#########################################################################
#########################################################################
######################################################################### LY2
#########################################################################
#########################################################################
c1, c2, c3 = st.beta_columns((1,1,1))


#########################################################################c1
c1.markdown("<h3 style='text-align: left; color: Gray;'> Género capturados </h3>", unsafe_allow_html=True)
s1c1e1_nombre = adu_capturados['GENERO'].value_counts().index[0]
s1c1e1_valor = adu_capturados['GENERO'].value_counts()[0]
s1c1e2_nombre = adu_capturados['GENERO'].value_counts().index[1]
s1c1e2_valor = adu_capturados['GENERO'].value_counts()[1]


 #Enviar a streamlit
c1.text(str(s1c1e1_nombre)+' = '+str(s1c1e1_valor))
c1.text(str(s1c1e2_nombre)+' = '+str(s1c1e2_valor))

#########################################################################c2
c2.markdown("<h3 style='text-align: left; color: Gray;'> Género víctimas </h3>", unsafe_allow_html=True)

s1c2e1_nombre = adu_policia['GENERO_VICTIMA'].value_counts().index[0]
s1c2e1_valor = adu_policia['GENERO_VICTIMA'].value_counts()[0]
s1c2e2_nombre = adu_policia['GENERO_VICTIMA'].value_counts().index[1]
s1c2e2_valor = adu_policia['GENERO_VICTIMA'].value_counts()[1]
s1c2e3_nombre = adu_policia['GENERO_VICTIMA'].value_counts().index[2]
s1c2e3_valor = adu_policia['GENERO_VICTIMA'].value_counts()[2]

 #Enviar a streamlit
c2.text(str(s1c2e1_nombre)+' = '+str(s1c2e1_valor))
c2.text(str(s1c2e2_nombre)+' = '+str(s1c2e2_valor))
c2.text(str(s1c2e3_nombre)+' = '+str(s1c2e3_valor))

#########################################################################c3
c3.markdown("<h3 style='text-align: left; color: Gray;'> Género indiciados </h3>", unsafe_allow_html=True)

s1c3e1_nombre = adu_indiciados['SEXO_INDICIADO'].value_counts().index[0]
s1c3e1_valor = adu_indiciados['SEXO_INDICIADO'].value_counts()[0]
s1c3e2_nombre = adu_indiciados['SEXO_INDICIADO'].value_counts().index[1]
s1c3e2_valor = adu_indiciados['SEXO_INDICIADO'].value_counts()[1]
s1c3e3_nombre = adu_indiciados['SEXO_INDICIADO'].value_counts().index[2]
s1c3e3_valor = adu_indiciados['SEXO_INDICIADO'].value_counts()[2]

 #Enviar a streamlit
c3.text(str(s1c3e1_nombre)+' = '+str(s1c3e1_valor))
c3.text(str(s1c3e2_nombre)+' = '+str(s1c3e2_valor))
c3.text(str(s1c3e3_nombre)+' = '+str(s1c3e3_valor))

#########################################################################
#########################################################################
######################################################################### LY3
#########################################################################
#########################################################################
c1, c2, c3 = st.beta_columns((1,1,1))

c1.markdown("<h3 style='text-align: left; color: Gray;'> Capturados por año según delito </h3>", unsafe_allow_html=True)
lista_delitos_cap = list(adu_capturados.iloc[:,14:-2].columns)
base = adu_capturados.groupby(by=['AÑO_CAPTURA','MES_CAPTURA'])[lista_delitos_cap].sum().reset_index()
delito_elegido_cap = c1.selectbox('elige el delito', lista_delitos_cap)
fig = px.box(base, x="AÑO_CAPTURA", y=delito_elegido_cap, color="AÑO_CAPTURA",
             width=450,  height=300)
fig.update_xaxes(tickangle=90,
                 tickmode='linear')

c1.plotly_chart(fig)

c2.markdown("<h3 style='text-align: left; color: Gray;'> Denuncias por año según delito </h3>", unsafe_allow_html=True)
lista_delitos_pol = list(adu_policia.iloc[:,11:].columns)
base = adu_policia.groupby(by=['ANO','MES'])[lista_delitos_pol].sum().reset_index()
delito_elegido_pol = c2.selectbox('elige el delito', lista_delitos_pol)
fig = px.box(base, x="ANO", y=delito_elegido_pol, color="ANO",
             width=450,  height=300)
fig.update_xaxes(tickangle=90,
                 tickmode='linear')
fig.update_layout(
    xaxis_title = 'AÑO DENUNCIAS')
c2.plotly_chart(fig)

c3.markdown("<h3 style='text-align: left; color: Gray;'> Indiciados por año según delito </h3>", unsafe_allow_html=True)
lista_delitos_ind = list(adu_indiciados.iloc[:,25:].columns)
base = adu_indiciados.groupby(by=['ANIO_HECHO'])[lista_delitos_ind].sum().reset_index()
base['ANIO_HECHO']=base['ANIO_HECHO'].astype('str')
delito_elegido_ind = c3.selectbox('elige el delito', lista_delitos_ind)
fig = px.bar(base, x="ANIO_HECHO", y=delito_elegido_ind, color="ANIO_HECHO",
             width=450,  height=300)
fig.update_xaxes(tickangle=90,
                 tickmode='linear')
fig.update_layout(
    xaxis_title = 'AÑO HECHO')

c3.plotly_chart(fig)

#########################################################################
#########################################################################
######################################################################### LY4
#########################################################################
#########################################################################
c1, c2 , c3= st.beta_columns((1,1,1))

c1.markdown("<h3 style='text-align: left; color: Gray;'> Histórico capturados por delito elegido </h3>", unsafe_allow_html=True)
#delito_elegido_caply4 = c1.selectbox('elige el delito', lista_delitos_cap)
base=pd.melt(adu_capturados.groupby(by=["FECHA_CAPTURA"])[lista_delitos_cap].sum().reset_index(),id_vars=["FECHA_CAPTURA"],value_vars=lista_delitos_cap,var_name="DELITO",value_name="CAPTURADOS")
base1=base.loc[base['DELITO']==delito_elegido_cap,]
fig = px.line(base1, x='FECHA_CAPTURA', y="CAPTURADOS",
              width=450,  height=300
              )
fig.update_layout(
    yaxis_title = delito_elegido_cap)
c1.plotly_chart(fig)

c2.markdown("<h3 style='text-align: left; color: Gray;'> Histórico denuncias por delito elegido </h3>", unsafe_allow_html=True)
#delito_elegido_caply4 = c1.selectbox('elige el delito', lista_delitos_cap)
base=pd.melt(adu_policia.groupby(by=["ANO"])[lista_delitos_pol].sum().reset_index(),id_vars=["ANO"],value_vars=lista_delitos_pol,var_name="DELITO",value_name="DENUNCIAS")
base1=base.loc[base['DELITO']==delito_elegido_pol,]
fig = px.line(base1, x='ANO', y="DENUNCIAS",
              width=450,  height=300
              )
fig.update_layout(
    yaxis_title = delito_elegido_pol,
    xaxis_title = "AÑO")
c2.plotly_chart(fig)

c3.markdown("<h3 style='text-align: left; color: Gray;'> Histórico indiciados por delito elegido </h3>", unsafe_allow_html=True)
#delito_elegido_caply4 = c1.selectbox('elige el delito', lista_delitos_cap)
base=pd.melt(adu_indiciados.groupby(by=["ANIO_HECHO"])[lista_delitos_ind].sum().reset_index(),id_vars=["ANIO_HECHO"],value_vars=lista_delitos_ind,var_name="DELITO",value_name="INDICIADOS")
base1=base.loc[base['DELITO']==delito_elegido_ind,]
fig = px.line(base1, x='ANIO_HECHO', y="INDICIADOS",
              width=450,  height=300
              )
fig.update_layout(
    yaxis_title = delito_elegido_ind,
    xaxis_title = "AÑO")
c3.plotly_chart(fig)

#########################################################################
#########################################################################
######################################################################### LY4.2
#########################################################################
#########################################################################
c1,c2,c3= st.beta_columns((1,1,1))


c1.markdown("<h3 style='text-align: left; color: Gray;'> Delitos captura por departamento </h3>", unsafe_allow_html=True)
#delito_elegido_caply4 = c1.selectbox('elige el delito', lista_delitos_cap)
d_e_1 = c1.selectbox('elige el departamento', list(adu_capturados['DEPTO'].unique()))
base=pd.melt(adu_capturados.groupby(by=["DEPTO"])[lista_delitos_cap].sum().reset_index(),id_vars=["DEPTO"],value_vars=lista_delitos_cap,var_name="DELITO",value_name="CAPTURADOS")
base1=base.loc[base['DEPTO']==d_e_1,]
fig = px.bar(base1, x='DEPTO', y="CAPTURADOS",color="DELITO",
              barmode='group',width=(500)
              )
fig.update_layout(
    xaxis_title = 'DEPARTAMENTO',
    #yaxis_title = 'N° Indiciados',
    template = 'simple_white',
    #title_x = 0.25
    showlegend=False
    )
c1.plotly_chart(fig)

c2.markdown("<h3 style='text-align: left; color: Gray;'> Delitos denuncia por departamento </h3>", unsafe_allow_html=True)
#delito_elegido_caply4 = c1.selectbox('elige el delito', lista_delitos_cap)
d_e_2 = c2.selectbox('elige el departamento', list(adu_policia['DEPARTAMENTO'].unique()))
base=pd.melt(adu_policia.groupby(by=["DEPARTAMENTO"])[lista_delitos_pol].sum().reset_index(),id_vars=["DEPARTAMENTO"],value_vars=lista_delitos_pol,var_name="DELITO",value_name="DENUNCIAS")
base1=base.loc[base['DEPARTAMENTO']==d_e_2,]
fig = px.bar(base1, x='DEPARTAMENTO', y="DENUNCIAS",color="DELITO",
              barmode='group',width=(500)
              )
fig.update_layout(
    #xaxis_title = 'Tipo de delito',
    #yaxis_title = 'N° Indiciados',
    template = 'simple_white',
    #title_x = 0.25
    showlegend=False
    )
c2.plotly_chart(fig)

c3.markdown("<h3 style='text-align: left; color: Gray;'> Delitos indiciados por departamento </h3>", unsafe_allow_html=True)
#delito_elegido_caply4 = c1.selectbox('elige el delito', lista_delitos_cap)
d_e_3 = c3.selectbox('elige el departamento', list(adu_indiciados['DEPARTAMENTO'].unique()))
base=pd.melt(adu_indiciados.groupby(by=["DEPARTAMENTO"])[lista_delitos_ind].sum().reset_index(),id_vars=["DEPARTAMENTO"],value_vars=lista_delitos_ind,var_name="DELITO",value_name="DENUNCIAS")
base1=base.loc[base['DEPARTAMENTO']==d_e_3,]
fig = px.bar(base1, x='DEPARTAMENTO', y="DENUNCIAS",color="DELITO",
              barmode='group',width=(500)
              )
fig.update_layout(
    #xaxis_title = 'Tipo de delito',
    #yaxis_title = 'N° Indiciados',
    template = 'simple_white',
    #title_x = 0.25
    showlegend=False
    )
c3.plotly_chart(fig)

############################################################################### OTRAS BD
st.markdown("<h2 style='text-align: center; color: #ff3396;'>Educación e indicadores socioeconómicos</h2>", unsafe_allow_html=True)

#########################################################################
#########################################################################
######################################################################### LY5
#########################################################################
#########################################################################
c1, c2, c3 = st.beta_columns((1,1,1))


base = adu_educacion.groupby(by=['DEPARTAMENTO'])[['COBERTURA_NETA','DESERCION','REPROBACION']].mean().reset_index()
base = base.melt(id_vars="DEPARTAMENTO",value_vars=['COBERTURA_NETA','DESERCION','REPROBACION'],var_name="CATEGORIA",value_name="Tasa")

# COBERTURA_NETA 
fig = px.bar(base.loc[base['CATEGORIA']=="COBERTURA_NETA",], x = 'CATEGORIA', y='Tasa', color = 'DEPARTAMENTO', barmode = 'group', 
             title= '<b>COBERTURA_NETA promedio por departamento<b>',
             width=540)

# agregar detalles a la gráfica
fig.update_layout(
    #xaxis_title = 'Tipo de delito',
    #yaxis_title = 'N° Indiciados',
    template = 'simple_white',
    #title_x = 0.25
)
c1.plotly_chart(fig)     

# DESERCION
fig = px.bar(base.loc[base['CATEGORIA']=="DESERCION",], x = 'CATEGORIA', y='Tasa', color = 'DEPARTAMENTO', barmode = 'group', 
             title= '<b>DESERCION promedio por departamento<b>',
             width=540)

# agregar detalles a la gráfica
fig.update_layout(
    #xaxis_title = 'Tipo de delito',
    #yaxis_title = 'N° Indiciados',
    template = 'simple_white',
    #title_x = 0.25
)
c2.plotly_chart(fig)  

# REPROBACION
fig = px.bar(base.loc[base['CATEGORIA']=="REPROBACION",], x = 'CATEGORIA', y='Tasa', color = 'DEPARTAMENTO', barmode = 'group', 
             title= '<b>REPROBACION promedio por departamento<b>',
             width=540)

# agregar detalles a la gráfica
fig.update_layout(
    #xaxis_title = 'Tipo de delito',
    #yaxis_title = 'N° Indiciados',
    template = 'simple_white',
    #title_x = 0.25
)
c3.plotly_chart(fig) 

#########################################################################
#########################################################################
######################################################################### LY6
#########################################################################
#########################################################################

di={'AÑO': [2015,2016,2017,2018,2019],
    'DEPTO': ["COLOMBIA","COLOMBIA","COLOMBIA","COLOMBIA","COLOMBIA"],
 'IND_POBR_MON': [34.96666666666666, 34.875, 32.949999999999996, 33.25, np.nan],
 'INFLACION': [6.77, 5.75, 4.0900000000000025, 3.180000000000001, 3.7999999999999985],
 'POBL_EDAD_TRAB': [78.54847928498442, 78.76632816397475, 78.96798971515996, 79.16023110991303, 79.34973502756998],
 'TD': [8.879015294321078, 9.29041714674583, 9.096737014426012, 9.340149423532894, 10.476147861877298],
 'TO': [56.898446077468, 56.788315319680066, 56.890104390799, 56.379287587413195, 54.675215984844186],
 'FECHA': ['2015-01-01 00:00:00',  '2016-01-01 00:00:00','2017-01-01 00:00:00','2018-01-01 00:00:00','2019-01-01 00:00:00']}
colombia=pd.DataFrame(di)

adu_indicadores_total = adu_indicadores.append(colombia)

d_elegido = st.selectbox('elige el departamento', list(adu_indicadores_total['DEPTO'].unique()))
base = adu_indicadores_total.loc[adu_indicadores_total['DEPTO']==d_elegido,].melt(
    id_vars=["FECHA","DEPTO"],value_vars=['POBL_EDAD_TRAB','TO','TD','IND_POBR_MON','INFLACION'],
    var_name="INDICADOR",value_name="TASA")


fig = px.line(base, x='FECHA', y='TASA', color = 'INDICADOR', width=1100, height=450,
              title=("Variables socioeconómicas según departamento"))

# Editar gráfica
fig.update_layout(
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        template = 'simple_white'
#        xaxis_title="<b>Año<b>",
#        yaxis_title='<b>Cantidad de incidentes<b>',
#        legend_title_text='',
#        
#        legend=dict(
#            orientation="h",
#            yanchor="bottom",
#            y=1.02,
#            xanchor="right",
#            x=0.8)
)

# Enviar gráfica a streamlit
st.plotly_chart(fig)

############################################################################### Analisis combinado
st.markdown("<h2 style='text-align: center; color: #39e16c;'>Análisis combinado</h2>", unsafe_allow_html=True)

#########################################################################
#########################################################################
######################################################################### LY7
#########################################################################
#########################################################################
c1, c2 = st.beta_columns((1,1))

############################################################### c1
sumarizar=list(adu_capturados.iloc[:,14:-2].columns)
ac_capturados = adu_capturados.groupby(by=['AÑO_CAPTURA','DEPTO','GENERO','GRUPO_EDAD_CAPTURADO'])[sumarizar].sum().reset_index()
ac_capturados = ac_capturados.add_prefix('CAP_')


ac_educacion_capturados= pd.merge(ac_capturados, adu_educacion, 
                                  left_on=['CAP_AÑO_CAPTURA', 'CAP_DEPTO'],
                                  right_on=['ANO','DEPARTAMENTO'],
                                  how='left')

delitos = list(ac_educacion_capturados.iloc[:,4:24].columns)

base = ac_educacion_capturados.groupby(by=['CAP_AÑO_CAPTURA','GRUPO_COBERTURA_SECUNDARIA'])[delitos].sum().reset_index()
base['GRUPO_COBERTURA_SECUNDARIA']=base['GRUPO_COBERTURA_SECUNDARIA'].astype('str')

d_7_1_a = c1.selectbox('elige el delito', list(base.iloc[:,2:].head(3).columns))

fig = px.box(base, x='GRUPO_COBERTURA_SECUNDARIA', y=d_7_1_a)

c1.plotly_chart(fig)


base = ac_educacion_capturados.groupby(by=['CAP_AÑO_CAPTURA','GRUPO_DESERCION_SECUNDARIA'])[delitos].sum().reset_index()
base['GRUPO_DESERCION_SECUNDARIA']=base['GRUPO_DESERCION_SECUNDARIA'].astype('str')
fig = px.box(base, x='GRUPO_DESERCION_SECUNDARIA', y=d_7_1_a)
c1.plotly_chart(fig)

ac_capturados_indicadores=pd.merge(ac_capturados, adu_indicadores, 
                                   left_on=['CAP_AÑO_CAPTURA', 'CAP_DEPTO'],
                                   right_on=['AÑO','DEPTO'],
                                   how='left')


ac_capturados_indicadores=pd.merge(ac_capturados, adu_indicadores, 
                                   left_on=['CAP_AÑO_CAPTURA', 'CAP_DEPTO'],
                                   right_on=['AÑO','DEPTO'],how='left')

c2.markdown("<h3 </h3>", unsafe_allow_html=True)
c2.markdown("<h3 </h3>", unsafe_allow_html=True)
c2.markdown("<h3 </h3>", unsafe_allow_html=True)


fig = px.scatter(ac_capturados_indicadores, x='CAP_TRAFICO FABRICACION O PORTE DE ESTUPEFACIENTES', y='INFLACION')
c2.plotly_chart(fig)

fig = px.scatter(ac_capturados_indicadores, x='CAP_HURTO', y='IND_POBR_MON')
c2.plotly_chart(fig)

indic = list(adu_indicadores.columns)
delit = list(ac_capturados.columns)
ac_capturados.corr().unstack().sort_values().head(30)
Tabla_correlacion=pd.DataFrame(ac_capturados_indicadores.corr().unstack().sort_values()).reset_index()
Tabla_correlacion.rename(columns={'level_0':'VARIABLE_1','level_1':'VARIABLE_2',0:'CORRELACION'},inplace=True)
Tabla_correlacion = Tabla_correlacion.loc[(Tabla_correlacion['VARIABLE_1']!=Tabla_correlacion['VARIABLE_2']),]
Tabla_correlacion = Tabla_correlacion.loc[Tabla_correlacion['VARIABLE_2'].isin(indic),]
Tabla_correlacion = Tabla_correlacion.loc[~Tabla_correlacion['VARIABLE_1'].isin(indic),]
Tabla_correlacion = Tabla_correlacion.loc[Tabla_correlacion['VARIABLE_1'].isin(delit),]
Tabla_correlacion = Tabla_correlacion.loc[abs(Tabla_correlacion['CORRELACION'])>0.25,]
Tabla_correlacion.iloc[:,:-1]

############################################################### c2

sumarizar=list(adu_policia.iloc[:,11:].columns)
ac_policia = adu_policia.groupby(by=['ANO','DEPARTAMENTO','GENERO_VICTIMA','EDAD_VICTIMA'])[sumarizar].sum().reset_index()
ac_policia.loc[ac_policia['DEPARTAMENTO']=="GUAJIRA","DEPARTAMENTO"]="LA GUAJIRA"
ac_policia.loc[ac_policia['DEPARTAMENTO']=="SAN ANDRES","DEPARTAMENTO"]="SAN ANDRES Y PROVIDENCIA"
ac_policia = ac_policia.add_prefix('DEN_')


############################################################### c3

sumarizar = list(adu_indiciados.iloc[:,25:].columns)
ac_indiciados = adu_indiciados.groupby(by=['ANIO_HECHO','DEPARTAMENTO','SEXO_INDICIADO','GRUPO_EDAD_INDICIADO'])[sumarizar].sum().reset_index()
ac_indiciados = ac_indiciados.add_prefix('IND_') #OJO CON "SIN DATO" EN GRUPO EDAD