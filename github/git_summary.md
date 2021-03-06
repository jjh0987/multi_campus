<aside> ๐ก Git ๊ด๋ จ ๋ช๋ น์ด๋ฅผ ํ๋์ ํ์ํฉ๋๋ค.

</aside>

### 1. basic

```bash
# ์์ฑ์ ์ด๋ฆ, ๋ฉ์ผ ๋ฑ๋ก (์ต์ด 1๋ฒ๋ง ์คํ)
git config --global user.name "github username"
git config --global user.email "github email"

# config ์ ๋ณด ์ถ๋ ฅ
git config --global --list

# ์ผ๋ฐ ํด๋ -> ๋ก์ปฌ ์ ์ฅ์
git init

# ๋ฒ์  ์ํ ์ถ๋ ฅ
git status

# Working Directory -> Staging Area
git add [File]
git add .  # ๋ชจ๋  ํ์ผ add

# Staging Area -> Commits
git commit -m "commit message"

# commits ๋ชฉ๋ก ์ถ๋ ฅ
git log
git log --oneline  # ํ์ค๋ก ๋ณด๊ธฐ ์ต์
git log -p  # ์ปค๋ฐ๋ง๋ค ์ฐจ์ด ๋ณด๊ธฐ ์ต์
```

### 2. remote

```bash
# ๋ก์ปฌ ์ ์ฅ์์ ์๊ฒฉ ์ ์ฅ์๋ฅผ ์ฐ๊ฒฐ
git remote add origin [Github repository URL]

# ์ฐ๊ฒฐ๋ ์๊ฒฉ ์ ์ฅ์ ๋ชฉ๋ก ์กฐํ
git remote -v

# ์๊ฒฉ ์ ์ฅ์ ์ฐ๊ฒฐ ์ญ์ 
git remote rm origin
git remote remove origin

# ๋ก์ปฌ ์ ์ฅ์์ commits์ ์๊ฒฉ ์ ์ฅ์์ ๋ฐ์
git push origin master
git push -u origin master  # -u ์ต์์ ํ๋ค๋ฉด ์ดํ pushํ  ๋๋ git push๋ง์ผ๋ก๋ ๊ฐ๋ฅ

# ์๊ฒฉ ์ ์ฅ์๋ฅผ ๋ก์ปฌ์ ๋ณต์ 
git clone [Github repository URL]

# ์๊ฒฉ ์ ์ฅ์์ ๋ณ๊ฒฝ ์ฌํญ ๋ก์ปฌ์ ๋ฐ์์ค๊ธฐ (๋๊ธฐํ)
git pull origin master
```

### 3. reset, revert

```bash
# ํน์  ์ปค๋ฐ ์ํ๋ก ๋๋๋ฆฌ๊ธฐ (soft, mixed, hard ์ธ ๊ฐ์ง ์ต์)
git reset --soft [commit ID]
git reset --mixed [commit ID]
git reset --hard [commit ID]

# ์ปค๋ฐ์ ์ทจ์ํ๋ ์ปค๋ฐ์ ์๋ก ์์ฑํ์ฌ ํน์  ์ปค๋ฐ์ ๋๋๋ฆฌ๊ธฐ
git revert [commit ID]

# ์ด์  ์ปค๋ฐ ๋ชฉ๋ก ๋ชจ๋ ์ถ๋ ฅ
git reflog
```

### 4. branch, merge

```bash
# ๋ธ๋์น ๋ชฉ๋ก ํ์ธ
git branch

# ์ ๋ธ๋์น ์์ฑ
git branch [branch name]

# ํน์  ๋ธ๋์น ์ญ์ 
git branch -d [branch name]
git branch -D [branch name]  # ๊ฐ์  ์ญ์ (๋ณํฉ๋์ง ์์ ๋ธ๋์น๋ ์ญ์ )

git switch [branch name]  # ๋ค๋ฅธ ๋ธ๋์น๋ก ์ด๋
git switch -c [branch name]  # ๋ธ๋์น๋ฅผ ์์ฑํจ๊ณผ ๋์์ ์ด๋

# ํ ์ค๋ก, ๋ชจ๋  ๋ธ๋์น์, ๊ทธ๋ํ๋ฅผ ํฌํจํ์ฌ ์ปค๋ฐ ๋ชฉ๋ก ์ถ๋ ฅ
git log --oneline --all --graph

# ๋ธ๋์น ๋ณํฉ
git merge [branch name]
```