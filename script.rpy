# The script of the game goes in this file.

# name of the character.

define py = Character("[name]", what_prefix = '{cps=75}')
define nrt = Character("", what_prefix = '{cps=75}')
define cat = Character("แมวปริศนา", what_prefix = '{cps=75}')
define human = Character("ชายผมทอง", what_prefix = '{cps=75}')
define kimera = Character("ปีศาจแห่งปัญญา", what_prefix = '{cps=75}')
define boss = Character("ชายในชุดคลุมสีดำ", what_prefix = '{cps=75}')
define dragon = Character("มังกรดำ", what_prefix = '{cps=75}')
define future = Character("ผู้มาจากอนาคต", what_prefix = '{cps=75}')
define fakegod = Character("ผู้งมงาย", what_prefix = '{cps=75}')
define seer = Character("หมอดู", what_prefix = '{cps=75}')
define kid = Character("เด็กขายแผนที่", what_prefix = '{cps=75}')


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

########## face position
transform posface:
    pos((25, 260))

########## cat position
transform poscatsleep:
    pos((500, 300))

transform poscatidle1:
    pos((500, 250))

transform poscatidle2:
    pos((520, 220))

######### human position
transform poshuman:
    pos((420, 135))

######### lion position
transform poslion:
    pos((250,200))

transform poslionawake:
    pos((250,50))

######### kimera position
transform poskimera:
    pos((350,100))

######### dragon position
transform posdragon_human:
    pos((300,150))

transform posdragon:
    pos((200,30))
    
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
    $beam = 0
    
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
        jump end0
    label iwant:
        play music "normalsong.mp3"
        scene first_scene
        nrt "ท่านตัดสินใจแล้วว่าจะออกเดินทาง แต่ว่า... ท่านยังไม่รู้ว่าจะเริ่มต้นยังไงดี\n{vspace=5}ท่านคิดว่าท่านจะถามคนในหมู่บ้าน ว่าแต่คุณจะถามใครดีล่ะ"
    label iwant1:
        menu:
            "ผู้มาจากอนาคต":
                jump future
            "ผู้งมงาย":
                jump fakegod
            "หมอดู":
                jump seer
            "เด็กขายแผนที่":
                jump kid
    label future:
        py "ข้าขอถาม-"
        future "เนื่องจาก String นั้นเกิดจากตัวอักษรหลายๆ ตัวต่อกันจนเกิดเป็น String"
        future "หรือกล่าวอีกนัยหนึ่งก็คือ"
        future "String คืออาเรย์ของตัวอักษรดังนั้นเราจึงสามารถเข้าถึงตัวอักษรตำแหน่งต่างๆ\n{vspace=5}ของ String ได้ผ่านทาง Index ของมัน เช่นเดียวกับการเข้าถึงข้อมูลใน List"
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
        seer "ท่านผู้กล้า ข้ารู้ว่าท่านต้องการจะออกไปช่วยหมู่บ้านและสืบหาความจริง\n{vspace=5}ของเทพที่หายไปข้าจะขอดูอนาคตของท่านซักหน่อย"
        seer "ข้าเห็นแล้ว ท่านควรจะไปที่หุบเขาหิมะ ที่แห่งนั้นมีแมววิเศษที่จะมีประโยชน์ต่อท่าน\n{vspace=5}เลือกให้ดีว่าจะใช้จิตใจหรือกิเลสในการแก้ปัญหา ทางที่ท่านเลือกจะส่งผลต่อการ\n{vspace=5}เดินทางทางต่อไปของท่าน"
        seer "ทุกสิ่งที่ท่านพบเจอที่ท่านคุยย่อมมีความหมาย ขอให้โชคดีกับการเดินทาง!"
        menu:
            nrt "ท่านนั้นได้คำตอบที่ต้องการแล้วต้องการท่านจะ..."
            "ไปตามทางหมอดูบอก":
                jump beforecat
            "กลับไปหาข้อมูลเพิ่มเติม":
                jump iwant1
    label kid:
        kid "ท่านมาหาข้าจะมาขอเส้นทางงั้นรึ แต่ท่านช่วยตอบคำถามข้าก่อนได้มะ"
        py "ได้สิ"
        kid "เพื่อนข้ามาจากแดนไกล ข้าจะส่งจดหมายไปหาเขา\n{vspace=5}แต่ข้าอ่านชื่อเพื่อนข้าไม่ออก มันอ่านว่าอะไร"
        nrt "เขายื่นจดหมายออกมา ท่านเห็นตรงชื่อมันเขียนไว้ว่า...."
        nrt "ปณต"
        kid "มันอ่านว่าปะนต หรือ ปะนะตะ หรือ ปนตะ ข้างงจะตายอยู่แล้ว"
        py "อ่าาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาา..........."
        nrt "ท่านเดินออกจากร้านด้วยความงงสุดขีด"
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
        cat "สวัสดีเจ้ามนุษย์ มาหาข้ามีอะไรงั้นเรอะ"
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
            cat "เจ้าสนใจน้ำนี่มั้ย"
            hide cat_face
            nrt "แมวตัวนั้นชูขวดน้ำทรงประหลาดขึ้นมา"
            show cat_face at posface
            cat "นี้คือน้ำวิเศษ มะ-หัด-สะ-จัน อยากรู้ไอ้น้ำนี้ทำอะไรได้"
            cat "มันสามารถเยียวยาร่างกายของเจ้าได้ แผลใหญ่แผลลึกแผลพุพอง\n{vspace=5}น้ำกัดเท้าฮ่องกงฟุตก็รักษาได้หมด!"
            cat "อยากได้ใช้ป่าว งั้นเจ้าช่วยขัดให้ข้าหน่อยได้ปะ เท้าข้ามันเอื้อมไม่ถึง\n{vspace=5}ข้าต้องทนใช้ต้นไม้ขัดหลังมานานแล้ว เจ้าช่วยข้าหน่อยได้ไหม"
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
            nrt "เจ้าแมวยังคงเลียเท้าของมันต่อไปไม่สนใจสิ่งที่ท่านพูด"
            jump catdialog
        label cattalk3:
            hide cat_idle1
            show cat_face at posface
            show cat_idle2 at poscatidle2
            if potion == 1:
                cat "\"อ่าห์ ข้าขอบใจเจ้ามากน้ำนี่เจ้าเอาไปเลย ถ้าไม่ได้เจ้าข้าคงคันหลังจนตายแน่ๆ\""
                cat "\"อ้อ ถ้าเจ้าเข้าป่าไป ที่นั่นอาจมีคนช่วยท่านได้น้อ โชคดี\""
                hide cat_face
                jump forest
            elif amulet == 1:
                cat "เจ้านี่เกาได้ดีเลยนะเนี่ย อู้ววว~ ดีจนเหมือนจะได้ขึ้นสวรรค์เลย"
                cat "เดี๋ยวๆ!! นั่นเจ้าจะทำอะไรน่ะ"
                hide cat_idle2
                hide cat_face
                nrt "จากนั้นท่านก็ได้ใช้ดาบแทงหลังของมัน\n{vspace=5}ศพที่แน่นิ่งก็เริ่มเปล่งแสงและก็กลายร่างเป็นเครื่องลางประหลาด"
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
                    nrt "พอชายหนุ่มได้ดื่มน้ำนั้นเข้าไปแล้ว บาดแผลของเขาหายเป็นปลิดทิ้งและ\n{vspace=5}เขาก็ดูแข็งแรงขึ้นมาทันทีอย่างน่าอัศจรรย์"
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
            nrt "ท่านเดินทางไปพร้อมกับชายหนุ่มคนนั้น เดินไปสักพักก็ได้เจอ\n{vspace=5}สิงโตมหึมาที่มีหัวสองหัว หัวข้างนึงเป็นแพะ ข้างนึงเป็นสิงโต และมีหางเป็นงู"
            nrt "สิงโตตัวนั่นมองมาที่ท่านทั้งสองพอมันได้เห็นชายหนุ่มผมทองมันก็ได้หมอบลง\n{vspace=5}ชายหนุ่มคนนั้นลูบหัวมันและสิงโตตัวนั้นก็กลายร่างเป็นดาบใหญ่เปล่งแสงสว่างไสว"
            jump desert
        label donthelp:
            scene forest2
            nrt "ท่านเดินทางต่อไปในป่าแล้วได้เก็บเห็ดพิษขึ้นมากำหนึ่งและเถาวัลล์มาด้วย"
            show lion_sleep2 at poslion
            nrt "ไม่นานท่านก็เจอสิงโตมหึมาที่มีหัวสองหัว\n{vspace=5}หัวข้างนึงเป็นแพะ ข้างนึงเป็นสิงโต และมีหางเป็นงู"
            if amulet == 1:
                menu:
                    nrt "มันยังไม่สังเกตเห็นท่าน ท่านจะ..."
                    "ใช้เห็ดพิษ":
                        jump killlion
                    "ย่องเอาเถาวัลล์ผูกคอสิงโต":
                        jump killbylion
                    "ใช้เครื่องราง":
                        jump killlionwithmagic
            else:
                menu:
                    nrt "มันยังไม่สังเกตเห็นท่าน ท่านจะ..."
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
            nrt "ท่านใช้จังหวะนี้แทงเข้าไปที่คอสิงโต สิงโตร้องออกมาด้วยความเจ็บปวดและล้มลงไป\n{vspace=5}ท่านดึงฟันของมันออกมาฟันของมันค่อยๆกลายสภาพเป็นเศษเหล็ก\n{vspace=5}รูปทรงเขี้ยวสัตว์ขนาดพอดีมือ 1 ชิ้น"
            jump desert
        label killlionwithmagic:
            hide lion_sleep2
            show lion_awake2 at poslionawake
            nrt "ท่านเดินไปหาสิงโต สิงโตตัวนั้นคำรามออกมาดังไปทั่วป่า"
            nrt "จังหวะที่สิงโตตัวนั้นพุ่งมาหาคุณ เครื่องรางของท่านก็เปล่าแสงออกมา\n{vspace=5}ท่านหยิบมันออกมา เครื่องรางนั่นก็ปล่อยลำแสงพุ่งไปหาสิงโตอย่างจัง\n{vspace=5}สิงโตถูกลำแสงเต็มๆ ร่างกายถูกเผาไหม้ มันได้นอนล้มลงไป"
            nrt "ท่านใช้จังหวะนี้แทงเข้าไปที่คอสิงโต สิงโตร้องออกมาด้วยความเจ็บปวดและล้มลงไป\n{vspace=5}ท่านดึงฟันของมันออกมาฟันของมันค่อยๆกลายสภาพเป็นเศษเหล็ก\n{vspace=5}รูปทรงเขี้ยวสัตว์ขนาดพอดีมือ 1 ชิ้น"
            jump desert
        label killbylion:
            hide lion_sleep2
            show lion_awake2 at poslionawake
            nrt "ท่านค่อยๆย่องไปหาสิงโตแล้วหาจังหวะกระโดดเข้าหาสิงโต แล้วเอาเถาวัลย์\n{vspace=5}มัดคอสิงโตจนแน่น จากนั้นท่านก็ทำการมัดเงื่อนเพื่อไม่ให้เจ้าสิงโตหลุดไปได้"
            nrt "ท่านกระโดดออกมาจากตัวสิงโต และได้เห็นว่าท่านดันไปผูกคอด้านที่เป็นแพะ\n{vspace=5}หัวที่เป็นสิงโตมองมาที่คุณแบบตาไม่กระพริบ"
            py "ชี้หาย"
            nrt "สิงโตตัวนั้นไม่รอช้า วิ่งเข้ามาหาคุณและเขมือบคุณเข้าไปในคำเดียว"
            jump end1

    label desert:
        scene before_desert
        stop music
        play music "pyramid_sands.mp3"
        nrt "ท่านได้ยินเสียงคำรามมาจากทะเลทราย"
        nrt "ท่านเดินทางไปยังทะเลทรายอันแห้งแล้ง\n{vspace=5}ท่านเดินทางอยู่นานและได้พบกับสัตว์ประหลาดตัวหนึ่ง"
        scene desert
        show kimera_sleep at poskimera
        nrt "{cps=50}{size=+10}............"
        hide kimera_sleep
        show kimera_normal at poskimera
        show kimeraface_normal at posface
        kimera "สวัสดีท่านนักเดินทาง ท่านมาหาข้าแล้วก็จำเป็นต้องตอบคำถามข้า"
        kimera "ถ้าตอบถูกหมดเจ้าจะได้โล่วิเศษที่ป้องกันเวทมนต์และพลังงานได้\n{vspace=5}แต่ถ้าตอบผิดแม้แต่ข้อเดียวเจ้าจะกลายเป็นปุ๋ย"
        jump question1
        label question1:
            kimera "คำถามแรก"
            kimera "1+1 เท่ากับเท่าไร"
            hide kimera_normal
            show kimera_happy at poskimera
            kimera "ยากมะยากมะ"
            hide kimera_happy
            show kimera_normal at poskimera
            hide kimeraface_normal
            menu:
                nrt "1+1 เท่ากับเท่าไร"
                "10":
                    jump incorrect
                "11":
                    jump incorrect
                "\"11\"":
                    jump incorrect
                "2":
                    jump question2

        label question2:
            show kimeraface_normal at posface
            hide kimera_normal
            show kimera_happy at poskimera
            kimera "ตอบได้ดี คำถามต่อไป"
            hide kimera_happy
            show kimera_normal at poskimera
            kimera "อะไรเอ่ยสี่ตีนเชื่อง ๆ ไม่มุงกระเบื้องแต่มุงเข็ม"
            hide kimeraface_normal
            menu:
                nrt "อะไรเอ่ยสี่ตีนเชื่อง ๆ ไม่มุงกระเบื้องแต่มุงเข็ม"
                "เต่า":
                    jump incorrect
                "เข็มกับด้าย":
                    jump incorrect
                "เม่น":
                    jump question3
                "อะไรวะเนี่ย":
                    jump incorrect
        label question3:
            kimera "ตอบได้ดี คำถามต่อไป"
            kimera "เกิดจากไฟ จากไปพร้อมลม สิ่งนี้คืออะไร"
            menu:
                nrt "เกิดจากไฟ จากไปพร้อมลม สิ่งนี้คืออะไร"
                "ควันไฟ":
                    jump correct
                "นกฟินิกซ์":
                    jump incorrect
                "ลาวา":
                    jump incorrect
                "ไม่รู้ ยอม":
                    jump incorrect
        label correct:
            show kimeraface_normal at posface
            kimera "เจ้าตอบคำถามข้าถูกทุกข้อ ข้าขอให้สิ่งนี้เป็นรางวัลให้ท่าน"
            hide kimeraface_normal
            nrt "หลังจากนั้นตัวมันก็เปล่งแสง กลายร่างเป็นโล่อันสวยงาม"
            scene godhill
            nrt "หลังจากที่ท่านสวมโล่แล้ว ท่านก็ออกเดินทางไปที่สุดท้าย...หุบเขาเทพเจ้า"
            jump volcano
        label incorrect:
            show kimeraface_normal at posface
            hide kimera_normal
            show kimera_sadistic at poskimera
            kimera "เสียใจด้วย เจ้าตอบผิด และเจ้าไม่สามารถหลีกหนีชะตากรรมของเจ้าได้"
            hide kimeraface_normal
            nrt "ทรายบนพี้นของท่านนั้นอยู่ๆก็สูบท่านลงไปสู่ความมืดด้านล่าง\n{vspace=5}และไม่ได้เห็นแสงตะวันอีกเลย"
            jump end2
        
    label volcano:
        stop music
        play music "dragon_fight.mp3"
        nrt "คุณเดินไปยังหุบเขาเทพเจ้าซึ่งตอนนี้ปกครุมไปด้วยพายุเพลิง\n{vspace=5}และเมฆเทาหลังจากที่ท่านเดินทางไปเรื่อยๆก็ได้เจอกับชายในชุดลัทธิ"
        scene dragon_lair
        show dragon_human at posdragon_human
        show dragon_humanface
        boss "เจ้าคิดจะมาปราบข้าอย่างงั้นรึ\n{vspace=5}คนธรรมดาอย่างเจ้าคิดจะกำราบข้าผู้สังหารเทพเจ้าอย่างงั้นรึ"
        hide dragon_humanface
        if human == 1:
            jump fight01
        elif amulet == 1:
            jump fight02
        elif potion == 1:
            jump fight03
    #label Fight01
    label fight01: #มีคน จะมีดาบ มีโล่
        show dragon_human at posdragon_human
        show dragon_humanface
        boss "จ..เจ้า เป็นไปไม่ได้"
        hide dragon_humanface
        nrt "ลัทธินั้นมองมาที่ชามผมทองคนนั้นอย่างตกตะลึง"
        show dragon_humanface
        boss "ข้าสังหารเจ้าไปแล้ว! เจ้าฟิ้นกลับมาได้ยังไง"
        hide dragon_humanface
        show human_face
        human "ร่างกาย พลัง ปัญญา และ ความตาย\n{vspace=5}ทั้ง 4 สิ่งแห่งชีวิตของข้าแตกกระจายออกไปตามดินแดนต่างๆ\n{vspace=5}และพลังนั้นสามารถกลับมารวมกันได้โดยมีนักเดินทางผู้นี้เป็นคนช่วย"
        hide human_face
        show dragon_humanface
        boss "ข้าฆ่าเจ้าได้รอบนึง ทำไมข้าจะฆ่าเจ้าอีกรอบไม่ได้"
        hide dragon_humanface
        nrt "ว่าแล้วมันก็ทำท่าทางประหลาด ก่อนที่มันจะปล่อยลำแสงออกมา"
        menu:
            "พุ่งไปหาฝ่าลำแสงไป":
                jump beam01
            "หลบ":
                jump hides01
            "ใช้โล่":
                jump shield_G01
        label beam01:
            nrt "คุณไม่รอช้า วิ่งพุ่งเข้าไป ฝ่าลำแสงนั่นไปแต่ลำแสงนั้นฝ่าลำแสงนั่นไป\n{vspace=5}แต่ลำแสงนั้นก็แรงขึ้นแล้วก็เผาท่านไหม้เกรียมในทันที"
            jump dead

        label hides01:
            nrt "ท่านได้หลบลำแสงนั้นอย่างฉิวเฉียด"
            jump arm01

        label shield_G01:
            nrt "ท่านใช้โล่กันไว้โล่นั้นแข็งแรงจนกันลำแสงได้อย่างดี"
            if human == 1:
                jump arm01
            elif amulet == 1:
                jump goodside
        label arm01:
            nrt "เจ้านั่นเสกแขนตัวเองเป็นกรงเล็บขนาดใหญ่ ทุ่มใส่พวกท่านอย่างสุดกำลัง"
            menu:
                "ใช้โล่":
                    jump shield_G02
                "ถือดาบพุ่งเข้าไปหามัน":
                    jump run2
                "ปาดาบใส่มัน":
                    jump swords
        label shield_G02:
            nrt "ท่านใช้โล่กันไว้แต่โล่นั่นก็ต้านไว้ไม่อยู่ ท่านบี้แบนในทันที"
            jump dead
        label run2:
            nrt "ท่านวิ่งไปหามันและแทงเข้าไปกลางอกมัน เจ้านั่นร้องด้วยความเจ็บปวด\n{vspace=5}ก่อนที่มันจะงอกหางออกมาหวังปัดและทับคุณ"
            nrt "ทันใดนั้น ดาบที่คุณถือก็กลายเป็นสิงโตตัวใหญ่\n{vspace=5}มันพุ่งเข้าไปหาทางนั้นแล้วกัดหางจนเป็นแผลลึก"
            show human_face
            human "เลิกเล่นแล้วมาเอาจริงกันดีกว่าเจ้ามังกร\n{vspace=5}เทพหัวทองคนนั้นกล่าวทันใดนั้นก็มีเปลวไฟพุ่งออกมา"
            hide human_face
            menu:
                "กระโดดหลบ":
                    jump jumping_hides
                "ใช้โล่":
                    jump sheild02
                "ใช้ดาบกัน":
                    jump sword_sheild
            label jumping_hides:
                nrt "ท่านพยายามหลบแบบเมทริกซ์แต่ไฟนั้นแผ่ขยายใหญ่\n{vspace=5}จนไม่มีทีให้หลบ ท่านถูกไฟคลอกตาย"
                jump dead
            label sheild02:
                nrt "ท่านใช้โล่กันไว้เปล่วไฟนั้นถูกโล่กันได้หมด ไม่ได้รับบาดเจ็บใดๆ"
                $pain += 0
                jump stay
            label sword_sheild:
                nrt "ท่านไช้ดาบกันไว้เปลวไฟยังเล็ดลอดทำให้พวกท่านบาดเจ็บ แต่ไม่ถึงกับตาย"
                $pain += 1
                jump stay
            label stay:
                show human_face
                human "ท่านพักเถอะ ต่อจากนี้ข้าจัดการเอง"
                hide human_face
                nrt "จากนั้นท่านผมทองก็เปล่งแสงออกจากมาทั้งอาวุธและดาบของท่าน\n{vspace=5}และอะไรบางอย่างพุ่งเข้ามาหาชายคนนั้น เขาเปล่งแสงสว่างไสวออกมา"
                hide dragon_human
                show dragon_normal at posdragon
                nrt "แล้วเทพเจ้าก็ได้ตื่นขึ้นมาอย่างแท้จริงแล้ว\n{vspace=5}เทพเจ้ามองไปชายในชุดลัทธิคนนั้น ที่ตอนนี้มันเผยร่างจริงเป็นมังกรขนาดยักษ์"
                nrt "มังกรพุ่งมาอย่างรวดเร็ว"
                menu:
                    "แมว 9 ชีวิต":
                        jump cat
                    "ดาบ ศักดิ์สิทธิ์":
                        jump tigers
                    "โล่ แห่งปัญญา":
                        jump sheild
                label staymenu:
                    menu:
                        "แมว 9 ชีวิต":
                            jump cat
                        "โล่ แห่งปัญญา":
                            jump sheild
                label cat:
                    nrt "เทพเจ้าเสกแมวออกมา แน่นอนว่ามันกันมังกรไม่ได้เลยมันพุ่งมาฟันท่านทั้ง2ในทันที"
                    jump dead
                label tigers:
                    nrt "เทพเจ้าเสกสิงโตออกไป ถึงมันจะตัวใหญ่แต่ก็สู้แรงมังกรไม่ไหว"
                    jump staymenu
                label sheild:
                    nrt "เทพเจ้าเสกปีศาจแห่งปัญญาออกมาขนาดและกำลังของมันเพียงพอที่จะหยุดมังกรได้"
                    jump dragon
            label dragon:
                nrt "มังกรกอดรัดฟัดเหวี่ยงกับปีศาจแห่งปัญญา"
                menu:
                    "ปล่อยลำแสง":
                        jump beemm
                    "ดาบ ศักดิ์สิทธิ์":
                        jump tigerss
                    "ปล่อยแมว":
                        jump let_cat
                label tigerss:
                    nrt "เทพเจ้าปล่อยสิงโตออกไป พวกมันช่วยกันกัดกระชากโจมตีอย่างเมามัน"
                    menu:
                        "ปล่อยลำแสง":
                            $beam += 1
                            jump windragon
                        "ปล่อยแมว":
                            jump let_cat
                label beemm:
                    nrt "เทพเจ้าหาจังหวะปล่อยลำแสงถูกเจ้ามังกรเต็มๆ มันบาดเจ็บสาหัส"
                    menu:
                        "ดาบ ศักดิ์สิทธิ์":
                            jump windragon
                        "ปล่อยแมว":
                            jump let_cat
                label let_cat:
                    nrt "เทพปล่อยแมวออกไป มันทำอะไรไม่ได้เลย"
                    jump dead
                label windragon:
                    if beam == 0:
                        nrt "เทพเจ้าปล่อยสิงโตออกไป พวกมันช่วยกันกัดกระชากโจมตีอย่างเมามัน"
                    elif beam == 1:
                        nrt "เทพเจ้าหาจังหวะปล่อยลำแสงถูกเจ้ามังกรเต็มๆ มันบาดเจ็บสาหัส"
                    menu:
                        "ปล่อยแมว":
                            jump god_cat
                        "ปล่อยแมว(แต่เป็นอีกข้อ)":
                            jump god_cat
            label god_cat:
                nrt "เทพเจ้าปิดท้ายด้วยแมวมันข่วนตามังกรทีนอนบาดเจ็บ"
                show dragon_face at posface
                dragon "ข้าจะไม่แพ้เจ้า ข้าจะต้องแก้แค้นให้เหล่าพวกพ้องของข้าให้ได้"
                hide dragon_face
                show human_face
                human "เผ่าพันธ์ุเจ้าสร้างปัญหาให้แผ่นดินนี้มามากพอแล้ว"
                hide human_face
                if pain == 1:
                    jump gpain
                elif pain == 0:
                    jump goodend
                label gpain:
                    nrt "ท่านมีหลายเรื่องอยากจะถามแต่ด้วยพิษบาดแผลทำให้ท่านทำอะไรไม่ได้\n{vspace=5}เทพใช้พลังปล่อยลำแสงพิฆาตใส่มังกรสิ้นใจตายในทันที"
                    nrt "หลังจากนั้นท่านเทพได้ไปดูท่าน แต่ด้วยพิษบาดแผลสาหัสท่านได้สิ้นใจตายตามมังกรไป"
                    jump Good_End01
                label goodend:
                    nrt "ท่านถามเทพเรื่องเหตุการณ์ว่ามันเกิดอะไรขึ้นกันแน่"
                    show human_face
                    human "เมื่ออดีตกาลเคยมีเหล่าเทพปกครองโลกหลายตนจนครั้นมีมังกรมาออกล่าสัตว์\n{vspace=5}และเผาทำลายธรรมชาติ เหล่าเทพตัดสินใจออกล่ามังกร"
                    human "จนกลายเป็นการทำสงครามกับมังกร จนในที่สุดทั้งเทพและมังกรก็สิ้นชีพจนเกือบหมด\n{vspace=5}ท่านเทพบอกว่าเขาเป็นเพียงเทพกระจอกที่พลังไม่กล้าแกร่ง"
                    human "เมื่อสงครามสิ้นสุดจึงมาใช้ชีวิตเป็นผู้ดูแลดินแดนบริเวณแถวหมู่บ้านของเรา\n{vspace=5}จนมีมังกรตัวนี้มาสังหารเทพนี้แหละ"
                    hide human_face
                    show dragon_face at posface
                    dragon "พวกข้าแค่ออกล่าสัตว์ประทังชีวิตแค่เผาป่าเพียงส่วนนึงเพื่อทำรังเท่านั้น\n{vspace=5}อยู่ๆพวกแกก็มาล่าล้างบางพวกข้าจนเหลือแค่ข้าตัวเดียว"
                    dragon "พวกแกมันก็คือปีศาจดีๆนี้หละ"
                    hide dragon_face
                    menu:
                        "ฆ่ามัน":
                            jump god_beem
                        "อย่าพึ่งฆ่ามัน":
                            jump god_why
                    label god_beem:
                        nrt "ท่านตัดสินใจแล้ว ให้เทพใช้พลังสังหารมังกรจนสิ้นใจ"
                        jump Good_End02
                    label god_why:
                        show human_face
                        human "ทำไมหละ? ทำไมถึงเจ้าถึงบอกว่าอย่าพึ่งสังหารมันหละ?"
                        hide human_face
                        menu:
                            "ฆ่าๆมันไปเถอะ":
                                jump god_beem
                            "ทั้งหมดเป็นแค่เรื่องเข้าใจผิด":
                                jump tell_god
                            "สงครามมันจบไปนานแล้วไม่จำเป็นต้องสร้างสงครามอีก":
                                jump tell_god
                    label tell_god:
                        nrt "ท่านบอกเทพไปอย่างนั้นหลังจากนั้นเทพก็เสกดาบขึั้นมาแล้วยกดาบขึ้นมา"
                        nrt "เทพได้โยนดาลนั่นทิ้งไปแล้วพูดกับมังกร ข้าจะไม่ขอก่อสงคราม\n{vspace=5}นี้ซ้ำอีกเจ้าจะไปไกลก็ไป แค่อย่าสร้างความเดือดร้อนก็พอ"
                        nrt "มังกรมองเทพแบบสายตาไม่กระพิบก่อนที่จะเป็นออกไปจากหุบเขา\n{vspace=5}ไม่มีใครได้เห็นมันอีกเลยหลังจากนั้น"
                        jump Good_End03
        label swords:
            nrt "ท่านปาดาบใส่มันแต่มันอยู่ใกล้เกินไปและดาบก็หนักเกินไปไม่ถึง\n{vspace=5}ท่านถูกกรงเล็บทันแบนในทันใด"
            jump dead

    #label Fight02
    label fight02:
        show dragon_humanface
        boss "เจ้าจะบังอาจเกินไปแล้วที่คิดจะต่อกรกับข้า"
        hide dragon_humanface
        nrt "ว่าแล้วมันก็ปล่อยลำแสงใส่ท่านในทันใด"
        menu:
            "พุ่งฝาลำแสง":
                jump beam01
            "หลบ":
                jump Goodside
            "ใช้โล่":
                jump shield_G01
        label Goodside:
            nrt "เจ้านั่นเสกแขนตัวเองเป็นกรงเล็บขนาดใหญ่ ทุ่มใส่ท่านอย่างสุดกำลัง"
            menu:
                "ใช้โล่":
                    jump shield_G02
                "ใช้เครื่องลาง":
                    jump use_beam
                "ปาดาบไล่":
                    jump swords
        label use_beam:
            nrt "ท่านใช้เครื่องลางปล่อยลำแสงออกไปโดนมันอย่างจังๆ มันร้องด้วยความเจ็บปวด\n{vspace=5}ก่อนที่จะงอกหางออกมาหวังจะทับคุณด้วยหางขนาดยักษ์"
            menu:
                "ใช้ดาบฟัน":
                    jump sword_tail
                "ยิงลำแสง":
                    jump beam_it
                "ยิงลำแสงใส่เพดาน":
                    jump beam_wall
        label sword_tail:
            nrt "ท่านใช้ดาบฟันหางนั้น แต่ดาบนั้นยังคมไม่พอจะฟันหางให้ขาดหลังจากนั้นท่านก็ถูกมัน\n{vspace=5}ทับจนแบนแต็ดแต๋"
            jump dead
        label beam_it:
            nrt "ท่านใช้เครื่องรางยิงลำแสงใส่มันอีกรอบ ลำแสงนั้นโดนหางมันอย่างจัง\n{vspace=5}แต่หางนั้นก็ยังหวดมาโดนคุณอย่างจัง"
            jump dead
        label beam_wall:
            nrt "ท่านใช้เครื่องรางยิงใส่เพดานถ้ำ ทำให้หินหลายก้อนหลายขนาดทับเจ้านั่นอย่างจัง"
            hide dragon_human
            show dragon_normal at posdragon
            nrt "ในขณะที่ท่านมองดูก้อนหินเหล่านั้น อยู่ๆกองหินก็ระเบิดออกเผยให้เห็นมังกรขนาด\n{vspace=5}มหึมาใต้กองหินนั่น"
            show dragon_face at posface
            dragon "เจ้านี่แข็งแกร่งมาก สนใจมาเป็นพวกข้ามั้ยละ"
            hide dragon_face
            menu:
                "สน":
                    jump Bad_End01
                "ไม่สน":
                    jump dragon_choose
            label dragon_choose:
                show dragon_face at posface
                dragon "เจ้าเลือกเองนะ"
                hide dragon_face
                nrt "แล้วมันก็พ่นไฟออกมา"
                menu:
                    "กระโดดหลบ":
                        jump jumping_hides
                    "ใช้โล่":
                        jump shilded03
                    "ใช้เครื่องลาง":
                        jump use_amulet
                label use_amulet:
                    nrt "ท่านใช้เครื่องลางต้านพลังไฟ แต่ลำแสงดันพุ่งฝ่าไฟเข้าปากมังกร\n{vspace=5}ทันที ส่วนท่านที่ถูกไฟคลอกตายตามมังกรไป"
                    jump dead
                label shilded03:
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
                label you_run:
                    nrt "คุณวิ่งหนีมันเร็วเกินไปมันโฉบท่านไปกินโดยทันที"
                    jump dead
                label sword_it:
                    nrt "คุณใช้ดาบนั้นเสียบตามัน มันร้องด้วยความเจ็บปวดมันหยุดพุ่งแล้วดิ้นไปมา"
                    hide dragon_normal
                    nrt "คุณใช้เครื่องรางปล่อยพลังใส่มันจนมันตายคาที่ในทันที"
                    nrt "หลังจากที่ท่านสังหารมังกรได้แล้วท่านก็รู้สึกถึงพลัง\n{vspace=5}ในเมื่อท่านมีพลังพอที่จะฆ๋ามังกร ท่านก็มีพลังที่จะทำอะไรก็ได้"
                    menu:
                        "ปกครอง":
                            jump Bad_End02
                        "ช่วยเหลือ":
                            jump N_End01
                label amulet_use:
                    nrt "ท่านใช้เครื่องลางจะยิงสวนไปแต่เหมือนว่าจะปล่อยพลังไม่ทันมันเร็ว\n{vspace=5}กว่ามันโฉบคุณไปกินในทันที"
                    jump dead

    #label Fight03
    label fight03:
        show dragon_humanface
        boss "เจ้าจะบังอาจเกินไปแล้วที่คิดจะต่อกรกับข้า"
        hide dragon_humanface
        nrt "ว่าแล้วมันก็ปล่อยลำแสงใส่ท่านในทันใด"
        menu:
            "ใช้โล่":
                jump shield_G02_2
            "พุ่งฝ่าลำแสง":
                jump beam01
            "หลบ":
                jump matrixn02
        label shield_G02_2:
            nrt "ท่านใช้โล่กันไว้โล่นั้นแข็งแรงจนกันลำแสงได้อย่างดี"
            jump continueNside
        label matrixn02:
            nrt "ท่านได้หลบลำแสงนั้นอย่างฉิวเฉียด"
            jump continueNside
        label continueNside:
            nrt "เจ้านั่นเสกแขนตัวเองเป็นกรงเล็บขนาดใหญ่ ทุ่มใส่พวกท่านอย่างสุดกำลัง"
            menu:
                "ใช้โล่":
                    jump shield_G02
                "ถือดาบพุ่งเข้าไปหามัน":
                    jump fire
                "ปาดาบใส่มัน":
                    jump swords
        label fire:
            nrt "ท่านวิ่งไปหามันและแทงเข้าไปกลางอกมัน เจ้านั่นร้องด้วยความเจ็บปวด"
            nrt "ทันใดนั้นก็มีเปลวไฟพุ่งออกมาจากปากมัน"
            menu:
                "ใช้ดาบกัน":
                    jump shield_fire
                "อยู่เฉยๆ":
                    jump fire_cock
                "ใช่โล่":
                    jump fire_correct
            label shield_fire:
                nrt "ท่านคิดจะกันไฟด้วยดาบแต่ท่านลืมไปว่าดาบยังอยู่ที่อกมัน"
                jump fire_cock
            label fire_cock:
                nrt "ท่านถูกไฟคลอกกลายเป็น ไก่ KFC ในทันที"
                jump dead
            label fire_correct:
                nrt "ท่านใช้โล่กันไฟไม่ได้รับบาดเจ็บใดๆ"
                nrt "ท่านสังเกตุเห็นว่าเจ้านั่นเริ่มหมดแรง ท่านจึงใช้โอกาสนี้พุ่งเข้าไปหามัน\n{vspace=5}ท่านใช้โล่พลักมันจนล้มลม และพยายามดึงดาบออกจากอกมัน"
                nrt "ทันใดนั้นเองมันก็กลายร่าง ทำให้ตัวท่านและดาบกระเด็นออกไป"
                show dragon_normal at posdragon
                nrt "เมื่อท่านหันหน้าขึ้นมามองก็พบกับมังกรขนาดยักษ์ และมันก็ได้พูดกับท่าน"
                hide dragon_human
                show dragon_face at posface
                dragon "เจ้านี่แข็งแกร่งมาก สนใจมาเป็นพวกข้ามั้ยละ"
                hide dragon_face
                menu:
                    "สน":
                        jump Bad_End01
                    "ไม่สน":
                        jump dragontalkpart3
            label dragontalkpart3:
                show dragon_face at posface
                dragon "เจ้าเลือกเองนะ"
                hide dragon_face
                nrt "จากนั้นเจ้ามังกรมันก็พ่นไฟออกมา"
                menu:
                    "กระโดดหลบ":
                        jump jumping_hides
                    "ใช้โล่":
                        jump shield_ne_01
                    "ใช้ดาบกัน":
                        jump sword_gun
            label sword_gun:
                nrt "ท่านจะหยิบดาบออกมาแต่ไม่ทันการ ท่านถูกไฟคลอกกลายเป็นได่ย่างในทันที"
                jump dead
            label shield_ne_01:
                nrt "ท่านใช้โล่กันไว้เปล่วไฟนั้นถูกโล่กันได้หมด ไม่ได้รับบาดเจ็บใดๆ"
                nrt "มังกรพุ่งมาหาคุณด้วยความเร็วสูง"
                menu:
                    "ใช้โล่":
                        jump shelid_ne_02
                    "ใช้ดาบพุ่งหามัน":
                        jump sword_ne_02
                    "ก็เผ่นซิคร้าบ":
                        jump you_run
                label shelid_ne_02:
                    nrt "ท่านใช้โล่กระแทกกับหน้ามัน มังกรจับท่านแล้วโยกตกเขาตายคาที่"
                    jump dead
                label sword_ne_02:
                    nrt "คุณใช้ดาบนั้นเสียบตามัน มันร้องด้วยความเจ็บปวดมันหยุดพุ่งแล้วดิ้นไปมา"
                    nrt "ท่านหลบไปใช้ดาบฟันไปทั่วร่างของมังกร มังกรหาจังหวะฟันเข้าที่อกของท่าน\n{vspace=5}อย่างจังอย่างจังด้วยกรงเล็บท่านหาจังหวะแทงคอมันจนมันล้มไปพร้อมกับท่าน"
                    nrt "ท่านได้รับบาดเจ็บมาก แต่ท่านยังเหลือน้ำอมฤตอยู่ ท่านจะใช้ให้หมดเลยหรือไม่"
                    menu:
                        "ใช้ให้หมด":
                            jump use_all_water
                        "ใช้ส่วนนึง":
                            jump use_little_water
                    label use_all_water:
                        nrt "ท่านราดน้ำใส่ร่างกายจนหมดตัว นอกจากแผลบนร่างกายจะหายแล้ว\n{vspace=5}ยังมีกำลังเพิ่มด้วย"
                        nrt "ท่านเดินไปหามังกรที่นอนบาดเจ็บอยู่และฟันคอมันจนขาดออกจากร่างตายคาที่ในทันที"
                        jump N_End01
                    label use_little_water:
                        nrt "ท่านใช้น้ำส่วนหนึ่งในการทาตามร่างกายบริเวณที่มีแผล จนบาดแผลส่วนใหญ่หายดี"
                        nrt "ท่านพูดกับมังกรไปว่า"
                        py "ถ้าเจ้าสัญญาว่าจะไม่ทำลายหมู่บ้านและหยุดภัยพิบัติทั้งหมดนี้ข้าจะรักษาเจ้า"
                        nrt "เจ้ามังกรได้หยุกชะงักไปชั่วครู่แล้วก็ได้พูดขึ้นมาว่า"
                        show dragon_face at posface
                        dragon "ข้าไม่ได้คิดจะทำร้ายใครยกเว้นเจ้าเทพสารเลวนั่น และข้าไม่ได้เป็นคนสร้างภัยพิบัติด้วย"
                        hide dragon_face
                        menu:
                            "ฆ่ามัน":
                                jump End_NO1
                            "ถามข้อมูล":
                                jump ask_question
                        label ask_question:
                            nrt "ท่านซักถามข้อมูลเจ้ามังกรได้ข้อมูลดังนี้"
                            nrt "มังกรตัวนี้รอดมาจากการฆ่าล้างเผ่าพันธุ์ของเหล่าเทพ มังกรตัวนี้หนีออกมา\n{vspace=5}และกลายร่างเป็นคนหลบซ่อนในดินแดนนี้มานานจนได้จังหวะที่เทพ\n{vspace=5}และมังกรสิ้นจนเกือบหมด"
                            nrt "เหลือแค่เทพองค์นี้ที่มาปักหลักบนดินแดนนี้"
                            nrt "ด้วยความแค้น มันจึงบินไปสังหารเทพโดยทันที"
                            show dragon_face at posface
                            dragon "เจ้าบอกว่าเทพดูแลดินแดนนี้มาก่อนใช่มั้ย ไม่แน่ที่ข้าฆ่าเทพ\n{vspace=5}อาจทำให้ธรรมชาติแปรปวนก็ได้"
                            dragon "ถ้าเป็นงั้นข้าคงทำอะไรกับมันไม่ได้"
                            hide dragon_face
                            nrt "ท่านรู้ความจริงแล้ว ท่านจะทำไรกับมัน"
                            menu:
                                "ฆ่ามัน":
                                    nrt "ท่านเดินไปหามังกรที่นอนบาดเจ็บอยู่และฟันคอมันจนขาดออกจากร่างตายคาที่ในทันที"
                                    jump N_End01
                                "ให้น้ำอมฤต":
                                    jump water_good
                            label water_good:
                                nrt "ท่านใช้น้ำอมฤษที่เหลือทาไปทั่วตัวมังกร แผลบนร่างกายมันหายไปมากแต่ปริมาณน้ำก็ไม่พอจะรักษามันทั้งตัว"
                                nrt "มันมองท่านก่อนที่มันจะบินออกจากถ้ำไป"
                                jump N_End02
                                
                            
    # end game
    label end0:
        scene end0
        nrt "ตอนจบที่ 0: สันหลังยาว"
        nrt "คุณได้กลับหมู่บ้านโดยทิ้งให้โลกนั้นปั่นป่วนต่อไป...\n{vspace=5}สักวันหนึ่งอาจจะมีผู้พิชิตคนใหม่มากอบกู้ความปั่นป่วนนี้"
        return
    label end1:
        nrt "ตอนจบที่ 1: ทำบุญทำทานให้อาหารสิงโต"
        nrt "สิงโตค่อยๆกัดกินร่างของคุณ คุณนั้นก็ได้กรีดร้องออกมาด้วยความเจ็บปวด"
        nrt "คงไม่มีทางเลือกนอกจากยอมรับชะตากรรม และกลายเป็นสารอาหารให้สิงโต"
        return
    label end2:
        nrt "ตอนจบที่ 2: ประตูสู่ความมืดมิด"
        nrt "ท่านไม่สามารถหลีกหนีชะตากรรมได้ และทรายก็ค่อยๆดูดกลืนลงไปเรื่อยๆ\n{vspace=5}จนท่านไม่ได้เห็นแสงตะวันอีกเลย"
        return
    label dead:
        nrt "ตอนจบที่ 3 : ยูอาเดด"
        nrt "ใช่คุณตายแล้ว พยายามแค่ไหนก็ไม่สมหวังหรอกนะ"
        nrt "ชีวิตจริงก็เช่นกัน"
        return
    label Good_End01:
        scene black
        stop music
        nrt "ตอนจบที่ 4: ตำนานนิรันด์กาล"
        nrt "หลังจากเหตุการณ์ทั้งหมดจบลงไป ภัยธรรมชาติทุกอย่างได้กลับคืนสู่ความปกติ\n{vspace=5}เทพกลับมาดูแลธรรมชาติเหมือนเดิม ปีศาจมังกรสิ้นใจไป"
        nrt "ท่านได้กลายเป็นตำนานผู้เสียสละชีพเพื่อปกป้องหมู่บ้านและผู้ฟื้นคืนเทพไปชั่วกาล"
        return
    label Good_End02:
        scene black
        stop music
        nrt "ตอนจบที่ 5: ผู้พิชิต"
        nrt "ท่านได้เป็นตำนานผู้พิชิตมังกร ผู้ปกป้องหมู่บ้านและผู้ฟื้นคืนเทพเจ้า\n{vspace=5}หลังจากนั้นท่านก็ใช้ชีวิตในหมู่บ้านนั้นอย่างมีความสุข"
        return
    label Good_End03:
        scene black
        stop music
        nrt "ตอนจบที่ 6: ความสงบสุขที่แท้จริง"
        nrt "หลังจากเหตุการณ์ทั้งหมดจบลง ภัยธรรมชาติทุกอย่างก็หายไป\n{vspace=5}เทพกลับมาดูแลธรรมชาติ เหมือนเดิมมังกรไม่ได้ฆ่ารุกรานอีกเลย"
        nrt "ท่านได้กลายเป็นตำนานผู้ปกป้องหมู่บ้านและผู้ฟื้นคืนเทพเจ้า\n{vspace=5}จากนั้นก็ใข้ขีวิตอย่างมีความสุขตลอดมา"
        return
    label Bad_End01:
        scene black
        stop music
        nrt "ตอนจบที่ 7: ทาสผู้ซื่อสัตย์"
        nrt "หลังจากเหตุการ์ณทั้งหมดมังกรก็ได้เป็นผู้ยิ่งใหญ่ในดินแดนแห่งนี้\n{vspace=5}และท่านก็ได้เป็นผู้รับใช้มังกรไปชั่วกาล"
        return
    label Bad_End02:
        scene black
        stop music
        nrt "ตอนจบที่ 8: ตอนต่อไปของความชั่วร้าย"
        nrt "ท่านมีพลังมากเหลือล้น แต่ท่านเลือกที่จะใช้พลังอำนาจ\n{vspace=5}ที่ท่านมีในการปกครองดินแดนและหมู่บ้านอย่างกดขี่"
        nrt "หลังจากเหตุการ์ณทุกอย่างจบลง ภัยธรรมชาติทุกอย่างยังคงอยู่ ท่านได้เป็น\n{vspace=5}ตำนานเทพปีศาจผู้สังหารมังกรและผู้ปกครองดินแดนคนใหม่"
        nrt "ผู้เหี้ยมโหด รอนักรบคนต่อไป ผู้ที่จะไปกำราบท่าน"
        return
    label N_End01:
        scene black
        stop music
        nrt "ตอนจบที่ 9: ผู้พิทักษ์"
        nrt "ท่านมีพลังมากเหลือล้น ท่านเลือกที่จะกลับหมู่บ้านและใช้พลังของท่าน\n{vspace=5}ในการปกป้องหมู่บ้านต่อไป"
        nrt "หลังจากเหตุการ์ณทุกอย่างจบลงภัยธรรมชาติยังคงอยู่ แต่หมู่บ้านก็มีนักรบผู้ปกป้องหมู่บ้านคนใหม่\n{vspace=5}ผู้สังหารมังกร ท่านจะอยู่ปกป้องหมู่บ้านและดินแดนแห่งนี้ไปชั่วกาล"
        return
    label N_End02:
        stop music
        nrt "ตอนจบที่ 10: การเดินทาง"
        nrt "หลังจากที่เหตุการ์ณทั้งหมดจบลง ภัยธรรมชาติทั้งหมดไม่หายไปและมังกรตัวนั้นก็หายไป\n{vspace=5}ไม่มีใครเห็นมันอีกเลย"
        nrt "ท่านตัดสินใจออกเดินทางออกจากดินแดนนี้ไปหาวิธีหยุดภัยพิบัตินี้ต่อไป"
        return


    label demoe:
        scene black
        nrt "ขอขอบคุณที่เล่นตัวทดลองของเรา เนื้อเรื่องต่อไปยังคงอยู่ในระหว่างการพัฒนา"
        nrt "คุณสามารถดูตัวอย่างเกมได้ที่\n{vspace=5}https://www.youtube.com/watch?v=BjDebmqFRuc"
        return