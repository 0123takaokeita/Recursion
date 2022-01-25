# String getStateString():   // 動物の情報を文字列として返します。
# double getBmi():           // 動物のBMIを返します。BMIの公式 kg/(height2) を使ってください。
# double getDailyCalories(): // 動物が毎日どれほどのカロリーを消費する必要があるか返します。計算式は、(70 * weightKg0.75) * activityMultiplierで求めることができます。
# bool isDangerous():        // 動物が危険かどうか判断するブーリアン値を返します。動物が捕食者だった場合、危険とみなされ、身長が1.7メートル以上、もしくは時速35km/h以上の場合も危険とみなされます。
# bool isFaster(animal):     // 動物のオブジェクトを受け取り、動物のオブジェクトがパラメータの入力として渡された動物より速いかどうか判断します。

from pydoc import describe
from tkinter import N


class Animal():
    activityMultiplier = 1.2

    def __init__(self, name, species, description, weightKg, heightM, isPredator, speedKph, urlPic, registerDate):
        self.name = name
        self.species = species
        self.description = description
        self.weightKg = weightKg
        self.heightM = heightM
        self.isPredator = isPredator
        self.speedKph = speedKph
        self.urlPic = urlPic
        self.registerDate = registerDate

    def getStateStrig(self):
        string = '動物のスペックの説明\n'
        string += f"名前    :{self.name}\n"
        string += f"属性    :{self.species}\n"
        string += f"説明    :{self.description}\n"
        string += f"体重    :{self.weightKg}kg\n"
        string += f"体高    :{self.heightM}M\n"
        string += f"危険度  :{self.isPredator}\n"
        string += f"速度    :{self.speedKph}Km/h\n"
        string += f"写真URL :{self.urlPic}\n"
        string += f"登録日時:{self.registerDate}\n"
        return string

    def getBmi(self):
        bmi = self.weightKg / self.heightM*2
        return f"{self.name}のBMIは{bmi}です\n"

    def getDailyCalories(self):
        return f"{(70 * self.weightKg ** 0.75) * self.activityMultiplier} \n"

    def isDangerous(self):
        if self.isPredator or self.heightM >= 1.7 or self.speedKph >= 35:
            return f"{self.name}は危険です。\n"
        else:
            return f"{self.name}は安全です。\n"

    def isFaster(self, animal):
        if self.speedKph > animal.speedKph:
            return f"{animal.name}より早いです\n"
        else:
            return f"{animal.name}より遅いです。\n"


rabbit = Animal("rabbit", "leporidae",
                "Rabbits are small mammals in the family Leporidae of the order Lagomorpha (along with the hare and the pika).",
                10, 0.3, False, 20, "img1", "2020/5/25")

print(rabbit.getStateStrig())
print(rabbit.getBmi())       # : 111.11111111111111
print(rabbit.getDailyCalories())    #: 472.36671315989327
print(rabbit.isDangerous())


elephant = Animal("elephant", "Elephantidae",
                  "Elephants are mammals of the family Elephantidae and the largest existing land animals.", 300, 3, False, 5, "img2", "2020/5/26")


print(elephant.getStateStrig())
print(elephant.getBmi())
print(elephant.getDailyCalories())
print(elephant.isDangerous())
print(elephant.isFaster(rabbit))
