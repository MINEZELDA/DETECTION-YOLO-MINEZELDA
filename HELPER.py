from ultralytics import YOLO
import streamlit as st
import cv2
import yt_dlp
import SETTING
def load_model(model_path):
    model = YOLO(model_path)
    return model
def display_tracker_options():
    display_tracker = st.radio("ตัวติดตามการแสดงผล", ('ใช่', 'ไม่'))
    is_display_tracker = True if display_tracker == 'ใช่' else False
    if is_display_tracker:
        tracker_type = st.radio("ตัวติดตาม", ("botsort.yaml", "bytetrack.yaml"))
        return is_display_tracker, tracker_type
    return is_display_tracker, None
def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    image = cv2.resize(image, (720, int(720*(9/16))))
    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        res = model.predict(image, conf=conf)
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='วิดีโอที่ตรวจพบ',
                   channels="BGR",
                   use_column_width=True
                   )
def play_stored_video(conf, model):
    source_vid = st.sidebar.selectbox(
        "เลือกวิดีโอ...", SETTING.VIDEOS_DICT.keys())

    is_display_tracker, tracker = display_tracker_options()

    with open(SETTING.VIDEOS_DICT.get(source_vid), 'rb') as video_file:
        video_bytes = video_file.read()
    if video_bytes:
        st.video(video_bytes)

    if st.sidebar.button('ตรวจจับวัตถุวิดีโอ'):
        try:
            vid_cap = cv2.VideoCapture(
                str(SETTING.VIDEOS_DICT.get(source_vid)))
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf,
                                             model,
                                             st_frame,
                                             image,
                                             is_display_tracker,
                                             tracker
                                             )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("เกิดข้อผิดพลาดในการโหลดวิดีโอ" + str(e))
