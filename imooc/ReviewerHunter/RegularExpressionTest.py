
import re

# testStr = "/gp/profile/amzn1.account.AHPJPSBB2H2ZQIV57YYHEM4GA3DA/ref=cm_cr_tr_tbl_2,211_name"
testStr = "<a class=\"a-link-normal\" href=\"/gp/profile/amzn1.account.AHPJPSBB2H2ZQIV57YYHEM4GA3DA/ref=cm_cr_tr_tbl_2,211_name\"><b>The Mysterious Amazon Customer</b></a>"

# 将正则表达式编译成Pattern对象
# pattern = re.compile(r'/gp/profile/amzn1.account.\w{20,30}/ref=cm_cr_tr_tbl_.{1,7}_name')

# print(re.search(r'/gp/profile/amzn1.account.\w+/ref=cm_cr_tr_tbl_.{1,7}_name', testStr))
print(re.findall(r'/gp/profile/amzn1.account.\w+/ref=cm_cr_tr_tbl_.{1,7}_name', testStr))


