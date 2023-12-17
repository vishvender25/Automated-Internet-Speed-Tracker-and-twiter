
# Automated-Internet-Speed-Tracker-and-twiter
A Python script that tests your internet speed and tweets if the internet speed is less than the claimed speed of your ISP.



## Authors

- [@vishvender tyagi](https://www.github.com/vishvender25)


## Appendix

## Working
The script interacts with the google.com home page and finds the internet speed using selenium.
If the current internet speed is less than the min speed promised by the ISP then the scripts automatically tweets the internet speed.

### Libraries Used
The script uses selenium library to interact with the webpages.
You also need to import time to add delays and os to store the environment variables.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

these are the environment variavble that will be used in the script to send you an alert message.     

`MY_PASS`   

`MY_EMAIL`

`MY_USERNAME`


## Deployment

To deploy this project run

```bash
  python3 main.py
```


