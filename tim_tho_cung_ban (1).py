import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Tìm Thợ Cùng Bạn",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful design
st.markdown("""
<style>
    /* Import beautiful fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@400;500;700&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global styles */
    .main {
        background: linear-gradient(135deg, #fbfaff 0%, #f6f4ff 100%);
    }
    
    /* Navigation Bar Title */
    .navbar-title {
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #6C5CE7 0%, #341F97 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 1rem 0 2rem 0;
    }
    
    /* Hero Section */
    .hero {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #f3f1fd 0%, #e6e1fb 100%);
        border-radius: 30px;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(108, 92, 231, 0.1);
    }
    
    .hero-title {
        text-align: center;
        font-family: 'Montserrat';
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #6C5CE7 0%, #341F97 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
    }

    .hero-title2 {
        font-family: 'Montserrat';
        font-size: 2.5rem;
        font-weight: 750;
        text-align: center;
        background: linear-gradient(135deg, #6C5CE7 0%, #341F97 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
    }

    .hero-title3 {
        font-family: 'Montserrat';
        font-size: 1.8rem;
        font-weight: 730;
        background: linear-gradient(135deg, #6C5CE7 0%, #341F97 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-family: 'Montserrat';
        font-size: 4rem;
        color: #666;
        margin-bottom: 1.5rem;
        font-weight: 600;
        animation: fadeInDown 1s ease;
    }

    .hero-subtitle2 {
        font-family: 'Montserrat';
        font-size: 1.5rem;
        color: #666;
        margin-bottom: 1.5rem;
        font-weight: 700;
        animation: fadeInDown 1s ease;
    }
    
    .hero-description {
        font-family: 'Montserrat';
        font-size: 1.1rem;
        color: #777;
        max-width: 1000px;
        margin: 0 auto 2rem !important;
        line-height: 1.8;
        animation: fadeInDown 1s ease;
    }
    
    /* Buttons */
    .cta-button {
        background: linear-gradient(135deg, #6C5CE7 0%, #341F97 100%);
        color: white;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-family: 'DM Sans', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 6px 25px rgba(108, 92, 231, 0.3);
        display: inline-block;
        margin: 0.5rem;
        text-decoration: none;
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 35px rgba(108, 92, 231, 0.4);
    }
    
    .cta-button-secondary {
        background: white;
        color: #6C5CE7;
        border: 2px solid #6C5CE7;
    }
    
    /* Feature Cards */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 12px 14px;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 2px solid transparent;
        margin-bottom: 24px;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(108, 92, 231, 0.15);
        border-color: #6C5CE7;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 6px;
        text-align: center;
    }
    
    .feature-title {
        font-family: 'Montserrat';
        font-size: 1.5rem;
        font-weight: 650;
        color: #333;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .feature-description {
        font-family: 'Montserrat';
        color: #666;
        line-height: 1.6;
        text-align: center;
    }
    
    /* Restaurant Cards */
    .restaurant-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
        cursor: pointer;
        border: 2px solid transparent;
    }
    
    .restaurant-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(108, 92, 231, 0.15);
        border-color: #6C5CE7;
    }
    
    .restaurant-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .restaurant-address {
        font-family: 'DM Sans', sans-serif;
        color: #666;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    .restaurant-info {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 1rem;
    }
    
    .info-badge {
        background: linear-gradient(135deg, #f3f1fd 0%, #e6e1fb 100%);
        color: #6C5CE7;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    /* Section Titles */
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 900;
        color: #333;
        margin: 3rem 0 2rem 0;
        text-align: center;
    }
    
    /* Filter Section */
    .filter-section {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        margin-bottom: 2rem;
    }
    
    /* Stats Cards */
    .stats-card {
        background: linear-gradient(135deg, #6C5CE7 0%, #341F97 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 6px 25px rgba(108, 92, 231, 0.3);
    }
    
    .stats-number {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Team Cards */
    .team-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .team-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(108, 92, 231, 0.15);
    }
    
    .team-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .team-role {
        font-family: 'DM Sans', sans-serif;
        color: #6C5CE7;
        font-weight: 500;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Form Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #e6e1fb;
        font-family: 'DM Sans', sans-serif;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #6C5CE7;
        box-shadow: 0 0 0 3px rgba(108, 92, 231, 0.1);
    }
    
    /* Streamlit Button Override */
    .stButton > button {
        background: linear-gradient(135deg, #6C5CE7 0%, #341F97 100%);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-family: 'DM Sans', sans-serif;
        font-weight: 700;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(108, 92, 231, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(108, 92, 231, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Dữ liệu về thợ chụp ảnh
restaurants_data = [
    {
        "name": "Nguyễn Bình An",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "<500k",
        "type": ["Wedding"],
        "time": ["3-5 năm"],
        "hours": "0375456289",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"},
        ],
        "reviews": [
            {"name": "Bùi Mai Ngọc", "rating": 4, "content": "Chụp ảnh đẹp, có tâm"},
            {"name": "Ngô Linh Giang", "rating": 3, "content": "Màu ảnh hơi chói"}
        ]
    },
    {
        "name": "Vũ Ngọc Anh",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "500k-1000k",
        "type": ["Sinh nhật"],
        "time": ["<1 năm"],
        "hours": "0344582819",
        "menu": [
            {"dish": "1 giờ", "price": "400k"},
            {"dish": "2 giờ", "price": "750k"}
        ],
        "reviews": [
            {"name": "Phạm Văn Bình", "rating": 4, "content": "Chụp ảnh chuyên nghiệp, trả ảnh chậm"},
            {"name": "Nguyễn Minh Thảo", "rating": 4, "content": "Màu ảnh đẹp, thợ nhiệt tình, tâm lý"}
        ]
    },
{
        "name": "Trương Hùng Sơn",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": ">2000k",
        "type": ["Concept"],
        "time": ["<1 năm"],
        "hours": "0345898207",
        "menu": [
            {"dish": "1 giờ", "price": "200k"},
            {"dish": "2 giờ", "price": "400k"}
        ],
        "reviews": [
            {"name": "Bùi Khánh Chi", "rating": 3, "content": "Thời gian setup lâu, màu ảnh đẹp"},
            {"name": "Bùi Thanh Hải", "rating": 4, "content": "Thợ ảnh nhiệt tình, hỗ trợ tạo dáng"}
        ]
    },
{
        "name": "Nguyễn Vũ Bảo Duy",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "<500k",
        "type": ["Sinh nhật"],
        "time": ["1-3 năm"],
        "hours": "0772540598",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Phan Thị Trà Giang", "rating": 4, "content": "Thợ đến đúng giờ, thiết bị chuyên nghiệp, nhiệt tình"},
            {"name": "Bùi Thanh Hải", "rating": 4, "content": "Ảnh xinh, hậu kỳ cũng đẹp, rcm nha"}
        ]
    },
{
        "name": "Phạm Anh Minh",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": ">2000k",
        "type": ["Sinh nhật"],
        "time": [">5 năm"],
        "hours": "0772540599",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Lê Thục Anh", "rating": 4, "content": "Thợ đến đúng giờ, thiết bị chuyên nghiệp, nhiệt tình"},
            {"name": "Vũ Mai Phương", "rating": 4, "content": ""}
        ]
    },
{
        "name": "Vũ Cao Khánh Linh",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "1500k-2000k",
        "type": ["Ngoại cảnh"],
        "time": ["3-5 năm"],
        "hours": "0772540600",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Khúc Phương Linh", "rating": 4, "content": "Thợ đến đúng giờ, thiết bị chuyên nghiệp, nhiệt tình"},
            {"name": "Trần Thị  Vân Giang", "rating": 4, "content": ""}
        ]
    },
{
        "name": "Nguyễn Mạnh Cường",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "500k-1000k",
        "type": ["Wedding"],
        "time": [">5 năm"],
        "hours": "0772540601",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Phan Vũ Trà My", "rating": 4, "content": "Thợ đến đúng giờ, thiết bị chuyên nghiệp, nhiệt tình"},
            {"name": "Trần Phương Anh", "rating": 4, "content": ""}
        ]
    },
{
        "name": "Phạm Văn Ngọc",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "1000k-1500k",
        "type": ["Sinh nhật"],
        "time": ["1-3 năm"],
        "hours": "0772540602",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Trịnh Phương Thảo", "rating": 4, "content": "Thợ đến đúng giờ, thiết bị chuyên nghiệp, nhiệt tình"},
            {"name": "Đỗ Ngọc Ánh", "rating": 4, "content": ""}
        ]
    },
{
        "name": "Nguyễn Hoàng Khánh Nam",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "<500k",
        "type": ["Tốt nghiệp"],
        "time": [">5 năm"],
        "hours": "0772540603",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Phạm Ngọc Hà", "rating": 4, "content": "Thợ đến đúng giờ, thiết bị chuyên nghiệp, nhiệt tình"},
            {"name": "Lê Phương Mai", "rating": 4, "content": ""}
        ]
    },
{
        "name": "Lê Tùng Anh",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "1000k-1500k",
        "type": ["Kỷ yếu"],
        "time": ["3-5 năm"],
        "hours": "0772540604",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Rating: 4", "rating": 4, "content": "Thợ đến đúng giờ, thiết bị chuyên nghiệp, nhiệt tình"},
            {"name": "Bùi Thanh Hải", "rating": 4, "content": ""}
        ]
    },
{
        "name": "Khúc Gia Bảo",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "1500k-2000k",
        "type": ["Ngoại cảnh"],
        "time": ["<1 năm"],
        "hours": "0772540605",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Phan Thị Trà Giang", "rating": 4, "content": "Thợ đến đúng giờ, thiết bị chuyên nghiệp, nhiệt tình"},
            {"name": "Bùi Thanh Hải", "rating": 4, "content": ""}
        ]
    },
{
        "name": "Nguyễn Minh Quân",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "<500k",
        "type": ["Ngoại cảnh"],
        "time": ["3-5 năm"],
        "hours": "0982345671",
        "menu": [
            {"dish": "1 giờ", "price": "350k"},
            {"dish": "2 giờ", "price": "650k"}
        ],
        "reviews": [
            {"name": "Trần Thị Mai", "rating": 5, "content": "Chụp rất đẹp, chỉnh màu tự nhiên."},
            {"name": "Hoàng Đức", "rating": 4, "content": "Đúng giờ, làm việc chuyên nghiệp."}
        ]
    },
{
        "name": "Trần Gia Huy",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": ">2000k",
        "type": ["Sinh nhật"],
        "time": ["<1 năm"],
        "hours": "0973456782",
        "menu": [
            {"dish": "1 giờ", "price": "600k"},
            {"dish": "2 giờ", "price": "1100k"}
        ],
        "reviews": [
            {"name": "Lê Thu Hà", "rating": 5, "content": "Góc chụp sáng tạo, rất hài lòng."},
            {"name": "Nguyễn Quỳnh", "rating": 4, "content": "Chỉnh ảnh nhanh, nhiệt tình."}
        ]
    },
{
        "name": "Phạm Tuấn Anh",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "500k-1000k",
        "type": ["Kỷ yếu"],
        "time": ["<1 năm"],
        "hours": "0914567893",
        "menu": [
            {"dish": "1 giờ", "price": "400k"},
            {"dish": "2 giờ", "price": "700k"}
        ],
        "reviews": [
            {"name": "Đặng Minh", "rating": 4, "content": "Hướng dẫn tạo dáng rất tốt."},
            {"name": "Vũ Lan", "rating": 5, "content": "Ảnh sắc nét, giao ảnh đúng hẹn."}
        ]
    },
{
        "name": "Lê Hoàng Nam",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "<500k",
        "type": ["Concept"],
        "time": ["3-5 năm"],
        "hours": "935678904",
        "menu": [
            {"dish": "1 giờ", "price": "800k"},
            {"dish": "2 giờ", "price": "1400k"}
        ],
        "reviews": [
            {"name": "Phương Anh", "rating": 5, "content": "Chụp chuyên nghiệp, màu đẹp."},
            {"name": "Minh Khoa", "rating": 4, "content": "Thái độ vui vẻ, hỗ trợ nhiệt tình."},
            {"name": "Huyền Trang", "rating": 5, "content": "Album rất ưng ý."}
        ]
    },
{
        "name": "Đỗ Khánh Linh",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "1000k-1500k",
        "type": ["Sinh nhật"],
        "time": ["3-5 năm"],
        "hours": "966789015",
        "menu": [
            {"dish": "1 giờ", "price": "250k"},
            {"dish": "2 giờ", "price": "450k"}
        ],
        "reviews": [
            {"name": "Thanh Tùng", "rating": 4, "content": "Giá hợp lý, ảnh đẹp."},
            {"name": "Bích Ngọc", "rating": 4, "content": "Chỉnh sửa ảnh cẩn thận."}
        ]
    },
{
        "name": "Vũ Đức Long",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "500k-1000k",
        "type": ["Wedding"],
        "time": ["3-5 năm"],
        "hours": "947890126",
        "menu": [
            {"dish": "1 giờ", "price": "550k"},
            {"dish": "2 giờ", "price": "950k"}
        ],
        "reviews": [
            {"name": "Quỳnh Anh", "rating": 5, "content": "Tư vấn concept rất có tâm."},
            {"name": "Thành Công", "rating": 4, "content": "Chụp nhanh, đúng lịch."}
        ]
    },
{
        "name": "Bùi Hải Đăng",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": ">2000k",
        "type": ["Wedding"],
        "time": ["1-3 năm"],
        "hours": "908901237",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Khánh Vy", "rating": 4, "content": "Màu ảnh đẹp, tự nhiên."},
            {"name": "Văn Sơn", "rating": 5, "content": "Rất thân thiện, dễ hợp tác."}
        ]
    },
{
        "name": "Hoàng Nhật Minh",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "500k-1000k",
        "type": ["Concept"],
        "time": [">5 năm"],
        "hours": "929012348",
        "menu": [
            {"dish": "1 giờ", "price": "750k"},
            {"dish": "2 giờ", "price": "1350k"}
        ],
        "reviews": [
            {"name": "Mai Chi", "rating": 5, "content": "Chất lượng ảnh vượt mong đợi."},
            {"name": "Quốc Bảo", "rating": 4, "content": "Chỉnh màu đẹp, giao ảnh nhanh."}
        ]
    },
{
        "name": "Nguyễn Quốc Bảo",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": ">2000k",
        "type": ["Sinh nhật"],
        "time": ["3-5 năm"],
        "hours": "950123459",
        "menu": [
            {"dish": "1 giờ", "price": "500k"},
            {"dish": "2 giờ", "price": "900k"}
        ],
        "reviews": [
            {"name": "Ngọc Hân", "rating": 5, "content": "Chụp rất có tâm và chuyên nghiệp."},
            {"name": "Đức Huy", "rating": 4, "content": "Tạo không khí thoải mái khi chụp."}
        ]
    },
{
        "name": "Trịnh Minh Khang",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "500k-1000k",
        "type": ["Tốt nghiệp"],
        "time": ["3-5 năm"],
        "hours": "981234560",
        "menu": [
            {"dish": "1 giờ", "price": "350k"},
            {"dish": "2 giờ", "price": "650k"}
        ],
        "reviews": [
            {"name": "Hải Yến", "rating": 4, "content": "Chụp đúng concept mong muốn."},
            {"name": "Minh Tú", "rating": 5, "content": "Ảnh đẹp, xử lý hậu kỳ nhanh."},
            {"name": "Kim Anh", "rating": 4, "content": "Giá hợp lý, đáng trải nghiệm."}
        ]
    },
{
        "name": "Nguyễn Hoàng Anh",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "1000k-1500k",
        "type": ["Tốt nghiệp"],
        "time": ["1-3 năm"],
        "hours": "0971387619",
        "menu": [
            {"dish": "1 giờ", "price": "250k"},
            {"dish": "2 giờ", "price": "500k"}
        ],
        "reviews": [
            {"name": "Phương Thảo", "rating": 4, "content": "Chụp ảnh đẹp, có tâm"},
            {"name": "Minh Phương", "rating": 4, "content": "Màu ảnh xinh, chỉnh sửa theo đúng ý"}
        ]
    },
{
        "name": "Nguyễn Phương Linh",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "500k-1000k",
        "type": ["Wedding"],
        "time": [">5 năm"],
        "hours": "'0334169203",
        "menu": [
            {"dish": "1 giờ", "price": "250k"},
            {"dish": "2 giờ", "price": "450k"}
        ],
        "reviews": [
            {"name": "Minh Thư", "rating": 4, "content": "takecare nhiệt tình, màu ảnh xinh"},
            {"name": "Hà Linh", "rating": 4, "content": "thân thiện, nhiệt tình, chụp có tâm"}
        ]
    },
{
        "name": "Quốc Anh",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "1500k-2000k",
        "type": ["Sinh nhật"],
        "time": ["3-5 năm"],
        "hours": "0976524958",
        "menu": [
            {"dish": "1 giờ", "price": "400k"},
            {"dish": "2 giờ", "price": "800k"}
        ],
        "reviews": [
            {"name": "Gia Bảo", "rating": 5, "content": "nhiều góc chụp đỉnh, màu ảnh đẹp"},
            {"name": "Tường Vy", "rating": 4, "content": "màu ảnh xinh, takecare nhiệt tình, chỉnh dáng đẹp"}
        ]
    },
{
        "name": "Nguyễn Trọng Nghĩa",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "500k-1000k",
        "type": ["Wedding"],
        "time": ["3-5 năm"],
        "hours": "0961120879",
        "menu": [
            {"dish": "1 giờ", "price": "400k"},
            {"dish": "2 giờ", "price": "800k"}
        ],
        "reviews": [
            {"name": "Yến Nhi", "rating": 5, "content": "màu ảnh đẹp, chụp có tâm, thân thiện"},
            {"name": "Vân Anh", "rating": 4, "content": "màu ảnh đẹp, chuyên nghiệp, nhiệt tình"}
        ]
    },
{
        "name": "Hạ Mây",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": ">2000k",
        "type": ["Concept"],
        "time": ["3-5 năm"],
        "hours": "0944860993",
        "menu": [
            {"dish": "1 giờ", "price": "250k"},
            {"dish": "2 giờ", "price": "450k"}
        ],
        "reviews": [
            {"name": "Thu Thủy", "rating": 4, "content": "Ảnh đẹp, xử lý hậu kỳ nhanh"},
            {"name": "Minh Hà", "rating": 4, "content": "Màu ảnh đẹp, chuyên nghiệp, nhiệt tình "}
        ]
    },
{
        "name": "Trịnh Hồng Minh",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "500k-1000k",
        "type": ["Ngoại cảnh"],
        "time": [">5 năm"],
        "hours": "0914502155",
        "menu": [
            {"dish": "1 giờ", "price": "300k"},
            {"dish": "2 giờ", "price": "500k"}
        ],
        "reviews": [
            {"name": "Phương Anh", "rating": 4, "content": "Thái độ vui vẻ, hỗ trợ nhiệt tình"},
            {"name": "Bảo Trâm", "rating": 4, "content": "Thợ đến đúng giờ, thiết bị chuyên nghiệp, nhiệt tình"}
        ]
    },
{
        "name": "Bùi Đức",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "<500k",
        "type": ["Tốt nghiệp"],
        "time": ["1-3 năm"],
        "hours": "0366971180",
        "menu": [
            {"dish": "1 giờ", "price": "400k"},
            {"dish": "2 giờ", "price": "800k"}
        ],
        "reviews": [
            {"name": "Mai Trang", "rating": 4, "content": "màu ảnh đẹp, design ảnh đẹp"},
            {"name": "Bảo Trâm", "rating": 4, "content": "concept chụp đẹp, nhiệt tình"}
        ]
    },
{
        "name": "Trần Ngọc Hoàng Anh",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "1500k-2000k",
        "type": ["Ngoại cảnh"],
        "time": ["<1 năm"],
        "hours": "0336568997",
        "menu": [
            {"dish": "1 giờ", "price": "250k"},
            {"dish": "2 giờ", "price": "500k"}
        ],
        "reviews": [
            {"name": "Linh Chi", "rating": 4, "content": "Chụp ảnh chuyên nghiệp, trả ảnh nhanh"},
            {"name": "Bích Giang", "rating": 4, "content": "Ảnh xinh, hậu kỳ cũng đẹp, rcm nha"}
        ]
    },
{
        "name": "Ngô Xuân Minh",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "1500k-2000k",
        "type": ["Ngoại cảnh"],
        "time": [">5 năm"],
        "hours": "0931355808",
        "menu": [
            {"dish": "1 giờ", "price": "450k"},
            {"dish": "2 giờ", "price": "850k"}
        ],
        "reviews": [
            {"name": "Thanh Hà", "rating": 4, "content": "góc chụp đẹp, nhiệt tình"},
            {"name": "Bích Giang", "rating": 4, "content": "màu ảnh đẹp, hỗ trợ tạo dáng"}
        ]
    },
{
        "name": "Võ Gia Huy",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": ">2000k",
        "type": ["Tốt nghiệp"],
        "time": ["<1 năm"],
        "hours": "0772540606",
        "menu": [
            {"dish": "1 giờ", "price": "200k"},
            {"dish": "2 giờ", "price": "380k"}
        ],
        "reviews": [
            {"name": "Đinh Hải Yến", "rating": 4, "content": "Thợ mát tay, tìm góc chụp rất tốt"},
            {"name": "Tạ Quốc Cường", "rating": 4, "content": "Giá hợp lý, hỗ trợ nhanh."}
        ]
    },
{
        "name": "Cao Nhật Minh",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "1000k-1500k",
        "type": ["Tốt nghiệp"],
        "time": ["3-5 năm"],
        "hours": "0774640607",
        "menu": [
            {"dish": "1 giờ", "price": "280k"},
            {"dish": "2 giờ", "price": "520k"}
        ],
        "reviews": [
            {"name": "Hồ Ngọc Anh", "rating": 5, "content": "Tay nghề cao, hoàn thành công việc tốt"},
            {"name": "Lâm Tuấn Kiệt", "rating": 4, "content": "Phục vụ rất nhiệt tình."}
        ]
    },
{
        "name": "Dương Minh Khang",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "500k-1000k",
        "type": ["Concept"],
        "time": ["<1 năm"],
        "hours": "0772870608",
        "menu": [
            {"dish": "1 giờ", "price": "350k"},
            {"dish": "2 giờ", "price": "650k"}
        ],
        "reviews": [
            {"name": "Trịnh Bảo Châu", "rating": 4, "content": "Thiết bị đầy đủ, làm việc chuyên nghiệp."},
            {"name": "Phùng Đức Thành", "rating": 4, "content": "Đúng hẹn và uy tín."}
        ]
    },
{
        "name": "Tô Hoàng Phúc",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": ">2000k",
        "type": ["Sinh nhật"],
        "time": ["<1 năm"],
        "hours": "0772540653",
        "menu": [
            {"dish": "1 giờ", "price": "450k"},
            {"dish": "2 giờ", "price": "850k"}
        ],
        "reviews": [
            {"name": "Vũ Khánh Hòa", "rating": 5, "content": "Chất lượng dịch vụ rất tốt."},
            {"name": "Hà Minh Quân", "rating": 4, "content": "Thợ tận tâm, làm việc sạch sẽ."}
        ]
    },
{
        "name": "Chu Quốc Bảo",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": ">2000k",
        "type": ["Ngoại cảnh"],
        "time": ["1-3 năm"],
        "hours": "0776156051",
        "menu": [
            {"dish": "1 giờ", "price": "550k"},
            {"dish": "2 giờ", "price": "1.000k"}
        ],
        "reviews": [
            {"name": "Bạch Thu Hiền", "rating": 4, "content": "Thao tác cẩn thận."},
            {"name": "Kiều Thanh Sơn", "rating": 4, "content": "Giá hợp lý."}
        ]
    },
{
        "name": "Lý Thành Công",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": "1000k-1500k",
        "type": ["Sinh nhật"],
        "time": ["<1 năm"],
        "hours": "0306164043",
        "menu": [
            {"dish": "1 giờ", "price": "700k"},
            {"dish": "2 giờ", "price": "1.300k"}
        ],
        "reviews": [
            {"name": "Ninh Thảo Vy", "rating": 5, "content": "Tay nghề xuất sắc."},
            {"name": "Quách Minh Duy", "rating": 4, "content": "Tư vấn kỹ."}
        ]
    },
{
        "name": "Tăng Đức Anh",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "1500k-2000k",
        "type": ["Tốt nghiệp"],
        "time": ["<1 năm"],
        "hours": "0873485345",
        "menu": [
            {"dish": "1 giờ", "price": "250k"},
            {"dish": "2 giờ", "price": "450k"}
        ],
        "reviews": [
            {"name": "Cấn Mai Hương", "rating": 4, "content": "Hỗ trợ nhanh."},
            {"name": "Hứa Quốc Việt", "rating": 4, "content": "Dịch vụ ổn định."}
        ]
    },
{
        "name": "Tôn Hải Nam",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "1000k-1500k",
        "type": ["Sinh nhật"],
        "time": ["<1 năm"],
        "hours": "0733461723",
        "menu": [
            {"dish": "1 giờ", "price": "650k"},
            {"dish": "2 giờ", "price": "1.200k"}
        ],
        "reviews": [
            {"name": "Ôn Bích Ngọc", "rating": 5, "content": "Kinh nghiệm lâu năm."},
            {"name": "Chế Anh Tuấn", "rating": 4, "content": "Hiệu quả."}
        ]
    },
{
        "name": "Hứa Minh Trí",
        "address": "Hà Nội",
        "distance": "Hà Nội",
        "price": ">2000k",
        "type": ["Tốt nghiệp"],
        "time": ["<1 năm"],
        "hours": "0734751848",
        "menu": [
            {"dish": "1 giờ", "price": "320k"},
            {"dish": "2 giờ", "price": "600k"}
        ],
        "reviews": [
            {"name": "Mạc Phương Linh", "rating": 4, "content": "Đến đúng giờ."},
            {"name": "Âu Thanh Bình", "rating": 4, "content": "Hài lòng."}
        ]
    },
{
        "name": "Đinh Quốc Hưng",
        "address": "TP.HCM",
        "distance": "TP.HCM",
        "price": "<500k",
        "type": ["Ngoại cảnh"],
        "time": ["1-3 năm"],
        "hours": "0473517237",
        "menu": [
            {"dish": "1 giờ", "price": "850k"},
            {"dish": "2 giờ", "price": "1.600k"}
        ],
        "reviews": [
            {"name": "La Ngọc Diễm", "rating": 5, "content": "Dịch vụ cao cấp."},
            {"name": "Doãn Hoàng Long", "rating": 4, "content": "Đáng tin cậy."}
        ]
    }
]

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_restaurant' not in st.session_state:
    st.session_state.selected_restaurant = None
if 'filters' not in st.session_state:
    st.session_state.filters = {
        'distance': 'Tất cả',
        'price': 'Tất cả',
        'type': 'Tất cả',
        'time': 'Tất cả'
    }

st.markdown("""
<style>
/* Style cho button trong navbar */
div[data-testid="column"] button {
    font-family: 'Montserrat', sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: #ffffff;
    background-color: #6C5CE7;
    border-radius: 12px;
    padding: 12px 0;
    border: none;
}

/* Hover effect */
div[data-testid="column"] button:hover {
    background-color: #4834B8;
    color: #ffffff;
}

/* Button đang được click */
div[data-testid="column"] button:focus {
    box-shadow: 0 0 0 0.2rem rgba(108, 92, 231, 0.4);
}
</style>
""", unsafe_allow_html=True)

# Navigation function
def navigate_to(page):
    st.session_state.page = page
    # Only keep selected_restaurant if going to detail page
    if page != 'detail':
        st.session_state.selected_restaurant = None
    st.rerun()

# Navigation Bar
def render_navbar():
    # Title
    st.markdown('<div class="navbar-title">📷 TÌM THỢ CÙNG BẠN</div>', unsafe_allow_html=True)
    
    # Navigation buttons
    pages = {
        'home': 'Trang chủ',
        'search': 'Tìm thợ',
        'about': 'Về dự án',
        'contribute': 'Đóng góp'
    }
    
    cols = st.columns(len(pages))
    for i, (page_key, page_name) in enumerate(pages.items()):
        with cols[i]:
            if st.button(page_name, key=f"nav_{page_key}", use_container_width=True):
                navigate_to(page_key)

# Page 1: Home
def render_home():
    # Hero Section
    st.markdown("""
    <div class="hero">
        <div class="hero-title2">Giới thiệu nhanh</div>
        <div class="hero-subtitle2">Nền tảng kết nối bạn với thợ chụp ảnh phù hợp quanh khu vực của bạn</div>
        <p class="hero-description">
            "Tìm Thợ Cùng Bạn" là nền tảng giúp bạn, đặc biệt là các bạn trẻ và sinh viên, nhanh chóng tìm được thợ chụp ảnh phù hợp dựa trên mức giá, thời gian rảnh, khoảng cách và đánh giá thực tế từ những khách hàng đã trải nghiệm.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # About Preview
    st.markdown('<div class="hero-title2">Đặc điểm nổi bật</div>', unsafe_allow_html=True)
    
    preview_cols = st.columns(4)
    previews = [
        ("⚡", "Tìm thợ chụp ảnh nhanh chóng"),
        ("📸", "Hồ sơ thợ được xác thực thực tế"),
        ("💰", "Phù hợp mọi mức ngân sách"),
        ("✨", "Giao diện đơn giản, dễ sử dụng")
    ]
    
    for col, (icon, text) in zip(preview_cols, previews):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <p class="feature-description">{text}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown('<div class="hero-title2">Các tính năng chính</div>', unsafe_allow_html=True)
    
    features = [
        {
            "icon": "🔍",
            "title": "Tìm kiếm thông minh",
            "description": "Lọc thợ chụp ảnh theo nhiều tiêu chí."
        },
        {
            "icon": "📍",
            "title": "Bản đồ vị trí",
            "description": "Xem vị trí thợ chụp ảnh và khoảng cách tới bạn."
        },
        {
            "icon": "⭐",
            "title": "Review thực tế",
            "description": "Đánh giá trực tiếp từ khách hàng, không quảng cáo."
        },
        {
            "icon": "⏱",
            "title": "Gợi ý theo thời gian",
            "description": "Gợi ý thợ nhận lịch chụp sáng, trưa, chiều."
        }
    ]
    
    feature_cols = st.columns(2)
    for idx, feature in enumerate(features):
        with feature_cols[idx % 2]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature['icon']}</div>
                <div class="feature-title">{feature['title']}</div>
                <p class="feature-description">{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)

# Page 2: Search/Explore
def render_search():
    st.markdown('<div class="hero-title3">Bộ lọc</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        distance_filter = st.selectbox(
            "Thành phố",
            ["Tất cả", "Hà Nội", "TP.HCM"],
            key="distance_filter"
        )
    
    with col2:
        price_filter = st.selectbox(
            "Mức giá",
            ["Tất cả", "<500k", "500k-1000k", "1000k-1500k", "1500k-2000k", ">2000k"],
            key="price_filter"
        )
    
    with col3:
        type_filter = st.selectbox(
            "Thể loại chụp",
            ["Tất cả", "Tốt nghiệp", "Sinh nhật", "Kỷ yếu", "Concept", "Ngoại cảnh", "Wedding"],
            key="type_filter"
        )
    
    with col4:
        time_filter = st.selectbox(
            "Số năm kinh nghiệm",
            ["Tất cả", "<1 năm", "1-3 năm", "3-5 năm", ">5 năm"],
            key="time_filter"
        )
    
    if st.button("Áp dụng bộ lọc", use_container_width=True):
        st.session_state.filters = {
            'distance': distance_filter,
            'price': price_filter,
            'type': type_filter,
            'time': time_filter
        }
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Filter restaurants
    filtered_restaurants = restaurants_data.copy()
    
    if st.session_state.filters['distance'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if r['distance'] == st.session_state.filters['distance']]
    
    if st.session_state.filters['price'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if r['price'] == st.session_state.filters['price']]
    
    if st.session_state.filters['type'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if st.session_state.filters['type'] in r['type']]
    
    if st.session_state.filters['time'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if st.session_state.filters['time'] in r['time']]
    
    # Display results
    st.markdown(
        f'''
        <div class="hero-title3">
            Kết quả ({len(filtered_restaurants)} thợ chụp ảnh)
        </div>
        ''',
        unsafe_allow_html=True
    )
        
    if len(filtered_restaurants) == 0:
        st.info("Không tìm thấy thợ chụp ảnh nào phù hợp với bộ lọc của bạn. Hãy thử thay đổi tiêu chí tìm kiếm!")
    else:
        for restaurant in filtered_restaurants:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"""
                <div class="restaurant-card">
                    <h3 class="restaurant-name">{restaurant['name']}</h3>
                    <p class="restaurant-address">📍 {restaurant['address']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                # Use unique key for each button and store restaurant data before navigating
                if st.button("Xem chi tiết", key=f"view_{restaurant['name']}", use_container_width=True):
                    st.session_state.selected_restaurant = restaurant
                    st.session_state.page = 'detail'
                    st.rerun()

# Page 3: Restaurant Detail
def render_detail():
    if st.session_state.selected_restaurant is None:
        st.markdown('<h2 class="section-title">Chưa chọn thợ</h2>', unsafe_allow_html=True)
        st.info("Vui lòng chọn một thợ chụp ảnh từ trang Tìm thợ để xem chi tiết!")
        st.markdown('<div style="height: 1rem;"></div>', unsafe_allow_html=True)
        if st.button("Đi đến trang Tìm thợ", use_container_width=True):
            navigate_to('search')
        return
    
    restaurant = st.session_state.selected_restaurant
    
    # Back button
    if st.button("<-  Quay lại danh sách"):
        navigate_to('search')
    
    st.markdown(f'<h2 class="section-title">{restaurant["name"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; color: #666; font-size: 1.1rem; margin-top: -1rem;">📍 {restaurant["address"]}</p>', unsafe_allow_html=True)
    
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    
    # Thông tin chi tiết
    st.markdown('<h3 style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; margin-bottom: 1rem;">Thông tin chi tiết</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Thành phố:</p>
            <p style="font-family: 'DM Sans', sans-serif; color: #666;">{restaurant['distance']}  </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Mức giá:</p>
            <p style="font-family: 'DM Sans', sans-serif; color: #666;">{restaurant['price']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Số điện thoại:</p>
            <p style="font-family: 'DM Sans', sans-serif; color: #666;">{restaurant['hours']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="margin-bottom: 1rem;">
        <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Thể loại chụp:</p>
        <p style="font-family: 'DM Sans', sans-serif; color: #666;">{', '.join(restaurant['type'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    
    # Bảng giá dịch vụ tiêu biểu
    st.markdown('<h3 style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; margin-bottom: 1rem;">Bảng giá dịch vụ</h3>', unsafe_allow_html=True)
    
    for item in restaurant['menu']:
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.8rem 0; border-bottom: 1px solid #f0f0f0;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 1.2rem;">📸</span>
                <span style="font-family: 'DM Sans', sans-serif; color: #333; font-size: 1rem;">{item['dish']}</span>
            </div>
            <span style="font-family: 'DM Sans', sans-serif; color: #6C5CE7; font-weight: 700; font-size: 1.1rem;">{item['price']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    
    # Đánh giá từ khách hàng
    st.markdown('<h3 style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; margin-bottom: 1rem;">Đánh giá từ khách hàng</h3>', unsafe_allow_html=True)

    for review in restaurant["reviews"]:
        stars = "⭐" * review["rating"]

        st.markdown(f"""
        <div style="margin-bottom: 1.5rem;">
            <div style="margin-bottom: 0.5rem;">
                <span style="color:#ffa500; font-size:1.2rem;">
                    {stars}
                </span>
                <span style="font-weight:700; margin-left:0.5rem;">
                    - {review["name"]}
                </span>
            </div>
            <p style="color:#666; font-style:italic;">
                "{review["content"]}"
            </p>
        </div>
        """, unsafe_allow_html=True)

# Page 4: About Project
def render_about():
    st.markdown('<div class="hero-title3">Giới thiệu dự án</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="feature-card">
        <p class="feature-description">
            "Tìm Thợ Cùng Bạn" là dự án được xây dựng nhằm hỗ trợ mọi người lựa chọn thợ chụp ảnh phù hợp 
            quanh khu vực sinh sống. Dự án xuất phát từ nhu cầu thực tế của người dùng, đặc biệt là những ai 
            mới tìm hiểu, gặp khó khăn trong việc tìm thợ chụp ảnh phù hợp với ngân sách 
            và thời gian rảnh của mình.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="hero-title3">Mục tiêu</div>', unsafe_allow_html=True)
    
    goals = [
        "Hỗ trợ người dùng tìm thợ chụp ảnh trong bán kính 0–2km",
        "Cho phép lọc theo giá, thể loại chụp, thời gian",
        "Cung cấp thông tin ngắn gọn, tập trung trải nghiệm thật",
        "Áp dụng kiến thức Python vào sản phẩm thực tế"
    ]
    
    for goal in goals:
        st.markdown(f"""
        <div class="restaurant-card">
            <p class="feature-description">{goal}</p>
        </div>
        """, unsafe_allow_html=True)
    
# Page 5: Contribute
def render_contribute():
    st.markdown('<div class="hero-title3">Đánh giá</div>', unsafe_allow_html=True)
    st.write("Đóng góp thông tin thợ chụp ảnh tại đây!")
    st.link_button(
        "📋 Điền Google Form",
        "https://docs.google.com/forms/d/e/1FAIpQLSdcoRypiVHZq5tAarzI_ou-fYJ_UHr0yDDiPFWwIs8Io8gRcQ/viewform?usp=header"
    )
    with st.form("contribute_form"):
        st.markdown('<div class="hero-title3">Thông tin thợ chụp ảnh</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Tên thợ / studio *", placeholder="VD: Nam Studio")
            address = st.text_input("Địa chỉ *", placeholder="VD: 123 Chùa Láng, Đống Đa")
            price = st.selectbox("Giá trung bình *", ["<30k", "30-50k", ">50k"])
        
        with col2:
            food_type = st.multiselect(
                "Thể loại chụp *",
                ["Cơm/Xôi/Cháo", "Bún/Phở/Miến/Bánh canh/Súp", "Gà/Thịt chiên", "Đồ Hàn", "Nem nướng", "Bánh mì pate/chảo/muối ớt", "Bánh tráng", "Tacos", "Bánh cuốn"],
            )
            time_slots = st.multiselect(
                "Số năm kinh nghiệm *",
                ["Sáng", "Trưa", "Tối", "Khuya"]
            )
            rating = st.slider("Đánh giá của bạn", 1.0, 5.0, 4.0, 0.5)
        
        review = st.text_area(
            "Đánh giá ngắn *",
            placeholder="Chia sẻ trải nghiệm của bạn về thợ chụp ảnh này...",
            height=150
        )
        
        submit = st.form_submit_button("Gửi đánh giá", use_container_width=True)
        
        if submit:
            if name and address and food_type and time_slots and review:
                st.success("Cảm ơn bạn đã đóng góp! Thông tin của bạn đã được ghi nhận.")
                st.balloons()
            else:
                st.error("Vui lòng điền đầy đủ các thông tin bắt buộc (*)")

# Main App Logic
def main():
    render_navbar()
    
    # Route to appropriate page
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'search':
        render_search()
    elif st.session_state.page == 'detail':
        render_detail()
    elif st.session_state.page == 'about':
        render_about()
    elif st.session_state.page == 'contribute':
        render_contribute()

if __name__ == "__main__":
    main()
