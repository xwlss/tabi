# tabi

1.tabi水龙头不需要验证码，同一ip重复领水将被拒绝，因此需要使用动态ip，已有在使用的动态ip经验的可直接配置41行。没有的可以注册使用[nstproxy register](https://app.nstproxy.com/register?i=zsqgWP).完成后在37行处替换nstproxy_Channel的XXX，38行处替换nstproxy_Password的XXX，删除37，38，39，40行的‘#‘，再删除掉41行即可，或者直接咨询所用代理的客服帮忙配置。

【注意】据反馈这个nstproxy动态代理区域似乎ip 被刷的较多，可能是代理设置或者ip池较小原因，建议大家使用更有效的ip代理，如rola-ip，iproyal等。

2.如果已有地址文件领水，请运行 python3 faucet_f.py，请自行配置27行提取地址格式。

如果由程序生成地址私钥助记词，请运行 python3 faucet_c.py，运行完成后相关地址、私钥和助记词都会保存在tabi-wallet.txt文件中，请妥善保存。

3.如果显示Error：No module named 'XXX' ,请在cmd下运行 pip install XXX。
