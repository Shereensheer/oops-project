import streamlit as st
import requests
from io import BytesIO

# ===================== 🎨 PAGE CONFIG ===================== #
st.set_page_config(page_title="Multi Image Generator", page_icon="🖼️", layout="centered")

# ===================== 🧠 BASE CLASS ===================== #
class BaseImageGenerator:
    def __init__(self, keyword: str, count: int = 1):
        self.keyword = keyword
        self.count = count

    def fetch_image_urls(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

# ===================== 🌐 INHERITED CLASS ===================== #
class UnsplashImageGenerator(BaseImageGenerator):
    def __init__(self, keyword: str, access_key: str, count: int = 1):
        super().__init__(keyword, count)
        self.__access_key = access_key

    def fetch_image_urls(self):
        url = f"https://api.unsplash.com/photos/random?query={self.keyword}&count={self.count}&client_id={self.__access_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [img['urls']['regular'] for img in data]
        else:
            return []

# ===================== 🔐 ACCESS KEY ===================== #
UNSPLASH_ACCESS_KEY = "HoyslQw_k6vhALjtEiNJyGPYHS0dPApQ99cftcMWTBM"  

# ===================== 🖼 UI ===================== #
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>🖼️ Multi Image Generator</h1>
    <p style='text-align: center; color: gray;'>Enter a keyword and select how many images you want!</p>
    <hr style='margin-top: 0;'>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    keyword = st.text_input("🔍 What images are you looking for?", placeholder="e.g. mountains, cats, stars")
with col2:
    count = st.slider("🖼️ Number of Images", min_value=1, max_value=10, value=3)

generate = st.button("✨ Generate Images")

# Logic
if generate:
    if keyword:
        with st.spinner("🔄 Fetching images..."):
            generator = UnsplashImageGenerator(keyword, UNSPLASH_ACCESS_KEY, count)
            image_urls = generator.fetch_image_urls()

        if image_urls:
            st.success(f"✅ Found {len(image_urls)} image(s) for '{keyword}'")
            cols = st.columns(2)
            for i, img_url in enumerate(image_urls):
                with cols[i % 2]:
                    st.image(img_url, use_column_width=True)
                    try:
                        img_data = requests.get(img_url).content
                        buffer = BytesIO(img_data)
                        st.download_button(
                            label="⬇️ Download Image",
                            data=buffer,
                            file_name=f"{keyword}_{i+1}.jpg",
                            mime="image/jpeg"
                        )
                    except:
                        st.warning("⚠️ Download failed.")
        else:
            st.error("❌ No images found. Try a different keyword.")
    else:
        st.warning("⚠️ Please enter a keyword to continue.")

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 13px; color: gray;'>
        Built by Shereen Ahmed ❤️ 
    </div>
""", unsafe_allow_html=True)

