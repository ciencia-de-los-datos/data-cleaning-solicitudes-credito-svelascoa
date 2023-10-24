"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


"""
df.idea_negocio=df.idea_negocio.str.replace(" ", "_").str.replace("-","_").str.rstrip("_")
df.línea_credito=df.línea_credito.str.lower()
df.línea_credito=df.línea_credito.str.rstrip(". ").str.rstrip("._").str.rstrip(".-")
df.línea_credito=df.línea_credito.str.replace("soli-diaria", "solidaria").str.replace(" ", "_").str.replace("-", "_")
df.monto_del_credito=pd.to_numeric(df.monto_del_credito.str.replace("$ ", "").str.replace(".00", "").str.replace(",", ""))
df.barrio=df.barrio.str.rstrip(" ").str.rstrip("_").str.rstrip("-").str.rstrip(".")
df.barrio=df.barrio.str.lower()
df.barrio=df.barrio.str.replace("-","_").str.replace(" ","_")
#df.barrio=df.barrio.str.replace("andaluc¿a","andalucia").str.replace("bel¿n","belen").str.replace("antonio_nari¿o", "antonio_nariño")
#df.barrio=df.barrio.str.replace("boyac¿","boyaca").str.replace("campo_vald¿s_no.1","campo_valdes_no._1").str.replace("barrio_caycedo","barrio_caicedo").str.replace("santo_domingo_savio","santo_domingo")

#-----FIN LIMPIAR STANDARIZAR COLUMNAS DE TEXTO

#df=df.drop_duplicates()

#----DEFINIR TABLA CON "tipo_de_emprendimiento","idea_negocio" SIN DATOS AMBIGUOS
df2=df[["tipo_de_emprendimiento","idea_negocio"]].drop_duplicates(subset=["tipo_de_emprendimiento","idea_negocio"], ignore_index=True)
#df2=df2.dropna(ignore_index=True)
df2=df2.assign(CantR=0)

for i in range(0, len(df2)):
       cant=len(df[(df.tipo_de_emprendimiento==df2.loc[i]["tipo_de_emprendimiento"])&
                (df.idea_negocio==df2.loc[i]["idea_negocio"])])
       df2.loc[i,"CantR"]=cant

df4=pd.DataFrame(df["idea_negocio"].drop_duplicates(ignore_index=True))
df4=df4.assign(tipo_de_emprendimiento="")

for i in range(0, len(df4)):
    j =df2[(df2.idea_negocio==df4.loc[i]["idea_negocio"])]["CantR"].idxmax()
    df4.loc[i, "tipo_de_emprendimiento"]=df2.loc[j,"tipo_de_emprendimiento"]

#----FIN DEFINIR TABLA CON "tipo_de_emprendimiento","idea_negocio" SIN DATOS AMBIGUOS

#----DEFINIR TABLA CON "barrio","comuna_ciudadano" SIN DATOS AMBIGUOS
df5=df[["barrio","comuna_ciudadano"]].drop_duplicates(subset=["barrio","comuna_ciudadano"], ignore_index=True)
#df5=df5.dropna(ignore_index=True)
df5=df5.assign(CantR=0)

for i in range(0, len(df5)):
       cant=len(df[(df.barrio==df5.loc[i]["barrio"])&
                (df.comuna_ciudadano==df5.loc[i]["comuna_ciudadano"])])
       df5.loc[i,"CantR"]=cant

df6=pd.DataFrame(df["barrio"].drop_duplicates(ignore_index=True))
#df6=df6.dropna(ignore_index=True)
df6=df6.assign(comuna_ciudadano="")

for i in range(0, len(df6)):
    try:
        j =df5[(df5.barrio==df6.loc[i]["barrio"])]["CantR"].idxmax()
        df6.loc[i, "comuna_ciudadano"]=df5.loc[j,"comuna_ciudadano"]
    except ValueError:
        df6.loc[i, "comuna_ciudadano"]=""
#----FIN DEFINIR TABLA CON "barrio","comuna_ciudadano" SIN DATOS AMBIGUOS

# APLICAR TABLA CON "tipo_de_emprendimiento","idea_negocio" SIN DATOS AMBIGUOS
for i in range(0, len(df)):
#    if pd.isna(df.loc[i,"tipo_de_emprendimiento"]):
        df.loc[i,"tipo_de_emprendimiento"]=str(df4[(df4.idea_negocio==df.loc[i]["idea_negocio"])]["tipo_de_emprendimiento"].values).replace("['","").replace("']","")
# FIN APLICAR TABLA CON "tipo_de_emprendimiento","idea_negocio" SIN DATOS AMBIGUOS

# APLICAR TABLA CON "barrio","comuna_ciudadano" SIN DATOS AMBIGUOS
for i in range(0, len(df)):
#    if pd.isna(df.loc[i,"comuna_ciudadano"]):
        df.loc[i,"comuna_ciudadano"]=str(df6[(df6.barrio==df.loc[i]["barrio"])]["comuna_ciudadano"].values).replace("[","").replace("]","")
# FIN APLICAR TABLA CON "barrio","comuna_ciudadano" SIN DATOS AMBIGUOS

dfnodup=df.drop_duplicates()
"""
def clean_data():

    
    #
    # Inserte su código aquí
    #
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    df=df.dropna(ignore_index=True)

    #-----LIMPIAR STANDARIZAR COLUMNAS DE TEXTO


    df.sexo=df.sexo.str.lower()
    df.tipo_de_emprendimiento=df.tipo_de_emprendimiento.str.lower()
    df.idea_negocio=df.idea_negocio.str.lower()
    df.barrio=df.barrio.str.lower()
    df.línea_credito=df.línea_credito.str.lower()

    df["sexo"]=df["sexo"].astype(str)
    df["tipo_de_emprendimiento"]=df["tipo_de_emprendimiento"].astype(str)
    df["idea_negocio"]=df["idea_negocio"].astype(str)
    df["barrio"]=df["barrio"].astype(str)
    df["línea_credito"]=df["línea_credito"].astype(str)
    df["comuna_ciudadano"]=df["comuna_ciudadano"].astype(str)

    df.sexo=df.sexo.str.replace("_","-").str.replace("-"," ")
    df.tipo_de_emprendimiento=df.tipo_de_emprendimiento.str.replace("_","-").str.replace("-"," ")
    df.idea_negocio=df.idea_negocio.str.replace("_","-").str.replace("-"," ")
    df.barrio=df.barrio.str.replace("_","-").str.replace("-"," ")
    df.línea_credito=df.línea_credito.str.replace("_","-").str.replace("-"," ")
    df.monto_del_credito=df.monto_del_credito.str.replace("$ ", "").str.replace(",", "")
    df["monto_del_credito"]=df["monto_del_credito"].astype(float)

    df.sexo=df.sexo.str.strip()
    df.tipo_de_emprendimiento=df.tipo_de_emprendimiento.str.strip()
    df.idea_negocio=df.idea_negocio.str.strip()
    #df.barrio=df.barrio.str.strip()
    df.línea_credito=df.línea_credito.str.strip()

    df.fecha_de_beneficio=pd.to_datetime(df.fecha_de_beneficio, format="mixed", dayfirst=True)

    #-----LIMPIAR STANDARIZAR COLUMNAS DE TEXTO

    df=df.drop_duplicates()
 
    return df

dff=clean_data()
lis=clean_data().barrio.value_counts().to_list()
