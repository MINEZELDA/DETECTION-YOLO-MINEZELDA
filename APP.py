from pathlib import Path
import PIL
import streamlit as st
import SETTING
import HELPER
st.set_page_config(
    page_title="การตรวจจับและติดตามวัตถุโดยใช้YOLOV11",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("การตรวจจับและติดตามวัตถุโดยใช้YOLOV11")
st.sidebar.header("การกำหนดค่าโมเดลYOLOV11")
model_type = st.sidebar.radio(
    "เลือกกระบวนการ", ['การตรวจจับ', 'การแบ่งส่วน'])
confidence = float(st.sidebar.slider(
    "เลือกความเชื่อมั่นของแบบจำลอง", 25, 100, 40)) / 100
if model_type == 'การตรวจจับ':
    model_path = Path(SETTING.DETECTION_MODEL)
elif model_type == 'การแบ่งส่วน':
    model_path = Path(SETTING.SEGMENTATION_MODEL)
try:
    model = HELPER.load_model(model_path)
except Exception as ex:
    st.error(f"ไม่สามารถโหลดโมเดลได้ ตรวจสอบเส้นทางที่ระบุ: {model_path}")
    st.error(ex)
st.sidebar.header("การกำหนดค่ารูปภาพ/วิดีโอ")
source_radio = st.sidebar.radio(
    "เลือกแหล่งที่มา", SETTING.SOURCES_LIST)
source_img = None
if source_radio == SETTING.IMAGE:
    source_img = st.sidebar.file_uploader(
        "เลือกภาพ...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    col1, col2 = st.columns(2)
    with col1:
        try:
            if source_img is None:
                default_image_path = str(SETTING.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="รูปภาพเริ่มต้น",
                         use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="รูปภาพที่อัปโหลด",
                         use_column_width=True)
        except Exception as ex:
            st.error("เกิดข้อผิดพลาดขณะเปิดรูปภาพ")
            st.error(ex)
    with col2:
        if source_img is None:
            default_detected_image_path = str(SETTING.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='ภาพที่ตรวจพบ',
                     use_column_width=True)
        else:
            if st.sidebar.button('วัตถุการตรวจจับ'):
                res = model.predict(uploaded_image,
                                    conf=confidence
                                    )
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='ภาพที่ตรวจพบ',
                         use_column_width=True)
                try:
                    with st.expander("ผลการตรวจจับ"):
                        for box in boxes:
                            st.write(box.data)
                except Exception as ex:
                    # st.write(ex)
                    st.write("ยังไม่มีภาพอัพโหลด!")

elif source_radio == SETTING.VIDEO:
    HELPER.play_stored_video(confidence, model)
