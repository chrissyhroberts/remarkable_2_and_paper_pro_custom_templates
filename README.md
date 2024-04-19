# remarkable_2_hacks

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
