# 記事の書き方(Pelican&GithubPages)

1. `/content` 下にmdファイルを作る
2. ビルド: `pelican content -o output -s pelicanconf.py`
3. 確認: `pelican --listen`
4. Github PagesにPush
```
ghp-import output
git push
```