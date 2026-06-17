import streamlit as st
import pandas as pd

st.set_page_config(page_title="Test Dashboard Fix", layout="wide")
st.title("Test — st.dataframe fix")

data = {
    "PRES": 1.013,
    "TEMP": 25.0,
    "INERTES": {"N2": 0.79, "CO2": 0.05, "H2O": 0.02},
    "FUEL": {"CH4": 85.0, "C2H6": 10.0, "C3H8": 5.0},
}

df_inertes = pd.DataFrame([data["INERTES"]])
df_fuel = pd.DataFrame(
    list(data["FUEL"].items()), columns=["Espèce", "Valeur"]
)

pres, temp = st.columns([1, 6.2])
pres.metric("Pressure", f"{data['PRES']:.2f} bar")
temp.metric("Temperature", f"{data['TEMP']:.2f} °C")

with st.expander("Added Species (mole fraction)", expanded=True):
    st.dataframe(
        df_inertes,
        hide_index=True,
        use_container_width=True,
        column_config={
            col: st.column_config.NumberColumn(col, format="%.2f")
            for col in df_inertes.columns
        }
    )

with st.expander("Fuel Composition (%)", expanded=True):
    st.dataframe(
        df_fuel,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Valeur": st.column_config.NumberColumn("Valeur (%)", format="%.2f")
        }
    )

st.success("✅ Fix correct — les tableaux s'affichent sans erreur !")