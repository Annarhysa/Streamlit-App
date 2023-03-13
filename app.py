import streamlit as st
import snowflake.connector

def load_data(query):
    conn = snowflake.connector.connect(
        user='your-username',
        password='your-password',
        account='your-account-name',
        database='your-database',
        schema='your-schema')

    cur = conn.cursor()

    df_data = cur.execute(query).fetch_pandas_all()
    
    return df_data

def main():

    df_data = load_data("SELECT"+ 
          "date, tradingpair, close, ma_10, ma_20, ma_30, ma_50, ma_100, ma_200, timeframe"+
          "FROM transform.transform_main "+
          "WHERE tradingpair = 'BTC-USD' "+
          "order by tradingpair, date;").set_index('DATE')
    

    st.header("HI")
    st.subheader("Visualizing data with streamlit")
    st.line_chart(df_data['CLOSE'])

if __name__ == '__main__':
    main()
