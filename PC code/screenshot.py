from PIL import ImageGrab
from PIL import Image
import pytesseract
import numpy as np
import re

def init():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def get_skills():
    skill_vertical_px_inc = 43
    threshold = 150

    skill_name_bbox_x1 = 1068
    skill_name_bbox_y1 = 300
    skill_name_bbox_x2 = 1245
    skill_name_bbox_y2 = 325
    skill_level_bbox_x1 = 1230
    skill_level_bbox_y1 = 320
    skill_level_bbox_x2 = 1245
    skill_level_bbox_y2 = 345

    skill_str = ''

    for i in range(2):
        skill_name_im = ImageGrab.grab(bbox =(skill_name_bbox_x1, skill_name_bbox_y1, skill_name_bbox_x2, skill_name_bbox_y2))

        skill_level_im = ImageGrab.grab(bbox =(skill_level_bbox_x1, skill_level_bbox_y1, skill_level_bbox_x2, skill_level_bbox_y2)).convert('L')
        skill_level_im = skill_level_im.point(lambda p: p > threshold and 255)

        skill_name1 = pytesseract.image_to_string(skill_name_im, lang='eng')[:-2]
        skill_name2 = pytesseract.image_to_string(skill_name_im.resize((250,25)), lang='eng')[:-2]
        if(len(skill_name1) > len(skill_name2)):
            skill_name = skill_name1
        else:
            skill_name = skill_name2
        skill_name = re.sub('[^A-Za-z ]+', '', skill_name.strip())
        skill_level = pytesseract.image_to_string(skill_level_im, config='--psm 10 --oem 3 -c tessedit_char_whitelist=1234567')[:-2]
        skill = skill_name + ' ' + skill_level

        # skill_name_im.save('skill_name' + str(i) + '.jpg')

        if(len(skill_name) < 4):
            break

        skill_str += skill
        skill_str += ', '

        skill_name_bbox_y1 += skill_vertical_px_inc
        skill_name_bbox_y2 += skill_vertical_px_inc
        skill_level_bbox_y1 += skill_vertical_px_inc
        skill_level_bbox_y2 += skill_vertical_px_inc

    return skill_str[:-2]

def get_slots():
    slot_horizontal_px_inc = 23

    slot_bbox_x1 = 1176
    slot_bbox_y1 = 250
    slot_bbox_x2 = 1198
    slot_bbox_y2 = 270

    zero_slot_data = np.asarray(Image.open('0slot.jpg'), dtype='float32').reshape(-1)
    one_slot_data = np.asarray(Image.open('1slot.jpg'), dtype='float32').reshape(-1)
    two_slot_data = np.asarray(Image.open('2slot.jpg'), dtype='float32').reshape(-1)
    three_slot_data = np.asarray(Image.open('3slot.jpg'), dtype='float32').reshape(-1)

    slot_str = ''

    for i in range(3):
        slot_im = ImageGrab.grab(bbox =(slot_bbox_x1, slot_bbox_y1, slot_bbox_x2, slot_bbox_y2))
        slot_data = np.asarray(slot_im, dtype='float32').reshape(-1)

        with_zero_slot_ovlp = np.sum(zero_slot_data * slot_data) / np.sqrt(np.sum(zero_slot_data * zero_slot_data) * np.sum(slot_data * slot_data))
        with_one_slot_ovlp = np.sum(one_slot_data * slot_data) / np.sqrt(np.sum(one_slot_data * one_slot_data) * np.sum(slot_data * slot_data))
        with_two_slot_ovlp = np.sum(two_slot_data * slot_data) / np.sqrt(np.sum(two_slot_data * two_slot_data) * np.sum(slot_data * slot_data))
        with_three_slot_ovlp = np.sum(three_slot_data * slot_data) / np.sqrt(np.sum(three_slot_data * three_slot_data) * np.sum(slot_data * slot_data))

        slot_str += str(np.argmax([with_zero_slot_ovlp, with_one_slot_ovlp, with_two_slot_ovlp, with_three_slot_ovlp]))
        slot_str += '-'

        # slot_im.save('slot' + str(i) + '.jpg')

        slot_bbox_x1 += slot_horizontal_px_inc
        slot_bbox_x2 += slot_horizontal_px_inc

    return slot_str[:-1]

def get_talisman_status(position='first'):
    talisman_horizontal_px_inc = 202

    talisman_bbox_x1 = 1085
    talisman_bbox_y1 = 485
    talisman_bbox_x2 = 1130
    talisman_bbox_y2 = 530

    if position == 'last':
        talisman_bbox_x1 += talisman_horizontal_px_inc
        talisman_bbox_x2 += talisman_horizontal_px_inc

    talisman_im = ImageGrab.grab(bbox =(talisman_bbox_x1, talisman_bbox_y1, talisman_bbox_x2, talisman_bbox_y2))
    talisman_data = np.asarray(talisman_im, dtype='float32').reshape(-1)

    yes_data = np.asarray(Image.open('with_talisman.jpg'), dtype='float32').reshape(-1)
    no_data = np.asarray(Image.open('without_talisman.jpg'), dtype='float32').reshape(-1)

    with_yes_ovlp = np.sum(yes_data * talisman_data) / np.sqrt(np.sum(yes_data * yes_data) * np.sum(talisman_data * talisman_data))
    with_no_ovlp = np.sum(no_data * talisman_data) / np.sqrt(np.sum(no_data * no_data) * np.sum(talisman_data * talisman_data))

    if with_yes_ovlp > with_no_ovlp:
        return True
    else:
        return False

if __name__ == '__main__':
   init()
   # print(get_skills())
   # print(get_slots())
   print(get_talisman_status())
   print(get_talisman_status('last'))
