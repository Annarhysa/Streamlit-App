import streamlit as st
import snowflake.connector as sf

def load_data(query):
    conn = sf.connect(
        user = 'anna21',
        password = 'Bombay@123',
        account = 'ZXNUXVJ.SA13369',
        database = 'SNOWFLAKE_SAMPLE_DATA',
        schema = 'WEATHER',     
    )

    cur = conn.cursor()

    df_data = cur.execute(query).fetch_pandas_all()

    return df_data

def main():
    df_data = load_data( " SELECT AVG(temperature) AS avg_temp
                        FROM weather_data
                        WHERE date BETWEEN '2022-01-01' AND '2022-01-31')
    
    
    st.header("Visualizing Crypto Data")

    trading_pair_option = st.selectbox('What would you like to plot', df_data['TRADINGPAIR'].unique())

    indicator_option = st.multiselect('Chose indicators to show', ['CLOSE', 'MA_10', 'MA_20', 'MA_30', 'MA_50', 'MA_100', 'MA_200'],
                                      default = ["CLOSE"])
    
    df_data_filtered = df_data[[df_data['TRADINGPAIR'] == trading_pair_option]]
    st.line_chart(df_data_filtered[indicator_option])

if __name__ == '__main__':
    main()