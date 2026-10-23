from cv2 import FONT_HERSHEY_SIMPLEX, putText

def get_matInfo(name, img):
    if img.dtype == "uint8": mat_T = "CV_8U"
    elif img.dtype == "int8": mat_T = "CV_8S"
    elif img.dtype == "uint16": mat_T = "CV_16U"
    elif img.dtype == "int16": mat_T = "CV_16S"
    elif img.dtype == "float32": mat_T = "CV_32F"
    elif img.dtype == "float64": mat_T = "CV_64F"

    n_channel = 3 if img.ndim == 3 else 1

    print(f"{name:12s}: depth({img.dtype}), channels({n_channel}) -> mat_T({mat_T}C{n_channel})")

def put_str(frame, text, pt, val, color=(120, 200, 90)):
    text += str(val)
    shade = (pt[0] + 2, pt[1] + 2)
    font = FONT_HERSHEY_SIMPLEX
    putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    putText(frame, text, pt, font, 0.7, color, 2)