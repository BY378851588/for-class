# app.py

import streamlit as st
import joblib
import numpy as np

# ✅ 修改这里：路径改为当前根目录下
model = joblib.load("house_price_model.pkl")

st.title("🏠 房价预测应用")
st.markdown("输入以下信息以预测加州房价中位数（单位：$100,000）")

med_inc = st.slider("家庭收入中位数 (MedInc)", 0.0, 20.0, 5.0)
ave_rooms = st.slider("平均房间数 (AveRooms)", 0.5, 10.0, 5.0)
house_age = st.slider("房龄 (HouseAge)", 1, 50, 10)

if st.button("预测房价"):
    input_data = np.array([[med_inc, ave_rooms, house_age]])
    prediction = model.predict(input_data)[0]
    st.success(f"📈 预测房价中位数为：${prediction * 100000:.2f}")