from qg_botsdk import BOT, ApiModel, Model
import requests
import json

with open('config.json', 'r', encoding='utf-8') as config_info:
    config_content = json.load(config_info)

bot = BOT(bot_id=f"{config_content['appid']}",bot_token=f"{config_content['token']}",is_private=False, is_sandbox=True)
def xz(xz_name, data: Model.MESSAGE):
    xz_return = requests.get(f"https://v2.xxapi.cn/api/horoscope?time=today&type={xz_name}")
    xz_json = xz_return.json()
    if xz_json['code'] == 200:
        data.reply(f"今日星座运势\n今天日期：{xz_json['data']['time']}\n评估：\n    财富：({xz_json['data']['index']['money']}){xz_json['data']['fortunetext']['money']}\n    健康：({xz_json['data']['index']['health']}){xz_json['data']['fortunetext']['health']}\n    工作：({xz_json['data']['index']['work']}){xz_json['data']['fortunetext']['work']}\n\n信息来源于网络，不确保信息真实性，请理性对待！")
    else:
        data.reply(f"请求失败！\n错误码：{xz_json['code']}\n错误原因：{xz_json['msg']}\n如果您认为该错误很重要，请前往官方频道反馈！")
def guild_message(data: Model.MESSAGE):
    msg = data.treated_msg
    bot.logger.info(f"接受到消息：{msg}")
    if msg.startswith("星座运势"):
        xz_strip = msg[4:].strip()
        if xz_strip == "白羊座":
            xz("aries", data)
        elif xz_strip == "金牛座":
            xz("taurus", data)
        elif xz_strip == "双子座":
            xz("gemini", data)
        elif xz_strip == "巨蟹座":
            xz("cancer", data)
        elif xz_strip == "狮子座":
            xz("leo", data)
        elif xz_strip == "处女座":
            xz("virgo", data)
        elif xz_strip == "天秤座":
            xz("libra", data)
        elif xz_strip == "天蝎座":
            xz("scorpio", data)
        elif xz_strip == "射手座":
            xz("sagittarius", data)
        elif xz_strip == "水瓶座":
            xz("aquarius", data)
        elif xz_strip == "摩羯座":
            xz("capricorn", data)
        elif xz_strip == "双鱼座":
            xz("pisces", data)
        else:
            data.reply("请指定参数或参数有误！\n目前支持参数：白羊座 金牛座 双子座 巨蟹座 狮子座 处女座 天秤座 天蝎座 射手座 水瓶座 摩羯座 双鱼座")
    elif msg.startswith("天气"):
        wt_strip = msg[2:].strip()
        if wt_strip:
            wt_return = requests.get(f"https://api.lolimi.cn/API/weather/api.php?city={wt_strip}")
            wt_json = wt_return.json()
            if wt_json['code'] == 1:
                if wt_json['data']['warning']:
                    data.reply(f"天气查询\n城市名称：{wt_json['data']['city']}/{wt_json['data']['cityEnglish']}\n温度：{wt_json['data']['current']['temp']}°C\n湿度：{wt_json['data']['current']['humidity']}\n风度：{wt_json['data']['current']['wind']}   {wt_json['data']['current']['windSpeed']}\n天气情况：{wt_json['data']['current']['weather']}\n时间：{wt_json['data']['current']['date']}   {wt_json['data']['current']['time']}\n{wt_json['data']['warning']['color']}{wt_json['data']['warning']['wind']}预警：{wt_json['data']['warning']['warning']}\n天气信息来源于网络，不确保信息真实性！")
                else:
                    data.reply(f"天气查询\n城市名称：{wt_json['data']['city']}/{wt_json['data']['cityEnglish']}\n温度：{wt_json['data']['current']['temp']}°C\n湿度：{wt_json['data']['current']['humidity']}\n风度：{wt_json['data']['current']['wind']}   {wt_json['data']['current']['windSpeed']}\n天气情况：{wt_json['data']['current']['weather']}\n时间：{wt_json['data']['current']['date']}   {wt_json['data']['current']['time']}\n天气信息来源于网络，不确保信息真实性！")
            else:
                data.reply(f"请求出错！\n错误码：{wt_json['code']}\n错误原因：{wt_json['text']}\n\n如果您认为该错误很重要，请前往官方频道反馈！")
        else:
            data.reply(f"请提供 城市名称 参数。\n示例：/天气 北京\n")
    elif msg.startswith("图片"):
        pic_strip = msg[2:].strip()
        if pic_strip == "二次元电脑":
            pic_return = requests.get(f"https://v2.xxapi.cn/api/randomAcgPic?type=pc")
            pic_json = pic_return.json()
            if pic_json['code'] == 200:
                bot.api.send_msg(
                    channel_id=data.channel_id,
                    image=pic_json['data']
                )
            else:
                data.reply(f"请求失败！\n错误码：{pic_json['code']}\n错误原因：{pic_json['msg']}\n如果您认为该错误很重要，请前往官方频道反馈！")
        elif pic_strip == "二次元手机":
            pic_return = requests.get(f"https://v2.xxapi.cn/api/randomAcgPic?type=wap")
            pic_json = pic_return.json()
            if pic_json['code'] == 200:
                bot.api.send_msg(
                    channel_id=data.channel_id,
                    image=pic_json['data']
                )
            else:
                data.reply(f"请求失败！\n错误码：{pic_json['code']}\n错误原因：{pic_json['msg']}\n如果您认为该错误很重要，请前往官方频道反馈！")
        elif pic_strip == "每日必应":
            bot.api.send_msg(
                channel_id=data.channel_id,
                image="https://v2.xxapi.cn/api/bing?return=302"
            )
        else:
            data.reply(f"请指定参数或参数有误！\n目前支持类别：\n①/图片 二次元电脑\n② /图片 二次元手机\n③/图片 每日必应")
    elif msg.startswith("歌曲"):
        music_strip = msg[2:].strip()
        if music_strip == "搜索":
            pass
    elif msg.startswith("随机一言"):
        say_json = requests.get(f"https://api.keguan.org.cn/api/yiyan/api.php")
        say_json = say_json.json()
        data.reply(f"一言：{say_json['text']}\n作者：{say_json['from']}")
    elif msg.startswith("新闻"):
        news_return = requests.get(f"https://v2.xxapi.cn/api/hot60s")
        news_json = news_return.json()
        if news_json['code'] == 200:
            bot.api.send_msg(
                channel_id=data.channel_id,
                image=news_json['data']
            )
        else:
            data.reply(f"请求失败！\n错误码：{news_json['code']}\n错误原因：{news_json['msg']}\n如果您认为该错误很重要，请前往官方频道反馈！")
    elif msg.startswith("菜单"):
        data.reply(f"MCBot菜单\n①天气查询：/天气 城市\n②新闻查询：/新闻\n③随机一言：/随机一言\n④二次元图片：/图片\n⑤星座运势：/星座运势")
    else:
        data.reply("消息指令错误❌。")
if __name__ == "__main__":
    bot.load_default_msg_logger()
    bot.bind_msg(guild_message, treated_data=True)
    bot.start()
