# Solitaire-housekeeper-auto
## 微信接龙管家小程序自动打卡
疫情的假期里即便在家也要健康打卡，打卡也就算了，这不当人的班主任嫌每天通知那些不打卡的同学麻烦，让学习委员出个主意来方便让她过一个***无忧无虑***的假期，这**学习委员**也是天才，直接又开了一个接龙小程序来打卡，让每天打完学校的卡后再来小程序里打卡。  
这本来没什么，但是偏偏这天才学习委员把打卡时间段设置在了早上六点至九点才能打卡（因为学校的健康打卡的建议打卡时间是十点以前）~~卷起来了~~，先不说我天天晚睡能不能起床，起床以后记不记得都是个问题，在被折磨了一个星期以后，我用我那***弱不禁风***的代码水平写了这个打卡程序。
***
## 说明
    本打卡脚本仅供学习交流使用，请勿过分依赖。开发者对使用或不使用本脚本造成的问题不负任何责任，不对脚本执行效果做出任何担保，原则上不提供任何形式的技术支持。
    （复制来的）
## 使用方法
    [接龙管家](https://i.jielong.co/)
打开要打卡的项目用F12查看network的xhr类型
     在headers的request hedaers中复制authorization的值
    ![headers](https://github.com/ljq2333/Solitaire-housekeeper-auto/blob/main/1.jpg)
<br>
    在preview中复制ThreadId
    ![preview](https://github.com/ljq2333/Solitaire-housekeeper-auto/blob/457fa3bfab8130a940bc6b20a30428c7ae0ed833/2.png)
    
    
打开[main](https://github.com/ljq2333/Solitaire-housekeeper-auto/blob/main/main.py)
填入authorization,ThreadId,name

   
### 结尾
    第一次弄这个写的看不懂实数抱歉。
    本人是个入门新手 代码水平有限 就算不能用了大概也不会再修改了。
