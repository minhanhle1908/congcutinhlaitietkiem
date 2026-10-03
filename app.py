```python
import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# Tiêu đề
st.title("💰 TÍNH LÃI GỬI TIẾT KIỆM")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

# =========================
# NHẬP THÔNG TIN
# =========================

tien_gui = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=100000000.0,
    step=1000000.0
)

ky_han = st.number_input(
    "Kỳ hạn (tháng)",
    min_value=1,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1
)

hinh_thuc = st.selectbox(
    "Hình thức nhận lãi",
    ["Cuối kỳ", "Hàng tháng", "Hàng quý"]
)

# =========================
# NÚT TÍNH
# =========================

if st.button("TÍNH LÃI"):

    # Đổi lãi suất từ % sang số thập phân
    lai_suat_decimal = lai_suat / 100

    # Tính tổng tiền lãi
    tong_lai = tien_gui * lai_suat_decimal * ky_han / 12

    # Tính tiền lãi định kỳ
    if hinh_thuc == "Cuối kỳ":
        lai_dinh_ky = tong_lai
        ten_ky = "cuối kỳ"

    elif hinh_thuc == "Hàng tháng":
        lai_dinh_ky = tien_gui * lai_suat_decimal / 12
        ten_ky = "tháng"

    else:
        lai_dinh_ky = tien_gui * lai_suat_decimal / 4
        ten_ky = "quý"

    # Tổng tiền gốc + lãi
    tong_tien = tien_gui + tong_lai

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.success("TÍNH TOÁN THÀNH CÔNG!")

    st.subheader("📊 Kết quả")

    st.write(
        "💵 **Tiền lãi định kỳ:** "
        + format(lai_dinh_ky, ",.0f")
        + " VNĐ / "
        + ten_ky
    )

    st.write(
        "📈 **Tổng tiền lãi:** "
        + format(tong_lai, ",.0f")
        + " VNĐ"
    )

    st.write(
        "💰 **Tiền gốc:** "
        + format(tien_gui, ",.0f")
        + " VNĐ"
    )

    st.write(
        "🏦 **Tổng số tiền gốc + lãi:** "
        + format(tong_tien, ",.0f")
        + " VNĐ"
    )

    # =========================
    # THÔNG TIN KHOẢN GỬI
    # =========================

    st.subheader("📋 Thông tin khoản gửi")

    st.write("Số tiền gửi:", format(tien_gui, ",.0f"), "VNĐ")
    st.write("Kỳ hạn:", ky_han, "tháng")
    st.write("Lãi suất:", lai_suat, "%/năm")
    st.write("Hình thức nhận lãi:", hinh_thuc)
```
