#buoc 1 : cho cno xem location hien tai la o HaNoi
#buoc 2 : cho cno xem list location
#buoc 3 : cho cno xem list boat
#buoc 4 : cho chọn
#bước 5 : tính toán thời gian đi
#bước 6 : bay và time sleep
#bước 7 : đến nơi
import math
import time
import random

now_location = "Hanoi"
places = ['Los angeles', 'Houston', 'Bern', 'Geneva', 'Cairo', 'Beijing', 'Nanjing', 'HCMcity', 'Da Nang', 'Kiev', 'Odessa', 'Ha Noi']
types = ['Boeing 747', 'Airbus A380', 'Airbus A350', 'Boeing 777', 'sukhoi su-34' ,'sukhoi su-35', 'A10-Warthog']
speed = {'Boeing 747':988,
          'Airbus A380':1076, 
          'Airbus A350':1185,
        'Boeing 777':945, 
        'sukhoi su-34': 2200,
        'sukhoi su-35':2778,
          'A10-Warthog':676}
while True : 
    exit = False
    if exit == True :
        break
    now_x = 0
    now_y = 0
    x = 0
    y = 0
    
    print("Vị trí hiện tại:", now_location)
    choice = ")"
    information = False
    while information != True :
        while choice != "s" :
                choice = input("Chon boats hoac locations de xem thong tin chi tiet. Chon S de tiep tuc: ").lower()
                if choice == "boats" :
                    with open("boats.txt") as  boats:
                        print(boats.read())
                        continue
                elif choice == "locations":
                    with open("location.txt") as location:
                        print(location.read())
                        continue 
                elif choice == "s":
                    break
                else :
                    print("Nhap dung chinh ta")
        
                    continue

        asking = True
        while asking == True :
            model = input("Chon thuyen (an B de quay lai):")
            if model in types:
                print("model da chon:", model)
                break
            elif model == "B" or model =="b":
                choice = "0"
                asking = False
                
                break
            else :
                print("-----------")
                print("chọn đúng tên thuyền")
                continue

        while asking == True :
            arrival = input("Chon diem den (an B de quay lai):")
            if arrival in places:
                if arrival == "Bern":
                    x =  -3064
                    y = 256
                elif arrival == "Geneva":
                    x =  -3257
                    y = 126
                elif arrival == "Kiev":
                    x =  -2075
                    y = 300
                elif arrival == "Odessa":
                    x =  -2200
                    y = 75
                elif arrival == "Nanjing":
                    x =  30
                    y = 325
                elif arrival == "Beijing":
                    x =  40
                    y = 756
                elif arrival == "Los angeles":
                    x =  4327
                    y = 780
                elif arrival == "Houston":
                    x =  4790
                    y = 453
                elif arrival == "DaNang":
                    x = 10
                    y = -128
                elif arrival == "HCMcity":
                    x = 5
                    y = -256
                elif arrival == "Ha Noi":
                    x = 0
                    y = 0
                print("Destination da chon:", arrival)
                asking = False
                break
            elif arrival == "B" or arrival == "b":
                choice = "0"
                asking = False
                break
            else :
                print("-----------")
                print("chọn đúng điểm đến")
                continue
        distance = math.sqrt((x-now_x)**2+(y-now_y)**2)
        distance = math.ceil(distance)
        weather = [0, 1]
        real_weather = random.choice(weather)
        now_location = arrival
        print("----------------START----------------")
        if real_weather == 0 :
            print("k co bao ae di nhanh")
            print("thoi gian can thiet de hoan thanh chuyen di:",distance/speed[model] + real_weather,"h")
        else : 
            print("Baox to vcl ae thong cam")
            print("Thoi gain di la :",distance/speed[model] + real_weather,"h")
        print("dang cheo thuyen ae doi ti.....")
        time.sleep(3600*(distance/speed[model] + real_weather))
        print("you are now at:",arrival)
        print("----------------THANKS----------------")
        break 
    

        
        
        