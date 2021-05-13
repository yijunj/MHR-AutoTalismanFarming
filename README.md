# AutoTalismanFarming-MHR
An automatic machine for farming talisman in Monster Hunter Rise.
This is an update from my other repo [Autocart-MHR](https://github.com/yijunj/Autocart-MHR), which only automates the carting process.

A 64x-speed demo is here. For demonstration I'm only making 2 melding batches. In practice it's most efficient to make 10.
![Demo](https://github.com/yijunj/AutoTalismanFarming-MHR/blob/main/Demo_64x_480p.gif)

## Background
Talisman is a key equipment in Monster Hunter Rise, with the capability of providing highly rated skills and slots. However, obtaining good (or even god) talismans requires effort and in-game resources, as they are generated from a random melding pot known as the Wisp of Mystery. A good description of the talisman mechanism can be found [here](https://game8.co/games/Monster-Hunter-Rise/archives/327175).

The problem is, each melding requires finishing a (non-expedition) quest to complete. It has been long discovered that the most efficient quest to take is the arena Rajang, and keep carting 10 times will complete 10 (the max number) melding batches in a "short" amount of time (about 15 minutes manually). However, talismans with the skill Weakness Exploit 2 and a 2-star slot, and potentially with the skill Critical Boost 2, are extremely rare, so even repeating the Rajang quest is time consuming. To address this problem, this repo presents an Arduino Switch controller that automatically accepts the Rajang quest and carts.

Also, to address the resource problem, thanks to [Ken_set](https://www.gamersky.com/handbook/202104/1384837.shtml), in 2.0 version of the game it is possible to save and reload the game to update the talisman results, without actually consuming (most of) the materials required for melding. The procedure is (please turn off auto-save in the game):

1. Save the game.
2. Make 10 melding batches (5 in each batch), do NOT save.
3. Cart in Rajang quest 10 times, do NOT save in the end.
4. Check the 50 talismans, if no good talisman comes out, do NOT save, then close the game.
5. Restart the game, make 1 melding (only 1 in this batch). The 150 pts worth of materials is what you WILL pay in this iteration.
6. Cart in Rajang quest once, then take the single talisman and SAVE.
7. If not a good talisman, go to step 1 and repeat.

Step 6 will refresh the talisman table so you end up with different talismans in each iteration. This procedure allows you to use 150 pts worth of materials to check 51 talismans, reducing the material cost by 51x.

## Arduino controller
Please refer to [HackerLoop's repo](https://github.com/HackerLoop/Arduino-JoyCon-Library-for-Nintendo-Switch) to learn how to turn an Arduino Leonardo into a Switch joycon. In short, the Arduino, when connected to a Switch via USB, can trigger joycon events. One can either store a button sequence in the Arduino itself, or send commands to the Arduino from a PC via serial port. Here I use the latter: my PC sends a string to the Arduino consisting of several 6-char commands, the Arduino translates the commands into joycon events.

## Visual feedback
I use a video capture card to acquire the Switch screen on PC. This is necessary for the program to automatically read talisman names and slots once melding is completed. It is also used to automatically hand in materials for making new batches of talismans. The software I'm using is [OBS Studio](https://obsproject.com/). Video recording is not necessary. The program only takes screenshots at specific times (so the OBS video window needs to be exposed) and uses the [pytesseract](https://pypi.org/project/pytesseract/) library to extract text.

## How to use
Note:
1. For some reasons the button sequence will not execute correctly when the Switch is connected to some TV models. For best performance please use the hand held mode.
2. I'm running the script on a Windows 10 PC with screen resolution 1920 x 1080. Depending on OS and resolution, functions in screenshot.py (which provides visual feedback) will need tweaking.
3. Please always have the OBS video window exposed in order for screen capturing to work properly.
4. The program will beep when it finds a Weakness Exploit 2 talisman. In that case, either unplug the USB and manually take the talisman, which ends the farming (you may want to kill the program as well), or if the talisman is still not good, press any key to let the program continue. All talisman history will be documented in talisman_history.txt under the same folder.
5. Please have enough material to make talismans. As described above, the procedure is not very material-consuming at all, but there is still material cost involved.
6. ALWAYS baby-sit the program for the first few rounds.

Here are the steps you need to take:
1. Do what is said in [HackerLoop's repo](https://github.com/HackerLoop/Arduino-JoyCon-Library-for-Nintendo-Switch) to modify the Arduino files, and download SwitchJoystick library from there. Write joycon.ino to an Arduino Leonardo.
2. Install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and [pytesseract](https://pypi.org/project/pytesseract/).
3. Connect the Arduino to PC using a serial-to-USB adapter (USB to computer, RX/TX to the Arduino corresponding pins). Check the serial port (for Windows you can go to device manager and look there). It can be different from what I have so you may want to modify the codes.
4. Connect the Switch HDMI to a video capture card, and plug the video capture card to PC. Open OBS and add the video capture card as a video capture device. Make sure you see the Switch screen on OBS.
5. Using a Pro controller, open Monster Hunter Rise. Make sure auto-save is off and pressing "-" opens up the map but not the chat screen. Save the game. The script assumes the game is on as a starting point.
6. Turn off the Pro controller. The Switch will start looking for a joycon. Connect the Arduino to Switch via a USB cable. Run register.py from PC command window. This will register the Arduino as a "USB controller".
7. Change the number of rounds you want to farm in main.py, and run it from PC command window. Baby-sit the program for a while. The code will run on its own, following the [Ken_set](https://www.gamersky.com/handbook/202104/1384837.shtml) sequence described above.

## Appendix: serial command table
I use 6 chars for each command: the first 2 indicating which key is pressed or released, and the last 4 indicating the time delay (in ms) after this event. E.g. AA0050 means "press A and wait 50 ms".

| 2-char key code | Action |
| ---------- | ---------- |
| AA | Press A |
| aa | Release A |
| BB | Press B |
| bb | Release B |
| XX | Press X |
| xx | Release X |
| YY | Press Y |
| yy | Release Y |
| DU | Press Up |
| du | Release Up |
| DD | Press Down |
| dd | Release Down |
| DR | Press Right |
| dr | Release Right |
| DL | Press Left |
| dl | Release Left |
| RI | Press R |
| ri | Release R |
| LE | Press L |
| le | Release L |
| ZR | Press ZR |
| zr | Release ZR |
| ZL | Press ZL |
| zl | Release ZL |
| PL | Press Plus |
| pl | Release Plus |
| MI | Press Minus |
| mi | Release Minus |
| HO | Press Home |
| ho | Release Home |
| CA | Press Capture |
| ca | Release Capture |
| RC | Press Right Stick |
| rc | Release Right Stick |
| LC | Press Left Stick |
| lc | Release Left Stick |
| RU | Push Right Stick Up |
| RD | Push Right Stick Down |
| RR | Push Right Stick Right |
| RL | Push Right Stick Left |
| RN | Return Right Stick Neutral |
| LU | Push Left Stick Up |
| LD | Push Left Stick Down |
| LR | Push Left Stick Right |
| LL | Push Left Stick Left |
| LN | Return Left Stick Neutral |

