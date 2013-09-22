from lib.entity import Entity
from lib.point import *

import math

class LetterX(Entity):
	def __init__(self):
		super(LetterX, self).__init__()

		self.direc = 1 # XXX TEMPORARY 

		points = [
			{'x': 42, 'y': 50},
			{'x': 42.263999938964844, 'y': 50},
			{'x': 42.52799987792969, 'y': 50},
			{'x': 42.79199981689453, 'y': 50},
			{'x': 43.055999755859375, 'y': 50},
			{'x': 43.31999969482422, 'y': 50},
			{'x': 43.58399963378906, 'y': 50},
			{'x': 43.847999572753906, 'y': 50},
			{'x': 44.11199951171875, 'y': 50},
			{'x': 44.375999450683594, 'y': 50},
			{'x': 44.63999938964844, 'y': 50},
			{'x': 44.90399932861328, 'y': 50},
			{'x': 45.167999267578125, 'y': 50},
			{'x': 45.43199920654297, 'y': 50},
			{'x': 45.69599914550781, 'y': 50},
			{'x': 45.959999084472656, 'y': 50},
			{'x': 46.2239990234375, 'y': 50},
			{'x': 46.487998962402344, 'y': 50},
			{'x': 46.75199890136719, 'y': 50},
			{'x': 47.01599884033203, 'y': 50},
			{'x': 47.279998779296875, 'y': 50},
			{'x': 47.54399871826172, 'y': 50},
			{'x': 47.80799865722656, 'y': 50},
			{'x': 48.071998596191406, 'y': 50},
			{'x': 48.33599853515625, 'y': 50},
			{'x': 48.599998474121094, 'y': 50},
			{'x': 48.86399841308594, 'y': 50},
			{'x': 49.12799835205078, 'y': 50},
			{'x': 49.391998291015625, 'y': 50},
			{'x': 49.65599822998047, 'y': 50},
			{'x': 49.91999816894531, 'y': 50},
			{'x': 50.183998107910156, 'y': 50},
			{'x': 50.447998046875, 'y': 50},
			{'x': 50.711997985839844, 'y': 50},
			{'x': 50.97599792480469, 'y': 50},
			{'x': 51.23999786376953, 'y': 50},
			{'x': 51.503997802734375, 'y': 50},
			{'x': 51.76799774169922, 'y': 50},
			{'x': 52.03199768066406, 'y': 50},
			{'x': 52.295997619628906, 'y': 50},
			{'x': 52.560001373291016, 'y': 50},
			{'x': 52.82400131225586, 'y': 50},
			{'x': 53.0880012512207, 'y': 50},
			{'x': 53.35200119018555, 'y': 50},
			{'x': 53.61600112915039, 'y': 50},
			{'x': 53.880001068115234, 'y': 50},
			{'x': 54.14400100708008, 'y': 50},
			{'x': 54.40800094604492, 'y': 50},
			{'x': 54.672000885009766, 'y': 50},
			{'x': 54.93600082397461, 'y': 50},
			{'x': 55.20000076293945, 'y': 50},
			{'x': 55.4640007019043, 'y': 50},
			{'x': 55.72800064086914, 'y': 50},
			{'x': 55.992000579833984, 'y': 50},
			{'x': 56.25600051879883, 'y': 50},
			{'x': 56.52000045776367, 'y': 50},
			{'x': 56.784000396728516, 'y': 50},
			{'x': 57.04800033569336, 'y': 50},
			{'x': 57.3120002746582, 'y': 50},
			{'x': 57.57600021362305, 'y': 50},
			{'x': 57.84000015258789, 'y': 50},
			{'x': 58.104000091552734, 'y': 50},
			{'x': 58.36800003051758, 'y': 50},
			{'x': 58.63199996948242, 'y': 50},
			{'x': 58.895999908447266, 'y': 50},
			{'x': 59.15999984741211, 'y': 50},
			{'x': 59.42399978637695, 'y': 50},
			{'x': 59.6879997253418, 'y': 50},
			{'x': 59.95199966430664, 'y': 50},
			{'x': 60.215999603271484, 'y': 50},
			{'x': 60.47999954223633, 'y': 50},
			{'x': 60.74399948120117, 'y': 50},
			{'x': 61.007999420166016, 'y': 50},
			{'x': 61.27199935913086, 'y': 50},
			{'x': 61.5359992980957, 'y': 50},
			{'x': 61.79999923706055, 'y': 50},
			{'x': 62.06399917602539, 'y': 50},
			{'x': 62.327999114990234, 'y': 50},
			{'x': 62.59199905395508, 'y': 50},
			{'x': 62.85600280761719, 'y': 50},
			{'x': 63.12000274658203, 'y': 50},
			{'x': 63.384002685546875, 'y': 50},
			{'x': 63.64800262451172, 'y': 50},
			{'x': 63.91200256347656, 'y': 50},
			{'x': 64.1760025024414, 'y': 50},
			{'x': 64.44000244140625, 'y': 50},
			{'x': 64.7040023803711, 'y': 50},
			{'x': 64.96800231933594, 'y': 50},
			{'x': 65.23200225830078, 'y': 50},
			{'x': 65.49600219726562, 'y': 50},
			{'x': 65.76000213623047, 'y': 50},
			{'x': 66.02400207519531, 'y': 50},
			{'x': 66.28800201416016, 'y': 50},
			{'x': 66.552001953125, 'y': 50},
			{'x': 66.81600189208984, 'y': 50},
			{'x': 67.08000183105469, 'y': 50},
			{'x': 67.34400177001953, 'y': 50},
			{'x': 67.60800170898438, 'y': 50},
			{'x': 67.87200164794922, 'y': 50},
			{'x': 68.13600158691406, 'y': 50},
			{'x': 68.4000015258789, 'y': 50},
			{'x': 68.66400146484375, 'y': 50},
			{'x': 68.9280014038086, 'y': 50},
			{'x': 69.19200134277344, 'y': 50},
			{'x': 69.45600128173828, 'y': 50},
			{'x': 69.72000122070312, 'y': 50},
			{'x': 69.98400115966797, 'y': 50},
			{'x': 70.24800109863281, 'y': 50},
			{'x': 70.51200103759766, 'y': 50},
			{'x': 70.7760009765625, 'y': 50},
			{'x': 71.04000091552734, 'y': 50},
			{'x': 71.30400085449219, 'y': 50},
			{'x': 71.56800079345703, 'y': 50},
			{'x': 71.83200073242188, 'y': 50},
			{'x': 72.09600067138672, 'y': 50},
			{'x': 72.36000061035156, 'y': 50},
			{'x': 72.6240005493164, 'y': 50},
			{'x': 72.88800048828125, 'y': 50},
			{'x': 73.1520004272461, 'y': 50},
			{'x': 73.41600036621094, 'y': 50},
			{'x': 73.68000030517578, 'y': 50},
			{'x': 73.94400024414062, 'y': 50},
			{'x': 74.20800018310547, 'y': 50},
			{'x': 74.47200012207031, 'y': 50},
			{'x': 74.73600006103516, 'y': 50},
			{'x': 75, 'y': 50},
			{'x': 75.26399993896484, 'y': 50},
			{'x': 75.52799987792969, 'y': 50},
			{'x': 75.79199981689453, 'y': 50},
			{'x': 76.05599975585938, 'y': 50},
			{'x': 76.31999969482422, 'y': 50},
			{'x': 76.58399963378906, 'y': 50},
			{'x': 76.8479995727539, 'y': 50},
			{'x': 77.11199951171875, 'y': 50},
			{'x': 77.3759994506836, 'y': 50},
			{'x': 77.63999938964844, 'y': 50},
			{'x': 77.90399932861328, 'y': 50},
			{'x': 78.16799926757812, 'y': 50},
			{'x': 78.43199920654297, 'y': 50},
			{'x': 78.69599914550781, 'y': 50},
			{'x': 78.95999908447266, 'y': 50},
			{'x': 79.2239990234375, 'y': 50},
			{'x': 79.48799896240234, 'y': 50},
			{'x': 79.75199890136719, 'y': 50},
			{'x': 80.01599884033203, 'y': 50},
			{'x': 80.27999877929688, 'y': 50},
			{'x': 80.54399871826172, 'y': 50},
			{'x': 80.80799865722656, 'y': 50},
			{'x': 81.0719985961914, 'y': 50},
			{'x': 81.33599853515625, 'y': 50},
			{'x': 81.5999984741211, 'y': 50},
			{'x': 81.86399841308594, 'y': 50},
			{'x': 82.12799835205078, 'y': 50},
			{'x': 82.39199829101562, 'y': 50},
			{'x': 82.65599822998047, 'y': 50},
			{'x': 82.91999816894531, 'y': 50},
			{'x': 83.18399810791016, 'y': 50},
			{'x': 83.447998046875, 'y': 50},
			{'x': 83.71200561523438, 'y': 50},
			{'x': 83.97599792480469, 'y': 50},
			{'x': 84.24000549316406, 'y': 50},
			{'x': 84.50399780273438, 'y': 50},
			{'x': 84.76800537109375, 'y': 50},
			{'x': 85.03199768066406, 'y': 50},
			{'x': 85.29600524902344, 'y': 50},
			{'x': 85.55999755859375, 'y': 50},
			{'x': 85.82400512695312, 'y': 50},
			{'x': 86.08799743652344, 'y': 50},
			{'x': 86.35200500488281, 'y': 50},
			{'x': 86.61599731445312, 'y': 50},
			{'x': 86.8800048828125, 'y': 50},
			{'x': 87.14399719238281, 'y': 50},
			{'x': 87.40800476074219, 'y': 50},
			{'x': 87.6719970703125, 'y': 50},
			{'x': 87.93600463867188, 'y': 50},
			{'x': 88.19999694824219, 'y': 50},
			{'x': 88.46400451660156, 'y': 50},
			{'x': 88.72799682617188, 'y': 50},
			{'x': 88.99200439453125, 'y': 50},
			{'x': 89.25599670410156, 'y': 50},
			{'x': 89.52000427246094, 'y': 50},
			{'x': 89.78399658203125, 'y': 50},
			{'x': 90.04800415039062, 'y': 50},
			{'x': 90.31199645996094, 'y': 50},
			{'x': 90.57600402832031, 'y': 50},
			{'x': 90.83999633789062, 'y': 50},
			{'x': 91.10400390625, 'y': 50},
			{'x': 91.36799621582031, 'y': 50},
			{'x': 91.63200378417969, 'y': 50},
			{'x': 91.89599609375, 'y': 50},
			{'x': 92.16000366210938, 'y': 50},
			{'x': 92.42399597167969, 'y': 50},
			{'x': 92.68800354003906, 'y': 50},
			{'x': 92.95199584960938, 'y': 50},
			{'x': 93.21600341796875, 'y': 50},
			{'x': 93.47999572753906, 'y': 50},
			{'x': 93.74400329589844, 'y': 50},
			{'x': 94.00799560546875, 'y': 50},
			{'x': 94.27200317382812, 'y': 50},
			{'x': 94.53599548339844, 'y': 50},
			{'x': 94.80000305175781, 'y': 50},
			{'x': 95.06399536132812, 'y': 50},
			{'x': 95.3280029296875, 'y': 50},
			{'x': 95.59199523925781, 'y': 50},
			{'x': 95.85600280761719, 'y': 50},
			{'x': 96.1199951171875, 'y': 50},
			{'x': 96.38400268554688, 'y': 50},
			{'x': 96.64799499511719, 'y': 50},
			{'x': 96.91200256347656, 'y': 50},
			{'x': 97.17599487304688, 'y': 50},
			{'x': 97.44000244140625, 'y': 50},
			{'x': 97.70399475097656, 'y': 50},
			{'x': 97.96800231933594, 'y': 50},
			{'x': 98.23199462890625, 'y': 50},
			{'x': 98.49600219726562, 'y': 50},
			{'x': 98.75999450683594, 'y': 50},
			{'x': 99.02400207519531, 'y': 50},
			{'x': 99.28799438476562, 'y': 50},
			{'x': 99.552001953125, 'y': 50},
			{'x': 99.81600189208984, 'y': 50},
			{'x': 100.08000183105469, 'y': 50},
			{'x': 100.34400177001953, 'y': 50},
			{'x': 100.60800170898438, 'y': 50},
			{'x': 100.87200164794922, 'y': 50},
			{'x': 101.13600158691406, 'y': 50},
			{'x': 101.4000015258789, 'y': 50},
			{'x': 101.66400146484375, 'y': 50},
			{'x': 101.9280014038086, 'y': 50},
			{'x': 102.19200134277344, 'y': 50},
			{'x': 102.45600128173828, 'y': 50},
			{'x': 102.72000122070312, 'y': 50},
			{'x': 102.98400115966797, 'y': 50},
			{'x': 103.24800109863281, 'y': 50},
			{'x': 103.51200103759766, 'y': 50},
			{'x': 103.7760009765625, 'y': 50},
			{'x': 104.04000091552734, 'y': 50},
			{'x': 104.30400085449219, 'y': 50},
			{'x': 104.56800079345703, 'y': 50},
			{'x': 104.83200073242188, 'y': 50},
			{'x': 105.09600067138672, 'y': 50},
			{'x': 105.36000061035156, 'y': 50},
			{'x': 105.6240005493164, 'y': 50},
			{'x': 105.88800048828125, 'y': 50},
			{'x': 106.1520004272461, 'y': 50},
			{'x': 106.41600036621094, 'y': 50},
			{'x': 106.68000030517578, 'y': 50},
			{'x': 106.94400024414062, 'y': 50},
			{'x': 107.20800018310547, 'y': 50},
			{'x': 107.47200012207031, 'y': 50},
			{'x': 107.73600006103516, 'y': 50},
			{'x': 108, 'y': 50},
			{'x': 75, 'y': 17.263999938964844},
			{'x': 75, 'y': 17.527999877929688},
			{'x': 75, 'y': 17.79199981689453},
			{'x': 75, 'y': 18.055999755859375},
			{'x': 75, 'y': 18.31999969482422},
			{'x': 75, 'y': 18.583999633789062},
			{'x': 75, 'y': 18.847999572753906},
			{'x': 75, 'y': 19.11199951171875},
			{'x': 75, 'y': 19.375999450683594},
			{'x': 75, 'y': 19.639999389648438},
			{'x': 75, 'y': 19.90399932861328},
			{'x': 75, 'y': 20.167999267578125},
			{'x': 75, 'y': 20.43199920654297},
			{'x': 75, 'y': 20.695999145507812},
			{'x': 75, 'y': 20.959999084472656},
			{'x': 75, 'y': 21.2239990234375},
			{'x': 75, 'y': 21.487998962402344},
			{'x': 75, 'y': 21.751998901367188},
			{'x': 75, 'y': 22.01599884033203},
			{'x': 75, 'y': 22.279998779296875},
			{'x': 75, 'y': 22.54399871826172},
			{'x': 75, 'y': 22.807998657226562},
			{'x': 75, 'y': 23.071998596191406},
			{'x': 75, 'y': 23.33599853515625},
			{'x': 75, 'y': 23.599998474121094},
			{'x': 75, 'y': 23.863998413085938},
			{'x': 75, 'y': 24.12799835205078},
			{'x': 75, 'y': 24.391998291015625},
			{'x': 75, 'y': 24.65599822998047},
			{'x': 75, 'y': 24.919998168945312},
			{'x': 75, 'y': 25.183998107910156},
			{'x': 75, 'y': 25.447998046875},
			{'x': 75, 'y': 25.711997985839844},
			{'x': 75, 'y': 25.975997924804688},
			{'x': 75, 'y': 26.23999786376953},
			{'x': 75, 'y': 26.503997802734375},
			{'x': 75, 'y': 26.76799774169922},
			{'x': 75, 'y': 27.031997680664062},
			{'x': 75, 'y': 27.295997619628906},
			{'x': 75, 'y': 27.55999755859375},
			{'x': 75, 'y': 27.823997497558594},
			{'x': 75, 'y': 28.087997436523438},
			{'x': 75, 'y': 28.35199737548828},
			{'x': 75, 'y': 28.615997314453125},
			{'x': 75, 'y': 28.87999725341797},
			{'x': 75, 'y': 29.143997192382812},
			{'x': 75, 'y': 29.407997131347656},
			{'x': 75, 'y': 29.6719970703125},
			{'x': 75, 'y': 29.935997009277344},
			{'x': 75, 'y': 30.199996948242188},
			{'x': 75, 'y': 30.46399688720703},
			{'x': 75, 'y': 30.727996826171875},
			{'x': 75, 'y': 30.99199676513672},
			{'x': 75, 'y': 31.255996704101562},
			{'x': 75, 'y': 31.519996643066406},
			{'x': 75, 'y': 31.78399658203125},
			{'x': 75, 'y': 32.047996520996094},
			{'x': 75, 'y': 32.31199645996094},
			{'x': 75, 'y': 32.57599639892578},
			{'x': 75, 'y': 32.839996337890625},
			{'x': 75, 'y': 33.10399627685547},
			{'x': 75, 'y': 33.36799621582031},
			{'x': 75, 'y': 33.63200378417969},
			{'x': 75, 'y': 33.89600372314453},
			{'x': 75, 'y': 34.160003662109375},
			{'x': 75, 'y': 34.42400360107422},
			{'x': 75, 'y': 34.68800354003906},
			{'x': 75, 'y': 34.952003479003906},
			{'x': 75, 'y': 35.21600341796875},
			{'x': 75, 'y': 35.480003356933594},
			{'x': 75, 'y': 35.74400329589844},
			{'x': 75, 'y': 36.00800323486328},
			{'x': 75, 'y': 36.272003173828125},
			{'x': 75, 'y': 36.53600311279297},
			{'x': 75, 'y': 36.80000305175781},
			{'x': 75, 'y': 37.064002990722656},
			{'x': 75, 'y': 37.3280029296875},
			{'x': 75, 'y': 37.592002868652344},
			{'x': 75, 'y': 37.85600280761719},
			{'x': 75, 'y': 38.12000274658203},
			{'x': 75, 'y': 38.384002685546875},
			{'x': 75, 'y': 38.64800262451172},
			{'x': 75, 'y': 38.91200256347656},
			{'x': 75, 'y': 39.176002502441406},
			{'x': 75, 'y': 39.44000244140625},
			{'x': 75, 'y': 39.704002380371094},
			{'x': 75, 'y': 39.96800231933594},
			{'x': 75, 'y': 40.23200225830078},
			{'x': 75, 'y': 40.496002197265625},
			{'x': 75, 'y': 40.76000213623047},
			{'x': 75, 'y': 41.02400207519531},
			{'x': 75, 'y': 41.288002014160156},
			{'x': 75, 'y': 41.552001953125},
			{'x': 75, 'y': 41.816001892089844},
			{'x': 75, 'y': 42.08000183105469},
			{'x': 75, 'y': 42.34400177001953},
			{'x': 75, 'y': 42.608001708984375},
			{'x': 75, 'y': 42.87200164794922},
			{'x': 75, 'y': 43.13600158691406},
			{'x': 75, 'y': 43.400001525878906},
			{'x': 75, 'y': 43.66400146484375},
			{'x': 75, 'y': 43.928001403808594},
			{'x': 75, 'y': 44.19200134277344},
			{'x': 75, 'y': 44.45600128173828},
			{'x': 75, 'y': 44.720001220703125},
			{'x': 75, 'y': 44.98400115966797},
			{'x': 75, 'y': 45.24800109863281},
			{'x': 75, 'y': 45.512001037597656},
			{'x': 75, 'y': 45.7760009765625},
			{'x': 75, 'y': 46.040000915527344},
			{'x': 75, 'y': 46.30400085449219},
			{'x': 75, 'y': 46.56800079345703},
			{'x': 75, 'y': 46.832000732421875},
			{'x': 75, 'y': 47.09600067138672},
			{'x': 75, 'y': 47.36000061035156},
			{'x': 75, 'y': 47.624000549316406},
			{'x': 75, 'y': 47.88800048828125},
			{'x': 75, 'y': 48.152000427246094},
			{'x': 75, 'y': 48.41600036621094},
			{'x': 75, 'y': 48.68000030517578},
			{'x': 75, 'y': 48.944000244140625},
			{'x': 75, 'y': 49.20800018310547},
			{'x': 75, 'y': 49.47200012207031},
			{'x': 75, 'y': 49.736000061035156},
			{'x': 75, 'y': 50},
			{'x': 75, 'y': 50.263999938964844},
			{'x': 75, 'y': 50.52799987792969},
			{'x': 75, 'y': 50.79199981689453},
			{'x': 75, 'y': 51.055999755859375},
			{'x': 75, 'y': 51.31999969482422},
			{'x': 75, 'y': 51.58399963378906},
			{'x': 75, 'y': 51.847999572753906},
			{'x': 75, 'y': 52.11199951171875},
			{'x': 75, 'y': 52.375999450683594},
			{'x': 75, 'y': 52.63999938964844},
			{'x': 75, 'y': 52.90399932861328},
			{'x': 75, 'y': 53.167999267578125},
			{'x': 75, 'y': 53.43199920654297},
			{'x': 75, 'y': 53.69599914550781},
			{'x': 75, 'y': 53.959999084472656},
			{'x': 75, 'y': 54.2239990234375},
			{'x': 75, 'y': 54.487998962402344},
			{'x': 75, 'y': 54.75199890136719},
			{'x': 75, 'y': 55.01599884033203},
			{'x': 75, 'y': 55.279998779296875},
			{'x': 75, 'y': 55.54399871826172},
			{'x': 75, 'y': 55.80799865722656},
			{'x': 75, 'y': 56.071998596191406},
			{'x': 75, 'y': 56.33599853515625},
			{'x': 75, 'y': 56.599998474121094},
			{'x': 75, 'y': 56.86399841308594},
			{'x': 75, 'y': 57.12799835205078},
			{'x': 75, 'y': 57.391998291015625},
			{'x': 75, 'y': 57.65599822998047},
			{'x': 75, 'y': 57.91999816894531},
			{'x': 75, 'y': 58.183998107910156},
			{'x': 75, 'y': 58.447998046875},
			{'x': 75, 'y': 58.711997985839844},
			{'x': 75, 'y': 58.97599792480469},
			{'x': 75, 'y': 59.23999786376953},
			{'x': 75, 'y': 59.503997802734375},
			{'x': 75, 'y': 59.76799774169922},
			{'x': 75, 'y': 60.03199768066406},
			{'x': 75, 'y': 60.295997619628906},
			{'x': 75, 'y': 60.55999755859375},
			{'x': 75, 'y': 60.823997497558594},
			{'x': 75, 'y': 61.08799743652344},
			{'x': 75, 'y': 61.35199737548828},
			{'x': 75, 'y': 61.615997314453125},
			{'x': 75, 'y': 61.87999725341797},
			{'x': 75, 'y': 62.14399719238281},
			{'x': 75, 'y': 62.407997131347656},
			{'x': 75, 'y': 62.6719970703125},
			{'x': 75, 'y': 62.935997009277344},
			{'x': 75, 'y': 63.19999694824219},
			{'x': 75, 'y': 63.46399688720703},
			{'x': 75, 'y': 63.727996826171875},
			{'x': 75, 'y': 63.99199676513672},
			{'x': 75, 'y': 64.25599670410156},
			{'x': 75, 'y': 64.5199966430664},
			{'x': 75, 'y': 64.78399658203125},
			{'x': 75, 'y': 65.0479965209961},
			{'x': 75, 'y': 65.31199645996094},
			{'x': 75, 'y': 65.57599639892578},
			{'x': 75, 'y': 65.83999633789062},
			{'x': 75, 'y': 66.10399627685547},
			{'x': 75, 'y': 66.36799621582031},
			{'x': 75, 'y': 66.63200378417969},
			{'x': 75, 'y': 66.89600372314453},
			{'x': 75, 'y': 67.16000366210938},
			{'x': 75, 'y': 67.42400360107422},
			{'x': 75, 'y': 67.68800354003906},
			{'x': 75, 'y': 67.9520034790039},
			{'x': 75, 'y': 68.21600341796875},
			{'x': 75, 'y': 68.4800033569336},
			{'x': 75, 'y': 68.74400329589844},
			{'x': 75, 'y': 69.00800323486328},
			{'x': 75, 'y': 69.27200317382812},
			{'x': 75, 'y': 69.53600311279297},
			{'x': 75, 'y': 69.80000305175781},
			{'x': 75, 'y': 70.06400299072266},
			{'x': 75, 'y': 70.3280029296875},
			{'x': 75, 'y': 70.59200286865234},
			{'x': 75, 'y': 70.85600280761719},
			{'x': 75, 'y': 71.12000274658203},
			{'x': 75, 'y': 71.38400268554688},
			{'x': 75, 'y': 71.64800262451172},
			{'x': 75, 'y': 71.91200256347656},
			{'x': 75, 'y': 72.1760025024414},
			{'x': 75, 'y': 72.44000244140625},
			{'x': 75, 'y': 72.7040023803711},
			{'x': 75, 'y': 72.96800231933594},
			{'x': 75, 'y': 73.23200225830078},
			{'x': 75, 'y': 73.49600219726562},
			{'x': 75, 'y': 73.76000213623047},
			{'x': 75, 'y': 74.02400207519531},
			{'x': 75, 'y': 74.28800201416016},
			{'x': 75, 'y': 74.552001953125},
			{'x': 75, 'y': 74.81600189208984},
			{'x': 75, 'y': 75.08000183105469},
			{'x': 75, 'y': 75.34400177001953},
			{'x': 75, 'y': 75.60800170898438},
			{'x': 75, 'y': 75.87200164794922},
			{'x': 75, 'y': 76.13600158691406},
			{'x': 75, 'y': 76.4000015258789},
			{'x': 75, 'y': 76.66400146484375},
			{'x': 75, 'y': 76.9280014038086},
			{'x': 75, 'y': 77.19200134277344},
			{'x': 75, 'y': 77.45600128173828},
			{'x': 75, 'y': 77.72000122070312},
			{'x': 75, 'y': 77.98400115966797},
			{'x': 75, 'y': 78.24800109863281},
			{'x': 75, 'y': 78.51200103759766},
			{'x': 75, 'y': 78.7760009765625},
			{'x': 75, 'y': 79.03999328613281},
			{'x': 75, 'y': 79.30400085449219},
			{'x': 75, 'y': 79.5679931640625},
			{'x': 75, 'y': 79.83200073242188},
			{'x': 75, 'y': 80.09599304199219},
			{'x': 75, 'y': 80.36000061035156},
			{'x': 75, 'y': 80.62399291992188},
			{'x': 75, 'y': 80.88800048828125},
			{'x': 75, 'y': 81.15199279785156},
			{'x': 75, 'y': 81.41600036621094},
			{'x': 75, 'y': 81.67999267578125},
			{'x': 75, 'y': 81.94400024414062},
			{'x': 75, 'y': 82.20799255371094},
			{'x': 75, 'y': 82.47200012207031},
			{'x': 75, 'y': 82.73599243164062},
		]

		for pt in points:
			self.points.append(Point(pt['x']*40, pt['y']*40))
