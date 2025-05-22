
# app.py

import streamlit as st
import joblib
import numpy as np

# 加载模型
model = joblib.load("model/house_price_model.pkl")

# 页面标题
st.title("🏠 房价预测应用")
st.markdown("输入以下信息以预测加州房价中位数（单位：$100,000）")

# 用户输入
med_inc = st.slider("家庭收入中位数 (MedInc)", 0.0, 20.0, 5.0)
ave_rooms = st.slider("平均房间数 (AveRooms)", 0.5, 10.0, 5.0)
house_age = st.slider("房龄 (HouseAge)", 1, 50, 10)

# 模型预测
if st.button("预测房价"):
    input_data = np.array([[med_inc, ave_rooms, house_age]])
    prediction = model.predict(input_data)[0]
    st.success(f"📈 预测房价中位数为：${prediction * 100000:.2f}")