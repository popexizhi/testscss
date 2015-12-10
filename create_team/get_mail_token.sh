echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
echo $0 $1
ls -all |grep test_mail*
rm test_mail*
grep "verify.html?email=" log/postman/0/postman.log >x.log
vim -es </home/jenkins/test/vitest/get_token.vim x.log
cat x.log |grep $1 > $1
rm x.log
ls -all |grep $1
cat $1
echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
