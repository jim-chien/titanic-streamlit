import streamlit as st
import pandas as pd

df = pd.read_csv('train.csv')


def main():
    st.title('Titanic: Machine Learning from Disaster')
    st.image('titanic.jpg', use_column_width=True)
    st.header('Dataset to analyze')
    st.subheader('Dataset info')
    st.text('Dataset shape')
    st.write(df.shape)
    infoDataFrame = df.dtypes.to_frame(name='dtypes')
    infoDataFrame['% of NaN'] = (df.isna().mean().round(4)*100).to_list()
    st.write(infoDataFrame)
    numberOfElementsToShow = st.slider('Number of elements', min_value=5,
                                       max_value=df.shape[0])
    st.dataframe(df.head(numberOfElementsToShow))


if __name__ == '__main__':
    main()
