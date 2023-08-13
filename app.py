import streamlit as st


st.title("Stock Input")


# Create a radio switch
selected_option = st.radio("Trade type", ["Buy on dip", "Short - Sell"])

st.write("")


col1, col2, col3, col4 = st.columns(4)

with col1:
    selected_stock = st.number_input("Enter Price :")

with col2:
    selected_gap = st.number_input("Enter gap : ")

with col3:
    buy_level = st.selectbox("Buy level", list(range(1, 9)))


with col4:
    sell_level = st.selectbox("sell level", list(range(1, 5)))


q_init = 10

# new_cmp=df[df['SYMBOL']==selected_stock].iloc[0]['CMP']
# gap=df[df['SYMBOL']==selected_stock].iloc[0]['GAP']

rupees_symbol = "\u20B9"

new_cmp = selected_stock
gap = selected_gap




# Display the selected option
if selected_option=="Buy on dip":
    av_sum = 0
    av_count = 0
    sell_lev = []

    st.write("")
    st.write("")
    for i in range(buy_level):
        st.markdown(f'<h5 style="color: grey;">{q_init} @ {round(new_cmp, 2)}</h5>', unsafe_allow_html=True)
        sell_lev.append(new_cmp)
        av_sum = av_sum + (q_init * new_cmp)
        av_count = av_count + q_init
        new_cmp = new_cmp - gap
        q_init = q_init + 10

    average = av_sum / av_count
    profit = sell_lev[sell_level - 1] - average

    st.write("")

    st.markdown(f'<h6 style="color: black; margin-bottom: 0px;">Total Amount: {av_sum:,.2f}</h6>', unsafe_allow_html=True)
    st.markdown(f'<h6 style="color: black; margin-bottom: 0px;">Total Quantity: {av_count:,.2f}</h6>', unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<h5 style="color: black; margin-bottom: 0px;">Average price: {rupees_symbol}{average:,.2f}</h5>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<h5 style="color: black; margin-bottom: 0px;">Profit per share:{rupees_symbol} {profit:,.2f}</h5>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<h5 style="color: black; margin-bottom: 0px;">Total Profit: {rupees_symbol}{(profit * av_count):,.2f}</h5>', unsafe_allow_html=True)
else:
    av_sum = 0
    av_count = 0
    sell_lev = []

    st.write("")
    st.write("")
    for i in range(buy_level):
        st.markdown(f'<h5 style="color: grey;">{q_init} @ {round(new_cmp, 2)}</h5>', unsafe_allow_html=True)
        sell_lev.append(new_cmp)
        av_sum = av_sum + (q_init * new_cmp)
        av_count = av_count + q_init
        new_cmp = new_cmp + gap
        q_init = q_init + 10

    average = av_sum / av_count
    profit = average - sell_lev[sell_level - 1]

    st.write("")

    st.markdown(f'<h6 style="color: black; margin-bottom: 0px;">Total Amount: {av_sum:,.2f}</h6>', unsafe_allow_html=True)
    st.markdown(f'<h6 style="color: black; margin-bottom: 0px;">Total Quantity: {av_count:,.2f}</h6>', unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<h5 style="color: black; margin-bottom: 0px;">Average price: {rupees_symbol}{average:,.2f}</h5>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<h5 style="color: black; margin-bottom: 0px;">Profit per share:{rupees_symbol} {profit:,.2f}</h5>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<h5 style="color: black; margin-bottom: 0px;">Total Profit: {rupees_symbol}{(profit * av_count):,.2f}</h5>', unsafe_allow_html=True)

