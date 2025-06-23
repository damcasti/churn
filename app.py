import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import io

# Cargar modelo y label encoder
model = joblib.load("modelo_churn.joblib")
le_state = joblib.load("label_encoder_state.joblib")

st.title("Predicción de Churn - Subí tu archivo Excel")

# Subida de archivo
uploaded_file = st.file_uploader("Cargá el archivo Excel", type=["xls", "xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        # Preprocesamiento (igual que en el entrenamiento)
        df = df.drop(columns=["Phone", "Day_Charge", "Eve_Charge", "Night_Charge", "Intl_Charge"], errors="ignore")
        df["Intl_Plan"] = df["Intl_Plan"].map({"yes": 1, "no": 0})
        df["Vmail_Plan"] = df["Vmail_Plan"].map({"yes": 1, "no": 0})

        if "State" in df.columns:
            df["State"] = le_state.transform(df["State"])

        # Verificamos que 'Churn' no esté (modelo ya predice eso)
        if "Churn" in df.columns:
            df = df.drop(columns=["Churn"])

        # Predecimos
        pred = model.predict(df)

        df_resultado = df.copy()
        df_resultado["Churn_Predicho"] = pred

        st.success("Predicción completada. Descargá el archivo con la columna `Churn_Predicho`.")

        # Descarga como Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df_resultado.to_excel(writer, index=False, sheet_name='Resultados')
        st.download_button(
            label="📥 Descargar Excel con resultados",
            data=output.getvalue(),
            file_name="predicciones_churn.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"Ocurrió un error: {str(e)}")
