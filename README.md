# Remarkable 2 and Remarkable Paper Pro hacks for custom sleep screens and templates. 

## Access to the template folder over ssh

* On the Remarkable 2
	* click Settings > General > About > Copyrights and Licenses
	* Copy down the password (like "abcD12E3Fg")
	* Also copy down the IP address (like "192.12.12.3")

* On your command line
	* `scp -r root@192.12.12.3:/usr/share/remarkable/templates/ ./`
	* Accept the connection for ssh security
	* At the prompt, type the password you got from the device
	* Make the changes you want to the template svg files
	* Edit the templates in something like Affinity/Inkscape etc.
	* Save your new templates as .svg and .png
	* Make a copy of the `templates.json` file in the New_Templates directory.
  	* Edit New_Templates/templates.json to add your custom template
	* Icon codes can be found [here](http://www.davisr.me/posts/2020/2020-10-07/rm-2.3.0.16-icon-codes.png)    

The addition to the json file should look like this example for "Eisenhower"
```
		{
      "name": "Checklist",
      "filename": "LS Checklist",
      "iconCode": "\ue9ab",
      "landscape": true,
      "categories": [
        "Life/organize"
      ]
    },
    {
      "name": "Eisenhower",
      "filename": "P eisenhower",
      "iconCode": "\ue9ab",
      "landscape": false,
      "categories": [
        "Life/organize"
      ]
    },
    {
      "name": "Dayplanner",
      "filename": "LS Dayplanner",
      "iconCode": "\ue9ac",
      "landscape": true,
      "categories": [
        "Life/organize"
      ]
    }
```


* Push your new templates back to the device 
	* `scp ./New_Templates/* root@192.12.12.3:/usr/share/remarkable/templates/`

* Restart the remarkable device	


### Custom Sleep screens

The various power off, sleep etc screens are also just png files, so you can add a custom sleep screen pretty easily
Just push them to `/usr/share/remarkable/`
There's examples in the `sleep_screens` folder
Rename the one you want to use as suspended.png




# Remarkable Paper Pro


The paper pro seems to have the same inner workings as the remarkable 2, except it doesn't show you how to connect via wifi without a bit of shenanigans. 

Your new templates need to be SVGs with 1620 x 2160 pixels

When you start the device for the first time, you need to enable developer mode   

* Go to settings > sotfware > advanced  
* This will factory reset in to developer mode  
* Set up as normal  
* Plug the system in to your computer with the usb cable  
* Go to settings > software > about  
* the top ip address is something like 10.11.99.2  
* use terminal to ```ssh root@10.11.99.2```  
* type the password shown in bold on the device  
* then type ```rm-ssh-over-wlan on```  
* from now on you can wifi connect with the other ip that starts 192.xxx  
* When you log in, you'll need to remount the filesystem with write permissions as it initially mounts as readonly  
* remount with ```mount -o remount,rw /```  
* check it worked with ```mount | grep .```  
* Transfer your templates as above, I use cyberduck for drag and drop.   

the json data for templates is now stored (on this version at least) in a file called `ferrari-templates.json`  
Edit that instead of the `templates.json` file.   
As with the previous device, there's a load of hidden pre-designed templates that you can activate by adding them back in to the json file.   

* Reboot to load it all back up again.   



NB there's some security risk of course with opening up wlan connection, so keep your password safe. 

![PHOTO-2024-09-14-11-18-00](https://github.com/user-attachments/assets/700bc131-4e2c-4c67-9817-b1f359e381cf)

