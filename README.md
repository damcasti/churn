# 🧠 Predicción de Churn con Árbol de Decisión

Este proyecto permite predecir la probabilidad de fuga de clientes (churn) a partir de datos históricos utilizando un modelo de árbol de decisión entrenado con `scikit-learn`. La interfaz está desarrollada con `Streamlit` y permite subir archivos Excel para procesarlos automáticamente.

## 🚀 Características

- Modelo entrenado con `DecisionTreeClassifier` y balanceo de clases con `SMOTE`.
- Interfaz amigable en `Streamlit`.
- Subida de archivos `.xls` o `.xlsx`.
- Predicción automática del churn para cada registro.
- Descarga de archivo Excel con las predicciones agregadas.

---

## 📁 Estructura del Proyecto

├── app.py # Aplicación principal en Streamlit

├── modelo_churn.joblib # Modelo entrenado guardado con joblib

├── label_encoder_state.joblib # Codificador de la columna 'State'

├── README.md # Documentación del proyecto

├── data/churn.xlsx # data utilizada para entrenamiento y testeo

📄 Formato esperado del archivo Excel

El archivo debe tener las siguientes columnas clave:
Account_Length, Intl_Plan, Vmail_Plan, State, CustServ_Calls, Day_Mins, Eve_Mins, Night_Mins, Intl_Mins, etc.

Algunas columnas serán eliminadas automáticamente:
Phone, Day_Charge, Eve_Charge, Night_Charge, Intl_Charge
Las columnas Intl_Plan y Vmail_Plan deben tener valores "yes" o "no".
La columna State debe coincidir con los valores usados en el entrenamiento original (se aplica codificación con LabelEncoder).

📝 Salida
Una vez procesado el archivo, se genera un nuevo Excel que incluye una nueva columna:
Churn_Predicho: 0 si no hay riesgo de fuga, 1 si hay riesgo de churn.

📌 Notas
Si necesitás reentrenar el modelo, asegurate de guardar nuevamente tanto el modelo_churn.joblib como el label_encoder_state.joblib.
Este proyecto está pensado para demostración o prototipado, no para producción sin mejoras adicionales (como validación avanzada, control de errores, logging, etc.).

# Instalar las dependencias

pip install -r requirements.txt
