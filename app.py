import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="APP CÔNG CỤ TÍNH TIỀN GỬI TIẾT KIỆM_LÊ THỊ MINH ANH",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰 APP CÔNG CỤ TÍNH TIỀN GỬI TIẾT KIỆM_LÊ THỊ MINH ANH")
st.write("Nhập thông tin khoản tiền gửi để tính số tiền lãi và tổng số tiền nhận được.")

st.divider()

# =========================
# NHẬP DỮ LIỆU
# =========================

# Số tiền gửi
tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0,
    value=100_000_000,
    step=1_000_000,
    format="%d"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# =========================
# TÍNH TOÁN
# =========================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Chuyển lãi suất % sang số thập phân
    lai_suat_nam = lai_suat / 100

    # Đổi kỳ hạn từ tháng sang năm
    so_nam = ky_han / 12

    # Tổng tiền lãi theo công thức:
    # Tiền lãi = Tiền gốc × Lãi suất năm × Số năm
    tong_lai = tien_gui * lai_suat_nam * so_nam

    # =========================
    # TÍNH LÃI ĐỊNH KỲ
    # =========================

    if hinh_thuc == "Cuối kỳ":
        lai_dinh_ky = tong_lai
        so_ky = 1
        don_vi = "cuối kỳ"

    elif hinh_thuc == "Hàng tháng":
        lai_dinh_ky = tien_gui * lai_suat_nam / 12
        so_ky = ky_han
        don_vi = "tháng"

    else:  # Hàng quý
        lai_dinh_ky = tien_gui * lai_suat_nam / 4
        so_ky = ky_han / 3
        don_vi = "quý"

    # Tổng số tiền nhận được
    tong_tien = tien_gui + tong_lai

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.subheader("📊 Kết quả")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="💰 Tiền lãi định kỳ",
            value=f"{lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            label="📈 Tổng tiền lãi",
            value=f"{tong_lai:,.0f} VNĐ"
        )

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            label="💵 Tiền gốc",
            value=f"{tien_gui:,.0f} VNĐ"
        )

    with col4:
        st.metric(
            label="🏦 Tổng số tiền nhận được",
            value=f"{tong_tien:,.0f} VNĐ"
        )

    st.divider()

    # =========================
    # CHI TIẾT KHOẢN GỬI
    # =========================

    st.subheader("📋 Chi tiết khoản gửi")

    st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")
    st.write(f"**Tiền lãi mỗi {don_vi}:** {lai_dinh_ky:,.0f} VNĐ")
    st.write(f"**Tổng tiền lãi:** {tong_lai:,.0f} VNĐ")
    st.write(f"**Tổng tiền gốc + lãi:** {tong_tien:,.0f} VNĐ")

    # =========================
    # CÔNG THỨC
    # =========================

    with st.expander("📐 Xem công thức tính"):

        st.write(
            "**Tổng tiền lãi = Tiền gốc × Lãi suất năm × Số năm**"
        )

        st.write(
            f"= {tien_gui:,.0f} × {lai_suat_nam:.4f} × {so_nam:.2f}"
        )

        st.write(
            f"= **{tong_lai:,.0f} VNĐ**"
        )

        if hinh_thuc == "Hàng tháng":
            st.write(
                "**Lãi hàng tháng = Tiền gốc × Lãi suất năm ÷ 12**"
            )

        elif hinh_thuc == "Hàng quý":
            st.write(
                "**Lãi hàng quý = Tiền gốc × Lãi suất năm ÷ 4**"
            )

        else:
            st.write(
                "**Lãi cuối kỳ = Tổng tiền lãi của toàn bộ kỳ hạn**"
            )
