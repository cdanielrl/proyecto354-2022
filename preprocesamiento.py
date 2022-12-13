import pandas as pd
import os

ruta = "./csv/"
# los datos se encuentran en tres archivos separados
csv_archs={"conjunto_de_datos_tmodulo_endiseg_web_2022.csv",
"conjunto_de_datos_tapart_a_endiseg_web_2022.csv",
"conjunto_de_datos_tapart_b_endiseg_web_2022.csv",
}

df_append = pd.DataFrame()
# unimos los archivos en un solo conjunto de datos
for i in csv_archs:
    file=ruta+i
    df_temp = pd.read_csv(file)
    df_append = df_append.append(df_temp, ignore_index=True)

num_encuestados=df_append.shape[0]

# reemplzamos NaN con 0

df_append.fillna(0,inplace=True)

# filtrado 
 
df_orientacion_sexual=df_append[["P8_1A","P8_1B","P8_2"]]
df_identidad_genero=df_append[["P9_1","P9_2","P9_10A"]]
df_discriminacion_padres=df_append[["P8_4_1","P8_4_2","P8_4_3"]]
df_discriminacion_genero=df_append[["P9_9","P9_10","P9_10A"]]
df_discriminacion_infancia=df_append[["P5_4_1","P5_4_2","P5_4_3","P5_4_4","P5_4_5"]]
df_discriminacion_adolecencia=df_append[["P6_11_1","P6_11_2","P6_11_3","P6_11_4","P6_11_5"]]
df_discriminacion_12_meses=df_append[["P11_4_1","P11_4_2","P11_4_3","P11_4_4","P11_4_5","P11_6_11","P11_6_12"]]
df_educacion_sexual=df_append[["P6_6_1","P6_6_2","P6_6_3","P6_6_4","P6_6_5","P6_6_6","P6_6_7","P6_6_8","P6_6_9","P6_12_1","P6_12_2","P6_12_3","P6_12_4","P6_12_5","P6_12_6","P6_12_7","P6_12_8","P6_12_9"]]

# estadígrafos

df_cuenta_orientacion=df_orientacion_sexual.value_counts()
df_cuenta_genero=df_identidad_genero.value_counts()
df_promedios_discriminacion_padres=df_discriminacion_padres.mean()
df_promedios_discriminacion_genero=df_discriminacion_genero.mean()
df_promedios_discriminacion_infancia=df_discriminacion_infancia.mean()
df_promedios_discriminacion_adolecencia=df_discriminacion_adolecencia.mean()
df_promedios_discriminacion_12_meses=df_discriminacion_12_meses.mean()
df_cuenta_educacion_sexual=df_educacion_sexual.value_counts()
df_promedios_educacion_sexual=df_educacion_sexual.mean()

df_cuenta_orientacion.to_csv("cuenta_orientacion.csv")
df_cuenta_genero.to_csv("cuenta_genero.csv")
df_promedios_discriminacion_padres.to_csv("promedios_discriminacion_padres.csv")
df_promedios_discriminacion_genero.to_csv("promedios_discriminacion_genero.csv")
df_promedios_discriminacion_infancia.to_csv("promedios_discriminacion_infancia.csv")
df_promedios_discriminacion_adolecencia.to_csv("promedios_discriminacion_adolecencia.csv")
df_promedios_discriminacion_12_meses.to_csv("promedios_discriminacion_12_meses.csv")
df_cuenta_educacion_sexual.to_csv("cuenta_educacion_sexual.csv")
df_promedios_educacion_sexual.to_csv("promedios_educacion_sexual.csv")