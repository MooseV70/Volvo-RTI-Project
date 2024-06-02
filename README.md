# Volvo RTI Project

In this project, a complete overhaul was undertaken to create a new system to replace the original RTI system. My car never had navigation before, and all the steps I will describe here are from the perspective of a layperson and beginner.

### What it can do?

- Retract and extend the display using a button on the phone control (ON/OFF)
- Automatically retract when the ignition is turned off
- PHM backlight and status LED
- Parking camera
- Complete control through the PHM module
-  Apple CarPlay

### What needs to be done?

- LIN bus reading of steering wheel buttons
- Fixing ground loop noise
- Fixing parking camera noise

# Each parts

### PHM Module

Everything from the PHM module has been removed. I left only the PCB board under the keyboard and the flexible cable, which I connected to the Arduino Leonardo using a 30-pin 0.5mm converter, creating a matrix keyboard.

[30pin 0.5mm](https://www.aliexpress.com/item/1005005523307261.html?spm=a2g0o.productlist.main.91.6a972e493YE6vg&algo_pvid=0f6ebca3-1c16-4c3b-a9de-b8af134397f3&algo_exp_id=0f6ebca3-1c16-4c3b-a9de-b8af134397f3-45&pdp_npi=4%40dis%21USD%212.22%211.89%21%21%2116.03%2113.63%21%4021038e8317173246459991826e623f%2112000033408736663%21sea%21CZ%21754802005%21&curPageLogUid=ZJkDbAfoJLxV&utparam-url=scene%3Asearch%7Cquery_from%3A) **$2.51**


### Display  

I used the casing and the sliding mechanism from the display. I replaced the original serial display with a higher-quality one with higher resolution. The original **400x240p** was replaced with **800x480p**. The difference is really noticeable. The display controller board fit right behind the display, and I replaced the serial port with HDMI. I used flexible cables from FPV drones, 20cm and connectors. All from AliExpress. The display with the board cost around 30 dollars and the cable with connectors cost 20 dollars. The sliding mechanism itself is controlled via Arduino Nano and the ON/OFF button from the keyboard. Details are in the code

[ATN065TN14 Display](https://www.aliexpress.com/item/32846472356.html?spm=a2g0o.order_list.order_list_main.211.2e2a1802xvvvjL) **$17.81**

[Driver board](https://www.aliexpress.com/item/4001175095149.html?spm=a2g0o.order_list.order_list_main.216.2e2a1802xvvvjL) **$13.70**

[Flexi HDMI cable](https://www.aliexpress.com/item/1005006382553701.html?spm=a2g0o.productlist.main.11.6ce216acHzzrii&algo_pvid=a392f77e-8b81-46d5-9c79-8076d6b58919&algo_exp_id=a392f77e-8b81-46d5-9c79-8076d6b58919-5&pdp_npi=4%40dis%21USD%217.28%217.28%21%21%217.28%217.28%21%402103864c17173244466304461ed224%2112000036972338192%21sea%21CZ%21754802005%21&curPageLogUid=YupHokAugJHy&utparam-url=scene%3Asearch%7Cquery_from%3A) **$11.70** For 50cm cable 

### Trunk Navi unit

I removed all the contents of the original unit and placed a Raspberry Pi, a relay for switching the parking camera, a relay for recognizing the ignition status, and a Carlink unit into the empty casing. Of course, there is also a time relay. The code and procedure were created according to [765GHF](https://bluewavestudio.io/community/thread-1128.html).

[Timer relay](https://timers.shop/Multi-Functional-3V-18V-Time-Delay-Relay-Timer--5-amp-V8_p_77.html)**$17.99** *Now in sale*

[ESP coder for relay](https://timers.shop/Universal-programmer-for-timer-V8_p_78.html)**$19.99** *Now in sale* 

[12V relay for Parking camera](https://www.aliexpress.com/item/32501322820.html?spm=a2g0o.productlist.main.3.24994d8523gtle&algo_pvid=a57b93c5-f83c-4f0c-9f92-29447fc54495&algo_exp_id=a57b93c5-f83c-4f0c-9f92-29447fc54495-1&pdp_npi=4%40dis%21USD%211.27%211.21%21%21%211.27%211.21%21%40211b618e17173251601893065e70ab%2112000029855842928%21sea%21CZ%21754802005%21&curPageLogUid=87pGXnk4J2VG&utparam-url=scene%3Asearch%7Cquery_from%3A) **$1.21**

[JD1914 relay for ignition](https://www.aliexpress.com/item/1005004387744016.html?spm=a2g0o.productlist.main.1.da74367f4Ax43z&algo_pvid=e0979646-c241-43f9-9111-6716a17499de&algo_exp_id=e0979646-c241-43f9-9111-6716a17499de-0&pdp_npi=4%40dis%21USD%213.10%213.10%21%21%213.10%213.10%21%40211b801917173252767138503e1614%2112000029003029779%21sea%21CZ%21754802005%21&curPageLogUid=c3idgqPfw77N&utparam-url=scene%3Asearch%7Cquery_from%3A) **$3.10**

# Some pictures
![PHM](https://i.ibb.co/XbN59bV/IMG-7083.jpg)
![Park camera](https://i.ibb.co/pwQz8Nf/IMG-7084.jpg)
![CarPlay](https://i.ibb.co/w6y1skY/IMG-7081.jpg)
![Trunk](https://i.ibb.co/mbZYnRF/IMG-7068.jpg)









