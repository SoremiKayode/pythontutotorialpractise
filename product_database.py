import sqlite3

connection = sqlite3.connect("product.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE if not exists product
(id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT,
product_price INTEGER, product_description TEXT, seller VARCHAR(100),
shipping_cost INTEGER)""")
cursor.execute("""
INSERT INTO product(product_name, product_price, product_description, seller, shipping_cost)
VALUES('TCWH004-C1 1.4 Inch HD Screen IP68 Waterproof Smart Watch', 19500, 'TCWH004-C1 1.4 inch HD Screen IP68 Waterproof Smart Watch
1. Processor: PHY6202
2. Memory: ROM: 512KB, RAM: 138KB
3. Display: 1.4-inch full-fit high-definition screen
4. Battery: 200mA
5. Bluetooth: 4.0
6. System: support Android 4.2, IOS 8.0 and higher
7. Languages: English, French, Spanish, Portuguese, Arabic, Persian
8. Functions: temperature measurement, IP68 waterproof, multi-dial switching, pedometer, multi-sports mode, electrocardiogram, heart rate monitoring, blood pressure monitoring, blood oxygen monitoring, sleep monitoring, sedentary reminder, call reminder, message reminder, stopwatch, music Control, photo control, anti-lost, alarm clock, weather, support OTA upgrade, etc.
9. Long standby: 7 days standby, about 3 days connected to mobile phone
10. Package includes: 1 x smart watch, 1 x charging cable, 1 x user manual', 'Soremi Kayode', 2000
)
""")

cursor.execute("""
INSERT INTO product(product_name, product_price, product_description, seller, shipping_cost)
VALUES('Infinix Note 10 Pro - 6.95" FHD+ (128GB ROM,8GB RAM) Android 11 (64/8/2/2)MP + 16MP Selfie - 4G LTE - 5000mAh - Nordic Secret', 189999, 'Note 10 Pro, 6.95" FHD+ (8GB RAM, 128GB ROM) Android 11 (64/8/2/2)MP + 16MP Selfie - 4G LTE - 5000mAh - Fingerprint - Nordic Secret
Launch	Announced	2021, May 12
Status	Available. Released 2021, June 07
Body	Dimensions	172.8 x 78.3 x 7.8 mm (6.80 x 3.08 x 0.31 in)
Weight	209 g (7.37 oz)
SIM	Dual SIM (Nano-SIM, dual stand-by)
Display	Type	IPS LCD, 90Hz
Size	6.95 inches, 114.7 cm2 (~84.8% screen-to-body ratio)
Resolution	1080 x 2460 pixels (~387 ppi density)
Platform OS	Android 11, XOS 7.6
Chipset	Mediatek Helio G95 (12 nm)
CPU	Octa-core (2x2.05 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)
GPU	Mali-G76 MC4
Memory	Card slot	microSDXC (dedicated slot)
Internal	64GB 6GB RAM, 128GB 8GB RAM, 256GB 8GB RAM
UFS 2.2', 'Soremi Kayode', 4000
)
""")

cursor.execute("""
INSERT INTO product(product_name, product_price, product_description, seller, shipping_cost)
VALUES('Gionee M12, 6.55-Inch HD+ 6GB RAM, 128GB ROM) Android 10 48MP + 5MP + 2MP + 2MP + 16MP Dual SIM 4G LTE - Green', 79900, 'The smartphone Features a 6.55-inch Full HD display, the Gionee M12 smartphone with a in-built memory of 6GB + 128GB (Expandable to 256 GB) compact for the screen and battery size. Youve got the real powerful smartphone. Its got: 48MP + 5MP + 2MP + 2MP (Quad rear Camera) & 16MP selfie camera. The fast charging battery lasts for several hours and this smartphone supports multi-band and LTE, as well as Bluetooth and runs on Android 10.  Rear For security, it has a fingerprint scanner &   AI face unlock.
Gionee M12 has been spotted on Google Play Console listing as the latest smartphone from the company. The brand introduced Gionee M12 Pro in September this year targeting the budget segment, MediaTek chipset, and more. The smartphone key specifications revealed on Google Play Console listing with some entry-level specifications. So, lets take a closer look at the key specs of the smartphone on the highlight below.
The Gionee M12 Google Play Console listing was spotted with real power and it reveals a render along with some key specifications. The image present in the listing shows that the smartphone come with a punch-hole cutout at the top-left corner for a selfie camera. The bezels look slim around the edges. The right side of the side features volume controls and power on/off button.', 'Franscis Elome', 3000)""")
cursor.execute("""
INSERT INTO product(product_name, product_price, product_description, seller, shipping_cost)
VALUES('F8 Waterproof General Body Fitness Health Smart Bracelet.', 14650, 'TThis is a 1.3 inch screen multi-functional smart bracelets. It is compatible for iOS 9.0 and above, for Android 4.2 and above. It will give you nice experience.



Features:

Stay in touch for messages, you will not miss important message or incoming call.

Support to monitor heart rate and bloods pressures continuously.

Multiple sport modes, scientific analysis to manage your health.

Fitness wristwatch, you can check your daily data on it.

Easy to use and perfect for running and outdoor sports.

Support IP67 water resistance function, which can better avoid damage from washing hand, water splashing, rain, etc.

Support BT 4.0, for Android 4.2 and above, for iOS 9.0 and above.

Low consumption, over 8 days standby time.

Durable and comfortable to wear.

Functions: Time date batterys weather display, sport, heart rate, bloods pressures, sleep monitor, applications remind, message notification, answer and refuse the call, sedentary reminder, reminder for drinking, shake the bracelet to take photo, find bracelet, alarm clock, restore factory settings, anti-lost...



Specifications:

Screen: 1.3inch colorful

Color: Black, Gold, Silver, Black&Green(Optional)

Mpdel: F8

Material: ABS+ PC 

Strap Material: TPU

Earphone Material: Silicone

Clasp Type: Buckle

BT: BT 4.0

Compatibility: for Android 4.2 / iOS 9.0 and above

Batterys: 1*3.7V 110mAh lithium batterys

Charge: USB

Standby Time: about 8 days

Functions: Time date batterys weather display, sport, heart rate, bloods pressures, sleep monitor, applications remind, message notification, answer and refuse the call, sedentary reminder, reminder for drinking, shake the bracelet to take photo, find bracelet, alarm clock, restore factory settings, anti-lost...

Water-Resistant Level: IP67

Total Length: 270mm/10.63in

Item Size: 41*23*8mm/1.61*0.91*0.31in

Item Weight: 59g/2.08oz

Package Size: 227*57*33mm/8.94*2.24*1.3in

Package Weight: 151g/5.33oz



Package Lists:

1*Smart Bracelets Base

1*USB Cable

1*User Manual', 'Tolani Brown', 1000
)
""")

cursor.execute("""
INSERT INTO product(product_name, product_price, product_description, seller, shipping_cost)
VALUES('Tecno Pova Neo, 6.8" IPS LCD Screen, 4GB/64GB Memory, 13MP Dual Camera, 6000 mAh Battery - Geek Blue', 68990, 'The POVA Neo is the cheaper variant of Tecno POVA 2. The key selling point of the phone is it large display and battery. Talking about display, the model sports a 6.82-inches screen with 720 x 1640 pixels, and a dewdrop notch on the front, housing the selfie camera. On the inside, the Tecno POVA Neo is powered by MediaTek MT6762V, a downgraded version of Helio P22 which has 4×1.8GHz and 4×1.5GHz Cortex-A53 CPUs. The model has 4GB RAM and 64GB of internal storage, which is expandable up 128GB via an SD card. There are two camera lenses on the rear of the POVA Neo; a 13-megapixel primary snapper and a secondary 2-megapixel depth lens, along with four LED flashes, while a single 8-megapixel selfie lens is kept on the front. The model come with a rear placed fingerprint scanner and it is available in Obsidian Black, Geek Blue and Powehi colors. There is a 6000mAh battery on the inside, while Google Android 11, with HiOS 7.6 is available out of the box.',
 'Adam Eloi', 6000
)
""")
cursor.execute("""
INSERT INTO product(product_name, product_price, product_description, seller, shipping_cost)
VALUES('UMIDIGI A11 (3GB,64GB ROM) Android 11 Infrared Temperature Sensor 2.0 (16MP+8MP+5MP)+8MP 5150mAh 6.53" Global Version-Frost Grey', 59900, 'Welcome to UMIDIGI Official Store on JUMIA.   UMIDIGI is a smartphone manufacturing-based company founded in China Shenzhen in 2012, which commits to delivering exquisite mobile electronic devices. That is focused on premium products, differentiating innovation, achieving technological breakthroughs, and delivering global customers an extraordinary mobile experience with meticulous designs and advanced technology. To make premium products accessible to everyone at an affordable price.   UMIDIGI A11 2021', 'Yetunde Slim', 2500
)
""")

connection.commit()
connection.close()