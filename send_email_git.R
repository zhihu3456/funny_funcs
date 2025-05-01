### make notify email
library(mailR)

# for finish notice
send.mail(email=T,
          from="540089728@qq.com",to="zhihu_xu@outlook.com",
          subject="Message from R",body="R is done",
          smtp = list(host.name="smtp.qq.com",port=587,
                      user.name="540089728@qq.com",passwd="afuvhcoycdggbcbc",ssl=T),
          authenticate=T,send=T)


