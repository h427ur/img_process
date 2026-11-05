import cv2 as cv

path = "./images/abs_test2.jpg"
img = cv.imread(path, cv.IMREAD_GRAYSCALE)

m_add1 = cv.add(img, 50)
m_sub1 = cv.subtract(img, 100)
m_div1 = cv.divide(img, 5.0)

scalar_m1 = img + 30
scalar_m2 = img - 50

titles= [
    "img",
    "m_add1",
    "m_sub1",
    "m_div1",
    "scalar_m1",
    "scalar_m2"
]

for title in titles:
    print(f"[{title}] = \n{eval(title)} \n")
    cv.imshow(title, eval(title))

cv.waitKey(0)