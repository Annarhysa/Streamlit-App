import streamlit as st
import snowflake.connector as sf

def load_data(query):
    conn = sf.connect(
        user = 'anna21',
        password = 'Bombay@123',
        account = 'ZXNUXVJ.SA13369',
        database = 'weather',
        schema = 'public',     
    )

    cur = conn.cursor()

    df_data = cur.execute(query).fetch_pandas_all()

    return df_data

def main():
    df_data = load_data("SELECT "+ 
                        "date, tradingpair, cose, ma_10, ma_20, ma_30, ma_50, ma_100, ma_200, timeframe "+
                        "FROM transform.transform_main "+
                        "WHERE tradingpair = 'BTC-USD" +
                        "order by tradingpair, date;").set_index('DATE')
    
    
    st.header("Visualizing Crypto Data")

    trading_pair_option = st.selectbox('What would you like to plot', df_data['TRADINGPAIR'].unique())

    indicator_option = st.multiselect('Chose indicators to show', ['CLOSE', 'MA_10', 'MA_20', 'MA_30', 'MA_50', 'MA_100', 'MA_200'],
                                      default = ["CLOSE"])
    
    df_data_filtered = df_data[[df_data['TRADINGPAIR'] == trading_pair_option]]
    st.line_chart(df_data_filtered[indicator_option])

if __name__ == '__main__':
    main()