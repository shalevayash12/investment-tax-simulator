import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['axes.labelweight'] = 'bold'

st.set_page_config(page_title="סימולטר מס על השקעה", layout="centered")

# עיצוב RTL + רקע בהיר
st.markdown("""
    <style>
    body {
        direction: rtl;
        text-align: right;
        background-color: #F9F9F9;
    }
    .main {
        direction: rtl;
        text-align: right;
        font-family: Arial;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💰 סימולטר מס על השקעה")
st.markdown("בדוק כמה תשלם מס וכמה תרוויח באמת, גם אחרי אינפלציה.")

st.header("הזן את פרטי ההשקעה")
investment = st.number_input("סכום השקעה התחלתי (₪)", value=100000)
years = st.slider("משך ההשקעה (שנים)", 1, 30, 10)
annual_return = st.slider("תשואה שנתית צפויה (%)", 0.0, 25.0, 7.0) / 100
inflation = st.slider("אינפלציה שנתית ממוצעת (%)", 0.0, 10.0, 2.5) / 100
capital_gains_tax = st.slider("מס רווח הון (%)", 0.0, 50.0, 25.0) / 100

nominal_final = investment * ((1 + annual_return) ** years)
profit_nominal = nominal_final - investment
tax_paid = profit_nominal * capital_gains_tax
final_after_tax = nominal_final - tax_paid
real_final = final_after_tax / ((1 + inflation) ** years)
real_profit = real_final - investment

st.header("📊 תוצאה")
st.write(f"שווי עתידי נומינלי: ₪{nominal_final:,.2f}")
st.write(f"רווח נומינלי לאחר מס: ₪{final_after_tax:,.2f}")
st.write(f"שווי ריאלי (מותאם לאינפלציה): ₪{real_final:,.2f}")
st.write(f"רווח ריאלי אמיתי לאחר מס: ₪{real_profit:,.2f}")

st.subheader("📈 השוואה גרפית בין תרחישים")
nominal_vals = [investment * ((1 + annual_return) ** yr) for yr in range(years + 1)]
after_tax_vals = [val - ((val - investment) * capital_gains_tax) for val in nominal_vals]
real_vals = [val / ((1 + inflation) ** yr) for yr, val in enumerate(after_tax_vals)]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(range(years + 1), nominal_vals, label="שווי נומינלי", linewidth=2, color="#1f77b4")
ax.plot(range(years + 1), after_tax_vals, label="אחרי מס", linestyle="--", linewidth=2, color="#ff7f0e")
ax.plot(range(years + 1), real_vals, label="שווי ריאלי", linestyle=":", linewidth=2, color="#2ca02c")
ax.set_xlabel("שנים", fontsize=12)
ax.set_ylabel("שווי השקעה (₪)", fontsize=12)
ax.set_title("התפתחות ההשקעה לאורך זמן", fontsize=14, fontweight='bold')
ax.legend(loc="upper left")
ax.grid(True, linestyle='--', alpha=0.5)

st.pyplot(fig)

st.markdown("---")
st.markdown("רוצה לבחון את תיק ההשקעות שלך בצורה מקצועית?")
st.markdown("[לחץ כאן לקביעת פגישה עם יועץ השקעות](https://skn.co.il)")
