import streamlit as st
from database import add_expense,view_expenses,total_expense,Dashboard

st.set_page_config(page_title="AI Expense Tracker", page_icon="💰")

st.title("💰 AI Expense Tracker")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Home", "Add Expense", "View Expense", "AI Analysis","Dashboard"]
)

if menu == "Home":
    st.header("Welcome")
    st.write("Track your income and expenses easily.")

elif menu == "Add Expense":
    st.header("Add Expense")

    expense_type = st.selectbox("Type", ["Income", "Expense"])
    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Salary", "Other"]
    )
    amount = st.number_input("Amount", min_value=0.0)
    date = st.date_input("Date")
    note = st.text_input("Note")

    if st.button("Save Expense"):
       add_expense(expense_type, category, amount, date, note)
       st.success("Expense Saved Successfully!")

elif menu == "View Expense":
    st.header("View Expenses")

    expenses = view_expenses()

    if expenses:
        st.table(expenses)
    else:
        st.warning("No Expenses Found")

elif menu == "Dashboard":
    st.header("📊 Dashboard")

    income, expense = Dashboard()

    st.metric("💰 Total Income", f"₹ {income}")
    st.metric("💸 Total Expense", f"₹ {expense}")
    st.metric("💵 Balance", f"₹ {income - expense}")

elif menu == "AI Analysis":
    st.header("🤖 AI Analysis")

    income, expense = total_expense()

    st.write("💰 Total Income :", income)
    st.write("💸 Total Expense :", expense)

    if expense > income:
        st.error("⚠️ You are spending more than your income.")
    elif income > expense:
        st.success("🎉 Great! You are saving money.")
    else:
        st.info("Income and Expense are equal.")        
