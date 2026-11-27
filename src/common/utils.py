import cv2 as cv
import numpy as np


def get_matInfo(name, img):
    if img.dtype == "uint8":
        mat_T = "CV_8U"
    elif img.dtype == "int8":
        mat_T = "CV_8S"
    elif img.dtype == "uint16":
        mat_T = "CV_16U"
    elif img.dtype == "int16":
        mat_T = "CV_16S"
    elif img.dtype == "float32":
        mat_T = "CV_32F"
    elif img.dtype == "float64":
        mat_T = "CV_64F"

    n_channel = 3 if img.ndim == 3 else 1

    print(
        f"{name:12s}: depth({img.dtype}), channels({n_channel}) -> mat_T({mat_T}C{n_channel})"
    )


def put_str(frame, text, pt, val, color=(120, 200, 90)):
    text += str(val)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    cv.putText(frame, text, pt, font, 0.7, color, 2)


def calc_histo(img, size, ranges=[0, 256]) -> np.ndarray:
    hist = np.zeros((size, 1), np.float32)  # <- 여기 에러
    gap = ranges[1] / size

    for i in (img / gap).flat:
        hist[int(i)] += 1

    return hist


def draw_histo(hist, shape: tuple[int, int] = (200, 256)):
    img = np.full(shape, 255, np.uint8)
    # 정규화; 값을 특정 범위로 제한 및 표현
    cv.normalize(hist, hist, 0, shape[0], cv.NORM_MINMAX)
    gap = (
        img.shape[1] / hist.shape[0]
    )  # 그래프 넓이를 계급 개수로 나눠 한 계급의 너비를 구함

    for i, h in enumerate(hist):
        x = int(round(i * gap))  # 막대가 그려지는 시작 좌표
        w = int(round(gap))  # 너비
        cv.rectangle(img, (x, 0, w, int(h)), 0, cv.FILLED)
        # 이러면 그래프가 위에서 아래로 그려진다.

    return cv.flip(img, 0)  # 그걸 상하반전


# sliding & stretching


def mk_pallete(rows):
    hue = [round(i * 180 / rows) for i in range(rows)]
    hsv = [[[h, 0xFF, 0xFF]] for h in hue]
    hsv = np.array(hsv, dtype=np.uint8)

    return cv.cvtColor(hsv, cv.COLOR_HSV2BGR)


def draw_histo_c(hist, shape: tuple[int, int, int] = (200, 256, 3)):
    hsv_pallete = mk_pallete(hist.shape[0])
    img = np.full(shape, 255, np.uint8)
    cv.normalize(hist, hist, 0, shape[0], cv.NORM_MINMAX)

    gap = img.shape[1] / hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        color = tuple(map(int, hsv_pallete[i][0]))
        cv.rectangle(img, (x, 0, w, int(h)), color, cv.FILLED)

    return cv.flip(img, 0)


def fltr_mat(img, m):
    r, c = img.shape[:2]
    dst = np.zeros((r, c), np.float32)
    y_cent, x_cent = m.shape[0] // 2, m.shape[1] // 2

    for i in range(y_cent, r - y_cent):
        for j in range(x_cent, c - x_cent):
            y1, y2 = i - y_cent, i + y_cent + 1
            x1, x2 = j - x_cent, j + x_cent + 1
            roi = img[y1:y2, x1:x2].astype("float32")
            tmp = cv.multiply(roi, m)
            dst[i, j] = cv.sumElems(tmp)[0]

    return dst


def fltr_px(img, m):
    r, c = img.shape[:2]
    dst = np.zeros((r, c), np.float32)
    y_cent, x_cent = m.shape[0] // 2, m.shape[1] // 2

    for i in range(y_cent, r - y_cent):
        for j in range(x_cent, c - x_cent):
            sum = 0.0
            for k in range(m.shape[0]):
                for l in range(m.shape[1]):
                    y, x = i + k - y_cent, j + l - x_cent
                    sum += img[y, x] * m[k, l]
            dst[i, j] = sum

    return dst
