import streamlit as st

# 이미지 / 동영상을 화면에 보여주기

from PIL import Image

def main() :
    
    img = Image.open('./data/image_03.jpg')

    print(img)

    st.image(img)

    st.image(img, use_column_width = True)

    img_url = 'data:image/jpeg;base64,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'

    st.image(img_url)

    # 동영상

    video_file = open('./data/video1.mp4', 'rb')

    st.video(video_file)

if __name__ == '__main__' :
    main()