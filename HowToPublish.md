# 記事の書き方(Pelican&GithubPages)

1. 記事作成: `/content` 下にmdファイルで作る
2. ビルド: `pelican content -o output -s pelicanconf.py -t bootstrap`
3. 確認: `pelican --listen`
4. Github PagesにPush: `ghp-import output -b main && git push`
- 注意: `ghp-import output -b main && git push` 後に個別のファイルをpushしようとするとHPが映らなくなります