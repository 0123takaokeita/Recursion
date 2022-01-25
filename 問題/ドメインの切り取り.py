def upperCaseDomain(mail):
  domain = mail.index('@') + 1
  return mail[domain:].upper()


# メールアドレスが与えられるので、
# メソッドチェーンを用いてドメイン名を大文字で切り出す 
# upperCaseDomain という関数を作成してください。


# 入力のデータ型： string email
# 出力のデータ型： string

print(upperCaseDomain("bjacobi@example.com")) #--> EXAMPLE.COM
print(upperCaseDomain("christine37@example.net")) #--> EXAMPLE.NET
print(upperCaseDomain("deontae.braun@metz.org")) #--> METZ.ORG
print(upperCaseDomain("elwyn.leannon@example.com")) #--> EXAMPLE.COM
print(upperCaseDomain("carter88@gmail.com")) #--> GMAIL.COM
print(upperCaseDomain("amaya.kohler@yahoo.com")) #--> YAHOO.COM