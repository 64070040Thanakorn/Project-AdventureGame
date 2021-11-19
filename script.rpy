﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# define a = Character("Panot",type=adv, color="#ee4705")

define py = Character("[name]", what_prefix = '{cps=75}')
define nrt = Character("", what_prefix = '{cps=75}')
define cat = Character("แมวปริศนา", what_prefix = '{cps=75}')
define human = Character("ชายผมทอง", what_prefix = '{cps=75}')
define kimera = Character("ปีศาจนิรนาม", what_prefix = '{cps=75}')
define boss = Character("ชายในชุดคลุมสีดำ", what_prefix = '{cps=75}')
define dragon = Character("มังกือ", what_prefix = '{cps=75}')
define future = Character("ผู้มาจากอนาคต", what_prefix = '{cps=75}')
define fakegod = Character("ผู้งมงาย", what_prefix = '{cps=75}')
define seer = Character("หมอดู", what_prefix = '{cps=75}')
define egg = Character("เด็กกะโปโล", what_prefix = '{cps=75}')


# transform bounce:
#     linear 3.0 xalign 1.0
#     linear 3.0 xalign 0.0
#     repeat

# transform headright:
#     linear 15 xalign 1.0

# screen choice(items):
#     style_prefix "choice"

#     vbox:
#         for i in items:
#             textbutton i.caption action i.action

#     if (timeout_label is not None) and persistent.timed_choices:

#         bar:
#             xalign 0.5
#             ypos 600
#             xsize 900
#             value AnimatedValue(old_value=0.0, value=2.0, range=2.0, delay=timeout)

#         timer timeout action Jump(timeout_label)

########## cat position
transform poscatsleep:
    pos((500, 300))

transform poscatidle1:
    pos((500, 250))

transform poscatidle2:
    pos((520, 220))

transform posface:
    pos((25, 265))

######### human position
transform poshuman:
    pos((420, 135))

transform poslion:
    pos((250,200))

transform poslionawake:
    pos((250,50))

transform poskimera:
    pos((350,100))

# The game starts here.
label start:
    $name = renpy.input("โปรดใส่ชื่อตัวละครของคุณ: ")
    $name = name.strip()
    $potion = 0
    $amulet = 0
    $compa = 0
    $sword = 0
    $armor = 0
    $pain = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    scene land
    nrt "ณ ดินแดนแห่งหนึ่งอันสงบสุขที่ปกครองโดยเทพเจ้า"
    nrt "แต่แล้ววันหนึ่งเทพเจ้าก็ได้หายไป ทำให้ทุกๆอย่างปั่นป่วน"
    nrt "นับตั้งแต่วันนั้น....ดินแดนต่างๆก็ได้เกิดเหตุการณ์ประหลาดขึ้น"
    scene dragon_lair
    nrt "หุบเข้าของเทพเจ้าทางตอนเหนือได้ถูกปกคลุมไปด้วยพายุเพลิง"
    scene before_desert
    nrt "ดินแดนทางใต้นั้นได้แห้งแล้งลงจนไม่สามารถปลูกอะไรได้"
    scene forest2
    nrt "ดินแดนทางตะวันออกถูกสัตว์ร้ายอันทรงพลังเข้ามายึดป่า"
    scene before_cat
    nrt "หุบเขาทางทิศตะวันตกก็ปกคลุมไปด้วยพายุหิมะ"
    scene black
    nrt "ท่านตัดสินใจออกเดินทางเพื่อค้นหาความจริงว่ามันเกิดอะไรขึ้นกันแน่"
    nrt "ท่านพร้อมออกเดินทางแล้วใช่หรือไม่"
    menu:
        "ใช่":
            jump iwant
        "ไม่ใช่":
            jump idontwant
    label idontwant:
        nrt "คุณตัดสินใจแล้ว...ว่าคุณขี้เกียจเดินทาง\n{vspace=5}หลังจากนั้นคุณก็กลับบ้านไปใช้ชีวิตอย่างมีความสุข?"
        label end0:
            scene end0
            nrt "ตอนจบที่ 0: ไอสันหลังยาว"
            nrt "คุณได้กลับหมู่บ้านโดยทิ้งให้โลกนั้นปั่นป่วนต่อไป...\n{vspace=5}สักวันหนึ่งอาจจะมีฮีโร่คนใหม่มากอบกู้ความปั่นป่วนนี้"
            return

    label iwant:
        scene first_scene
        nrt "ท่านตัดสินใจแล้วว่าจะออกเดินทาง\n{vspace=5}แต่ว่า... ท่านยังไม่รู้ว่าจะเริ่มต้นยังไงดี ท่านคิดว่าท่านจะถามคนในหมู่บ้าน แต่ว่า คุณจะถามใครดีล่ะ"
    label iwant1:
        menu:
            "ผู้มาจากอนาคต":
                jump future
            "ผู้งมงาย":
                jump fakegod
            "หมอดู":
                jump seer
            "เด็กแถวบ้าน":
                jump egg
    label future:
        py "ข้าขอถาม-"
        future "เนื่องจาก String นั้นเกิดจากตัวอักษรหลายๆ ตัวต่อกันจนเกิดเป็น String"
        future "หรือกล่าวอีกนัยหนึ่งก็คือ"
        future "String คืออาเรย์ของตัวอักษรดังนั้นเราจึงสามารถเข้าถึงตัวอักษรตำแหน่งต่างๆ\n{vspace=5}ของ String ได้ผ่านทาง Index ของมัน\n{vspace=5}เช่นเดียวกับการเข้าถึงข้อมูลใน List"
        py "เอ่อ............"
        future "Index ของ String นั้นจะเริ่มจาก 0 สำหรับตำแหน่งแรก และเพิ่มขึ้นทีละ 1\n{vspace=5}ไปจนถึงตำแหน่งสุดท้าย"
        nrt "ท่านอยู่ในยุคที่ยังใช้นกพิราบส่งจดหมายอยู่เลยด้วยซ้ำ\n{vspace=5}ท่านจึงไม่รู้ว่าไอนี่มันพูดอะไรของมัน"
        jump iwant1
    label fakegod:
        fakegod "ท่านๆ วันนี้วันศุกร์ที่13! วันที่13! 013! วันนี้เป็นวันอัปมงคลอย่างยิ่ง!\n{vspace=5}ท่านอย่าออกจากที่อยู่ของท่านโดยเด็ดขาด!"
        py "แต่วันนี้มันวันอังคารไม่ใช่รึ?"
        fakegod "ทุกวันคือวันที่13!!1!\n{vspace=5}อ้ากกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกก*ตะโกนอย่างบ้าคลั่ง*"
        nrt "ท่านแน่ใจแล้วว่าท่านคงถามคนนี้ไม่รู้เรื่องแน่"
        jump iwant1
    label seer:
        seer "ท่านผู้กล้า ข้ารู้ว่าท่านต้องการจะออกไปช่วยหมู่บ้านและสืบหาความจริงของเทพที่หายไป\n{vspace=5}ข้าจะขอดูอนาคตของท่านซักหน่อย"
        seer "ข้าเห็นแล้ว ท่านควรจะไปที่หุบเขา ที่แห่งนั้นมีแมววิเศาที่จะมีประโยชน์ต่อท่าน\n{vspace=5}เลือกให้ดีว่าจะใช้จิตใจหรือกิเลสในการแก้ปัญหา\n{vspace=5}ทางที่ท่านเลือกจะส่งผลต่อการเดินทางทางต่อไปของท่านของท่าน"
        seer "ทุกสิ่งที่ท่านพบเจอที่ท่านคุยย่อมมีความหมาย ขอให้โชคดีกับการเดินทาง นักเดินทาง!"
        jump beforecat
    label egg:
        egg ""
        jump iwant1
    label beforecat:
        nrt "ท่านตัดสินใจแล้วว่าจะไปที่ภูเขาหิมะ!"
        scene before_cat
        nrt "ท่านเดินทางฝ่าพายุหิมะและได้พบกับแมวตัวหนึ่ง\n{vspace=5}ระหว่างที่ท่านกำลังกำลังมองมันอยู่นั้นทันใดนั้นมันก็พูดขึ้นมา"
        jump ice

    label ice:
        scene cat_scene
        show cat_face at posface
        show cat_sleep at poscatsleep
        cat "\"สวัสดีเจ้ามนุษย์ มาหาข้ามีอะไรงั้นเรอะ\""
        hide cat_face
        menu:
            "ข้ามาขอให้ท่านช่วย":
                jump cattalk1
            "เจ้าคือแมววิเศษตัวที่ข้าได้ยินมารึเปล่า":
                jump cattalk1
            "แมวอะไรพูดได้ด้วย..?":
                jump cattalk1
        label cattalk1:
            hide cat_sleep
            show cat_idle1 at poscatidle1
            nrt "มันไม่ได้ฟังสิ่งที่ท่านพูดเลยแม้แต่นิดเดียว"
            show cat_face at posface
            cat "\"เจ้าสนใจน้ำนี่มั้ย\""
            hide cat_face
            nrt "แมวตัวนั้นชูขวดน้ำทรงประหลาดขึ้นมา"
            show cat_face at posface
            cat "\"นี้คือน้ำวิเศษ มะ-หัด-สะ-จัน อยากรู้ไอ้น้ำนี้ทำอะไรได้\""
            cat "\"มันสามารถเยียวยาร่างกายของเจ้าได้\n{vspace=5}แผลใหญ่แผลลึกแผลพุพองน้ำกัดเท้าฮ่องกงฟุตก็รักษาได้หมด!\""
            cat "\"อยากได้ใช้ป่าว งั้นเจ้าช่วยขัดให้ข้าหน่อยได้ปะ เท้าข้ามันเอื้อมไม่ถึง\n{vspace=5}ข้าต้องทนใช้ต้นไม้ขัดหลังมานานแล้ว เจ้าช่วยข้าหน่อยได้ไหม\""
            hide cat_face
            jump catdialog
        label catdialog:
            menu:
                "เจ้าคือใครกัน":
                    jump cattalk2
                "ขัดหลังให้มัน":
                    $ potion += 1
                    jump cattalk3
                "แทงมัน":
                    $ amulet += 1
                    jump cattalk3

        label cattalk2:
            nrt "................."
            jump catdialog
        label cattalk3:
            hide cat_idle1
            show cat_face at posface
            if potion == 1:
                show cat_idle2 at poscatidle2
                cat "\"อ่าห์ ข้าขอบใจเจ้ามากน้ำนี่เจ้าเอาไปเลย ถ้าไม่ได้เจ้าข้าคงทันหลังจนคายแน่ๆ\""
                cat "\"อ้อ ถ้าเจ้าเข้าป่าไป ที่นั่นอาจมีคนช่วยท่านได้น้อ โชคดี\""
                hide cat_face
                jump forest
            elif amulet == 1:
                hide cat_face
                nrt "{cps=15}{size=+10}........................"
                cat "{cps=50}\"ข้าแนะนำว่าเจ้าไม่ควรทำอย่างงั้นหรอกนะ\""
                hide cat_idle1
                nrt "ท่านไม่สนคำเตือนของเจ้าแมวปริศนาและได้ใช้ดาบแทงหลังของมัน\n{vspace=5}จากนั้นศพที่แน่นิ่งก็เริ่มเปล่งแสงและก็กลายร่างเป็นเครื่องลางประหลาด"
                nrt "ท่านมองหาน้ำนั่นแต่ก็พบว่ามันหายไปแล้ว\n{vspace=5}ท่านหยิบเครื่องลางแล้วก็เลือกเดินทางไปทางป่า"
                jump forest


    label forest:
        scene before_forest 
        nrt "ข้างหน้าท่านเห็นป่าใหญ่ที่ดูไม่น่าไว้วางใจ แต่ท่านนั้นก็เลือกที่จะเข้าไปอยู่ดี"
        scene forest1
        show human_inj at poshuman
        nrt "ท่านเดินทางเข้าไปในป่าและในระหว่างเราก็ได้พบกับชายคนหนึ่งกำลังนั่งบาดเจ็บอยู่"
        show human_face
        human "\"ท่านนักเดินทางคนนั้น พอจะมียารักษาหรืออะไรที่พอรักษาข้าหน่อยได้ไหม\""
        hide human_face
        if potion == 1:
            nrt "ท่านนั้นมีแต่นั้นมีแต่น้ำวิเศษที่เจ้าแมวปริศนาให้มา\n{vspace=5}ถ้าจะช่วยเค้าก็คงจะมีอยู่ทางเลือกเดียว..."
            menu:
                "ให้":
                    hide human_inj
                    show human_happy at poshuman
                    $ potion -= 1
                    $ compa += 1
                    nrt "พอชายหนุ่มได้ดื่มน้ำนั้นเข้าไปแล้ว\n{vspace=5}บาดแผลของเขาหายเป็นปลิดทิ้งและเขาก็ดูแข็งแรงขึ้นมาทันทีอย่างน่าอัศจรรย์"
                    nrt "นักเดินทางกล่าวขอบคุณท่านและ ขอเดินทางไปกับท่าน"
                    jump helpp
                "ไม่ให้":
                    nrt "ท่านไม่สนชายผมทองและออกเดินทางเข้าไปในป่าต่อไป"
                    jump donthelp
        else:
            nrt "ท่านนั้นไม่มีสิ่งที่พอจะช่วยเขาได้เลย\n{vspace=5}คุณจึงเลือกที่จะปล่อยให้ชายคนนั้นนอนบาดเจ็บต่อไป"
            jump donthelp
        label helpp:
            scene forest2
            show lion_sleep2 at poslion
            $ sword += 1
            nrt "ท่านเดินทางไปพร้อมกับชายหนุ่มคนนั้น เดินไปสักพักก็ได้เจอสิงโตตัวใหญ่มหึมา"
            nrt "สิงโตตัวนั่นมองมาที่ท่านทั้งสองพอมันได้เห็นชายหนุ่มผมทองมันก็ได้หมอบลง\n{vspace=5}ชายหนุ่มคนนั้นลูบหัวมันและสิงโตตัวนั้นก็กลายร่างเป็นดาบใหญ่เปล่งแสงสว่างไสว"
            jump desert
        label donthelp:
            scene forest2
            show lion_sleep2 at poslion
            nrt "ท่านเดินทางต่อไปในป่าแล้วได้เก็บเห็ดพิษขึ้นมากำหนึ่งและเถาวัลล์มาด้วย\n{vspace=5}ไม่นานท่านก็เจอสิงโตยักษ์ตัวหนึ่ง มันยังไม่สังเกตเห็นท่าน ท่านจะ..."
            if amulet == 1:
                menu:
                    "ใช้เห็ดพิษ":
                        jump killlion
                    "ย่องเอาเถาวัลล์ผูกคอสิงโต":
                        jump killbylion
                    "ใช้เครื่องราง":
                        jump killlionwithmagic
            else:
                menu:
                    "ใช้เห็ดพิษ":
                        jump killlion
                    "ย่องเอาเถาวัลล์ผูกคอสิงโต":
                        jump killbylion
    label lion:
        label killlion:
            hide lion_sleep2
            show lion_awake2 at poslionawake
            nrt "ท่านเดินไปหาสิงโต สิงโตตัวนั้นคำรามออกมาดังไปทั่วป่า"
            nrt "จังหวะที่สิงโตตัวนั้นคำราม ท่านโยนเห็ดพิษข้าไปในปากสิงโต\n{vspace=5}มันค่อยๆโซเซลงและล้มลงไป"
            nrt "ท่านใช้จังหวะนี้แทงเข้าไปที่คอสิงโต สิงโตร้องออกมาด้วยความเจ็บปวดและล้มลงไป\n{vspace=5}ท่านดึงฟันของมันออกมา\n{vspace=5}ฟันของมันค่อยๆกลายสภาพเป็นเศษเหล็กรูปทรงเขี้ยวสัตว์ขนาดพอดีมือ1ชิ้น"
            jump desert
        label killlionwithmagic:
            hide lion_sleep2
            show lion_awake2 at poslionawake
            nrt "ท่านเดินไปหาสิงโต สิงโตตัวนั้นคำรามออกมาดังไปทั่วป่า"
            nrt "จังหวะที่สิงโตตัวนั้นพุ่งมาหาคุณ เครื่องรางของท่านก็เปล่าแสงออกมา\n{vspace=5}ท่านหยิบมันออกมา เครื่องรางนั่นก็ปล่อยลำแสงพุ่งไปหาสิงโตอย่างจัง\n{vspace=5}สิงโตถูกลำแสงเต็มๆ ร่างกายถูกเผาไหม้ มันได้นอนล้มลงไป"
            nrt "ท่านใช้จังหวะนี้แทงเข้าไปที่คอสิงโต สิงโตร้องออกมาด้วยความเจ็บปวดและล้มลงไป\n{vspace=5}ท่านดึงฟันของมันออกมา\n{vspace=5}ฟันของมันค่อยๆกลายสภาพเป็นเศษเหล็กรูปทรงเขี้ยวสัตว์ขนาดพอดีมือ1ชิ้น"
            jump desert
        label killbylion:
            hide lion_sleep2
            show lion_awake2 at poslionawake
            nrt "ท่านค่อยๆย่องไปหาสิงโตแล้วหาจังหวะกระโดเข้าหาสิงโต\n{vspace=5}แล้วเอาเถาวัลย์มัดคอสิงโตจนแน่น เมื่อแน่นแล้วท่านก็มัดเงื่อนจนแน่น"
            nrt "สิงโตตัวนั้นดิ้นไปมา ก่อนที่จะใช้กรงเล็บของมันตัดเถาวัลย์จนขาด\n{vspace=5}ตอนนั้นท่านตระหนักได้ว่า เถาวัลย์นั่นแข็งแรงไม่พอ"
            py "ชี้หาย"
            nrt "สิงโตตัวนั้นไม่รอช้า วิ่งเข้ามาหาคุณและเขมือบคุณเข้าไปในคำเดียว"
            jump end1
        label end1:
            hide lion_sleep2
            nrt "ตอนจบที่ 1"
            nrt "ทำบุญทำทานให้อาหารสิงโต"
            return

    label desert:
        scene before_desert
        hide all
        nrt "ท่านได้ยินเสียงคำรามมาจากทะเลทราย"
        nrt "ท่านเดินทางไปยังทะเลทรายอันแห้งแล้ง ท่านเดินทางอยู่นานและได้พบกับสัตว์ประหลาดตัวหนึ่ง"
        scene desert
        show kimera_sleep at poskimera
        nrt ".........."
        hide kimera_sleep
        show kimera_normal at poskimera
        show kimeraface_normal at posface
        kimera "สวัสดีท่านนักเดินทาง ท่านมาหาข้าแล้วก็จำเป็นต้องตอบคำถามข้า"
        kimera "ถ้าตอบถูกหมดเจ้าจะได้โล่วิเศษที่ป้องกันเวทมนต์และพลังงานได้\n{vspace=5}แต่ถ้าตอบผิดแม้แต่ข้อเดียวเจ้าจะกลายเป็นปุ๋ย"
        jump question1
        label question1:
            kimera "1+1 เท่ากับเท่าไร"
            kimera "ยากมะยากมะ"
            hide kimeraface_normal
            menu:
                "ไม่ตอบ":
                    jump incorrect
                "2":
                    jump question2
                "11":
                    jump incorrect
                "\"11\"":
                    jump incorrect
        label question2:
            show kimeraface_normal at posface
            kimera "ตอบได้ดี คำถามต่อไป"
            kimera "ปณต อ่านว่าอะไร"
            hide kimeraface_normal
            menu:
                "ไม่ตอบ":
                    jump incorrect
                "ปะนะตะ":
                    jump veryincorrect
                "ปะนต":
                    jump correct
                "ปนตะ":
                    jump veryincorrect

            # if compa == 1:
            #     jump demoe
            # elif sword == 1 and amulet == 1:
            #     jump demoe
            # elif potion == 1:
            #     jump demoe
            
                
            label correct:
                show kimeraface_normal at posface
                kimera "เจ้าตอบคำถามข้าถูกทุกข้อ ข้าขอให้สิ่งนี้เป็นรางวัลให้ท่าน"
                hide kimeraface_normal
                nrt "หลังจากนั้นตัวมันก็เปล่งแสง กลายร่างเป็นโล่อันสวยงาม"
                nrt "หลังจากที่ท่านสวมโล่แล้ว ท่านก็ออกเดินทางไปที่สุดท้าย...หุบเขาเทพเจ้า"
                jump volcano
            label incorrect:
                show kimeraface_normal at posface
                kimera "เสียใจด้วย เจ้าตอบผิด และเจ้าไม่สามารถหลีกหนีชะตากรรมของเจ้าได้"
                hide kimeraface_normal
                nrt "ทรายบนพี้นของท่านนั้น อยู่ๆก็สูบท่านลงไปสู่ความมืดด้านล่าง และไม่ได้เห็นแสงตะวันอีกเลย"
                jump end2
            label veryincorrect:
                show kimeraface_normal at posface
                kimera "มันก็ถูกแหละนะแต่กูไม่อยากให้ตอบอันนั้นว่ะ by ปณต เดอะ เด็กเหี้ย"
                hide kimeraface_normal
                jump end2
            label end2:
                nrt "ตอนจบที่ 2"
                nrt "ประตูสู่ความมืดมิด"
                return
        
    label volcano:
        scene end0
        nrt "คุณเดินไปยังหุบเขาเทพเจ้าซึ่งตอนนี้ปกครุมไปด้วยพายุเพลิง\n{vspace=5}และเมฆเทาหลังจากที่ท่านเดินทางไปเรื่อยๆก็ได้เจอกับชายในชุดลัทธิ"
        nrt "เจ้าคิดจะมาปราบข้าอย่างงั้นรึ\n{vspace=5}คนธรรมดาอย่างเจ้าคิดจะกำราบข้าผู้สังหารเทพเจ้าอย่างงั้นรึ"
        if human == 1:
            jump fight01
        elif amulet == 1:
            jump fight02
    label fight01: #มีคน จะมีดาบ มีโล่
        boss "\"จ..เจ้า เป็นไปไม่ได้\""
        nrt "ลัทธินั้นมองมาที่ชามผมทองคนนั้นอย่างตกตะลึง"
        boss "\"ข้าสังหารเจ้าไปแล้ว! เจ้าฟิ้นกลับมาได้ยังไง\""
        human "\"ร่างกาย พลัง ปัญญา และ ความตาย\n{vspace=5}ทั้ง 4 สิ่งแห่งชีวิตของข้าแตกกระจายออกไปตามดินแดนต่างๆ\n{vspace=5}และพลังนั้นสามารถกลับมารวมกันได้โดยมีนักเดินทางผู้นี้เป็นคนช่วย\""
        boss "\"ข้าฆ่าเจ้าได้รอบนึง ทำไมข้าจะฆ่าเจ้าอีกรอบไม่ได้\""
        nrt "ว่าแล้วมันก็ทำท่าทางประหลาด ก่อนที่มันจะปล่อยลำแสงออกมา"
        menu:
            "พุ่งไปหาฝ่าลำแสงไป":
                jump beam01
            "หลบ":
                jump hides01
            "ใช้โล่":
                jump shield_G01
        label beam01:
            nrt "คุณทั้งสองไม่รอช้า วิ่งพุ่งเข้าไป ฝ่าลำแสงนั่นไปแต่ลำแสงนั้นฝ่าลำแสงนั่นไป\n{vspace=5}แต่ลำแสงนั้นก็แรงขึ้นแล้วก็เผาท่านทั้งสองทันที"
            jump demoe

        label hides01:
            nrt "ท่านได้หลบลำแสงนั้นอย่างฉิวเฉียด"
            jump arm01

        label shield_G01:
            nrt "ท่านใช้โล่กันไว้โล่นั้นแข็งแรงจนกันลำแสงได้อย่างดี"
            jump arm01

        label arm01:
            nrt "เจ้านั่นเสกแขนตัวเองเป็นกรงเล็บขนาดใหญ่ ทุ่มใส่พวกท่านอย่างสุดกำลัง"
            menu:
                "ใช้โล่":
                    jump shield_G02
                "พุ่งเข้าไปหามัน":
                    jump run
                "ปาดาบใส่มัน":
                    jump swords
                
        label shield_G02:
            nrt "ท่านใช้โล่กันไว้แต่โล่นั่นก็ต้านไว้ไม่อยู่ ท่านบี้แบนในทันที"
            jump demoe
        label run:
            nrt "ท่านวิ่งไปหามันและแทงเข้าไปกลางอกมัน เจ้านั่นร้องด้วยความเจ็บปวด\n{vspace=5}ก่อนที่มันจะงอกหางออกมาหวังปัดและทับคุณ"
            nrt "ทันใดนั้น ดาบที่คุณถือก็กลายเป็นสิงโตตัวใหญ่ มันพุ่งเข้าไปหาทางนั้นแล้วกัดหางจนเป็นแผลลึก"
            human "เลิกเล่นแล้วมาเอาจริงกันดีกว่าเจ้ามังกร เทพหัวทองคนนั้นกล่าวทันใดนั้นก็มีเปลวไฟพุ่งออกมา"
            menu:
                "กระโดดหลบ":
                    jump jumping_hides
                "ใช้โล่":
                    jump sheild02
                "ใช้ดาบกัน":
                    jump sword_sheild
            label jumping_hides:
                nrt "ท่านพยายามหลบแบบเมทริกซ์แต่ไฟนั้นแผ่ขยายใหญ่ จนไม่มีทีให้หลบ ท่านถูกไฟคลอกตาย"
            label sheild02:
                nrt "ท่านใช้โล่กันไว้เปล่วไฟนั้นถูกโล่กันได้หมด ไม่ได้รับบาดเจ็บใดๆ"
                $pain += 1
            label sword_sheild:
                nrt "ท่านได้ดาบกันไว้เปลวไฟยังเล็ดลอดทำให้พวกท่านบาดเจ็บ แต่ไม่ถึงกับตาย"
                jump stay
            label stay:
                god "ท่านพักเถอะ ต่อจากนี้ข้าจัดการเอง"
                nrt "จากนั้นท่านผมทองก็เปล่งแสงออกจากมาทั้งอาวุธและดาบของท่านและอะไรบางอย่างพุ่งเข้ามาหาชายคนนั้น เขาเปล่งแสงสว่างไสวออกมา"
                nrt "แล้วเทพเจ้าก็ได้ตื่นขึ้นมาอย่างแท้จริงแล้ว เทพเจ้ามองไปชายในชุดลัทธิคนนั้น ที่ตอนนี้มันเผยร่างจริงเป็นมังกรขนาดยักษ์"
                nrt "มังกรพุ่งมาอย่างรวดเร็ว"
                menu:
                    "แมว 9 ชีวิต":
                        jump cat
                    "ดาบ เสือ":
                        jump tigers
                    "โล่ นิรนาม":
                        jump sheild
                label cat:
                    nrt "เทพเจ้าเสกแมวออกมา แน่นอนว่ามันกันมังกรไม่ได้เลยมันพุ่งมาฟันท่านทั้ง2ในทันที"
                    jump demoe
                label tigers:
                    nrt "เทพเจ้าเสกเสือออกไป พวกมันช่วยกันกัดกระชากโจมตีอย่างเมามัน"
                    jump demoe
                label sheild:
                    nrt "เทพเจ้าเสกปีศาจนิรนามออกมาขนาดและกำลังของมันเพียงพอที่จะหยุดมังกรได้"
                    jump dragon
            label dragon:
                nrt "มังกรกอดรัดฟัดเหวี่ยงกับปีศาจนิรนาม"
                menu:
                    "ปล่อยลำแสง":
                        jump let_beem
                    "ดาบ เสือ":
                        jump tigerss
                    "ปล่อยแมว":
                        jump let_cat
                label let_beem:
                    nrt "เทพเจ้าหาจังหวะปล่อยลำแสงถูกเจ้ามังกรเต็มๆ มันบาดเจ็บสาหัส"
                    menu:
                        "ปล่อยแมว":
                            jump god_cat
                        "ปล่อยแมว(แต่เป็นอีกข้อ)":
                            jump god_cat
                label tigerss:
                    nrt "เทพเจ้าปล่อยเสือออกไป พวกมันช่วยกันกัดกระชากโจมตีอย่างเมามัน"
                    menu:
                        "ปล่อยลำแสง":
                            jump let_beem
                        "ปล่อยแมว":
                            jump let_cat
                label let_cat:
                    nrt "ทำไปเพื่อไรวะ"
                    jump demoe
            label god_cat:
                nrt "เทพเจ้าปิดท้ายด้วยแมวมันข่วนตามังกรทีนอนบาดเจ็บ"
                nrt "ข้าจะไม่แพ้เจ้า ข้าจะต้องแก้แค้นให้เหล่าพวกพ้องของข้าให้ได้"
                human "เผ่าพันธ์ุเจ้าสร้างปัญหาให้แผ่นดินนี้มามากพอแล้ว"
                if pain == 1:
                    jump gpain
                elif pain == 0:
                    jump goodend
                label gpain:
                    nrt "ท่านมีหลายเรื่องอยากจะถามแต่ด้วยพิษบาดแผลทำให้ท่านทำอะไรไม่ได้\n{vspace=5}เทพใช้พลังปล่อยลำแสงพิฆาตใส่มังกรสิ้นใจตายในทันที"
                    nrt "หลังจากนั้นเทพได้ไปดูท่าน แต่ด้วยพิษบาดแผลสาหัส ท่านได้สิ้นใจตายตามมังกรไป"
                    jump End_G01
                label goodend:
                    nrt "ท่านถามเทพเรื่องเหตุการณ์ว่ามันเกิดอะไรขึ้นกันแน่ เทพได้ อธิบายเหตุการณ์ไว้ดังนี้"
                    nrt "เมื่ออดีตกาลเคยมีเหล่าเทพปกครองโลกหลายตนจนครั้นมีมังกรมาออกล่าสัตว์\n{vspace=5}และเผาทำลายธรรมชาติ เหล่าเทพตัดสินใจออกล่ามังกร"
                    nrt "จนกลายเป็นการทำสงครามกับมังกร จนในที่สุดทั้งเทพและมังกรก็สิ้นชีพจนเกือบหมด\n{vspace=5}ท่านเทพบอกว่าเขาเป็นเพียงเทพกระจอกที่พลังไม่กล้าแกร่ง"
                    nrt "เมื่อสงครามสิ้นสุดจึงมาใช้ชีวิตเป็นผู้ดูแลดินแดนบริเวณแถวหมู่บ้านของเรา\n{vspace=5}จนมีมังกรตัวนี้มาสังหารเทพนี้แหละ"
                    dragon "พวกข้าแค่ออกล่าสัตว์ประทังชีวิตแค่เผาป่าเพียงส่วนนึงเพื่อทำรังเท่านั้น\n{vspace=5}อยู่ๆพวกแกก็มาล่าล้างบางพวกข้าจนเหลือแค่ข้าตัวเดียว"
                    dragon "พวกแกมันก็คือปีศาจดีๆนี้หละ"
                    menu:
                        "ฆ่ามัน":
                            jump god_beem
                        "อย่าพึ่งฆ่ามัน":
                            jump god_why
                    label god_beem:
                        nrt "ท่านตัดสินใจแล้ว ให้เทพใช้พลังสังหารมังกรจนสิ้นใจ"
                        jump End_G02
                    label god_why:
                        human "ทำไมหละ? ทำไมถึงเจ้าถึงบอกว่าอย่าพึ่งสังหารมันหละ?"
                        menu:
                            "ฆ่าๆมันไปเถอะ":
                                jump god_beem
                            "ทั้งหมดเป็นแค่เรื่องเข้าใจผิด":
                                jump tell_god
                            "สงครามมันจบไปนานแล้วไม่จำเป็นต้องสร้างสงครามอีก":
                                jump tell_god
                    label tellgod:
                        nrt "ท่านบอกเทพไปอย่างนั้นหลังจากนั้นเทพก็เสกดาบขึั้นมาแล้วยกดาบขึ้นมา"
                        nrt "เทพได้โยนดาลนั่นทิ้งไปแล้วพูดกับมังกร ข้าจะไม่ขอก่อสงคราม\n{vspace=5}นี้ซ้ำอีกเจ้าจะไปไกลก็ไป แค่อย่าสร้างความเดือดร้อนก็พอ"
                        nrt "มังกรมองเทพแบบสายตาไม่กระพิบก่อนที่จะเป็นออกไปจากหุบเขา\n{vspace=5}ไม่มีใครได้เห็นมันอีกเลยหลังจากนั้น"
                        jump End_G03
        label swords:
            nrt "ท่านปาดาบใส่มันแต่มันอยู่ใกล้เกินไปและดาบก็หนักเกิน จะพุ่งไปถึงกรงเล็บนั่นทับคุณในทันที"
            jump demoe
            
        label fight02:
            boss "เจ้าจะบังอาจเกินไปแล้วที่คิดจะต่อกรกับข้า"
            nrt "ว่าแล้วมันก็ปล่อยลำแสงใส่ท่านในทันใด"
            menu:
                "พุ่งฝาลำแสง":
                    jump Goodside
                "หลบ":
                    jump Goodside
                "ใช้โล่":
                    jump Goodside
            label Goodside:
                nrt "เจ้านั่นเสกแขนตัวเองเป็นกรงเล็บขนาดใหญ่ ทุ่มใส่พวกท่านอย่างสุดกำลัง"
                menu:
                    "ใช้โล่":
                        jump Goodside
                    "ใช้เครื่องลาง":
                        jump use_beam
                    "ปาดาบไล่":
                        jump Goodside
            label use_beam:
                nrt "ท่านใช้เครื่องลางปล่อยลำแสงออกไปโดนมันอย่างจังๆ มันร้องอย่างเจ็บปวด\n{vspace=5}ก่อนที่จะงอกหางออกมาหวังจะทับคุณด้วยหางขนาดยักษ์"
                menu:
                    "ใช้ดาบฟัน":
                        jump sword_tail
                    "ยิงลำแสง":
                        jump beam_it
                    "ยิงลำแสงใส่เพดาน":
                        jump beam_wall
            label sword_tall:
                nrt "ท่านใช้ดาบฟันหางนั้น แต่ดาบนั้นยังคมไม่พอจะฟันหางให้ขาดหลังจากนั้นท่านก็ถูกมัน\n{vspace=5}ทับแบนแต็ดแต๋"
                jump demoe
            label beam_it:
                nrt "ท่านใช้เครื่องรางยิงลำแสงใส่มันอีกรอบ ลำแสงนั้นโดนหางมันอย่างจัง\n{vspace=5}แต่หางนั้นก็ยังหวดมาโดนคุณอย่างจัง"
                jump demoe
            label beam_wall:
                nrt "ท่านใช้เครื่องรางยิงใส่เพดานถ้ำ ทำให้หินหลายก้อนหลายขนาดทับเจ้านั่นอย่างจัง"
                nrt "ในขณะที่ท่านมองดูก้อนหินเหล่านั้น อยู่ๆกองหินก็ระเบิดออกเผยให้เห็นมังกรขนาด\n{vspace=5}มหึมาใต้กองหินนั่น"
                nrt "มังกรได้พูดกับท่าน"
                dragon "เจ้านี่แข็งแกร่งมาก สนใจมาเป็นพวกข้ามั้ยละ"
                menu:
                    "สน":
                        jump End_B01
                    "ไม่สน":
                        jump dragon_choose
                label dragon_choose:
                    dragon "เจ้าเสือกเองนะแล้วมันก็พ่นไฟออกมา"
                    menu:
                        "กระโดดหลบ":
                            jump Goodside
                        "ใช้โล่":
                            jump shilded03
                        "ใช้เครื่องลาง":
                            jump use_amulet
                    label use_amulet:
                        nrt "ท่านใช้เครื่องลางต้านพลังไฟ แต่ลำแสงดันพุ่งฝ่าไฟเข้าปากมังกร\n{vspace=5}ทันที ส่วนท่านที่ถูกไฟคลอกตายตามมังกรไป"
                        nrt "ขี้เกียจแยกตอนจบงั้นให้ตายและกัน"
                            jump demoe
                    label shilded03
                        nrt "ท่านใช้โล่กันไว้เปล่วไฟนั้นถูกโล่กันได้หมด ไม่ได้รับบาดเจ็บใดๆ"
                            jump dragonpung
                    label dragonpung:
                        nrt "มังกรพุ่งมาหาคุณอย่างรวดเร็ว"
                        menu:
                            "ก็เผ่นสิคร้าบ":
                                jump you_run
                            "ใช้ดาบพุ่งไปหามัน":
                                jump sword_it
                            "ใช้เครื่องลาง":
                                jump amulet_use
                    label you_rum:
                        nrt "คุณวิ่งหนีมันเร็วเกินไปมันโฉบท่านไปกินโดยทันที"
                        jump demoe
                    label sword_it:
                        nrt "คุณใช้ดาบนั้นเสียบตามันร้องด้วยความเจ็บปวดมันหยุดพุ่งแล้วดิ้นไปมา"
                        nrt "คุณใช้เครื่องรางปล่อยพลังใส่มันจนมันตายคาที่ในทันที"
                    label amulet_use:
                        nrt "ท่านใช้เครื่องลางจะยังสวนไปแต่เหมือนว่าจะปล่อยพลังไม่ทันมันเร็ว\n{vspace=5}กว่ามันโฉบคุณไปกินในทันที"
    label End_G01:
        nrt "หลังจากเหตุการณ์ทั้งหมดจบลงไป ภัยธรรมชาติทุกอย่างได้กลับคืนสู่ความปกติ\n{vspace=5}เทพกลับมาดูแลธรรมชาติเหมือนเดิม ปีศาจมังกรสิ้นใจไป"
        nrt "ท่านได้กลายเป็นตำนานผู้เสียสละชีพเพื่อปกป้องหมู่บ้านและผู้ฟื้นคืนเทพไปชั่วกาล"
    label End_G02:
        nrt "Good ท่านได้เป็นตำนานผู้พิชิตมังกร ผู้ปกป้องหมู่บ้านและผู้ฟื้นคืนเทพเจ้าหลังจากนั้นท่านก็"
        nrt "ใช้ชีวิตในหมู่บ้านนั้นอย่างมีความสุข"
    label End_G03:
        nrt "หลังจากเหตุการณ์ทั้งหมดจบลง กับธรรมชาติทุกอย่างก็หายไป เทพกลับมาดูแลธรรมชาติเหมือนเดิมมังกรไม่ได้ฆ่ารุกรานอีกเลย ท่านได้กลายเป็นตำนานผู้ปกป้องหมู่บ้านและผู้ฟื้นคืนเทพเจ้าและใข้ขีวิตอย่างมีความสุขตลอดมา"
    label End_B01:
        nrt "หลังจากเหตุการ์ณทั้งหมดมังกรก็ได้เป็นผู้ครางดินแดนและท่านก็ได้เป็นผู้รับใช้มังกรไปชั่วกาล"
    label demoe:
        scene black
        nrt "ขอขอบคุณที่เล่นตัวทดลองของเรา เนื้อเรื่องต่อไปยังคงอยู่ในระหว่างการพัฒนา"
        nrt "คุณสามารถดูตัวอย่างเกมได้ที่\n{vspace=5}https://www.youtube.com/watch?v=BjDebmqFRuc"
    return
     


