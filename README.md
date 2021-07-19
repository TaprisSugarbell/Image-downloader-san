# Image-downloader-san

## Dependencies
- ### Python >= 3.8
- ### [requests](http://docs.python-requests.org/en/latest/)

## Example of use

### Site Recognize

```python
from Id import Bruteforce

b = Bruteforce()
b.site_recognize("https://e-shuushuu.net/image/1056471/")
```

### Safebooru

```python
from Id import Bruteforce

b = Bruteforce()
b.site_recognize("https://safebooru.donmai.us/posts/4510322?q=order%3Arank")
```

#### Login example

```python
from Id import Bruteforce

b = Bruteforce(username="YOUR-USERNAME", api_key="YOUR-API-KEY")
b.safebooru("https://safebooru.donmai.us/posts/4510322?q=order%3Arank")
```

### Sankaku Complex

```python
from Id import Bruteforce

b = Bruteforce()
b.sankaku("https://chan.sankakucomplex.com/post/show/25048523")
```

### Download Image

```python
from Id import Bruteforce

b = Bruteforce()
b.yandere("https://yande.re/post/show/782256").download()
```

### Force Download

```python
from Id import Bruteforce

b = Bruteforce()
b.download_image("https://pbs.twimg.com/media/E0uKGhTWUAgXb3a?format=jpg&name=large", force=True)
```

### Information

```python
from Id import Bruteforce

b = Bruteforce()
b.konachan("https://konachan.com/post/show/326520/bikini-breast_hold-close-gray_eyes-gray_hair-infin", info=True)
```

