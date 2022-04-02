# Space Heroes CTF: R2D2
### Description

> We wouldn't miss the opportunity to make this dad joke. \
http://173.230.138.139/ \
https://spaceheroes-web-r2d2.chals.io

**Author:** v10l3nt

<details closed>
<summary>Solution</summary>
  
  
### Detailed Solution

Let's take a look at the source code with `F12`.

```html
<html>
<h1>Roger, Roger</h1>
<img src="/static/images/robots.jpeg" />
<h4>No, you are the one who is useless.</h4>
</html>
```
We see that the image on the website is named `robots.jpeg`. What happens if we visit `robots.txt`? 🤔
```sh
$ curl http://173.230.138.139/robots.txt
shctf{________}
```
Hmmm... that challenge was pretty guessy. Let us know if you had a more elegant solution!
</details>
