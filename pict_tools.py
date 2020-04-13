import cv2
import numpy as np

def adjust_size(img, width, height):
    '''
    画像に指定されたサイズまで余白（黒）を追加する処理
    元画像は中央に合成されます。
    指定されたサイズよりも大きい画像の場合は、余白は追加されません。
    '''
    h, w, chanel = img.shape
    width, height = max(width, w), max(height, h)
    w_adjust, h_adjust = int((width-w)/2), int((height-h)/2)

    zero = cv2.resize(np.zeros((1, 1, chanel), np.float), (width, height))  # 余白用の画像を作成
    zero.resize(height, width, chanel)  # grayscale の場合に chanel が消えるための対応
    zero[h_adjust:h_adjust+h, w_adjust:w_adjust+w] = img    # 作成した余白画像の中央に元画像を入れる
    return zero
