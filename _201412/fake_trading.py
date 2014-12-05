# encoding: utf-8

import random

config = {
    'init_price': 200.0,
    'buy_ratio': 0.7,  # buy when the price is 70% of the last trading price
    'sell_ratio': 1.4, # sell when the price is 150% of the last trading price
}


class Trader(object):
    def __init__(self, cash=1000000):
        self.cash = cash    # total
        self.market_value = 0
        self.market_volume = 0
        self.trade_record = []

    def buy(self, p, v):# p --> price   v --> volume
        if self.cash < p*v:
            return
        self.cash -= p*v  
        self.market_volume += v
        self.market_value += p*v
        self.trade_record.append(('B', p, v))

    def sell(self, p, v):
        if self.market_volume < v:
            return
        self.cash += p*v
        self.market_volume -= v
        self.market_value -= p*v
        self.trade_record.append(('S', p, v))

    def fake_trading(self, price_list):
        br = config['buy_ratio']
        sr = config['sell_ratio']
        if len(self.trade_record) == 0:
            self.buy(config['init_price'], 1000)
        for p in price_list:
            if p <= 0:
                return
            last_trade = self.trade_record[-1]
            last_trade_price = last_trade[1]
            last_trade_volume = last_trade[2]
            if p >= last_trade_price * sr:
                
                #volume = last_trade_volume
                volume = int(self.market_volume / 5)
                self.sell(p, volume)
            elif p <= last_trade_price * br:
                volume = int(last_trade_price * last_trade_volume / p)
                #volume = last_trade_volume  # no
                self.buy(p, volume)


def price_list(length):
    plist = []
    price = config['init_price']
    for n in range(length):
        price += random.randint(-20, 20)
        plist.append(price*1.0001)  # 
        print 'in price_list' , price
    print plist
    return plist
plist1 = [200.02, 193.0193, 201.02009999999999, 212.0212, 211.0211, 215.0215, 220.022, 227.0227, 221.0221, 219.0219, 207.0207, 226.0226, 228.0228, 245.0245, 233.0233, 247.0247, 252.02519999999998, 264.0264, 280.028, 278.0278, 273.0273, 276.0276, 291.02909999999997, 303.0303, 285.0285, 291.02909999999997, 272.0272, 260.026, 275.0275, 272.0272, 276.0276, 265.0265, 281.0281, 298.0298, 306.0306, 290.029, 297.0297, 279.0279, 286.0286, 285.0285, 288.0288, 286.0286, 299.0299, 291.02909999999997, 285.0285, 283.0283, 272.0272, 267.0267, 272.0272, 286.0286, 303.0303, 306.0306, 313.0313, 304.0304, 302.0302, 321.0321, 325.03249999999997, 308.0308, 294.0294, 293.0293, 306.0306, 318.0318, 299.0299, 289.0289, 297.0297, 313.0313, 313.0313, 330.033, 320.032, 324.0324, 322.0322, 316.03159999999997, 299.0299, 309.0309, 318.0318, 316.03159999999997, 320.032, 304.0304, 308.0308, 309.0309, 293.0293, 292.0292, 273.0273, 289.0289, 277.0277, 296.0296, 280.028, 291.02909999999997, 288.0288, 282.02819999999997, 290.029, 283.0283, 282.02819999999997, 275.0275, 264.0264, 258.0258, 258.0258, 259.0259, 247.0247, 241.0241, 251.0251, 263.0263, 265.0265, 266.0266, 254.0254, 234.0234, 221.0221, 219.0219, 201.02009999999999, 196.0196, 211.0211, 230.023, 227.0227, 222.0222, 214.0214, 203.0203, 214.0214, 194.0194, 194.0194, 192.0192, 188.0188, 190.019, 191.0191, 186.0186, 201.02009999999999, 192.0192, 195.0195, 181.0181, 195.0195, 203.0203, 193.0193, 193.0193, 180.018, 189.0189, 207.0207, 227.0227, 238.0238, 220.022, 212.0212, 207.0207, 224.0224, 209.0209, 227.0227, 215.0215, 229.0229, 233.0233, 226.0226, 232.0232, 226.0226, 239.0239, 233.0233, 242.0242, 236.0236, 235.02349999999998, 237.0237, 219.0219, 231.0231, 243.0243, 244.02439999999999, 234.0234, 243.0243, 256.0256, 260.026, 244.02439999999999, 256.0256, 239.0239, 245.0245, 244.02439999999999, 241.0241, 221.0221, 231.0231, 213.0213, 231.0231, 226.0226, 209.0209, 220.022, 232.0232, 214.0214, 232.0232, 244.02439999999999, 243.0243, 254.0254, 261.0261, 261.0261, 267.0267, 258.0258, 274.0274, 288.0288, 305.0305, 305.0305, 320.032, 309.0309, 310.031, 308.0308, 295.0295, 308.0308, 319.0319, 330.033, 314.0314, 319.0319, 306.0306, 290.029, 275.0275, 256.0256, 265.0265, 284.0284, 271.0271, 284.0284, 279.0279, 279.0279, 265.0265, 282.02819999999997, 267.0267, 268.0268, 252.02519999999998, 232.0232, 233.0233, 253.0253, 259.0259, 268.0268, 281.0281, 287.0287, 269.0269, 252.02519999999998, 238.0238, 240.024, 250.025, 247.0247, 258.0258, 240.024, 237.0237, 249.0249, 241.0241, 256.0256, 246.0246, 261.0261, 270.027, 274.0274, 282.02819999999997, 300.03, 306.0306, 304.0304, 285.0285, 287.0287, 298.0298, 299.0299, 288.0288, 301.0301, 317.0317, 332.0332, 331.0331, 320.032, 328.0328, 327.0327, 328.0328, 327.0327, 320.032, 301.0301, 302.0302, 309.0309, 313.0313, 300.03, 305.0305, 292.0292, 291.02909999999997, 272.0272, 252.02519999999998, 234.0234, 249.0249, 258.0258, 276.0276, 263.0263, 259.0259, 249.0249, 258.0258, 263.0263, 251.0251, 247.0247, 260.026, 265.0265, 275.0275, 281.0281, 287.0287, 270.027, 259.0259, 246.0246, 248.0248, 256.0256, 237.0237, 247.0247, 232.0232, 236.0236, 245.0245, 237.0237, 220.022, 210.021, 194.0194, 207.0207, 187.0187, 187.0187, 186.0186, 196.0196, 199.0199, 214.0214, 230.023, 225.0225, 216.0216, 207.0207, 218.02179999999998, 227.0227, 238.0238, 244.02439999999999, 253.0253, 268.0268, 288.0288, 269.0269, 263.0263, 249.0249, 253.0253, 263.0263, 275.0275, 285.0285, 292.0292, 311.0311, 301.0301, 313.0313, 309.0309, 298.0298, 295.0295, 276.0276, 270.027, 289.0289, 278.0278, 263.0263, 280.028, 292.0292, 272.0272, 264.0264, 247.0247, 258.0258, 241.0241, 238.0238, 240.024, 235.02349999999998, 245.0245, 242.0242, 230.023, 215.0215, 195.0195, 203.0203, 200.02, 220.022, 214.0214, 224.0224, 220.022, 232.0232, 240.024, 226.0226, 209.0209, 224.0224, 233.0233, 227.0227, 246.0246, 243.0243, 246.0246, 238.0238, 235.02349999999998, 231.0231, 244.02439999999999, 240.024, 241.0241, 255.0255, 267.0267, 264.0264, 283.0283, 286.0286, 275.0275, 280.028, 284.0284, 297.0297, 286.0286, 267.0267, 251.0251, 266.0266, 258.0258, 242.0242, 255.0255, 273.0273, 276.0276, 275.0275, 289.0289, 277.0277, 267.0267, 280.028, 294.0294, 308.0308, 310.031, 326.0326, 345.0345, 351.0351, 366.0366, 376.0376, 394.0394, 397.0397, 391.0391, 404.0404, 399.0399, 400.04, 413.0413, 412.0412, 431.0431, 415.0415, 428.0428, 416.0416, 427.04269999999997, 422.0422, 413.0413, 424.0424, 426.0426, 415.0415, 417.0417, 397.0397, 396.0396, 402.04019999999997, 397.0397, 388.0388, 371.0371, 361.0361, 347.0347, 363.0363, 370.037, 359.03589999999997, 379.0379, 394.0394, 402.04019999999997, 392.0392, 390.039, 371.0371, 371.0371, 383.0383, 394.0394, 410.041, 423.0423, 434.0434, 454.0454, 468.0468, 459.0459, 457.0457, 439.0439, 424.0424, 430.043, 411.0411, 402.04019999999997, 383.0383, 380.038, 365.0365, 376.0376, 390.039, 391.0391, 374.0374, 369.0369, 365.0365, 373.0373, 373.0373, 359.03589999999997, 340.034, 344.0344, 355.0355, 347.0347, 330.033, 325.03249999999997, 339.0339, 324.0324, 330.033, 337.0337, 341.0341, 322.0322, 302.0302, 300.03, 317.0317, 302.0302, 300.03, 313.0313, 297.0297, 278.0278, 273.0273, 272.0272, 260.026, 257.0257, 277.0277, 290.029, 306.0306, 308.0308, 319.0319, 321.0321, 335.0335, 343.0343, 354.0354, 366.0366, 368.03679999999997, 364.0364, 351.0351, 370.037, 350.03499999999997, 335.0335, 332.0332, 333.0333, 332.0332, 351.0351, 342.0342, 349.0349, 362.0362, 381.0381, 362.0362, 357.0357, 373.0373, 365.0365, 382.0382, 378.0378, 392.0392, 395.0395, 405.0405, 388.0388, 373.0373, 363.0363, 353.0353, 337.0337, 348.0348, 330.033, 317.0317, 328.0328, 346.0346, 346.0346, 359.03589999999997, 343.0343, 348.0348, 352.0352, 365.0365, 354.0354, 341.0341, 324.0324, 311.0311, 291.02909999999997, 275.0275, 272.0272, 289.0289, 289.0289, 274.0274, 257.0257, 263.0263, 282.02819999999997, 283.0283, 290.029, 300.03, 308.0308, 321.0321, 319.0319, 305.0305, 308.0308, 322.0322, 311.0311, 327.0327, 338.0338, 349.0349, 332.0332, 340.034, 350.03499999999997, 365.0365, 368.03679999999997, 358.0358, 349.0349, 346.0346, 341.0341, 350.03499999999997, 361.0361, 371.0371, 385.0385, 385.0385, 375.0375, 356.0356, 348.0348, 344.0344, 355.0355, 338.0338, 357.0357, 341.0341, 361.0361, 349.0349, 335.0335, 318.0318, 333.0333, 318.0318, 308.0308, 323.0323, 334.0334, 338.0338, 352.0352, 366.0366, 369.0369, 376.0376, 389.0389, 376.0376, 364.0364, 380.038, 388.0388, 394.0394, 376.0376, 378.0378, 365.0365, 384.0384, 394.0394, 391.0391, 405.0405, 416.0416, 403.0403, 422.0422, 429.0429, 422.0422, 418.0418, 416.0416, 419.0419, 414.0414, 398.0398, 395.0395, 382.0382, 385.0385, 391.0391, 395.0395, 378.0378, 398.0398, 394.0394, 383.0383, 392.0392, 393.03929999999997, 398.0398, 404.0404, 411.0411, 409.0409, 390.039, 395.0395, 395.0395, 394.0394, 389.0389, 397.0397, 416.0416, 409.0409, 422.0422, 408.0408, 423.0423, 413.0413, 429.0429, 432.0432, 445.04449999999997, 455.0455, 440.044, 460.046, 463.0463, 456.0456, 446.0446, 461.04609999999997, 442.0442, 438.0438, 430.043, 446.0446, 457.0457, 474.0474, 485.0485, 469.0469, 476.0476, 463.0463, 464.0464, 448.0448, 454.0454, 435.0435, 419.0419, 437.0437, 417.0417, 420.042, 438.0438, 435.0435, 438.0438, 448.0448, 443.0443, 445.04449999999997, 453.0453, 452.0452, 434.0434, 414.0414, 422.0422, 441.0441, 459.0459, 476.0476, 492.0492, 505.0505, 520.052, 532.0532, 524.0524, 520.052, 521.0521, 516.0516, 529.0529, 541.0541, 521.0521, 530.053, 520.052, 539.0539, 553.0553, 542.0542, 527.0527, 535.0535, 515.0515, 497.0497, 517.0517, 531.0531, 542.0542, 531.0531, 516.0516, 524.0524, 523.0523, 537.0537, 547.0547, 545.0545, 552.0552, 561.0561, 546.0546, 529.0529, 528.0528, 511.0511, 499.0499, 492.0492, 510.051, 499.0499, 516.0516, 500.05, 496.0496, 508.0508, 517.0517, 536.0536, 553.0553, 550.055, 530.053, 512.0512, 498.0498, 493.0493, 508.0508, 520.052, 528.0528, 546.0546, 563.0563, 562.0562, 546.0546, 560.056, 558.0558, 558.0558, 573.0572999999999, 563.0563, 546.0546, 529.0529, 510.051, 491.0491, 482.0482, 494.0494, 506.0506, 526.0526, 546.0546, 557.0557, 554.0554, 574.0574, 585.0585, 587.0587, 596.0596, 580.058, 585.0585, 575.0575, 564.0563999999999, 570.057, 589.0589, 606.0606, 602.0602, 604.0604, 611.0611, 616.0616, 606.0606, 625.0625, 640.064, 646.0646, 665.0665, 674.0674, 676.0676, 688.0688, 672.0672, 678.0678, 659.0658999999999, 673.0673, 683.0683, 666.0666, 669.0669, 668.0668, 675.0675, 682.0682, 696.0696, 715.0715, 699.0699, 710.071, 724.0724, 727.0726999999999, 734.0734, 737.0737, 753.0753, 747.0747, 727.0726999999999, 735.0735, 739.0739, 738.0738, 738.0738, 728.0728, 729.0729, 720.072, 735.0735, 717.0717, 715.0715, 707.0707, 691.0691, 705.0705, 713.0713, 696.0696, 700.0699999999999, 705.0705, 686.0686, 705.0705, 716.0716, 700.0699999999999, 700.0699999999999, 715.0715, 724.0724, 717.0717, 723.0723, 707.0707, 725.0725, 719.0719, 705.0705, 687.0687, 692.0692, 706.0706, 714.0714, 695.0695, 675.0675, 660.066, 649.0649, 637.0637, 626.0626, 635.0635, 624.0624, 624.0624, 611.0611, 596.0596, 598.0598, 602.0602, 598.0598, 609.0609, 603.0603, 586.0586, 588.0588, 586.0586, 580.058, 567.0567, 549.0549, 559.0559, 576.0576, 590.059, 586.0586, 587.0587, 592.0592, 604.0604, 622.0622, 602.0602, 620.062, 634.0634, 631.0631, 639.0639, 650.0649999999999, 667.0667, 657.0657, 674.0674, 672.0672, 669.0669, 678.0678, 678.0678, 672.0672, 674.0674, 688.0688, 671.0671, 671.0671, 651.0651, 658.0658, 672.0672, 665.0665, 651.0651, 634.0634, 626.0626, 624.0624, 608.0608, 606.0606, 618.0618, 638.0638, 619.0619, 617.0617, 632.0631999999999, 625.0625, 631.0631, 617.0617, 601.0601, 612.0612, 609.0609, 592.0592, 593.0593, 588.0588, 596.0596, 579.0579, 570.057, 563.0563, 555.0554999999999, 562.0562, 582.0581999999999, 583.0583, 592.0592, 603.0603, 622.0622, 612.0612, 632.0631999999999, 632.0631999999999, 639.0639, 657.0657, 646.0646, 646.0646, 633.0633, 629.0629, 619.0619, 603.0603, 602.0602, 588.0588, 607.0607, 601.0601, 585.0585, 596.0596, 593.0593, 593.0593, 584.0584, 580.058, 596.0596, 603.0603, 613.0613, 613.0613, 617.0617, 610.061, 620.062, 609.0609, 594.0594, 609.0609, 619.0619, 628.0628, 621.0621, 602.0602, 592.0592, 589.0589, 599.0599, 588.0588, 594.0594, 574.0574, 580.058, 587.0587, 591.0591, 577.0577, 585.0585, 566.0566, 564.0563999999999, 569.0569, 554.0554, 551.0551, 542.0542, 532.0532, 533.0533, 543.0543, 523.0523, 531.0531, 511.0511, 501.0501, 492.0492, 499.0499, 515.0515, 525.0525, 541.0541, 561.0561, 581.0581, 600.06, 619.0619, 609.0609, 599.0599, 595.0595]


trader = Trader()
#trader.fake_trading(price_list(999))
trader.fake_trading(plist1)
for r in trader.trade_record:
    print r
print 'current cash: ', trader.cash
print 'current market value: ', trader.market_value
print 'current market volume: ', trader.market_volume