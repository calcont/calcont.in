# CalConT

### What was my motivation ?
So, It is a website that I have created as a side project to explore my knowledge towards web development and Django ( you"ll get this how beginner I was by reading folder,project app name ) and I wanted a project to be ready -> deployed .That's why thought let's create something which will have tools such as calculators, translators, converters. And back then I was in second year of my college had a DSA subject so I was learning through it and adding various tools in website Examples:- postfix calculator , prefix calculator etc.

### What actually it does ?
Finally, <a href="https://www.calcont.in">calcont.in</a> is a website which contains various tools such as calculators ,converters ,AI-based analyzers, translators which can help people to save their time in day-to-day life.
We have >= 15k visitors who invest their valuable time in this website in a month and around 500-600 users per day.

## Installation

First up of all you need to create python virtual environment.(<a href="https://docs.python.org/3/library/venv.html">ref</a>)

For windows,
```
python3 -m venv venv_name 
```
then go to that directory where venv is
```
cd venv_name
```
fork & then clone calcont.in project
```
git clone git@github.com:calcont/calcont.in.git
```
activate the venv
```
.\Scripts\activate
```
go to calcont.in
```
cd calcont.in
```
install all python packages mentioned in requirements.txt
```
pip install -r requirements.txt
```
create .env in root directory and add
```
SECRET_KEY=anystring
client_secret_captcha=anystring
GRAMMAR_API_URL=anystring
GRAMMAR_API_KEY=anystring
GRAMMAR_API_HOST=anystring
```
as this app consist few database schemas that need to be migrated.so,run
```
python manage.py migrate
```
run django server
```
python manage.py runserver
```

## Usage

Once you done with your setup, you need to understand workflow of the project
1. `basicsite` is the root or we can say main project name, which contains essential files such as `urls.py` , `views.py` , `settings.py` etc.
As, django framework follows `MVT` i.e Model View Template structure to handle request on server

### Settings
There is a folder called `settings` in which 3 major files are there i.e `dev.py` , `prod.py` , `base.py` .
 - `base.py` consist of all the common settings for both dev.py & prod.py
 - `dev.py` consist development settings & credentials
 - `prod.py` consist all heroku related configurations and some of production credentials

### urls
urls.py have several url patterns such as for `social_auth` to handle social login, `admin` and very important is `mysite.url` which basically handles all the urls and request info.

### mysite
It is basically a core app of calcont which contains important folders,files such templates, all_urls , all_views etc.
- `models.py` - It consist of database schema , relation between different entities and attributes under it.
- `templates` - Templates consist of all the html files and every category has different folder which has html files of all tools comes under either calculators , converters etc.
- `all_urls` - It is folder which has different url files and those urls.py files again different for different category. When any user request some url it first goes to basicsite i.e root app and then to the mysite app wherein logic to handle request is been written in views.
- `all_views` - It is folder which contains files of views for all categories wherein logic is been written over here like which html file to show for particular request and as well as handling post & get request, form submission and save the details to the database etc. is been written over here.




## Contributing

Pull requests are welcome. For major changes, please open an issue first or u can create new discussion topic
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[APACHE 2.0](LICENSE.md)
