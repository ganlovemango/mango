from  PIL import Image
from  PIL import ImageDraw
from  PIL import ImageFont
from random import randint


class VerifyCode:
    def __init__(self,width=100,height=40,size=4):
        """
        初始化验证码
        :param width: 图片宽度
        :param height: 高度
        :param size: 字符个数
        """
        self.width = width
        self.height = height
        self.size = size
        self.__code = None  #验证码字符串
    @property
    def code(self):
        return self.__code

    def generate(self):
        #1 初始化画笔画布
        self.__init_image()

        # 2.生成验证码字符
        self.rand_string()
        # 3.画字符
        self.__draw_string()

        #4.画干扰点
        self.__draw_point()

        #5.画干扰线
        self.__draw_line()

        #6.保存图片
        self.im.save("yzm.png")

    def __draw_string(self):
        width = (self.width - 10)/self.size  #字符宽度
        font1 = ImageFont.truetype("UbuntuMono-RI.ttf",size=20)
        for i in range(len(self.__code)):
            x = 15 + i * width
            y = randint(6,16)
            self.pen.text((x,y),self.__code[i],fill=self.__rand_color(40,120),font=font1)

    def rand_string(self):
        s1 = ''
        for i in range(self.size):
            s1 += str(randint(0,9))
        self.__code = s1

    # 画干扰线
    def __draw_line(self):
        for i in range(6):
            x1 = randint(1, self.width - 1)
            y1 = randint(1, self.height - 1)
            x2 = randint(1, self.width - 1)
            y2 = randint(1, self.height - 1)
            self.pen.line([(x1,y1),(x2,y2)],fill=self.__rand_color(40,160))

    #画干扰点
    def __draw_point(self):
        for i in range(150):
            x = randint(1,self.width-1)
            y = randint(1,self.height-1)
            self.pen.point((x,y),fill=self.__rand_color(40,160))


    def __init_image(self):
        self.im = Image.new("RGB",(self.width,self.height),self.__rand_color(160,255))
        self.pen = ImageDraw.Draw(self.im)

    #随机颜色
    def __rand_color(self,low,high):
        return randint(low,high),randint(low,high),randint(low,high)

if __name__ == "__main__":
    vc = VerifyCode()
    vc.generate()
    print(vc.code)