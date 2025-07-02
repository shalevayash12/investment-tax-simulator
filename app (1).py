
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="סימולטר מס על השקעה", layout="centered")
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

st.subheader("השוואה גרפית")
nominal_vals = [investment * ((1 + annual_return) ** yr) for yr in range(years + 1)]
after_tax_vals = [val - ((val - investment) * capital_gains_tax) for val in nominal_vals]
real_vals = [val / ((1 + inflation) ** yr) for yr, val in enumerate(after_tax_vals)]

fig, ax = plt.subplots()
ax.plot(nominal_vals, label="שווי נומינלי", linewidth=2)
ax.plot(after_tax_vals, label="אחרי מס", linestyle="--")
ax.plot(real_vals, label="שווי ריאלי", linestyle=":")
ax.set_xlabel("שנים")
ax.set_ylabel("שווי השקעה (₪)")
ax.set_title("צמיחה נומינלית מול ריאלית")
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.markdown("---")
st.markdown("רוצה לבחון את תיק ההשקעות שלך בצורה מקצועית?")
st.markdown("[לחץ כאן לקביעת פגישה עם יועץ השקעות](https://skn.co.il)")
