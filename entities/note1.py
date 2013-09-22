from lib.entity import Entity
from lib.point import *

import math

class Note1(Entity):
	def __init__(self):
		super(Note1, self).__init__()

		self.direc = 1 # XXX TEMPORARY 

		# Omg old points sampled from an SVG image!
		points = [
			{'x': 2495, 'y': 5928},
			{'x': 2468.16162109375, 'y': 5740.3505859375},
			{'x': 2442.387451171875, 'y': 5552.546875},
			{'x': 2416.822509765625, 'y': 5364.71484375},
			{'x': 2391.37548828125, 'y': 5176.8662109375},
			{'x': 2365.969482421875, 'y': 4989.0126953125},
			{'x': 2340.62744140625, 'y': 4801.14990234375},
			{'x': 2315.330810546875, 'y': 4613.28125},
			{'x': 2290.083251953125, 'y': 4425.40625},
			{'x': 2264.8388671875, 'y': 4237.53076171875},
			{'x': 2239.63720703125, 'y': 4049.649169921875},
			{'x': 2214.447998046875, 'y': 3861.766357421875},
			{'x': 2189.349365234375, 'y': 3673.87109375},
			{'x': 2164.352783203125, 'y': 3485.96240234375},
			{'x': 2139.267578125, 'y': 3298.065185546875},
			{'x': 2114.1357421875, 'y': 3110.174560546875},
			{'x': 2088.94140625, 'y': 2922.292236328125},
			{'x': 2063.68505859375, 'y': 2734.418212890625},
			{'x': 2038.355712890625, 'y': 2546.55419921875},
			{'x': 2012.9141845703125, 'y': 2358.705078125},
			{'x': 1987.3470458984375, 'y': 2170.873046875},
			{'x': 1961.613037109375, 'y': 1983.0640869140625},
			{'x': 1935.4381103515625, 'y': 1795.3160400390625},
			{'x': 1841.04296875, 'y': 1733.9970703125},
			{'x': 1670.3150634765625, 'y': 1816.3446044921875},
			{'x': 1494.4705810546875, 'y': 1887.01806640625},
			{'x': 1313.344970703125, 'y': 1942.72412109375},
			{'x': 1127.2652587890625, 'y': 1977.9169921875},
			{'x': 937.851318359375, 'y': 1982.9830322265625},
			{'x': 748.9135131835938, 'y': 1971.74072265625},
			{'x': 567.4451904296875, 'y': 1917.83251953125},
			{'x': 399.9424743652344, 'y': 1829.8275146484375},
			{'x': 255.78787231445312, 'y': 1707.357177734375},
			{'x': 142.57981872558594, 'y': 1555.7828369140625},
			{'x': 62.668724060058594, 'y': 1384.2020263671875},
			{'x': 15.220380783081055, 'y': 1201.0164794921875},
			{'x': 5.37522029876709, 'y': 1011.8203125},
			{'x': 13.640718460083008, 'y': 822.51171875},
			{'x': 55.41569900512695, 'y': 638.12744140625},
			{'x': 139.79977416992188, 'y': 468.89996337890625},
			{'x': 261.24853515625, 'y': 323.8444519042969},
			{'x': 408.3321228027344, 'y': 204.60943603515625},
			{'x': 572.9482421875, 'y': 111.0409164428711},
			{'x': 750.6455078125, 'y': 45.63210678100586},
			{'x': 936.5621948242188, 'y': 9.673659324645996},
			{'x': 1125.82763671875, 'y': 3.1615171432495117},
			{'x': 1313.95166015625, 'y': 25.059606552124023},
			{'x': 1497.0404052734375, 'y': 73.58061218261719},
			{'x': 1671.890625, 'y': 146.44761657714844},
			{'x': 1835.44970703125, 'y': 242.02008056640625},
			{'x': 1988.5631103515625, 'y': 353.6866455078125},
			{'x': 2131.60107421875, 'y': 477.9855041503906},
			{'x': 2260.94775390625, 'y': 616.4490356445312},
			{'x': 2293.763916015625, 'y': 800.4649658203125},
			{'x': 2317.6337890625, 'y': 988.5196533203125},
			{'x': 2341.503662109375, 'y': 1176.5751953125},
			{'x': 2365.20068359375, 'y': 1364.65234375},
			{'x': 2389.15771484375, 'y': 1552.6961669921875},
			{'x': 2413.328857421875, 'y': 1740.712890625},
			{'x': 2437.670654296875, 'y': 1928.7076416015625},
			{'x': 2462.185302734375, 'y': 2116.679931640625},
			{'x': 2486.849609375, 'y': 2304.632568359375},
			{'x': 2511.685546875, 'y': 2492.562744140625},
			{'x': 2536.4892578125, 'y': 2680.497314453125},
			{'x': 2561.071044921875, 'y': 2868.460205078125},
			{'x': 2585.59765625, 'y': 3056.430908203125},
			{'x': 2610.050048828125, 'y': 3244.412353515625},
			{'x': 2634.40234375, 'y': 3432.405029296875},
			{'x': 2658.594482421875, 'y': 3620.4189453125},
			{'x': 2682.417724609375, 'y': 3808.479736328125},
			{'x': 2705.96533203125, 'y': 3996.5751953125},
			{'x': 2734.134765625, 'y': 4183.9833984375},
			{'x': 2864.848388671875, 'y': 4104.32470703125},
			{'x': 2998.9765625, 'y': 3970.3720703125},
			{'x': 3130.775634765625, 'y': 3834.128173828125},
			{'x': 3255.62353515625, 'y': 3691.58837890625},
			{'x': 3370.571533203125, 'y': 3540.87939453125},
			{'x': 3476.157958984375, 'y': 3383.490234375},
			{'x': 3569.080078125, 'y': 3218.3330078125},
			{'x': 3645.48779296875, 'y': 3044.94873046875},
			{'x': 3701.889892578125, 'y': 2864.084228515625},
			{'x': 3736.67138671875, 'y': 2677.84326171875},
			{'x': 3749.17138671875, 'y': 2488.86669921875},
			{'x': 3734.99169921875, 'y': 2299.93115234375},
			{'x': 3705.354736328125, 'y': 2112.753662109375},
			{'x': 3660.15478515625, 'y': 1928.7032470703125},
			{'x': 3604.568115234375, 'y': 1747.484619140625},
			{'x': 3544.074462890625, 'y': 1567.835205078125},
			{'x': 3481.80615234375, 'y': 1388.7913818359375},
			{'x': 3484.532470703125, 'y': 1266.4117431640625},
			{'x': 3647.267578125, 'y': 1363.4068603515625},
			{'x': 3798.888916015625, 'y': 1476.9935302734375},
			{'x': 3936.782470703125, 'y': 1606.9410400390625},
			{'x': 4060.227783203125, 'y': 1750.6829833984375},
			{'x': 4168.0234375, 'y': 1906.511474609375},
			{'x': 4259.1171875, 'y': 2072.65771484375},
			{'x': 4332.57275390625, 'y': 2247.3193359375},
			{'x': 4387.53173828125, 'y': 2428.650634765625},
			{'x': 4423.2158203125, 'y': 2614.734130859375},
			{'x': 4438.9443359375, 'y': 2803.55419921875},
			{'x': 4434.19384765625, 'y': 2992.963623046875},
			{'x': 4409.81640625, 'y': 3180.890625},
			{'x': 4369.857421875, 'y': 3366.1416015625},
			{'x': 4315.0185546875, 'y': 3547.544921875},
			{'x': 4246.38134765625, 'y': 3724.201171875},
			{'x': 4165.494140625, 'y': 3895.60400390625},
			{'x': 4074.0869140625, 'y': 4061.643798828125},
			{'x': 3973.519287109375, 'y': 4222.29638671875},
			{'x': 3860.74609375, 'y': 4374.60205078125},
			{'x': 3737.652587890625, 'y': 4518.73046875},
			{'x': 3608.062744140625, 'y': 4657.0703125},
			{'x': 3481.089599609375, 'y': 4797.80224609375},
			{'x': 3377.391357421875, 'y': 4955.9560546875},
			{'x': 3295.841796875, 'y': 5127.0283203125},
			{'x': 3223.420166015625, 'y': 5302.20361328125},
			{'x': 3155.5302734375, 'y': 5479.1904296875},
			{'x': 3090.14794921875, 'y': 5657.12255859375},
			{'x': 3025.4267578125, 'y': 5835.2958984375},
			{'x': 2858.1962890625, 'y': 5890.482421875},
			{'x': 2671.196533203125, 'y': 5921.55029296875},
			{'x': 2495, 'y': 5928},
			{'x': 2495, 'y': 5928},
			{'x': 2490.601318359375, 'y': 5899.90966796875},
			{'x': 2486.536865234375, 'y': 5871.76708984375},
			{'x': 2482.546630859375, 'y': 5843.61376953125},
			{'x': 2478.59521484375, 'y': 5815.455078125},
			{'x': 2474.68017578125, 'y': 5787.29150390625},
			{'x': 2470.76513671875, 'y': 5759.12744140625},
			{'x': 2466.86865234375, 'y': 5730.9609375},
			{'x': 2462.989501953125, 'y': 5702.79248046875},
		]


		for pt in points:
			self.points.append(Point(pt['x'], pt['y']))

